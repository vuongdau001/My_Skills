"""Schema-2 knowledge records, pinned trace links and scoped obligation checks.

Checks declarations and locally available evidence only; never authenticates an approver.
"""
from datetime import date, datetime
import hashlib
from pathlib import Path, PureWindowsPath
import re
from urllib.parse import unquote, urlsplit

KINDS = {'Meeting':'MTG','Decision':'DEC','Assumption':'ASM','Constraint':'CST'}
STATES = {
    'Meeting':('meeting_state', {'Draft','Confirmed','Amended'}),
    'Decision':('decision_state', {'Pending','Proposed','Approved','Superseded','Rejected','Withdrawn'}),
    'Assumption':('assumption_state', {'Unverified','Validated','Invalidated','Retired'}),
    'Constraint':('constraint_state', {'Proposed','Confirmed','Superseded','Retired'}),
}
RELATIONS = {'supports','derived-from','applies-to','supersedes','superseded-by','depends-on','resolves','parent','verifies'}


def entries(meta):
    """One record in its own artifact, or records with local ownership in a register."""
    if isinstance(meta.get('record'), dict):
        yield dict(meta['record'], id=meta.get('artifact_id'), kind=meta.get('kind'))
    rows = meta.get('records', [])
    if isinstance(rows, list):
        for row in rows:
            if isinstance(row, dict):
                yield row


def defined_ids(meta):
    return [r['id'] for r in entries(meta) if isinstance(r.get('id'),str)]


def intake(api, repo, ws, inputs):
    """Index declared records for intake. Applicability, provenance and authority require review."""
    root = api['relative'](repo, ws['spec_root'])
    kinds = ('Assumption', 'Constraint', 'Decision')

    def inspect(path):
        try:
            content = path.read_bytes()
            meta = api['metadata'](content.decode('utf-8')) or {}
        except (OSError, UnicodeError):
            return 'unreadable', None, []
        except api['KitError']:
            return 'invalid-metadata', hashlib.sha256(content).hexdigest(), []

        rows = list(entries(meta))
        if meta.get('schema_version') == 1 and meta.get('kind') in kinds and not rows:
            rows = [dict(meta, id=meta.get('artifact_id'))]
        records = []
        for row in rows:
            kind = row.get('kind')
            if kind not in kinds:
                continue
            fields = {'id': row.get('id'), 'revision': row.get('revision'),
                      'scope': row.get('scope'), 'declared_state': row.get(STATES[kind][0])}
            records.append(dict(kind=kind, **{k: v if isinstance(v, str) else None for k, v in fields.items()}))
        return ('structured' if records else 'review-source'), hashlib.sha256(content).hexdigest(), records

    existing, issues = [], []
    for path in sorted(root.rglob('*.md')):
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
            continue
        inspection, sha, records = inspect(path)
        name = path.relative_to(repo).as_posix()
        existing.extend(dict(row, path=name, sha256=sha) for row in records)
        if inspection in ('unreadable', 'invalid-metadata'):
            issues.append(dict(path=name, inspection=inspection))

    configured = list(ws['sources'])
    supplied = [dict(path=raw) for raw in inputs]
    if ws.get('input_root'):
        supplied.append(dict(path=ws['input_root']))
    source_rows, seen = [], set()
    for source in configured + supplied:
        path = api['relative'](repo, source['path'])
        if 'id' not in source and path in seen:
            continue
        seen.add(path)
        entry = dict(path=source['path'], source_id=source.get('id'))
        if not path.exists():
            inspection, sha, records = 'missing', None, []
        elif path.is_file() and path.suffix.lower() == '.md':
            inspection, sha, records = inspect(path)
        else:
            inspection, sha, records = 'manual-review', None, []
        source_rows.append(dict(entry, inspection=inspection, sha256=sha, candidates=records))
    return dict(existing_records=existing, sources=source_rows, issues=issues,
                note='Declared metadata only. Read and reconcile the inputs; verify scope, evidence and authority before reuse. Source candidates are not registered records.')


def audit(api, repo, cfg, ws, docs, definitions, issue, args):
    gate, selected = getattr(args,'gate','draft'), getattr(args,'target',None)
    epic_policy = api['support']('epics')
    all_docs = dict(docs)
    for stream in cfg['workstreams']:
        root = api['relative'](repo,stream['spec_root'])
        if root.exists():
            for p in root.rglob('*.md'):
                if p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(root) and p not in all_docs:
                    all_docs[p] = p.read_text(encoding='utf-8')
    metas, records, owners, revisions, links, outgoing = {}, {}, {}, {}, [], {}
    dependencies, supersedes, unverified = {}, {}, set()
    for p,text in all_docs.items():
        try:
            meta = api['metadata'](text)
        except api['KitError']:
            continue
        if not meta:
            continue
        metas[p] = meta
        for identity in [meta.get('artifact_id')] + (meta.get('defined_ids',[]) if isinstance(meta.get('defined_ids',[]),list) else []):
            if isinstance(identity,str):
                owners[identity] = p
                revisions[identity] = meta.get('revision')
        for row in entries(meta):
            identity = row.get('id')
            if isinstance(identity,str):
                records[identity] = (p,row)
                owners[identity] = p
                revisions[identity] = row.get('revision')

    # Epic and Use Case share the same gate obligations regardless of which ID a consumer pins.
    case_locations = {}
    for p, meta in metas.items():
        case = epic_policy.case_id(meta)
        epic = meta.get('artifact_id')
        if case and meta.get('epic_policy') == epic_policy.POLICY:
            case_locations[p] = case
            name = p.relative_to(repo).as_posix()
            if (isinstance(epic, str) and name in definitions.get(case, ())
                    and name in definitions.get(epic, ())):
                dependencies.setdefault(case, set()).add(epic)
                dependencies.setdefault(epic, set()).add(case)
    anchors_by_path = {}

    def emit(level, code, p, message):
        issue(level,code,p.relative_to(repo).as_posix(),message)

    def text_field(row, field, p):
        if not isinstance(row.get(field),str) or not row[field].strip():
            emit('ERROR','record-field',p,str(row.get('id'))+': nonempty '+field+' required')

    def time_field(row, field, p):
        try:
            value = datetime.fromisoformat(row.get(field,'').replace('Z','+00:00'))
            if value.tzinfo is None:
                raise ValueError()
        except (ValueError,TypeError,AttributeError):
            emit('ERROR','record-time',p,str(row.get('id'))+': '+field+' requires ISO datetime with timezone')

    def reference(p, ref, *, evidence=False, source=None):
        if not isinstance(ref,dict):
            emit('ERROR','record-reference',p,'Expected reference object')
            return
        href = ref.get('path')
        if not isinstance(href,str) or not href:
            emit('ERROR','record-reference',p,'Reference requires path')
            return
        revision, sha = ref.get('revision'), ref.get('sha256')
        if not isinstance(revision,str) or not revision.strip():
            emit('ERROR','reference-revision',p,'Reference requires revision: '+href)
        if sha is not None and (not isinstance(sha,str) or not re.fullmatch(r'[a-f0-9]{64}',sha)):
            emit('ERROR','reference-hash',p,'Invalid SHA-256: '+href)
        if evidence and not sha:
            emit('ERROR','evidence-pin',p,'Evidence requires SHA-256: '+href)
        url = urlsplit(href)
        if url.scheme in {'http','https'}:
            if not evidence:
                emit('ERROR','trace-external',p,'Typed trace target must be a local definition; keep external source under evidence')
                return
            emit('WARN','external-evidence-unverified',p,'Not fetched/authenticated; use accessible pinned evidence for gate: '+href)
            if source:
                unverified.add(source)
            return
        if url.scheme or url.netloc or Path(url.path).is_absolute() or PureWindowsPath(url.path).drive or '\\' in href:
            emit('ERROR','reference-path',p,'Only repo-contained relative references or HTTPS/HTTP evidence supported')
            return
        target = (p.parent/unquote(url.path)).resolve() if url.path else p
        if not target.is_relative_to(repo) or not target.is_file():
            emit('ERROR','reference-path',p,'Missing or escaping reference: '+href)
            return
        if sha and api['digest'](target) != sha:
            emit('ERROR','stale-reference',p,'Content hash mismatch: '+href)
        if url.fragment:
            if target.suffix != '.md' or unquote(url.fragment) not in api['load_validator']().anchors(target.read_text(encoding='utf-8'))[0]:
                emit('ERROR','reference-anchor',p,'Missing Markdown anchor: '+href)
        if evidence:
            return
        identity, relation = ref.get('id'), ref.get('relation')
        if not isinstance(identity,str) or not re.fullmatch(api['id_pattern'](),identity):
            emit('ERROR','trace-id',p,'Trace link requires valid target ID')
            return
        if not isinstance(relation,str) or relation not in RELATIONS:
            emit('ERROR','trace-relation',p,'Unknown trace relation')
            return
        if identity not in definitions:
            emit('ERROR','trace-unresolved',p,'Undefined target ID: '+identity)
        elif target.relative_to(repo).as_posix() not in definitions[identity]:
            emit('ERROR','trace-owner',p,'Target ID is not defined by referenced file: '+identity)
        if case_locations.get(target) == identity:
            if target not in anchors_by_path:
                anchors_by_path[target] = epic_policy.case_anchors(api, all_docs[target])
            if '#' + unquote(url.fragment) not in anchors_by_path[target]:
                emit('ERROR','trace-use-case-locator',p,'Use Case trace must point to an explicit E03 anchor: '+href)
        target_revision = revisions.get(identity)
        if target_revision is not None and target_revision != revision:
            emit('ERROR','stale-revision',p,'Target revision mismatch: '+identity)
        elif target_revision is None and not sha:
            emit('WARN','revision-unverified',p,'Target has no structured revision; pin SHA-256: '+identity)
            if source:
                unverified.add(source)
        if source:
            links.append((source,identity,relation,p))
            outgoing.setdefault(source,[]).append((identity,relation))

    for p,meta in metas.items():
        # Do not impose schema-2 record fields on legacy schema-1 decisions.
        if meta.get('kind') in {'Meeting','Assumption','Constraint'} and meta.get('schema_version') != 2:
            if p in docs:
                emit('ERROR','record-schema',p,'New knowledge record kinds require metadata schema_version=2')
        elif ('record' in meta or 'records' in meta) and meta.get('schema_version') != 2:
            emit('ERROR','record-schema',p,'Structured record/records require metadata schema_version=2')
        if meta.get('schema_version') == 2:
            if 'records' in meta and (not isinstance(meta['records'],list) or not all(isinstance(r,dict) for r in meta['records'])):
                emit('ERROR','record-list',p,'records must be a list of record objects')
            if meta.get('kind') in KINDS and not isinstance(meta.get('record'),dict):
                emit('ERROR','record-required',p,'Standalone knowledge artifact requires record object')
            seen = set()
            for row in entries(meta):
                identity, kind = row.get('id'), row.get('kind')
                if not isinstance(identity,str) or not isinstance(kind,str) or kind not in KINDS or not re.fullmatch(KINDS[kind]+r'-CRM-\d{3,}',identity):
                    emit('ERROR','record-id',p,'Record ID/prefix must match its kind')
                    continue
                if identity in seen:
                    emit('ERROR','duplicate-record',p,identity)
                seen.add(identity)
                for field in ('revision','scope'):
                    text_field(row,field,p)
                state_field, states = STATES[kind]
                if not isinstance(row.get(state_field),str) or row[state_field] not in states:
                    emit('ERROR','record-state',p,identity+': invalid '+state_field)
                state = row.get(state_field)
                state = state if isinstance(state,str) else None
                if kind != 'Meeting':
                    text_field(row,'statement',p)
                    if 'owner' not in row or (row['owner'] is not None and (not isinstance(row['owner'],str) or not row['owner'].strip())):
                        emit('ERROR','record-owner',p,identity+': owner is string or explicit null while unassigned')
                if kind == 'Meeting':
                    if row.get('event_type') not in ('meeting','workshop','chat','email'):
                        emit('ERROR','meeting-type',p,'Record actual event type; do not invent a formal meeting')
                    text_field(row,'summary',p)
                    if state in {'Confirmed','Amended'} or row.get('occurred_at') is not None:
                        time_field(row,'occurred_at',p)
                    people = row.get('participants')
                    if not isinstance(people,list) or not all(isinstance(v,str) and v.strip() for v in people) or (state in {'Confirmed','Amended'} and not people):
                        emit('ERROR','meeting-participants',p,'participants must list actual participants; confirmed record cannot be empty')
                    if not isinstance(row.get('actions'),list):
                        emit('ERROR','meeting-actions',p,'actions must be a list; [] if none recorded')
                    else:
                        for action in row['actions']:
                            if not isinstance(action,dict) or not isinstance(action.get('description'),str) or not action['description'].strip() or 'owner' not in action or 'due' not in action:
                                emit('ERROR','meeting-action',p,'Action requires description, owner and due (null if unknown); no automatic product Task')
                    if state == 'Amended':
                        text_field(row,'amendment_reason',p)
                elif kind == 'Decision':
                    for field in ('context','options','rationale','consequences'):
                        text_field(row,field,p)
                    if state in {'Approved','Rejected'}:
                        text_field(row,'authority',p)
                        time_field(row,'decided_at',p)
                elif kind == 'Assumption':
                    for field in ('basis','validation_method','if_false'):
                        text_field(row,field,p)
                    if 'review_due' not in row:
                        emit('ERROR','assumption-review',p,'review_due required (date or null while unassigned)')
                    elif row['review_due'] is not None:
                        try:
                            date.fromisoformat(row['review_due'])
                        except (TypeError,ValueError):
                            emit('ERROR','assumption-review',p,'review_due must be an ISO date or null')
                    if state in {'Validated','Invalidated'}:
                        text_field(row,'owner',p)
                        text_field(row,'validation_result',p)
                elif kind == 'Constraint':
                    text_field(row,'constraint_type',p)
                    text_field(row,'verification_method',p)
                    if state == 'Confirmed':
                        text_field(row,'authority',p)
                        text_field(row,'effective_from',p)
                required = ((kind=='Decision' and state in {'Approved','Rejected'}) or
                            (kind=='Meeting' and state in {'Confirmed','Amended'}) or
                            (kind=='Assumption' and state in {'Validated','Invalidated'}) or
                            (kind=='Constraint' and state=='Confirmed'))
                evidence = row.get('evidence',[])
                if not isinstance(evidence,list) or (required and not evidence):
                    emit('ERROR','record-evidence',p,identity+': state requires evidence list with pinned local evidence')
                else:
                    for ref in evidence:
                        reference(p,ref,evidence=True,source=identity)
                trace = row.get('trace_links',[])
                if not isinstance(trace,list):
                    emit('ERROR','trace-list',p,'trace_links must be a list')
                else:
                    for ref in trace:
                        reference(p,ref,source=identity)
        trace = meta.get('trace_links',[])
        if not isinstance(trace,list):
            emit('ERROR','trace-list',p,'trace_links must be a list')
        else:
            if trace and not isinstance(meta.get('artifact_id'),str):
                emit('ERROR','trace-source',p,'Top-level trace_links require artifact_id; place register links inside their record')
            for ref in trace:
                reference(p,ref,source=meta.get('artifact_id'))

    # Build dependency closure in the semantic direction, regardless of which file stores the link.
    for source,target,relation,p in links:
        if relation in {'depends-on','derived-from','parent','resolves','verifies'}:
            dependencies.setdefault(source,set()).add(target)
        elif relation in {'supports','applies-to'}:
            dependencies.setdefault(target,set()).add(source)
        if relation in {'supersedes','superseded-by'}:
            newer,older = (source,target) if relation=='supersedes' else (target,source)
            supersedes.setdefault(newer,set()).add(older)
            if newer == older:
                emit('ERROR','supersession-cycle',p,'A record cannot supersede itself')
            if older in records:
                old = records[older][1]
                if newer in records and records[newer][1].get('kind') != old.get('kind'):
                    emit('ERROR','supersession-kind',p,'Replacement record must have the same kind: '+older)
                if old.get(STATES.get(old.get('kind'),('',set()))[0]) != 'Superseded':
                    emit('ERROR','supersession-state',p,'Old record must be marked Superseded: '+older)
    visiting, visited = set(), set()
    def cycle(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        result = any(cycle(child) for child in supersedes.get(node,()))
        visiting.remove(node)
        visited.add(node)
        return result
    obligations, impacts = [], []
    for identity,(p,row) in records.items():
        if row.get(STATES.get(row.get('kind'),('',set()))[0]) == 'Superseded':
            replacements = {target for target,rel in outgoing.get(identity,[]) if rel=='superseded-by'}
            if len(replacements) != 1:
                emit('ERROR','supersession-missing',p,identity+': requires exactly one superseded-by trace link')
        if cycle(identity):
            emit('ERROR','supersession-cycle',p,'Supersession graph contains a cycle')
    historical = {identity for identity,(_,r) in records.items()
                  if r.get('kind') in STATES and r.get(STATES[r['kind']][0]) in {'Superseded','Retired','Rejected','Withdrawn'}}
    scope = set(definitions) - historical if not selected else {selected}
    if selected and selected not in definitions:
        issue('ERROR','gate-target',ws['spec_root'],'Undefined target: '+selected)
    queue = list(scope)
    while queue:
        for parent in dependencies.get(queue.pop(),()):
            if parent not in scope:
                scope.add(parent)
                queue.append(parent)
    epic_policy.audit(api, repo, cfg, ws, all_docs, metas, definitions, scope, issue, gate, selected)
    for identity,(p,row) in records.items():
        if identity not in scope or (not selected and p not in docs):
            continue
        kind = row.get('kind')
        if kind not in STATES:
            continue
        state = row.get(STATES[kind][0])
        blocked = ((kind=='Assumption' and state!='Validated') or
                   (kind=='Decision' and state!='Approved') or
                   (kind=='Constraint' and state!='Confirmed'))
        # Reverse dependency closure exposes declared consumers needing refinement/review.
        affected, pending = set(), [identity]
        while pending:
            parent = pending.pop()
            for consumer,inputs in dependencies.items():
                if parent in inputs and consumer not in affected and consumer != identity:
                    affected.add(consumer)
                    pending.append(consumer)
        impact = {'id':identity,'kind':kind,'state':state,'revision':row.get('revision'),
                  'path':p.relative_to(repo).as_posix(),'affected_ids':sorted(affected)}
        impacts.append(impact)
        if blocked:
            obligations.append(impact)
            emit('WARN' if gate=='draft' else 'ERROR','record-obligation',p,
                 identity+': '+str(state)+'; resolve or explicitly remove dependency with reviewed rationale before '+gate)
    if gate != 'draft':
        for identity in sorted(scope & unverified):
            p = owners[identity]
            emit('ERROR','gate-evidence-unverified',p,identity+': dependency/evidence revision not verified locally')
    return {'record_obligations':obligations,'record_impacts':impacts,'trace_link_count':len(links),'gate_scope':{'gate':gate,'target':selected,
            'dependency_ids':sorted(scope) if selected else []}}
