"""Explicit project-wide clean reset; no archives or saved artifact contents."""
import hashlib
import json
from pathlib import Path

INSTRUCTIONS = {'AGENTS.md', 'AGENTS.override.md', 'CLAUDE.md'}
LEDGER = '.agents/crm-spec-kit-id-reservations.json'


def plan(api, repo, cfg):
    error = api['KitError']
    roots = [ws['spec_root'] for ws in cfg['workstreams']]
    extra = cfg.get('generated_output_paths', [])
    if not isinstance(extra, list) or any(not isinstance(p, str) for p in extra):
        raise error('generated_output_paths must be a list of repo-relative owned output paths')
    roots += extra
    protected = [api['CONFIG'], '.git', '.agents', '.claude', '.codex']
    # Also protect the executing kit, including a source kit located inside repo.
    kit = api['KIT'].resolve()
    if kit.is_relative_to(repo):
        protected.append(kit.relative_to(repo).as_posix())
    resolved = []
    for raw in roots:
        target = api['relative'](repo, raw)
        for part in Path(raw).parts:
            if part.startswith('.'):
                raise error('Reset outputs cannot use hidden/tool paths: ' + raw)
        current = repo
        for part in Path(raw).parts:
            current /= part
            if current.is_symlink():
                raise error('Reset refuses symlink paths: ' + raw)
        if any(api['overlaps'](target, api['relative'](repo, p)) for p in protected):
            raise error('Reset output overlaps instructions/config/tools: ' + raw)
        if any(api['overlaps'](target, old) for old in resolved):
            raise error('Reset output paths must not overlap: ' + raw)
        resolved.append(target)
    api['check_write_boundaries'](repo, cfg, resolved)
    # Find identifiable CRM outputs left outside declared ownership. Never delete
    # them heuristically: require an explicit generated_output_paths entry.
    ignored = [api['relative'](repo, p) for p in ('.git', '.agents', '.claude', '.codex')]
    if kit.is_relative_to(repo):
        ignored.append(kit)
    for ws in cfg['workstreams']:
        ignored += [api['relative'](repo, p) for p in ws.get('read_only', [])]
        ignored += [api['relative'](repo, x['path']) for x in ws.get('sources', [])]
        if ws.get('input_root'):
            ignored.append(api['relative'](repo, ws['input_root']))
    unowned = []
    # Prune protected directories instead of reading source/baseline trees.
    import os
    for parent, dirs, names in os.walk(repo, followlinks=False):
        base = Path(parent)
        dirs[:] = [d for d in dirs if not (base/d).is_symlink()
                   and not any((base/d).resolve().is_relative_to(q) for q in ignored + resolved)]
        for name in names:
            path = base/name
            if path.is_symlink() or not path.is_file() or name in INSTRUCTIONS:
                continue
            if any(path.resolve().is_relative_to(q) for q in ignored + resolved):
                continue
            if name.endswith(('.md', '.md.txt', '.json')):
                content = path.read_text(encoding='utf-8', errors='replace')
                generated = '```crm-spec-kit' in content
                if name.endswith('.json'):
                    try:
                        value = json.loads(content)
                        generated = (name == 'historical-ids.json' or isinstance(value, dict)
                                     and (str(value.get('policy', '')).startswith('crm-definition-')
                                          or value.get('kind') in ('Epic','Capability','Story','Task','Review','Report')))
                    except ValueError:
                        pass
                if generated:
                    unowned.append(path.relative_to(repo).as_posix())
    if unowned:
        raise error('CRM outputs outside reset ownership; declare generated_output_paths or classify as read-only inputs: '
                    + ', '.join(sorted(unowned)))
    files, directories, retained = {}, set(), []
    for target in resolved:
        entries = [target, *target.rglob('*')] if target.is_dir() else [target]
        for path in entries:
            if path.is_symlink():
                raise error('Reset refuses symlinks before any deletion: ' + path.relative_to(repo).as_posix())
            if not path.exists():
                continue
            name = path.relative_to(repo).as_posix()
            if path.is_dir():
                directories.add(name)
            elif not path.is_file():
                raise error('Reset refuses special files: ' + name)
            elif path.name in INSTRUCTIONS:
                retained.append(name)
            else:
                files[name] = api['digest'](path)
    ledger = repo / LEDGER
    if ledger.is_symlink() or ledger.parent.is_symlink():
        raise error('Reset refuses symlink reservation ledger')
    if ledger.exists():
        if not ledger.is_file():
            raise error('Reservation ledger is not a file')
        files[LEDGER] = api['digest'](ledger)
    # A dry-run snapshot includes protected instructions so changed instructions
    # also invalidate apply; none of their bytes are copied into reset output.
    payload = dict(scope='project', workstreams=[w['id'] for w in cfg['workstreams']],
                   output_paths=sorted(set(roots)), delete_files=files,
                   directories=sorted(directories), preserved_instructions=sorted(set(retained)),
                   config_sha256=api['digest'](repo / api['CONFIG']),
                   preserved_instruction_hashes={n:api['digest'](repo/n) for n in set(retained)})
    payload['plan_sha256'] = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    return payload


def run(api, args):
    repo = args.repo.resolve()
    cfg = api['load_config'](repo)
    error = api['KitError']
    # Same allocation lock as next-id; reset must never erase an active lock.
    lock = api['relative'](repo, '.agents/crm-spec-kit-id-lock')
    if lock.exists():
        raise error('ID allocation locked; stop concurrent work or inspect stale lock before reset')
    preview = plan(api, repo, cfg)
    if not args.apply:
        return dict(mode='dry-run', **preview,
                    note='Deletes all configured project outputs and reservations, no archive. Sources/config/kit/instructions remain. Stop other authoring before apply.')
    if not args.plan_sha256 or args.plan_sha256 != preview['plan_sha256']:
        raise error('reset --apply requires matching --plan-sha256 from a fresh dry-run')
    lock.mkdir()
    try:
        # Recheck bytes after allocation lock acquisition, before first deletion.
        fresh = plan(api, repo, cfg)
        if fresh['plan_sha256'] != args.plan_sha256:
            raise error('Reset plan changed; rerun dry-run')
        for name in fresh['delete_files']:
            (repo / name).unlink()
        for name in sorted(fresh['directories'], key=lambda s: len(Path(s).parts), reverse=True):
            path = repo / name
            if path.exists() and not any(path.iterdir()):
                path.rmdir()
        # Keep only empty layout markers; no prior spec/history/approval receipt.
        for ws in cfg['workstreams']:
            root = api['relative'](repo, ws['spec_root'])
            for name in api['scaffold'](ws):
                folder = root / name
                folder.mkdir(parents=True, exist_ok=True)
                (folder / '.crm-spec-kit-keep').write_text('', encoding='utf-8')
        remaining = api['all_used_ids'](repo, cfg)
        if remaining:
            raise error('Reset deleted outputs but verification found remaining IDs; inspect preserved instructions/outputs before Setup')
        return dict(mode='applied', scope='project', workstreams=fresh['workstreams'],
                    deleted_files=len(fresh['delete_files']), output_paths=fresh['output_paths'],
                    preserved_instructions=fresh['preserved_instructions'],
                    next_ids={p:f'{p}-CRM-001' for p in sorted(api['PREFIXES'] - {'MTG'})},
                    archives_created=False, artifacts_restored=False,
                    note='Clean reset verified. Run doctor then context crm-setup-project. No approval/baseline/maturity inherited. No reset receipt persisted.')
    finally:
        lock.rmdir()
