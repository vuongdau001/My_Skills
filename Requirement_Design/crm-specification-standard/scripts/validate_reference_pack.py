#!/usr/bin/env python3
"""Structural validation only; no network, Jira/CI action or requirements verdict."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile


def unfenced(text):
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            marker = match[1][0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            result.append('')
        else:
            result.append(line if fence is None else '')
    return '\n'.join(result)


def anchors(text):
    visible = unfenced(text)
    explicit = re.findall(r'<a\s+id="([^"]+)"', visible)
    found, seen = set(explicit), {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', visible, re.M):
        heading = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading)
        slug = re.sub(r'[^\w\-\s]', '', heading.lower()).replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        found.add(slug if not count else f'{slug}-{count}')
    return found, explicit


def source_sections(text):
    starts, offset, fence = [(0, 'preamble')], 0, False
    for line in text.splitlines(keepends=True):
        if line.startswith('```'):
            fence = not fence
        if not fence:
            match = re.match(r'^#{2,3} (\d+(?:\.\d+)*|D\d+)\.? (.+)', line)
            if match:
                starts.append((offset, match[1]))
        offset += len(line)
    return {key: text[start:(starts[i+1][0] if i+1 < len(starts) else len(text))]
            for i, (start, key) in enumerate(starts)}


def validate(root):
    root, errors = root.resolve(), []
    try:
        manifest = json.loads((root / 'reference-manifest.json').read_text())
    except (OSError, ValueError) as exc:
        return [f'Manifest unreadable: {exc}'], {}
    texts = {p: p.read_text() for p in root.rglob('*.md')}
    anchor_sets = {}
    for path, text in texts.items():
        found, explicit = anchors(text)
        anchor_sets[path] = found
        if len(explicit) != len(set(explicit)):
            errors.append(f'Duplicate explicit anchor: {path.relative_to(root)}')
        if re.search(r'\[[^]\n]*\[[^]\n]+\]\(', unfenced(text)):
            errors.append(f'Nested Markdown link: {path.relative_to(root)}')
        if re.search(r'/(?:Users|home|tmp|private)/', text):
            errors.append(f'Machine-specific path: {path.relative_to(root)}')
    def resolve(path, fragment='', origin='manifest'):
        full = (root / unquote(path)).resolve()
        if not full.is_relative_to(root):
            errors.append(f'Path outside pack: {origin}: {path}')
        elif not full.is_file():
            errors.append(f'Missing target: {origin}: {path}')
        elif fragment and unquote(fragment) not in anchor_sets.get(full, set()):
            errors.append(f'Missing anchor: {origin}: {path}#{fragment}')
    ids, registered = set(), set()
    for entry in manifest.get('entries', []):
        if entry['id'] in ids:
            errors.append(f'Duplicate manifest ID: {entry["id"]}')
        ids.add(entry['id']); registered.add(entry['path'])
        resolve(entry['path'], entry.get('anchor', ''), entry['id'])
        if not entry.get('title') or entry['title'] == entry['id']:
            errors.append(f'Descriptive title required: {entry["id"]}')
    for prefix, count in [('F',8),('E',16),('S',12),('T',8),('Q',7),('D',10)]:
        expected = {f'{prefix}{i:02}' for i in range(1,count+1)}
        actual = {key for key in ids if re.fullmatch(prefix+r'\d{2}',key)}
        if actual != expected:
            errors.append(f'Catalog inventory mismatch: {prefix}')
    mapping_path = root / 'references/catalog-check-model-mapping.md'
    mapping_text = texts.get(mapping_path, '')
    mapped_items = re.findall(r'^\| ([ES]\d{2}) — ', mapping_text, re.M)
    expected_items = {f'E{i:02}' for i in range(1, 17)} | {f'S{i:02}' for i in range(1, 13)}
    if set(mapped_items) != expected_items or len(mapped_items) != len(expected_items):
        errors.append('E/S review mapping coverage mismatch or duplicate item')
    for path, text in texts.items():
        relative = path.relative_to(root).as_posix()
        if relative.startswith(('references/', 'assets/')) and relative not in registered:
            errors.append(f'Unregistered document: {relative}')
        for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', unfenced(text)):
            href = href.strip().strip('<>'); parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root):
                errors.append(f'Link outside pack: {relative}: {href}')
            else:
                resolve(target.relative_to(root).as_posix(),parsed.fragment,relative)
    try:
        with zipfile.ZipFile(root / manifest['source_archive']) as archive:
            expected_sections = {}
            for source,info in manifest['sources'].items():
                content = archive.read(info['filename'])
                if hashlib.sha256(content).hexdigest() != info['sha256']:
                    errors.append(f'Source snapshot hash mismatch: {source}')
                for section,body in source_sections(content.decode()).items():
                    expected_sections[source,section] = hashlib.sha256(body.encode()).hexdigest()
            mapped = {}
            for item in manifest['migration']:
                key = (item['source'],item['section'])
                if key in mapped:
                    errors.append(f'Duplicate migration section: {key}')
                mapped[key] = item['source_sha256']
                resolve(item['target'],item['anchor'],f'migration {key}')
                for related in item.get('related_targets', []):
                    resolve(related, origin=f'migration detail {key}')
            if mapped != expected_sections:
                errors.append('Migration coverage/hash differs from archived source sections')
    except (OSError,KeyError,zipfile.BadZipFile) as exc:
        errors.append(f'Source archive validation failed: {exc}')
    return errors, {'markdown_documents':len(texts),'manifest_entries':len(ids),
                    'source_sections':len(manifest.get('migration',[]))}


if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    failures,counts = validate(root)
    if failures:
        print('\n'.join('FAIL: '+error for error in failures)); raise SystemExit(1)
    print('PASS — reference pack structure: '+json.dumps(counts))
    print('Not verified: external URLs, CRM approvals, requirement semantics, Jira/CI configuration or runtime tests.')
