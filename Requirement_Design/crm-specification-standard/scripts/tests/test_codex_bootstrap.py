"""Codex bootstrap compatibility on disposable repositories; no live runtime calls."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
PACK = Path(__file__).resolve().parents[2]


class CodexBootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='crm-codex-bootstrap-')
        self.base = Path(self.temp.name)
        self.repo = self.base/'repo'
        self.repo.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, command, *args, code=0, repo=None):
        p = subprocess.run([sys.executable,str(PACK/'scripts/kit.py'),command,
                            '--repo',str(repo or self.repo),*args],capture_output=True,text=True)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr)
        return json.loads(p.stderr if code == 2 else p.stdout)

    def install(self, *args, repo=None):
        return self.cli('install','--agent','codex','--workstream','p3',
                        '--spec-root','phase-3/spec',*args,'--apply',repo=repo)

    def hashes(self, repo=None):
        root = repo or self.repo
        return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                for p in root.rglob('*') if p.is_file() and not p.is_symlink()}

    def smoke(self, *args, code=0):
        return self.cli('smoke-prompt','crm-check-readiness','--agent','codex',
                        '--workstream','p3','--target','STORY-CRM-001','--target-kind','Story',
                        '--revision','draft-r1','--format','json',*args,code=code)

    def test_codex_alias_matches_antigravity_bytes_and_reuses_package(self):
        self.install()
        other = self.base/'antigravity';other.mkdir()
        self.cli('install','--agent','antigravity','--workstream','p3',
                 '--spec-root','phase-3/spec','--apply',repo=other)
        self.assertEqual(self.hashes(),self.hashes(other))
        before = self.hashes()
        self.cli('install','--agent','antigravity','--workstream','p3','--apply')
        self.assertEqual(before,self.hashes())
        self.assertEqual(len(list((self.repo/'.agents/skills').rglob('SKILL.md'))),1)

    def test_legacy_defaults_and_both_meaning_unchanged(self):
        self.cli('install','--apply')
        self.assertTrue((self.repo/'.agents/skills/crm-spec-kit').is_dir())
        self.assertFalse((self.repo/'.claude/skills/crm-spec-kit').exists())
        self.assertFalse((self.repo/'AGENTS.md').exists())
        self.cli('install','--agent','both','--apply')
        self.assertTrue((self.repo/'.claude/skills/crm-spec-kit').is_dir())
        self.assertFalse((self.repo/'AGENTS.md').exists())

    def test_codex_does_not_create_root_router_by_default(self):
        self.install()
        self.assertFalse((self.repo/'AGENTS.md').exists())

    def test_router_dry_run_does_not_write(self):
        r = self.cli('install','--agent','codex','--with-router')
        self.assertIn({'action':'create-router','path':'AGENTS.md'},r['plan'])
        self.assertEqual(list(self.repo.iterdir()),[])

    def test_router_opt_in_creates_only_missing_root_and_repeat_is_identical(self):
        (self.repo/'CLAUDE.md').write_text('Existing Claude instructions\n')
        self.install('--with-router')
        router = self.repo/'AGENTS.md'
        self.assertEqual(router.read_bytes(),(PACK/'assets/installation/codex-router.md').read_bytes())
        before = self.hashes()
        self.cli('install','--agent','codex','--workstream','p3','--with-router','--apply')
        self.assertEqual(before,self.hashes())
        self.assertEqual((self.repo/'CLAUDE.md').read_text(),'Existing Claude instructions\n')

    def test_existing_root_is_never_merged_by_apply(self):
        root = self.repo/'AGENTS.md';root.write_text('Existing BA/DDД rules\n')
        r = self.install('--with-router')
        proposal = next(x for x in r['plan'] if x['action']=='propose-router-addition')
        self.assertEqual(proposal['path'],'AGENTS.md')
        self.assertIn('snippet',proposal)
        self.assertEqual(root.read_text(),'Existing BA/DDД rules\n')
        before = self.hashes()
        self.cli('install','--agent','codex','--workstream','p3','--with-router','--apply')
        self.assertEqual(before,self.hashes())

    def test_nonempty_override_prevents_creating_shadowed_router(self):
        override = self.repo/'AGENTS.override.md';override.write_text('Effective custom instructions\n')
        r = self.install('--with-router')
        self.assertFalse((self.repo/'AGENTS.md').exists())
        proposal = next(x for x in r['plan'] if x['action']=='propose-router-addition')
        self.assertEqual(proposal['path'],'AGENTS.override.md')
        self.assertEqual(override.read_text(),'Effective custom instructions\n')

    def test_override_and_root_both_preserved(self):
        for name in ('AGENTS.md','AGENTS.override.md'):
            (self.repo/name).write_text('User instructions '+name+'\n')
        before = self.hashes();r = self.install('--with-router')
        for rel,sha in before.items():self.assertEqual(self.hashes()[rel],sha)
        self.assertEqual(next(x['path'] for x in r['plan'] if x['action']=='propose-router-addition'),'AGENTS.override.md')

    def test_empty_override_does_not_hide_root_router(self):
        (self.repo/'AGENTS.override.md').write_text(' \n')
        self.install('--with-router')
        self.assertTrue((self.repo/'AGENTS.md').is_file())
        self.assertEqual((self.repo/'AGENTS.override.md').read_text(),' \n')

    def test_router_refuses_internal_and_external_instruction_symlinks(self):
        for outside in (False,True):
            with self.subTest(outside=outside):
                root = self.base/('external-case' if outside else 'internal-case');root.mkdir()
                target = (self.base if outside else root)/'instructions.md'
                target.write_text('Do not change\n')
                (root/'AGENTS.md').symlink_to(target)
                r = self.cli('install','--agent','codex','--with-router','--apply',repo=root,code=2)
                self.assertIn('symlink',r['error'])
                self.assertEqual(target.read_text(),'Do not change\n')
                self.assertFalse((root/'.agents/skills/crm-spec-kit').exists())

    def test_router_is_not_created_over_a_protected_path(self):
        r = self.cli('install','--agent','codex','--with-router','--read-only','AGENTS.md','--apply',code=2)
        self.assertIn('source/read_only',r['error'])
        self.assertFalse((self.repo/'AGENTS.md').exists())
        self.assertFalse((self.repo/'.agents/skills/crm-spec-kit').exists())

    def test_root_router_is_codex_only(self):
        for agent in ('antigravity','claude','both'):
            with self.subTest(agent=agent):
                r = self.cli('install','--agent',agent,'--with-router','--apply',code=2)
                self.assertIn('Codex-only',r['error'])
                self.assertEqual(list(self.repo.iterdir()),[])

    def test_selected_doctor_ignores_unused_adapter_and_scoped_file(self):
        self.install('--with-router')
        (self.repo/'phase-3/spec/CLAUDE.md').unlink()
        r = self.cli('doctor','--agent','codex')
        self.assertTrue(r['healthy']);self.assertFalse(r['runtime_verified'])
        codes = {x['code'] for x in r['checks']}
        self.assertNotIn('adapter-not-present',codes)
        self.assertNotIn('scoped-instructions',codes)
        self.assertIn('router-present',codes)
        legacy = self.cli('doctor')
        self.assertTrue(any(x['code']=='adapter-not-present' for x in legacy['checks']))

    def test_selected_claude_doctor_does_not_require_agents_files(self):
        self.cli('install','--agent','claude','--workstream','p3','--spec-root','phase-3/spec','--apply')
        (self.repo/'phase-3/spec/AGENTS.md').unlink()
        r = self.cli('doctor','--agent','claude')
        self.assertTrue(r['healthy'])
        self.assertFalse(any(x['code'] in {'adapter-not-present','scoped-instructions','router-not-present'} for x in r['checks']))

    def test_selected_missing_adapter_is_an_error(self):
        self.cli('install','--agent','claude','--apply')
        r = self.cli('doctor','--agent','codex',code=1)
        self.assertFalse(r['healthy'])
        self.assertTrue(any(x['code']=='adapter-not-present' and x['level']=='ERROR' for x in r['checks']))

    def test_all_copy_audit_still_detects_unselected_drift(self):
        self.cli('install','--agent','both','--apply')
        (self.repo/'.claude/skills/crm-spec-kit/START-HERE.md').write_text('drift\n')
        self.assertTrue(self.cli('doctor','--agent','codex')['healthy'])
        r = self.cli('doctor',code=1)
        self.assertTrue(any(x['code']=='adapter-integrity' for x in r['checks']))

    def test_selected_doctor_handles_escaping_adapter(self):
        self.install()
        target = self.repo/'.claude/skills';target.parent.mkdir()
        target.symlink_to(self.base)
        r = self.cli('doctor','--agent','claude',code=1)
        self.assertTrue(any(x['code']=='adapter-integrity' for x in r['checks']))

    def test_missing_router_is_optional_not_runtime_failure(self):
        self.install()
        r = self.cli('doctor','--agent','codex')
        self.assertTrue(r['healthy'])
        self.assertTrue(any(x['code']=='router-not-present' and x['level']=='WARN' for x in r['checks']))

    def test_existing_router_customization_is_preserved_and_requires_review(self):
        root = self.repo/'AGENTS.md';root.write_text('Project routes manually to crm-spec-kit\n')
        self.install('--with-router')
        r = self.cli('doctor','--agent','codex')
        self.assertTrue(r['healthy'])
        self.assertTrue(any(x['code']=='router-review' for x in r['checks']))

    def test_smoke_prompt_is_read_only_and_not_discovery_evidence(self):
        self.install('--with-router');before = self.hashes()
        r = self.smoke()
        self.assertEqual(self.hashes(),before)
        e = r['evidence_template']
        self.assertFalse(r['runtime_verified']);self.assertFalse(e['runtime_verified'])
        self.assertEqual(e['verdict'],'Chưa kiểm');self.assertIsNone(e['observed_output'])
        self.assertEqual(e['context']['target'],'STORY-CRM-001')
        self.assertEqual(e['context']['input_revision'],'draft-r1')
        self.assertEqual(e['context']['package_root'],'.agents/skills/crm-spec-kit')
        self.assertEqual(e['context']['function'],'crm-check-readiness')
        self.assertIn('$crm-spec-kit',r['prompt'])
        self.assertNotIn('{{CONTEXT_JSON}}',r['prompt'])

    def test_smoke_prompt_works_for_other_adapters_without_codex_syntax(self):
        self.cli('install','--agent','both','--workstream','p3','--spec-root','phase-3/spec','--apply')
        before = self.hashes()
        for agent in ('antigravity','claude'):
            r = self.smoke('--agent',agent)
            self.assertNotIn('$crm-spec-kit',r['prompt'])
            self.assertEqual(r['evidence_template']['context']['agent'],agent)
        self.assertEqual(before,self.hashes())

    def test_smoke_prompt_rejects_empty_revision_and_incompatible_target(self):
        self.install();before = self.hashes()
        self.assertIn('nonempty',self.smoke('--revision','',code=2)['error'])
        self.assertIn('Unsupported target',self.smoke('--target-kind','Capability',code=2)['error'])
        self.assertEqual(before,self.hashes())

    def test_smoke_prompt_requires_managed_package_and_never_installs(self):
        self.install()
        shutil.rmtree(self.repo/'.agents/skills/crm-spec-kit');before = self.hashes()
        self.smoke(code=2)
        self.assertEqual(before,self.hashes())
        self.assertFalse((self.repo/'.agents/skills/crm-spec-kit').exists())

    def test_internal_claude_alias_and_codex_remain_one_package(self):
        (self.repo/'.agents/skills').mkdir(parents=True)
        (self.repo/'.claude').mkdir()
        (self.repo/'.claude/skills').symlink_to('../.agents/skills')
        self.install('--with-router');before = self.hashes()
        self.cli('install','--agent','both','--workstream','p3','--apply')
        self.assertEqual(before,self.hashes())
        self.assertEqual(len(list((self.repo/'.agents/skills').rglob('SKILL.md'))),1)
        r = self.cli('doctor','--agent','both')
        self.assertTrue(r['healthy'])


if __name__ == '__main__':
    unittest.main()
