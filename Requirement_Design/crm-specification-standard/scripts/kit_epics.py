"""Structural checks for the Epic–Use Case policy."""
import re

POLICY = 'use-case-v1'
LEGACY = 'legacy'
ANCHOR = re.compile(r'#[a-z][a-z0-9-]*')


def case_anchors(api, source):
    validator = api['load_validator']()
    visible = validator.unfenced(source)
    match = re.search(r'^## E03\b[^\n]*\n(.*?)(?=^## |\Z)', visible, re.M | re.S)
    if not match:
        return set()
    _, all_explicit = validator.anchors(visible)
    _, local_explicit = validator.anchors(match[1])
    return {'#' + name for name in local_explicit if all_explicit.count(name) == 1}


def case_id(meta):
    binding = meta.get('use_case')
    if meta.get('kind') == 'Epic' and isinstance(binding, dict):
        value = binding.get('id')
        if isinstance(value, str) and re.fullmatch(r'MOD-CRM-\d{3,}', value):
            return value
    return None


def audit(api, repo, cfg, ws, all_docs, metas, definitions, scope, issue, gate, selected):
    claims = {}
    for stream in cfg['workstreams']:
        root = api['relative'](repo, stream['spec_root'])
        epic_dirs = (root / api['artifact_paths'](stream)['epics'], root / 'epics', root / '02-epics')
        for path, source in all_docs.items():
            if not path.is_relative_to(root):
                continue
            name = path.relative_to(repo).as_posix()
            meta = metas.get(path, {})
            epic = meta.get('kind') == 'Epic' or (
                not meta and (any(path.is_relative_to(d) for d in epic_dirs)
                              or re.match(r'^# EPIC-CRM-\d{3,}\b', source)))
            if not epic:
                if stream == ws and ('epic_policy' in meta or 'use_case' in meta):
                    issue('ERROR', 'epic-policy', name, 'Only an Epic can declare a Use Case binding')
                continue
            binding = meta.get('use_case')
            use_case_id = case_id(meta)
            if use_case_id:
                claims.setdefault(use_case_id, []).append(name)
            if selected:
                owned = api['legacy_definitions'](source) if not meta else {
                    i for i in scope if name in definitions.get(i, ())
                }
                applies = bool(scope & owned) or use_case_id in scope
            else:
                applies = stream == ws and (gate == 'draft' or meta.get('work_status') != 'cancel')
            if not applies:
                continue
            if 'epic_policy' not in meta and 'use_case' not in meta:
                issue('WARN' if gate == 'draft' else 'ERROR', 'epic-legacy', name,
                      'Legacy Epic; migrate the delivery scope to use-case-v1 before a delivery gate')
                continue
            if meta.get('epic_policy') != POLICY:
                issue('ERROR', 'epic-policy', name, 'Epic binding requires epic_policy=use-case-v1')
                continue
            if not use_case_id or binding.get('level') != 'user-goal':
                issue('ERROR', 'epic-use-case', name, 'Expected one use_case object with a MOD ID and level=user-goal')
                continue
            identity, revision = meta.get('artifact_id'), meta.get('revision')
            if not (isinstance(identity, str) and re.fullmatch(r'EPIC-CRM-\d{3,}', identity)
                    and isinstance(revision, str) and revision.strip()):
                issue('ERROR', 'epic-use-case', name, 'Use Case owner requires an Epic ID and nonempty revision')
            declared = meta.get('defined_ids')
            if not isinstance(declared, list) or declared.count(use_case_id) != 1:
                issue('ERROR', 'epic-use-case-owner', name, 'Epic must define its Use Case ID exactly once in defined_ids')
            locator = binding.get('locator')
            if not (isinstance(locator, str) and ANCHOR.fullmatch(locator)
                    and locator in case_anchors(api, source)):
                issue('ERROR', 'epic-use-case-locator', name, 'Use Case locator must be a unique explicit anchor inside E03')

    for identity, paths in claims.items():
        if len(paths) > 1:
            issue('ERROR', 'duplicate-use-case', ', '.join(sorted(paths)), identity)
