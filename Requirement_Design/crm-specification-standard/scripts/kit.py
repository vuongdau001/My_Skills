#!/usr/bin/env python3
"""Portable CRM kit tooling. Python 3.11+, standard library, no network or git writes."""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PureWindowsPath
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True
KIT = Path(__file__).resolve().parents[1]
CONFIG = '.agents/crm-spec-kit.json'
RECEIPT = 'crm-spec-kit-installation.json'
DIRECTORIES = ['00-project', 'features', 'epics', 'stories', 'tasks', 'reviews', 'baselines', 'reports', 'pilot']  # Legacy API; scaffold resolves artifact_paths.
PREFIXES = {'FEAT','EPIC','STORY','TASK','REQ','BR','AC','MOD','DEC','BASE','TC','RUN','Q','MTG','ASM','CST'}
VERDICTS = {'Đạt','Không đạt','Chưa kiểm','N/A'}
DECISIONS = {'Pending','Proposed','Approved','Superseded','Rejected','Withdrawn'}
STATUSES = {'Epic':{'todo','inprogress','done','cancel'},
            'Story':{'todo','inprogress','pending','resolved','done','cancel'},
            'Task':{'todo','inprogress','review','pending','resolved','done','cancel'}}
AGENT_ROOTS = {'antigravity': '.agents', 'codex': '.agents', 'claude': '.claude'}
ROUTER_START = '<!-- crm-spec-kit:router:start -->'
ROUTER_END = '<!-- crm-spec-kit:router:end -->'

class KitError(Exception):
    pass


def support(name):
    spec = importlib.util.spec_from_file_location('crm_' + name, KIT / 'scripts' / ('kit_' + name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def artifact_paths(ws):
    return support('layout').artifact_paths(ws, KitError)


def scaffold(ws):
    paths = artifact_paths(ws)
    result = list(paths.values())
    if ws.get('record_schema_version') == 2:
        result += [paths['project'] + '/' + name for name in
                   ('01-meetings','02-decisions','03-assumptions','04-constraints')]
    return result


def now():
    return datetime.now(timezone.utc).isoformat()


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise KitError(f'Cannot read JSON {path.name}: {exc}') from exc


def json_text(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(root, raw, *, allow_root=False):
    """Resolve repo-owned paths; reject traversal, absolute and escaping symlinks."""
    if not isinstance(raw, str) or not raw or '\\' in raw:
        raise KitError(f'Use a nonempty POSIX relative path: {raw!r}')
    if Path(raw).is_absolute() or PureWindowsPath(raw).is_absolute() or PureWindowsPath(raw).drive:
        raise KitError(f'Absolute path forbidden: {raw}')
    if '..' in Path(raw).parts:
        raise KitError(f'Traversal forbidden: {raw}')
    root = root.resolve()
    path = (root / raw).resolve()
    if not path.is_relative_to(root) or (path == root and not allow_root):
        raise KitError(f'Path outside allowed root: {raw}')
    return path


def overlaps(a, b):
    return a == b or a.is_relative_to(b) or b.is_relative_to(a)


def config_check(repo, config):
    if not isinstance(config, dict) or config.get('schema_version') != 1 or config.get('kit_id') != 'crm-specification-standard':
        raise KitError('Unsupported project config: expected schema_version=1 and CRM kit_id')
    if config.get('id_namespace') != 'CRM':
        raise KitError('This standard uses id_namespace CRM; other namespaces need a standards decision')
    streams = config.get('workstreams')
    if not isinstance(streams, list) or not streams:
        raise KitError('Config requires a nonempty workstreams list')
    ids, roots = set(), []
    for ws in streams:
        if not isinstance(ws, dict) or not re.fullmatch(r'[a-z][a-z0-9-]*', ws.get('id', '')) or ws['id'] in ids:
            raise KitError('Invalid or duplicate workstream id')
        ids.add(ws['id'])
        spec = relative(repo, ws.get('spec_root'))
        if ws.get('record_schema_version', 1) not in (1, 2):
            raise KitError('Unsupported record_schema_version')
        for raw in artifact_paths(ws).values():
            relative(spec, raw)
            if any(part.startswith('.') for part in Path(raw).parts):
                raise KitError('Artifact paths cannot use hidden/tool directories')
            if any((spec/Path(*Path(raw).parts[:i])).is_symlink() for i in range(1,len(Path(raw).parts)+1)):
                raise KitError('Artifact category path is a symlink; inspect before scaffold')
        if any(overlaps(spec, relative(repo, part)) for part in ('.git','.agents','.claude')):
            raise KitError('spec_root overlaps tool/config directories')
        if any(overlaps(spec, old) for old in roots):
            raise KitError('Overlapping workstream spec_roots')
        roots.append(spec)
        readonly = ws.get('read_only', [])
        sources = ws.get('sources', [])
        if not isinstance(readonly, list) or not isinstance(sources, list):
            raise KitError('sources/read_only must be lists')
        seen = set()
        for source in sources:
            if not isinstance(source, dict) or not re.fullmatch(r'SRC-[A-Z0-9-]+', source.get('id', '')) or source['id'] in seen:
                raise KitError('Invalid or duplicate source ID within workstream')
            seen.add(source['id'])
            path = relative(repo, source.get('path'))
            if overlaps(spec, path):
                raise KitError('A source path overlaps writable spec_root')
        for raw in readonly:
            if overlaps(spec, relative(repo, raw)):
                raise KitError('read_only overlaps writable spec_root')
        if ws.get('input_root'):
            inp = relative(repo, ws['input_root'])
            if any(overlaps(inp,relative(repo,part)) for part in ('.git','.agents','.claude')):
                raise KitError('input_root overlaps tool/config directories')
            if overlaps(inp, spec) or any(overlaps(inp, relative(repo, raw)) for raw in readonly):
                raise KitError('input_root overlaps spec_root/read_only')
    # Protection applies across streams, including future input/scaffold roots.
    writes = [relative(repo, ws[key]) for ws in streams for key in ('spec_root','input_root') if ws.get(key)]
    check_write_boundaries(repo, config, writes)
    return config


def check_write_boundaries(repo, config, writes):
    for ws in config['workstreams']:
        protected = ws.get('read_only', []) + [source['path'] for source in ws.get('sources', [])]
        for raw in protected:
            path = relative(repo, raw)
            for write in writes:
                if overlaps(write, path):
                    raise KitError(f'Write path {write.relative_to(repo)} overlaps source/read_only {raw} in workstream {ws["id"]}')


def load_config(repo, override=None):
    path = Path(override) if override else relative(repo, CONFIG)
    return config_check(repo, read_json(path))


def select_stream(config, chosen):
    streams = config['workstreams']
    if chosen:
        for stream in streams:
            if stream['id'] == chosen:
                return stream
        raise KitError(f'Unknown workstream: {chosen}')
    if len(streams) != 1:
        raise KitError('Multiple workstreams: specify --workstream; no implicit active target')
    return streams[0]


def package_files(root):
    files = {}
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root).as_posix()
        if any(part in {'.git','__pycache__'} for part in path.relative_to(root).parts) or rel == RECEIPT or path.suffix == '.pyc':
            continue
        if path.is_symlink():
            raise KitError(f'Package contains a symlink: {rel}')
        if path.is_file():
            files[rel] = digest(path)
    return files


def validate_package(source):
    # Run the current, trusted structural validator against data in the source.
    spec = importlib.util.spec_from_file_location('crm_pack_validator', KIT / 'scripts/validate_reference_pack.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    errors, counts = module.validate(source)
    if errors:
        raise KitError('Package validation failed: ' + '; '.join(errors[:8]))
    return counts


def installed_files(source):
    result = {}
    for rel in package_files(source):
        data = (source / rel).read_bytes()
        if rel == 'SKILL.md':
            text = data.decode()
            text, count = re.subn(r'^name: crm-specification-standard$', 'name: crm-spec-kit', text, count=1, flags=re.M)
            if not count and not re.search(r'^name: crm-spec-kit$', text, re.M):
                raise KitError('Unexpected root skill name')
            data = text.encode()
        result[rel] = data
    return result


def snapshot(data):
    hashes = {rel: hashlib.sha256(content).hexdigest() for rel, content in data.items()}
    overall = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    return hashes, overall


def write_package(source, target):
    data = installed_files(source)
    hashes, overall = snapshot(data)
    for rel, content in data.items():
        path = relative(target, rel)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    receipt = {'schema_version':1, 'kit_id':'crm-specification-standard',
               'installed_skill':'crm-spec-kit', 'version':read_json(source/'reference-manifest.json')['version'],
               'snapshot_sha256':overall, 'files':hashes}
    (target / RECEIPT).write_text(json_text(receipt), encoding='utf-8')
    return receipt


def integrity(root):
    receipt = read_json(root / RECEIPT)
    if receipt.get('kit_id') != 'crm-specification-standard' or not isinstance(receipt.get('files'),dict):
        raise KitError('Unknown package ownership receipt')
    actual = package_files(root)
    if receipt.get('version') != read_json(root/'reference-manifest.json').get('version'):
        raise KitError('Receipt version does not match installed manifest')
    if actual != receipt['files']:
        changed = sorted(set(actual) ^ set(receipt['files']) | {k for k in actual.keys() & receipt['files'].keys() if actual[k] != receipt['files'][k]})
        raise KitError('Package drift: ' + ', '.join(changed[:12]))
    overall = hashlib.sha256(json.dumps(actual, sort_keys=True).encode()).hexdigest()
    if overall != receipt.get('snapshot_sha256'):
        raise KitError('Invalid snapshot digest')
    return receipt


def destinations(repo, agents):
    choices = ['antigravity','claude'] if agents == 'both' else [agents]
    result = []
    for choice in choices:
        if choice not in AGENT_ROOTS:
            raise KitError('Unknown agent: ' + str(choice))
        rel = AGENT_ROOTS[choice] + '/skills/crm-spec-kit'
        path = relative(repo, rel)
        # resolve() deduplicates an existing internal .claude/skills -> .agents/skills link.
        if path not in [item[1] for item in result]:
            result.append((rel, path))
    return result


def codex_router(repo):
    """Plan a new router or suggest a snippet; never merge existing instructions."""
    snippet = (KIT/'assets/installation/codex-router.md').read_text(encoding='utf-8')
    for rel in ('AGENTS.override.md', 'AGENTS.md'):
        raw = repo/rel
        if raw.is_symlink():
            raise KitError('Root instruction path is a symlink; inspect before router setup: '+rel)
        path = relative(repo, rel)
        if path.exists():
            if not path.is_file():
                raise KitError('Root instruction path is not a file: '+rel)
            content = path.read_text(encoding='utf-8')
            if rel == 'AGENTS.override.md' and not content.strip():
                continue  # Codex skips empty instructions.
            action = 'unchanged' if snippet in content else 'propose-router-addition'
            plan = {'action':action, 'path':rel}
            if action != 'unchanged':
                plan['snippet'] = snippet
                plan['reason'] = 'Existing effective instructions preserved; review this addition against repository rules.'
            return plan, None
    return {'action':'create-router', 'path':'AGENTS.md'}, (repo/'AGENTS.md', snippet)


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix='.crm-spec-kit-write-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as out:
            out.write(json_text(value))
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def install(args):
    repo = args.repo.resolve()
    if not repo.is_dir():
        raise KitError('--repo must be an existing directory')
    if args.with_router and args.agent != 'codex':
        raise KitError('--with-router is a Codex-only opt-in; other adapters keep their existing behavior')
    validate_package(KIT)
    cfgpath = relative(repo, CONFIG)
    original = cfgpath.read_bytes() if cfgpath.exists() else None
    config = load_config(repo) if original is not None else read_json(KIT/'assets/installation/project-config.template.json')
    if not args.workstream and len(config['workstreams']) > 1:
        raise KitError('Multiple workstreams: specify --workstream')
    wsid = args.workstream or (config['workstreams'][0]['id'] if len(config['workstreams']) == 1 else 'default')
    existing = next((w for w in config['workstreams'] if w['id']==wsid), None)
    if existing:
        if args.layout and args.layout != existing.get('layout', 'legacy'):
            raise KitError('Existing layout preserved; use plan-layout before an explicit migration')
        if args.title and args.title != existing.get('title'):
            raise KitError('Existing title differs; edit repo-owned config explicitly')
        if args.spec_root and args.spec_root != existing['spec_root']:
            raise KitError('Existing spec_root differs; edit repo-owned config explicitly, not via install')
        if args.source or args.input_root or args.read_only:
            raise KitError('Existing workstream config is preserved; edit it explicitly to change sources/boundaries')
        ws = existing
    else:
        if config['workstreams'] and not args.spec_root:
            raise KitError('Adding a workstream requires explicit --spec-root')
        sources=[]
        for entry in args.source:
            sid, sep, path = entry.partition('=')
            if not sep:
                raise KitError('--source expects SRC-ID=repo/relative/path')
            sources.append({'id':sid,'path':path,'use':''})
        ws={'id':wsid,'title':args.title or wsid,'spec_root':args.spec_root or 'spec','sources':sources,'read_only':args.read_only,
            'layout':args.layout or 'numbered','record_schema_version':2}
        if args.input_root:
            ws['input_root']=args.input_root
        config['workstreams'].append(ws)
    config_check(repo, config)
    specroot = relative(repo, ws['spec_root'])
    planned, packages, writes, dirs = [], [], [], [specroot] + [relative(specroot, d) for d in scaffold(ws)]
    if ws.get('input_root'):
        dirs.append(relative(repo, ws['input_root']))
    for rel, target in destinations(repo, args.agent):
        if target.exists():
            receipt = integrity(target)
            if receipt['files'] != snapshot(installed_files(KIT))[0]:
                raise KitError('Installed package content differs; use update, not install')
            planned.append({'action':'unchanged','path':rel})
        else:
            packages.append(target); planned.append({'action':'create-package','path':rel})
    for directory in dirs:
        if not directory.resolve().is_relative_to(repo) or directory.is_symlink():
            raise KitError('Scaffold path is a symlink or escapes repo')
        if directory.exists() and not directory.is_dir():
            raise KitError(f'Scaffold path is not a directory: {directory.relative_to(repo)}')
        if not directory.exists():
            planned.append({'action':'create-directory','path':directory.relative_to(repo).as_posix()})
    rules = {
      specroot/'AGENTS.md': (KIT/'assets/installation/scoped-instructions.md').read_text(encoding='utf-8'),
      specroot/'CLAUDE.md': (KIT/'assets/installation/claude-import.md').read_text(encoding='utf-8'),
    }
    for directory in dirs:
        if directory != specroot:
            rules[directory/'.crm-spec-kit-keep'] = 'CRM scaffold marker. This is not a requirement or approval.\n'
    for path, text in rules.items():
        if path.is_symlink():
            raise KitError('Scoped instruction path is a symlink; inspect before install')
        if path.exists():
            action = 'unchanged' if path.read_text(encoding='utf-8')==text else 'preserve-existing-instructions'
            planned.append({'action':action,'path':path.relative_to(repo).as_posix()})
        else:
            writes.append((path,text));planned.append({'action':'create-file','path':path.relative_to(repo).as_posix()})
    if args.with_router:
        router, addition = codex_router(repo)
        planned.append(router)
        if addition:
            path, text = addition
            protected = ws.get('read_only', []) + [s['path'] for s in ws.get('sources', [])]
            if any(overlaps(path, relative(repo, raw)) for raw in protected):
                raise KitError('Codex router overlaps a source/read_only path')
            writes.append((path, text))
    config_changed = original is None or json.loads(original) != config
    if config_changed:
        planned.append({'action':'create-config' if original is None else 'add-workstream','path':CONFIG})
    check_write_boundaries(repo,config,dirs + packages + [path for path,_ in writes] + ([cfgpath] if config_changed else []))
    output={'mode':'apply' if args.apply else 'dry-run','workstream':wsid,'artifact_paths':artifact_paths(ws),'plan':planned}
    if not args.apply:
        return output
    created_files, created_dirs, created_packages=[] ,[],[]
    def mkdir(path):
        missing=[];node=path
        while not node.exists():missing.append(node);node=node.parent
        for item in reversed(missing):item.mkdir();created_dirs.append(item)
    try:
        for target in packages:
            mkdir(target.parent)
            with tempfile.TemporaryDirectory(prefix='.crm-spec-kit-stage-',dir=target.parent) as temp:
                stage=Path(temp)/'package';stage.mkdir();write_package(KIT,stage)
                if target.exists():raise KitError('Install target appeared concurrently; retry after doctor')
                os.rename(stage,target);created_packages.append(target)
        for directory in dirs:mkdir(directory)
        for path,text in writes:
            with path.open('x',encoding='utf-8') as out:out.write(text)
            created_files.append(path)
        if config_changed:
            if (cfgpath.read_bytes() if cfgpath.exists() else None) != original:
                raise KitError('Config changed concurrently; no overwrite')
            mkdir(cfgpath.parent);atomic_json(cfgpath,config)
    except Exception:
        for path in created_files:path.unlink(missing_ok=True)
        for path in created_packages:shutil.rmtree(path)
        for path in reversed(created_dirs):
            with contextlib.suppress(OSError):path.rmdir()
        raise
    output['note']=('Existing shared instructions preserved; a missing root router is created only with --agent codex --with-router. '
                    if args.with_router else 'No shared repository instructions changed. ')
    output['note']+='Runtime skill/rule discovery still requires a fresh-session smoke test.'
    return output


def doctor(args):
    repo=args.repo.resolve();checks=[]
    def add(level,code,message):checks.append({'level':level,'code':code,'message':message})
    try:
        config=load_config(repo,args.config);add('INFO','config','Config paths/boundaries valid')
    except KitError as exc:
        return {'checks':[{'level':'ERROR','code':'config','message':str(exc)}],'healthy':False}
    try:validate_package(KIT);add('INFO','kit-structure','Structural validator passed')
    except KitError as exc:add('ERROR','kit-structure',str(exc))
    receipts=[]
    selected = getattr(args, 'agent', None)
    try:
        locations = [rel for rel, _ in destinations(repo, selected)] if selected else ['.agents/skills/crm-spec-kit','.claude/skills/crm-spec-kit']
    except KitError as exc:
        add('ERROR','adapter-integrity',str(exc))
        return {'healthy':False,'runtime_verified':False,'checks':checks}
    for rel in locations:
        try:
            path=relative(repo,rel)
            if not path.exists():
                add('ERROR' if selected else 'WARN','adapter-not-present',rel);continue
            receipt=integrity(path);receipts.append(receipt['snapshot_sha256']);add('INFO','package-integrity',rel+' matches receipt')
            if not re.search(r'^name: crm-spec-kit$',(path/'SKILL.md').read_text(),re.M):
                add('ERROR','adapter-name',rel)
        except KitError as exc:add('ERROR','adapter-integrity',str(exc))
    if not receipts:add('ERROR','installation','No managed installation; inspect legacy wrappers before install (see INSTALL.md migration guide)')
    if len(set(receipts))>1:add('ERROR','adapter-drift','Installed copies differ')
    for ws in config['workstreams']:
        root=relative(repo,ws['spec_root'])
        for directory in scaffold(ws):
            if not (root/directory).is_dir():add('ERROR','scaffold',ws['id']+': missing '+directory)
        scoped = ('CLAUDE.md',) if selected == 'claude' else ('AGENTS.md',) if selected in {'codex','antigravity'} else ('AGENTS.md','CLAUDE.md')
        for file in scoped:
            if not (root/file).is_file():add('WARN','scoped-instructions',ws['id']+': missing '+file)
            elif 'CRM' not in (root/file).read_text(encoding='utf-8'):add('WARN','existing-instructions',ws['id']+': review existing '+file+' for conflicts')
        for source in ws['sources']:
            if not relative(repo,source['path']).exists():add('WARN','source-missing',ws['id']+': '+source['id']+' '+source['path'])
    if selected == 'codex':
        try:
            router, _ = codex_router(repo)
            if router['action'] == 'create-router':
                add('WARN','router-not-present','Optional root router absent; explicit skill invocation can still be used. See BOOTSTRAP.md.')
            elif router['action'] == 'propose-router-addition':
                add('WARN','router-review',router['path']+': no exact kit router snippet; inspect effective routing, not an automatic failure')
            else:
                add('INFO','router-present',router['path']+': kit router snippet present; semantic compatibility still requires review')
        except (KitError, OSError) as exc:
            add('WARN','router-review',str(exc))
    add('WARN','runtime-not-verified','Filesystem presence is not proof of skill/rule discovery. Run a fresh-session smoke test for each tool/version.')
    try:
        result=subprocess.run(['git','-C',str(repo),'status','--porcelain','--untracked-files=normal'],capture_output=True,text=True,check=False)
        if result.returncode==0:
            if result.stdout.strip():add('WARN','working-tree','Repository has uncommitted changes; review before distributing. No commit was made.')
        else:add('WARN','git-not-verified','Repository is not a verified git working tree')
    except OSError:add('WARN','git-not-available','Git status not checked')
    return {'healthy':not any(c['level']=='ERROR' for c in checks),'runtime_verified':False,'checks':checks}


def smoke_prompt(args):
    """Generate a read-only fresh-session probe; do not execute it or claim discovery."""
    if not args.target or not args.revision:
        raise KitError('smoke-prompt requires a nonempty target and revision')
    probe = argparse.Namespace(**(vars(args) | {'reference':[], 'full':False, 'format':'json'}))
    bundle = context(probe)
    rel, package = destinations(args.repo.resolve(), args.agent)[0]
    receipt = integrity(package)
    data = {'agent':args.agent, 'skill':'crm-spec-kit', 'package_root':rel,
            'package_version':receipt['version'], 'package_snapshot_sha256':receipt['snapshot_sha256'],
            'function':bundle['function'], 'profile':bundle['profile'],
            'workstream':bundle['workstream']['id'], 'spec_root':bundle['workstream']['spec_root'],
            'target':bundle['target'], 'target_kind':bundle['target_kind'], 'input_revision':bundle['input_revision']}
    template = (KIT/'assets/installation/smoke-test-prompt.md').read_text(encoding='utf-8')
    prompt = template.replace('{{CONTEXT_JSON}}',json_text(data).rstrip())
    if args.agent == 'codex':
        prompt = '$crm-spec-kit\n\n'+prompt
    evidence = {'tool':args.agent,'tool_version':None,'observed_at':None,
                'context':data,'observed_output':None,'target_hashes_before':{},'target_hashes_after':{},
                'runtime_verified':False,'verdict':'Chưa kiểm',
                'note':'Fill only from an observed fresh session. Prompt generation is not runtime discovery or approval.'}
    result = {'prompt':prompt,'evidence_template':evidence,'runtime_verified':False}
    return result if args.format == 'json' else prompt+'\n\n## Evidence template — chưa quan sát\n\n'+json_text(evidence)


def section(text, title):
    match=re.search(r'^## '+re.escape(title)+r'\s*\n(.*?)(?=^## |\Z)',text,re.M|re.S)
    return match.group(1).strip() if match else ''


def context(args):
    repo=args.repo.resolve();config=load_config(repo,args.config);ws=select_stream(config,args.workstream)
    manifest=read_json(KIT/'reference-manifest.json')
    function=next((f for f in manifest['functions'] if f['id']==args.function),None)
    if not function:raise KitError('Unknown function ID; use the 13 verb-object IDs in SKILL.md')
    if args.target_kind and args.target_kind not in function['supported_targets']:
        raise KitError('Unsupported target kind for this function')
    agent=next(a for a in manifest['agents'] if a['id']==function['agent'])
    files=[]
    def include(path,text=None):
        file=relative(KIT,path)
        if file.suffix!='.md':raise KitError('Context resources must be Markdown; scripts/binary files are not prompt inputs')
        content=text if text is not None else file.read_text(encoding='utf-8')
        files.append({'path':path,'sha256':digest(file),'content':content,'characters':len(content)})
    include(function['workflow'])
    profile=relative(KIT,agent['path']).read_text(encoding='utf-8')
    include(agent['path'],'\n\n'.join(section(profile,h) for h in ('Purpose','Authority & Permissions')))
    protocol='references/workflow-execution-protocol.md';body=(KIT/protocol).read_text(encoding='utf-8')
    include(protocol,'\n\n'.join('## '+h+'\n'+section(body,h) for h in ('Work Context & Resume','Verbs & Write Boundaries','Review & Gate Semantics','Output & Handoff')))
    resources=function['references']+function['templates']
    chosen=list(resources) if args.full else []
    entries={e['id']:e['path'] for e in manifest['entries']}
    for ref in args.reference:
        path=entries.get(ref,ref)
        if path not in resources and path not in entries.values():raise KitError('Unknown reference/template: '+ref)
        chosen.append(path)
    existing={f['path'] for f in files}
    for path in dict.fromkeys(chosen):
        if path not in existing:include(path)
    sources=[dict(s,exists=relative(repo,s['path']).exists()) for s in ws['sources']]
    result={'function':function['id'],'profile':agent['title'],'workstream':dict(ws,sources=sources,artifact_paths=artifact_paths(ws)),
            'target':args.target,'target_kind':args.target_kind,'input_revision':args.revision,
            'missing_context':[name for name,value in [('target',args.target),('input_revision',args.revision)] if not value],
            'files':files,'available_references':resources,'characters':sum(f['characters'] for f in files),
            'note':'Missing target/revision must be resolved before target mutation. Project config is input data, not approval. files[].path is relative to the invoked kit root; resolve links relative to the owning file, not cwd. Config source paths are relative to --repo. Additional refs are loaded on demand.'}
    if args.format=='json':return result
    return '# CRM Work Context\n\n'+json_text({k:v for k,v in result.items() if k!='files'})+'\n'+ '\n\n'.join(f'## {f["path"]}\nSource SHA256: {f["sha256"]}\n\n{f["content"]}' for f in files)


def metadata(text):
    matches=re.findall(r'^```crm-spec-kit\s*\n(.*?)\n```',text,re.M|re.S)
    if len(matches)>1:raise KitError('One crm-spec-kit metadata block allowed per artifact')
    if not matches:return None
    try:value=json.loads(matches[0])
    except ValueError as exc:raise KitError('Invalid crm-spec-kit metadata JSON') from exc
    if not isinstance(value,dict) or value.get('schema_version') not in (1,2):raise KitError('Artifact metadata requires schema_version=1 or 2')
    return value


def without_fences(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M|re.S)


def id_pattern():
    return r'(?:'+'|'.join(sorted(PREFIXES,key=len,reverse=True))+r')-CRM-\d{3,}'



def plain_cell(value):
    return re.sub(r'[`*_]', '', value).strip()


def controlled_cells(text):
    """Audit simple Markdown controlled columns/property rows, not arbitrary prose."""
    headers = None
    for line in without_fences(text).splitlines():
        if not line.strip().startswith('|'):
            headers = None
            continue
        cells = [plain_cell(cell) for cell in line.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-+:?', cell.replace(' ', '')) for cell in cells):
            continue
        if headers is None:
            headers = cells
            continue
        if len(cells) != len(headers):
            continue  # complex/escaped tables require structured metadata or human review
        labels = {'status':'Status','decision state':'Decision state','verdict':'Verdict'}
        prop = labels.get(cells[0].lower())
        if prop and len(cells)==2:
            yield prop,cells[1]
        for header, value in zip(headers,cells):
            h=header.lower()
            field='Verdict' if h.startswith('verdict') else labels.get(h)
            if field:
                yield field,value


def legacy_definitions(text):
    found=set(re.findall(r'^# ('+id_pattern()+r')\b',without_fences(text),re.M))
    headers=None
    for line in without_fences(text).splitlines():
        if not line.strip().startswith('|'):
            headers=None
            continue
        cells=[plain_cell(c) for c in line.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-+:?',c.replace(' ','')) for c in cells):continue
        if headers is None:
            headers=cells;continue
        if len(cells)!=len(headers):continue
        if len(cells)==2 and re.fullmatch(r'(?:Feature|Epic|Story|Task|Requirement|Rule|AC|Model|Decision|Baseline|Question) ID',cells[0],re.I):
            if re.fullmatch(id_pattern(),cells[1]):found.add(cells[1])
        for header,value in zip(headers,cells):
            if header.lower() in {'definition id','artifact id','feature id','epic id','story id','task id','requirement id','rule id','ac id','model id','decision id','baseline id','question id'}:
                match=re.match(r'^('+id_pattern()+r')(?:$|\s)',value)
                if match:found.add(match[1])
    return found


def lint(args):
    repo=args.repo.resolve();cfg=load_config(repo,args.config);ws=select_stream(cfg,args.workstream);root=relative(repo,ws['spec_root']);issues=[];definitions={};refs=[]
    def issue(level,code,path,message):issues.append({'level':level,'code':code,'path':path,'message':message})
    if not root.is_dir():raise KitError('spec_root is missing; run install --apply')
    docs={p:p.read_text(encoding='utf-8') for p in root.rglob('*.md') if p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(root)}
    record_support=support('records')
    dirs=artifact_paths(ws)
    kind_dirs=[(dirs[key],kind) for key,kind in [('features','Feature'),('epics','Epic'),('stories','Story'),('tasks','Task')]]
    # Audit both known spellings even during a mixed-layout migration.
    kind_dirs += [(d,kind) for d,kind in [('features','Feature'),('epics','Epic'),('stories','Story'),('tasks','Task'),
                                          ('01-features','Feature'),('02-epics','Epic'),('03-stories','Story'),('04-tasks','Task')]]
    for path,text in docs.items():
        name=path.relative_to(repo).as_posix()
        try:meta=metadata(text)
        except KitError as exc:issue('ERROR','metadata',name,str(exc));meta=None
        visible=without_fences(text)
        inferred_kind=next((kind for directory,kind in kind_dirs if path.is_relative_to(root/directory)),None)
        kind=meta.get('kind') if meta else inferred_kind
        if meta:
            if not isinstance(kind,str) or kind not in {'Feature','Epic','Story','Task','Review','Baseline','Report','Pilot','Project','Decision','Requirement','Model','TestCase','TestRun','Meeting','Assumption','Constraint'}:issue('ERROR','kind',name,'Unknown metadata kind')
            for field,allowed in [('review_verdict',VERDICTS),('decision_state',DECISIONS)]:
                if field in meta and (not isinstance(meta[field],str) or meta[field] not in allowed):issue('ERROR',field,name,'Invalid controlled value')
            if 'review_verdict' in meta and meta['review_verdict']=='N/A' and not meta.get('na_reason'):issue('ERROR','na-reason',name,'N/A requires na_reason; authority still needs human evidence')
            if 'work_status' in meta:
                if not isinstance(kind,str) or kind not in STATUSES:issue('ERROR','work_status',name,'No work_status vocabulary for this kind; Feature is doc-only')
                elif not isinstance(meta['work_status'],str) or meta['work_status'] not in STATUSES[kind]:issue('ERROR','work_status',name,'Status invalid for artifact kind')
            ids=meta.get('defined_ids',[])
            if not isinstance(ids,list) or not all(isinstance(x,str) for x in ids):issue('ERROR','defined_ids',name,'Expected string list');ids=[]
            ids=list(ids)
            ids += record_support.defined_ids(meta)
            if 'artifact_id' in meta:
                if not isinstance(meta['artifact_id'],str):issue('ERROR','artifact_id',name,'Expected string ID')
                else:ids.append(meta['artifact_id'])
            for value in {x for x in ids if isinstance(x,str)}:
                if not re.fullmatch(id_pattern(),value):issue('ERROR','id-format',name,str(value));continue
                definitions.setdefault(value,set()).add(name)
            references=meta.get('references',[])
            if not isinstance(references,list) or not all(isinstance(x,str) for x in references):issue('ERROR','references',name,'Expected relative-link string list');references=[]
            refs.extend((path,href) for href in references)
        elif inferred_kind:
            issue('WARN','legacy-metadata',name,'No structured metadata; only explicit fields/links audited')
        if not meta:
            for value in legacy_definitions(text):definitions.setdefault(value,set()).add(name)
            if re.search(r'^\|\s*ID\s*\|',visible,re.M|re.I):
                issue('WARN','legacy-id-ownership',name,'Generic ID columns may be references; declare definitions in metadata or Definition ID column')
        for field,value in controlled_cells(text):
            allowed=DECISIONS if field=='Decision state' else VERDICTS if field=='Verdict' else STATUSES.get(kind,set().union(*STATUSES.values()))
            if not any(re.match(r'^'+re.escape(v)+r'(?:$|\s|[(:])',value) for v in allowed):
                issue('ERROR','table-'+field,name,'Invalid controlled cell: '+value)
        for field,raw in re.findall(r'^(?:[-*]\s+)?(?:\*\*)?(Status|Decision state|Verdict)(?:\*\*)?:\s*(.+)$',visible,re.M):
            value=raw.strip().strip('`')
            allowed=DECISIONS if field=='Decision state' else VERDICTS if field=='Verdict' else STATUSES.get(kind,set().union(*STATUSES.values()))
            if value not in allowed:issue('ERROR','legacy-'+field,name,'Invalid controlled field: '+value)
        if re.search(r'(?<!\w)(?:/(?:Users|home|private|tmp)/[^\s)\]]+|[A-Za-z]:[\\/][^\s)\]]+)',text):issue('ERROR','absolute-path',name,'Personal/absolute filesystem path in artifact')
        refs.extend((path,href.strip('<>')) for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',visible))
        if ws.get('require_question_for_inferred'):
            for line in visible.splitlines():
                if '[INFERRED]' in line and not re.search(r'\bQ-CRM-\d{3,}\b',line):issue('ERROR','inferred-question',name,'[INFERRED] requires question ID on same line per workstream setting')
    for other in cfg['workstreams']:
        if other['id'] == ws['id']:
            continue
        other_root = relative(repo, other['spec_root'])
        if not other_root.exists():
            continue
        for file in other_root.rglob('*.md'):
            if file.is_symlink() or not file.is_file():
                continue
            try:
                record = metadata(file.read_text(encoding='utf-8'))
            except KitError:
                continue  # The other stream needs its own full lint; do not infer definitions.
            if not record:
                for value in legacy_definitions(file.read_text(encoding='utf-8')):
                    definitions.setdefault(value,set()).add(file.relative_to(repo).as_posix())
                continue
            values = record.get('defined_ids', [])
            values = values if isinstance(values, list) else []
            values = values + [record.get('artifact_id')]
            values += record_support.defined_ids(record)
            for value in {x for x in values if isinstance(x, str) and re.fullmatch(id_pattern(), x)}:
                definitions.setdefault(value, set()).add(file.relative_to(repo).as_posix())
    for value,locations in definitions.items():
        if len(locations)>1:issue('ERROR','duplicate-id',', '.join(sorted(locations)),value)
    for path,href in refs:
        parsed=urlsplit(href)
        if parsed.scheme in {'http','https','mailto'}:continue
        name=path.relative_to(repo).as_posix()
        if parsed.scheme or parsed.netloc or Path(parsed.path).is_absolute() or PureWindowsPath(parsed.path).drive:
            issue('ERROR','link-path',name,'Unsupported or absolute link: '+href);continue
        target=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
        if not target.is_relative_to(repo):issue('ERROR','link-boundary',name,href);continue
        if not target.is_file():issue('ERROR','broken-link',name,href);continue
        if parsed.fragment and target.suffix=='.md':
            mod=load_validator();anchors,_=mod.anchors(target.read_text(encoding='utf-8'))
            if unquote(parsed.fragment) not in anchors:issue('ERROR','broken-anchor',name,href)
    record_result=record_support.audit(globals(), repo, cfg, ws, docs, definitions, issue, args)
    return {'workstream':ws['id'],'files':len(docs),'definitions':len(definitions),'issues':issues,
            'valid':not any(i['level']=='ERROR' for i in issues),'semantic_approval':False,**record_result}


def load_validator():
    spec=importlib.util.spec_from_file_location('crm_validator',KIT/'scripts/validate_reference_pack.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def score(args):
    return support('scoring').run(globals(),args)


def plan_layout(args):
    return support('layout').plan(globals(), args)


def all_used_ids(repo,cfg):
    used=set()
    for ws in cfg['workstreams']:
        root=relative(repo,ws['spec_root'])
        if root.exists():
            for p in root.rglob('*.md'):
                if p.is_file() and not p.is_symlink():used.update(re.findall(r'\b'+id_pattern()+r'\b',p.read_text(encoding='utf-8')))
    ledger=relative(repo,'.agents/crm-spec-kit-id-reservations.json')
    if ledger.exists():used.update(read_json(ledger).get('reservations',{}))
    return used


def next_id(args):
    repo=args.repo.resolve();cfg=load_config(repo)
    if args.prefix not in PREFIXES:raise KitError('Unknown prefix')
    if args.reserve and (not args.apply or not args.owner):raise KitError('--reserve requires --apply and --owner')
    if args.apply and not args.reserve:raise KitError('--apply only valid with --reserve')
    lock=relative(repo,'.agents/crm-spec-kit-id-lock')
    if args.reserve:
        try:lock.mkdir()
        except FileExistsError as exc:raise KitError('ID allocation locked; inspect active/stale lock, do not delete automatically') from exc
    try:
        used=all_used_ids(repo,cfg);prefix=args.prefix+'-CRM-'
        high=max([int(value[len(prefix):]) for value in used if value.startswith(prefix)] or [0])
        value=f'{prefix}{high+1:03}'
        if args.reserve:
            path=relative(repo,'.agents/crm-spec-kit-id-reservations.json')
            ledger=read_json(path) if path.exists() else {'schema_version':1,'reservations':{}}
            ledger['reservations'][value]={'owner':args.owner,'reserved_at':now()};atomic_json(path,ledger)
        return {'id':value,'reserved':args.reserve,'note':'Reservation lock is local to this checkout. Parallel clones need reconciliation/central allocation; lint before merge. Suggestions alone do not reserve an ID.'}
    finally:
        if args.reserve:lock.rmdir()


@contextlib.contextmanager
def update_source(source, ref):
    source=source.resolve()
    if not source.is_dir():raise KitError('--source must be a local trusted kit folder')
    if not ref:
        yield source;return
    if not re.fullmatch(r'[0-9a-fA-F]{40}|[0-9a-fA-F]{64}',ref):raise KitError('--ref requires a full commit SHA')
    try:
        gitroot=Path(subprocess.check_output(['git','-C',str(source),'rev-parse','--show-toplevel'],text=True).strip())
        prefix=source.relative_to(gitroot).as_posix()
        blob=subprocess.check_output(['git','-C',str(gitroot),'archive',ref,'--',prefix])
    except (OSError,subprocess.CalledProcessError,ValueError) as exc:raise KitError('Cannot export pinned local source commit') from exc
    with tempfile.TemporaryDirectory(prefix='crm-spec-kit-source-') as temp:
        dest=Path(temp)
        with tarfile.open(fileobj=io.BytesIO(blob)) as archive:
            for member in archive:
                if member.isdir():continue
                if not member.isfile():raise KitError('Pinned package contains nonregular file')
                name=Path(member.name).relative_to(prefix).as_posix() if prefix!='.' else member.name
                path=relative(dest,name);path.parent.mkdir(parents=True,exist_ok=True)
                path.write_bytes(archive.extractfile(member).read())
        yield dest


def update(args):
    repo=args.repo.resolve();config=load_config(repo)
    target=relative(repo,args.install_path)
    if KIT==target or KIT.is_relative_to(target):raise KitError('Run update using a separate source kit helper, not from inside the installation being replaced')
    old=integrity(target)
    with update_source(args.source,args.ref) as source:
        validate_package(source)
        data=installed_files(source);hashes,overall=snapshot(data)
        changed=sorted(set(hashes)^set(old['files']) | {k for k in hashes.keys()&old['files'].keys() if hashes[k]!=old['files'][k]})
        result={'mode':'apply' if args.apply else 'dry-run','old_version':old['version'],
                'new_version':read_json(source/'reference-manifest.json')['version'],'changed_files':changed,'ref':args.ref,'snapshot_sha256':overall}
        # Retain backups outside every adapter's skills discovery directory.
        key=hashlib.sha256(target.relative_to(repo).as_posix().encode()).hexdigest()[:12]
        if (repo/'.agents/crm-spec-kit-backups').is_symlink():raise KitError('Backup path is a symlink')
        backup_root=relative(repo,'.agents/crm-spec-kit-backups')
        backup=relative(repo,f'.agents/crm-spec-kit-backups/{key}-{old["snapshot_sha256"][:12]}')
        check_write_boundaries(repo,config,[target,backup])
        if backup_root.is_symlink() or backup.is_symlink():raise KitError('Backup path is a symlink')
        result['backup']=backup.relative_to(repo).as_posix()
        if not args.apply or not changed:return result
        # Candidate is treated as data. Never run candidate tests/scripts as part of update.
        if backup.exists():raise KitError('Previous backup exists; inspect it before another update')
        backup_root.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.crm-spec-kit-stage-',dir=backup_root) as temp:
            stage=Path(temp)/'package';stage.mkdir()
            receipt=write_package(source,stage)
            receipt['source_commit']=args.ref
            (stage/RECEIPT).write_text(json_text(receipt),encoding='utf-8')
            integrity(stage);validate_package(stage)
            integrity(target) # recheck local drift immediately before replacing managed files
            os.rename(target,backup)
            try:os.rename(stage,target)
            except Exception:
                os.rename(backup,target);raise
        result['backup']=backup.relative_to(repo).as_posix()
        result['note']='Backup retained. Config/spec artifacts untouched. Other adapter copies must be updated explicitly; doctor detects drift. No network, candidate code, commit or push executed.'
        return result



@contextlib.contextmanager
def operation_lock(repo):
    repo = repo.resolve()
    if not repo.is_dir():
        raise KitError('--repo must be an existing directory')
    parent = relative(repo, '.agents')
    created_parent = not parent.exists()
    parent.mkdir(exist_ok=True)
    lock = relative(repo, '.agents/crm-spec-kit-operation-lock')
    try:
        lock.mkdir()
    except FileExistsError as exc:
        raise KitError('Install/update is locked; inspect an active or stale operation lock') from exc
    try:
        yield
    finally:
        lock.rmdir()
        if created_parent:
            with contextlib.suppress(OSError):
                parent.rmdir()


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    for command in ['install','doctor','context','lint','next-id','update','smoke-prompt','plan-layout','score']:
        s=sub.add_parser(command);s.add_argument('--repo',type=Path,required=True)
        if command in {'install','context','lint','smoke-prompt','plan-layout','score'}:s.add_argument('--workstream')
        if command in {'doctor','context','lint','smoke-prompt','plan-layout','score'}:s.add_argument('--config',type=Path,help='Explicit read-only config for migration/audit; paths still resolve within --repo')
        if command=='install':
            s.add_argument('--agent',choices=[*AGENT_ROOTS,'both'],default='antigravity')
            s.add_argument('--with-router',action='store_true',help='Codex only: create missing root AGENTS.md or print a proposed snippet without merging existing files')
            s.add_argument('--spec-root');s.add_argument('--input-root');s.add_argument('--title')
            s.add_argument('--layout',choices=['legacy','numbered'],help='New workstream defaults to numbered; existing configs are preserved')
            s.add_argument('--source',action='append',default=[]);s.add_argument('--read-only',action='append',default=[]);s.add_argument('--apply',action='store_true')
        elif command=='score':
            s.add_argument('--assessment',help='Repo-relative JSON assessment inventory')
            s.add_argument('--output',help='Explicitly save Markdown report to a new file under workstream reports; never overwrite')
            s.add_argument('--target');s.add_argument('--scope');s.add_argument('--item')
            s.add_argument('--init',action='store_true',help='Emit unknown full-catalog assessment JSON to stdout; no writes')
            s.add_argument('--artifact');s.add_argument('--kind',choices=['Feature','Epic','Story','Requirement']);s.add_argument('--revision')
            s.add_argument('--format',choices=['json','markdown'],default='json')
        elif command=='plan-layout':
            s.add_argument('--to',choices=['legacy','numbered'],default='numbered')
        elif command=='lint':
            s.add_argument('--gate',choices=['draft','readiness','baseline'],default='draft')
            s.add_argument('--target',help='Limit record-obligation gate checks to the dependency closure of this defined ID')
        elif command=='context':
            s.add_argument('function');s.add_argument('--target');s.add_argument('--target-kind');s.add_argument('--revision')
            s.add_argument('--reference',action='append',default=[]);s.add_argument('--full',action='store_true');s.add_argument('--format',choices=['markdown','json'],default='markdown')
        elif command=='doctor':
            s.add_argument('--agent',choices=[*AGENT_ROOTS,'both'],help='Check selected adapters only; omitted preserves the legacy all-copy audit')
        elif command=='smoke-prompt':
            s.add_argument('function');s.add_argument('--agent',choices=list(AGENT_ROOTS),required=True)
            s.add_argument('--target',required=True);s.add_argument('--target-kind',required=True);s.add_argument('--revision',required=True)
            s.add_argument('--format',choices=['markdown','json'],default='markdown')
        elif command=='next-id':
            s.add_argument('prefix');s.add_argument('--reserve',action='store_true');s.add_argument('--owner');s.add_argument('--apply',action='store_true')
        elif command=='update':
            s.add_argument('--source',type=Path,required=True);s.add_argument('--ref');s.add_argument('--install-path',default='.agents/skills/crm-spec-kit');s.add_argument('--apply',action='store_true')
    return p


def main(argv=None):
    if sys.version_info<(3,11):
        print('Python 3.11+ required',file=sys.stderr);return 2
    args=parser().parse_args(argv)
    try:
        handler=globals()[args.command.replace('-','_')]
        if args.command in {'install','update'} and args.apply:
            with operation_lock(args.repo):
                result=handler(args)
        else:
            result=handler(args)
        print(result if isinstance(result,str) else json_text(result),end='' if isinstance(result,str) else '')
        return 1 if isinstance(result,dict) and (result.get('healthy') is False or result.get('valid') is False) else 0
    except (KitError,OSError,ValueError,KeyError,TypeError) as exc:
        print(json_text({'error':str(exc),'command':args.command}),file=sys.stderr,end='');return 2


if __name__=='__main__':
    raise SystemExit(main())
