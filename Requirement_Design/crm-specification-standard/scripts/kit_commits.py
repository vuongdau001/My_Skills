"""Commit policy validation shared by agent preflight, Git hooks and CI (stdlib)."""
from pathlib import Path
import argparse
import json
import os
import re
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKER = '# crm-spec-kit:commit-msg:v1'


def policy():
    return json.loads((ROOT/'assets/installation/commit-policy.json').read_text(encoding='utf-8'))


def validate(message):
    config = policy()
    lines = message.strip().splitlines()
    errors = []
    if not lines:
        return ['Commit message is empty']
    header = lines[0]
    match = re.fullmatch(r'([a-z]+)\(([A-Za-z0-9][A-Za-z0-9._/-]*)\)(!)?: (\S.*)', header)
    if not match:
        errors.append('Expected type(scope)[!]: description')
    else:
        typ, scope, breaking, description = match.groups()
        if typ not in config['types']:
            errors.append('Unsupported type: '+typ)
        if description.strip().lower().rstrip('.') in config['vague_descriptions']:
            errors.append('Describe the actual change; generic update/fix/done is not sufficient')
        if breaking and not re.search(r'^BREAKING CHANGE: \S.+', message, re.M):
            errors.append('Breaking change requires BREAKING CHANGE: impact and Migration: instructions')
    if len(header) > config['header_max_length']:
        errors.append('Header exceeds '+str(config['header_max_length'])+' characters')
    if len(lines) < 3 or lines[1].strip():
        errors.append('Separate header and body with a blank line')
    for field in config['required_fields']:
        if not re.search(r'^'+re.escape(field)+r': \S.+', message, re.M):
            errors.append(field+': requires a concrete nonempty value')
    if re.search(r'^BREAKING CHANGE:', message, re.M):
        if not re.search(r'^Migration: \S.+', message, re.M):
            errors.append('Migration: is required for a breaking change')
    if re.search(r'<[^>\n]+>|\b(?:TODO|TBD)\b', message):
        errors.append('Replace all placeholders before committing')
    return errors


def git(repo, *args):
    result = subprocess.run(['git','-C',str(repo),*args], text=True, capture_output=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or 'Git command failed')
    return result.stdout.strip()


def hook_location(repo):
    repo = Path(git(repo,'rev-parse','--show-toplevel')).resolve()
    configured = git(repo,'config','--get','core.hooksPath') if subprocess.run(
        ['git','-C',str(repo),'config','--get','core.hooksPath'],capture_output=True).returncode == 0 else None
    raw = Path(git(repo,'rev-parse','--git-path','hooks/commit-msg'))
    path = raw if raw.is_absolute() else repo/raw
    return repo, path, configured


def wrapper(repo):
    script = ROOT/'scripts/commit_policy.py'
    if not script.is_relative_to(repo):
        raise ValueError('Install the kit inside this repository before enabling its hook')
    rel = script.relative_to(repo).as_posix()
    return '#!/bin/sh\n'+MARKER+'\n'+'repo=$(git rev-parse --show-toplevel) || exit 2\n'+'exec python3 "$repo"/'+shlex.quote(rel)+' validate --message-file "$1"\n'


def doctor(repo):
    try:
        root, path, configured = hook_location(repo)
        if path.is_symlink() or any(p.is_symlink() for p in path.parents):
            return [dict(level='WARN',code='commit-hook-conflict',message='Hook path uses symlinks; inspect existing hooks manually')]
        if not path.is_file():
            return [dict(level='WARN',code='commit-hook-not-enabled',message='No commit-msg hook at effective Git hook path; commit policy is not locally enforced')]
        actual = path.read_text(encoding='utf-8')
        if actual == wrapper(root) and os.access(path,os.X_OK):
            return [dict(level='INFO',code='commit-hook-enabled',message='Effective executable commit-msg hook matches this kit; remote enforcement not verified')]
        return [dict(level='WARN',code='commit-hook-conflict',message='Existing/custom commit-msg hook preserved; verify manual integration with the shared validator')]
    except (ValueError,OSError,UnicodeError) as exc:
        return [dict(level='WARN',code='commit-hook-unverified',message=str(exc))]


def install_hook(repo, apply=False):
    root, path, configured = hook_location(repo)
    expected = wrapper(root)
    if configured:
        raise ValueError('Existing core.hooksPath preserved; integrate commit_policy.py validate into your hook manager manually')
    if path.is_symlink() or any(p.is_symlink() for p in path.parents):
        raise ValueError('Hook path contains a symlink; no changes made')
    if path.exists():
        if path.is_file() and path.read_text(encoding='utf-8') == expected and os.access(path,os.X_OK):
            return dict(mode='apply' if apply else 'dry-run',action='unchanged',path=str(path))
        raise ValueError('Existing commit-msg hook preserved; integrate validator manually; no overwrite')
    if apply:
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open('x',encoding='utf-8',newline='\n') as f:
            f.write(expected)
        path.chmod(0o755)
    return dict(mode='apply' if apply else 'dry-run',action='create-hook',path=str(path),remote_enforcement_verified=False)


def validate_range(repo, base, head):
    # Resolve user refs to immutable commit IDs before passing a range to Git.
    base_sha=git(repo,'rev-parse','--verify','--end-of-options',base+'^{commit}')
    head_sha=git(repo,'rev-parse','--verify','--end-of-options',head+'^{commit}')
    commits=git(repo,'rev-list','--reverse',base_sha+'..'+head_sha).splitlines()
    failures=[]
    for sha in commits:
        errors=validate(git(repo,'show','-s','--format=%B',sha))
        if errors:failures.append(dict(commit=sha,errors=errors))
    return dict(valid=not failures,commits=len(commits),base=base_sha,head=head_sha,failures=failures)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('validate');p.add_argument('--message-file',type=Path,required=True)
    p=sub.add_parser('range');p.add_argument('--repo',type=Path,required=True);p.add_argument('--base',required=True);p.add_argument('--head',default='HEAD')
    p=sub.add_parser('install-hook');p.add_argument('--repo',type=Path,required=True);p.add_argument('--apply',action='store_true')
    p=sub.add_parser('doctor');p.add_argument('--repo',type=Path,required=True)
    args=parser.parse_args(argv)
    try:
        if args.command=='validate':
            errors=validate(args.message_file.read_text(encoding='utf-8'));result=dict(valid=not errors,errors=errors)
        elif args.command=='range':result=validate_range(args.repo,args.base,args.head)
        elif args.command=='install-hook':result=install_hook(args.repo,args.apply)
        else:result=dict(checks=doctor(args.repo))
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return 1 if result.get('valid') is False else 0
    except (ValueError,OSError,UnicodeError) as exc:
        print(json.dumps(dict(error=str(exc)),ensure_ascii=False),file=sys.stderr)
        return 2
