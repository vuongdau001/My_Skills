"""Exercise real Git hooks and bypass detection on isolated disposable repositories."""
from pathlib import Path
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

PACK=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('crm_commits_test',PACK/'scripts/kit_commits.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
VALID='fix(records): giữ đúng revision của review\n\nWhy: Target thay đổi làm review cũ mất hiệu lực.\nValidation: Chạy fixture stale revision và kiểm kết quả.\n'

class CommitPolicyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.repo=Path(self.temp.name).resolve()/'repo';self.repo.mkdir()
        self.git('init','-q');self.git('config','user.name','Fixture');self.git('config','user.email','fixture@example.invalid')
        self.dest=self.repo/'.agents/skills/crm-spec-kit'
        (self.dest/'scripts').mkdir(parents=True);(self.dest/'assets/installation').mkdir(parents=True)
        for n in ['commit_policy.py','kit_commits.py']:shutil.copyfile(PACK/'scripts'/n,self.dest/'scripts'/n)
        shutil.copyfile(PACK/'assets/installation/commit-policy.json',self.dest/'assets/installation/commit-policy.json')
        self.tool=self.dest/'scripts/commit_policy.py'

    def git(self,*args,code=0):
        env=dict(os.environ,GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull)
        p=subprocess.run(['git','-C',str(self.repo),*args],capture_output=True,text=True,env=env)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr);return p.stdout.strip()

    def cli(self,*args,code=0):
        env=dict(os.environ,GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull)
        p=subprocess.run([sys.executable,'-B',str(self.tool),*args],capture_output=True,text=True,env=env)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr)
        return json.loads(p.stdout if p.stdout else p.stderr)

    def enable(self):return self.cli('install-hook','--repo',str(self.repo),'--apply')

    def test_unicode_and_breaking_change_require_migration(self):
        self.assertEqual(module.validate(VALID),[])
        msg=VALID.replace('fix(records):','refactor(layout)!:')
        self.assertTrue(module.validate(msg))
        msg+='\nBREAKING CHANGE: Bỏ category cũ.\n'
        self.assertTrue(module.validate(msg))
        self.assertEqual(module.validate(msg+'Migration: Đối soát consumer trước khi đổi path.\n'),[])

    def test_rejects_vague_missing_fields_and_placeholders(self):
        for msg in ['1','update','fix(records): update\n\nWhy: vì thế\nValidation: chưa chạy\n',VALID.replace('Why:','Reason:'),VALID.replace('kiểm kết quả','<kết quả>')]:
            with self.subTest(message=msg):self.assertTrue(module.validate(msg))

    def test_hook_dry_run_does_not_mutate_and_doctor_observes_activation(self):
        before={str(p):p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}
        self.cli('install-hook','--repo',str(self.repo))
        self.assertEqual(before,{str(p):p.read_bytes() for p in self.repo.rglob('*') if p.is_file()})
        self.assertEqual(self.cli('doctor','--repo',str(self.repo))['checks'][0]['code'],'commit-hook-not-enabled')
        self.enable()
        self.assertEqual(self.cli('doctor','--repo',str(self.repo))['checks'][0]['code'],'commit-hook-enabled')
        self.assertEqual(self.enable()['action'],'unchanged')

    def test_real_commit_rejected_then_valid_message_accepted(self):
        self.enable()
        self.git('commit','--allow-empty','-m','update',code=1)
        self.git('commit','--allow-empty','-m',VALID)
        self.assertEqual(self.git('show','-s','--format=%B','HEAD'),VALID.strip())

    def test_range_catches_non_head_bad_commit_created_by_bypassing_local_hook(self):
        self.enable();self.git('commit','--allow-empty','-m',VALID)
        base=self.git('rev-parse','HEAD')
        self.git('-c','core.hooksPath='+os.devnull,'commit','--allow-empty','-m','update')
        bad=self.git('rev-parse','HEAD')
        self.git('commit','--allow-empty','-m',VALID)
        result=self.cli('range','--repo',str(self.repo),'--base',base,code=1)
        self.assertEqual(result['commits'],2)
        self.assertEqual(result['failures'][0]['commit'],bad)
        self.assertEqual(len(result['failures']),1)

    def test_preserves_existing_hook_and_custom_hook_manager(self):
        hook=self.repo/'.git/hooks/commit-msg';hook.write_text('#!/bin/sh\nexit 0\n');hook.chmod(0o755)
        before=hook.read_bytes();self.cli('install-hook','--repo',str(self.repo),'--apply',code=2)
        self.assertEqual(before,hook.read_bytes())
        custom=self.repo/'.existing-hooks';custom.mkdir()
        self.git('config','core.hooksPath','.existing-hooks')
        self.cli('install-hook','--repo',str(self.repo),'--apply',code=2)
        self.assertEqual(self.git('config','--get','core.hooksPath'),'.existing-hooks')
        self.assertFalse((custom/'commit-msg').exists())

    def test_doctor_detects_non_executable_or_drifted_hook(self):
        self.enable();hook=self.repo/'.git/hooks/commit-msg';hook.chmod(0o644)
        self.assertEqual(self.cli('doctor','--repo',str(self.repo))['checks'][0]['code'],'commit-hook-conflict')
        hook.chmod(0o755);hook.write_text(hook.read_text()+'\nexit 0\n')
        self.assertEqual(self.cli('doctor','--repo',str(self.repo))['checks'][0]['code'],'commit-hook-conflict')

    def test_amend_and_revert_must_satisfy_same_policy(self):
        self.enable();self.git('commit','--allow-empty','-m',VALID)
        self.git('commit','--allow-empty','--amend','-m','done',code=1)
        self.assertEqual(module.validate(VALID.replace('fix(records):','revert(records):')),[])

if __name__=='__main__':unittest.main()
