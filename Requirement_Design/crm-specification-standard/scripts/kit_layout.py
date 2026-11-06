"""Layout policy and read-only migration planning; no filesystem mutations."""
from pathlib import Path
import hashlib
import json
import os
import re
from urllib.parse import unquote, urlsplit

KEYS = ('project','capabilities','epics','stories','tasks','reviews','baselines','reports','pilot','prototypes')
LEGACY = dict(zip(KEYS, ('00-project','capabilities','epics','stories','tasks','reviews','baselines','reports','pilot','prototypes')))
NUMBERED = dict(zip(KEYS, ('00-project','01-capabilities','02-epics','03-stories','04-tasks','05-reviews','06-baselines','07-reports','08-pilot','09-prototypes')))


def artifact_paths(ws, error=ValueError):
    layout = ws.get('layout', 'legacy')
    if layout not in ('legacy','numbered'):
        raise error('Unknown layout; expected legacy or numbered')
    result = dict(LEGACY if layout == 'legacy' else NUMBERED)
    overrides = ws.get('artifact_paths', {})
    if not isinstance(overrides, dict) or set(overrides) - set(KEYS):
        raise error('artifact_paths must map known artifact categories to relative directories')
    if not ws.get('prototype_gate') and 'prototypes' not in overrides:
        result.pop('prototypes')
    result.update(overrides)
    paths = []
    for raw in result.values():
        if not isinstance(raw, str) or not raw or raw == '.' or '\\' in raw or ':' in raw:
            raise error('Invalid artifact directory')
        p = Path(raw)
        if p.is_absolute() or '..' in p.parts:
            raise error('Artifact directory must stay within spec_root')
        if any(p == old or p.is_relative_to(old) or old.is_relative_to(p) for old in paths):
            raise error('Artifact category directories overlap')
        paths.append(p)
    return result


def plan(api, args):
    repo = args.repo.resolve()
    cfg = api['load_config'](repo, args.config)
    ws = api['select_stream'](cfg, args.workstream)
    root = api['relative'](repo, ws['spec_root'])
    old = artifact_paths(ws, api['KitError'])
    # An explicit migration to a preset removes custom overrides in the candidate only.
    candidate = dict(ws, layout=args.to)
    candidate.pop('artifact_paths', None)
    new = artifact_paths(candidate, api['KitError'])
    moves, mapping, blockers, historical = [], {}, [], []
    for key in KEYS:
        if key not in old:
            continue
        src, dst = root / old[key], root / new.get(key, old[key])
        if src == dst:
            continue
        src_rel, dst_rel = src.relative_to(repo).as_posix(), dst.relative_to(repo).as_posix()
        if dst.exists() or dst.is_symlink():
            blockers.append('Destination already exists: ' + dst_rel)
        if not src.exists():
            moves.append({'category':key,'from':src_rel,'to':dst_rel,'action':'create-empty-category'})
            continue
        if src.is_symlink() or not src.is_dir():
            blockers.append('Source is not a regular directory: ' + src_rel)
            continue
        moves.append({'category':key,'from':src_rel,'to':dst_rel,'action':'move-directory'})
        for p in sorted(src.rglob('*')):
            if p.is_symlink():
                blockers.append('Symlink requires manual inspection: ' + p.relative_to(repo).as_posix())
            elif p.is_file():
                mapping[p] = dst / p.relative_to(src)
    rewrites, pins, hashes = [], [], {}
    moved_hashes = {p:api['digest'](p) for p in mapping}
    hashes.update({p.relative_to(repo).as_posix():sha for p,sha in moved_hashes.items()})
    # Inspect inbound references as well as the moved files, excluding managed tool packages.
    for directory, dirs, names in os.walk(repo, followlinks=False):
        parent = Path(directory)
        dirs[:] = [d for d in dirs if d not in {'.git','__pycache__','node_modules','.venv'}
                   and not (parent/d).is_symlink()
                   and not ((parent/d).relative_to(repo).parts[0] in {'.agents','.claude','.codex'} and d == 'skills')]
        for name in sorted(names):
            p = parent/name
            if p.is_symlink() or p.suffix not in {'.md','.json'}:
                continue
            try:
                text = p.read_text(encoding='utf-8')
            except (UnicodeError, OSError):
                continue
            rel = p.relative_to(repo).as_posix()
            hashes[rel] = api['digest'](p)
            meta = None
            if p.suffix == '.md':
                try:
                    meta = api['metadata'](text)
                except api['KitError']:
                    pass
            if p.is_relative_to(root/old['baselines']) or p.is_relative_to(root/old['pilot']) or (meta and meta.get('kind') in {'Baseline','Review','Pilot'}):
                historical.append(rel)
            # JSON and inline canonical locators can pin a path or digest without a Markdown link.
            mentioned = [str(src.relative_to(repo).as_posix()) for src in mapping
                         if src.relative_to(repo).as_posix() in text or moved_hashes[src] in text]
            if mentioned:
                pins.append({'path':rel,'references_to_moved_files':mentioned,'action':'inspect-locators-and-revision-pins'})
            links = re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)',text) if p.suffix == '.md' else []
            # Include structured reference path strings; unrelated strings are ignored by target resolution.
            links += re.findall(r'"(?:path|references)"\s*:\s*"([^"\n]+)"',text)
            if meta and isinstance(meta.get('references'),list):
                links += [v for v in meta['references'] if isinstance(v,str)]
            for href in sorted(set(links)):
                url = urlsplit(href)
                if url.scheme or url.netloc or Path(url.path).is_absolute():
                    continue
                target = (p.parent/unquote(url.path)).resolve() if url.path else p
                if target not in mapping and p not in mapping:
                    continue
                new_source, new_target = mapping.get(p,p), mapping.get(target,target)
                rewritten = Path(os.path.relpath(new_target,new_source.parent)).as_posix()
                rewritten += ('#'+url.fragment) if url.fragment else ''
                if rewritten != href:
                    rewrites.append({'path':rel,'new_path':new_source.relative_to(repo).as_posix(),
                                     'old_link':href,'suggested_link':rewritten})
    candidate_cfg = json.loads(json.dumps(cfg))
    index = next(i for i,w in enumerate(cfg['workstreams']) if w['id'] == ws['id'])
    candidate_cfg['workstreams'][index] = candidate
    material = {'config':cfg,'hashes':hashes,'moves':moves,'rewrites':rewrites}
    return {'mode':'dry-run','workstream':ws['id'],'from_layout':ws.get('layout','legacy'),'to_layout':args.to,
            'moves':moves,'link_rewrites':rewrites,'locator_or_hash_impacts':pins,
            'historical_records_to_preserve':sorted(historical),'blockers':blockers,
            'candidate_config':candidate_cfg,'snapshot_sha256':hashlib.sha256(json.dumps(material,sort_keys=True).encode()).hexdigest(),
            'automatic_apply_supported':False,
            'note':'Plan only; no files/config/receipts changed. Link suggestions are not a complete parser for prose or embedded scripts. Preserve historical records and pinned snapshots at their original paths (or an explicitly reviewed archive); do not rewrite old approval/hash receipts. A separately authorized migration must reconcile every inbound reference, re-review changed revisions and rerun doctor/lint. No apply flag is provided.'}
