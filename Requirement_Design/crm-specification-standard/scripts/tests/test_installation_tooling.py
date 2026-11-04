"""Real filesystem/CLI tests in disposable repositories; no network or live repo writes."""
from pathlib import Path
import contextlib
import hashlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode=True
PACK=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('kit_tooling',PACK/'scripts/kit.py')
kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)

class InstallationToolingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='crm-install-test-')
        self.base=Path(self.temp.name);self.repo=self.base/'repo';self.repo.mkdir()
    def tearDown(self):self.temp.cleanup()
    def cli(self,*args,code=0):
        p=subprocess.run([sys.executable,str(PACK/'scripts/kit.py'),*args,'--repo',str(self.repo)],capture_output=True,text=True)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr)
        return json.loads(p.stdout if code!=2 else p.stderr)
    def install(self,*args):return self.cli('install','--workstream','p3','--spec-root','phase-3/spec',*args,'--apply')
    def hashes(self):return {p.relative_to(self.repo).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in self.repo.rglob('*') if p.is_file() and not p.is_symlink()}
    def artifact(self,name,record,body=''):
        f=self.repo/'phase-3/spec'/name;f.parent.mkdir(parents=True,exist_ok=True)
        f.write_text('# Fixture\n\n```crm-spec-kit\n'+json.dumps(record,ensure_ascii=False)+'\n```\n'+body)
        return f
    def candidate(self):
        p=self.base/'candidate';shutil.copytree(PACK,p,ignore=shutil.ignore_patterns('__pycache__'))
        f=p/'reference-manifest.json';m=json.loads(f.read_text());m['version']='1.6.1';f.write_text(json.dumps(m,ensure_ascii=False))
        return p
    def test_dry_run_has_no_writes(self):
        result=self.cli('install','--agent','both');self.assertEqual(result['mode'],'dry-run');self.assertEqual(list(self.repo.iterdir()),[])
    def test_install_copy_adapters_and_scaffold(self):
        self.install('--agent','both')
        for root in ('.agents/skills/crm-spec-kit','.claude/skills/crm-spec-kit'):
            package=self.repo/root;self.assertFalse(package.is_symlink())
            self.assertEqual(len(list(package.rglob('SKILL.md'))),1)
            self.assertIn('name: crm-spec-kit',(package/'SKILL.md').read_text())
        for d in kit.DIRECTORIES:self.assertTrue((self.repo/'phase-3/spec'/d).is_dir())
        result=self.cli('doctor');self.assertTrue(result['healthy']);self.assertFalse(result['runtime_verified'])
    def test_copied_folder_bootstraps_from_its_own_helper(self):
        self.install()
        other=self.base/'fresh repo';other.mkdir()
        target=other/'.agents/skills/crm-spec-kit';target.parent.mkdir(parents=True)
        shutil.copytree(self.repo/'.agents/skills/crm-spec-kit',target)
        result=subprocess.run([sys.executable,str(target/'scripts/kit.py'),'install','--repo',str(other),'--apply'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertTrue((other/kit.CONFIG).is_file())
        self.assertTrue((other/'spec/features').is_dir())
        self.assertEqual(len(list((other/'.agents/skills').rglob('SKILL.md'))),1)
    def test_repeat_install_is_byte_identical(self):
        self.install('--agent','both');before=self.hashes();self.cli('install','--workstream','p3','--agent','both','--apply');self.assertEqual(self.hashes(),before)
    def test_preserve_existing_repo_and_scoped_rules(self):
        for path in ('AGENTS.md','CLAUDE.md','.agents/rules/rulePreFlight.md','phase-3/spec/AGENTS.md'):
            f=self.repo/path;f.parent.mkdir(parents=True,exist_ok=True);f.write_text('Existing owned by the repository\n')
        before=self.hashes();self.install()
        for path,sha in before.items():self.assertEqual(self.hashes()[path],sha)
    def test_refuse_unowned_skill_folder(self):
        f=self.repo/'.agents/skills/crm-spec-kit';f.mkdir(parents=True);(f/'SKILL.md').write_text('existing skill')
        self.cli('install','--apply',code=2);self.assertEqual((f/'SKILL.md').read_text(),'existing skill')
    def test_internal_symlink_deduplicated(self):
        (self.repo/'.agents/skills').mkdir(parents=True);(self.repo/'.claude').mkdir()
        try:(self.repo/'.claude/skills').symlink_to('../.agents/skills',target_is_directory=True)
        except OSError:self.skipTest('Symlink creation not available')
        result=self.install('--agent','both');self.assertEqual(sum(x['action']=='create-package' for x in result['plan']),1)
        self.assertTrue(self.cli('doctor')['healthy'])
    def test_external_symlink_rejected(self):
        outside=self.base/'outside';outside.mkdir();(self.repo/'.agents').mkdir()
        try:(self.repo/'.agents/skills').symlink_to(outside,target_is_directory=True)
        except OSError:self.skipTest('Symlink creation not available')
        self.cli('install','--apply',code=2);self.assertEqual(list(outside.iterdir()),[])
    def test_scaffold_symlink_rejected(self):
        outside=self.base/'outside';outside.mkdir();root=self.repo/'phase-3/spec';root.mkdir(parents=True)
        try:(root/'features').symlink_to(outside,target_is_directory=True)
        except OSError:self.skipTest('Symlink creation not available')
        self.cli('install','--workstream','p3','--spec-root','phase-3/spec','--apply',code=2);self.assertEqual(list(outside.iterdir()),[])
    def test_paths_and_readonly_boundaries(self):
        for root in ('../escape','/tmp/escape','C:/escape','.agents/spec'):
            self.cli('install','--spec-root',root,code=2)
        self.cli('install','--spec-root','docs/spec','--read-only','docs',code=2)
    def test_multiple_streams_preserve_config_and_require_selection(self):
        self.install();p=self.repo/kit.CONFIG;cfg=json.loads(p.read_text());cfg['custom_owner_field']='keep me';p.write_text(json.dumps(cfg))
        self.cli('install','--workstream','p4','--spec-root','phase-4/spec','--apply')
        cfg=json.loads(p.read_text());self.assertEqual(cfg['custom_owner_field'],'keep me');self.assertEqual(len(cfg['workstreams']),2)
        self.cli('context','crm-define-feature','--format','json',code=2)
        self.cli('install','--apply',code=2)
    def test_missing_source_is_explicit_warning(self):
        self.install('--source','SRC-FL=input/missing.md');r=self.cli('doctor');self.assertTrue(r['healthy']);self.assertTrue(any(c['code']=='source-missing' for c in r['checks']))
    def test_context_minimal_and_expanded(self):
        self.install();a=self.cli('context','crm-define-feature','--format','json');b=self.cli('context','crm-define-feature','--full','--format','json')
        self.assertLess(a['characters'],b['characters']);self.assertEqual(len(a['files']),3);self.assertIn('target',a['missing_context'])
        self.cli('context','crm-check-readiness','--target-kind','Feature','--format','json',code=2)
        c=self.cli('context','crm-review-specification','--reference','Q03','--format','json');self.assertTrue(any('cross-model-consistency' in f['path'] for f in c['files']))
    def test_lint_controlled_metadata(self):
        self.install();self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature','review_verdict':'Đạt-một-phần'})
        r=self.cli('lint','--workstream','p3',code=1);self.assertTrue(any(x['code']=='review_verdict' for x in r['issues']))
    def test_lint_kind_specific_status(self):
        self.install();self.artifact('epics/a.md',{'schema_version':1,'artifact_id':'EPIC-CRM-001','kind':'Epic','work_status':'review'})
        r=self.cli('lint',code=1);self.assertTrue(any(x['code']=='work_status' for x in r['issues']))
    def test_duplicate_definitions_not_references(self):
        self.install();meta={'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature'}
        self.artifact('features/a.md',meta,'\nMentions FEAT-CRM-001 twice: FEAT-CRM-001\n')
        self.assertTrue(self.cli('lint')['valid']);self.artifact('features/b.md',meta)
        self.assertTrue(any(x['code']=='duplicate-id' for x in self.cli('lint',code=1)['issues']))
    def test_cross_stream_duplicate_definitions(self):
        self.install();self.cli('install','--workstream','p4','--spec-root','phase-4/spec','--apply')
        f=self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature'})
        d=self.repo/'phase-4/spec/features/b.md';d.write_bytes(f.read_bytes())
        r=self.cli('lint','--workstream','p3',code=1);self.assertTrue(any(x['code']=='duplicate-id' for x in r['issues']))
    def test_lint_links_ids_paths_and_legacy_verdict(self):
        self.install();self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-01','kind':'Feature'},'\nVerdict: Đạt-một-phần\n[missing](no.md)\nPersonal: /Users/example/secret.md\n')
        codes={x['code'] for x in self.cli('lint',code=1)['issues']};self.assertTrue({'id-format','legacy-Verdict','broken-link','absolute-path'}<=codes)
    def test_lint_anchor_and_na_reason(self):
        self.install();self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature','review_verdict':'N/A'},'\n[bad](a.md#absent)\n')
        codes={x['code'] for x in self.cli('lint',code=1)['issues']};self.assertTrue({'na-reason','broken-anchor'}<=codes)
    def test_optional_inferred_question_rule(self):
        self.install();cfg=self.repo/kit.CONFIG;data=json.loads(cfg.read_text());data['workstreams'][0]['require_question_for_inferred']=True;cfg.write_text(json.dumps(data))
        self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature'},'\n[INFERRED] missing question\n')
        self.assertTrue(any(x['code']=='inferred-question' for x in self.cli('lint',code=1)['issues']))
    def test_table_verdict_and_legacy_definitions(self):
        self.install()
        root=self.repo/'phase-3/spec/features'
        (root/'a.md').write_text('# FEAT-CRM-001 — A\n\n| Item | Verdict + evidence |\n|---|---|\n| F01 | Đạt-một-phần |\n')
        (root/'b.md').write_text('# FEAT-CRM-001 — B\n')
        codes={x['code'] for x in self.cli('lint',code=1)['issues']}
        self.assertTrue({'table-Verdict','duplicate-id'}<=codes)
    def test_generic_id_column_is_not_a_duplicate_definition(self):
        self.install()
        self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature','defined_ids':['REQ-CRM-001']})
        f=self.repo/'phase-3/spec/features/b.md'
        f.write_text('# FEAT-CRM-002 — Reference\n\n| ID | Applies to this Feature |\n|---|---|\n| REQ-CRM-001 | Shared rule reference |\n')
        result=self.cli('lint');self.assertTrue(result['valid'])
        self.assertTrue(any(x['code']=='legacy-id-ownership' for x in result['issues']))
    def test_explicit_config_audits_without_installing(self):
        root=self.repo/'existing/spec/features';root.mkdir(parents=True)
        (root/'a.md').write_text('# FEAT-CRM-001 — Legacy\n')
        config=self.base/'candidate.json'
        config.write_text(json.dumps({'schema_version':1,'kit_id':'crm-specification-standard','id_namespace':'CRM','workstreams':[{'id':'audit','title':'Audit','spec_root':'existing/spec','sources':[],'read_only':[]}]}))
        result=self.cli('lint','--config',str(config));self.assertTrue(result['valid'])
        self.assertFalse((self.repo/kit.CONFIG).exists());self.assertFalse((self.repo/'.agents').exists())
    def test_next_id_suggestion_reservation_and_lock(self):
        self.install();a=self.cli('next-id','FEAT');b=self.cli('next-id','FEAT');self.assertEqual(a['id'],b['id']);self.assertFalse(a['reserved'])
        a=self.cli('next-id','FEAT','--reserve','--owner','test','--apply');self.assertTrue(a['reserved']);self.assertNotEqual(a['id'],self.cli('next-id','FEAT')['id'])
        (self.repo/'.agents/crm-spec-kit-id-lock').mkdir();self.cli('next-id','FEAT','--reserve','--owner','test','--apply',code=2)
    def test_next_id_scans_all_streams(self):
        self.install();self.cli('install','--workstream','p4','--spec-root','phase-4/spec','--apply')
        (self.repo/'phase-4/spec/features/a.md').write_text('Mention FEAT-CRM-099\n');self.assertEqual(self.cli('next-id','FEAT')['id'],'FEAT-CRM-100')
    def test_doctor_detects_tamper_and_copy_drift(self):
        self.install('--agent','both');f=self.repo/'.claude/skills/crm-spec-kit/START-HERE.md';f.write_text(f.read_text()+'\nchanged\n')
        r=self.cli('doctor',code=1);self.assertTrue(any(x['code']=='adapter-integrity' for x in r['checks']))
    def test_update_dry_run_and_apply_preserve_project(self):
        self.install();source=self.candidate();cfg=(self.repo/kit.CONFIG).read_bytes();artifact=self.artifact('features/a.md',{'schema_version':1,'artifact_id':'FEAT-CRM-001','kind':'Feature'});before=artifact.read_bytes()
        old=(self.repo/'.agents/skills/crm-spec-kit/reference-manifest.json').read_bytes()
        self.cli('update','--source',str(source));self.assertEqual((self.repo/'.agents/skills/crm-spec-kit/reference-manifest.json').read_bytes(),old)
        r=self.cli('update','--source',str(source),'--apply');self.assertEqual(r['new_version'],'1.6.1');self.assertTrue((self.repo/r['backup']).is_dir())
        self.assertEqual((self.repo/kit.CONFIG).read_bytes(),cfg);self.assertEqual(artifact.read_bytes(),before)
    def test_update_refuses_local_changes(self):
        self.install();f=self.repo/'.agents/skills/crm-spec-kit/START-HERE.md';f.write_text(f.read_text()+'\nlocal edit\n')
        self.cli('update','--source',str(self.candidate()),'--apply',code=2)
    def test_update_refuses_bad_candidate(self):
        self.install();source=self.candidate();(source/'START-HERE.md').write_text('[broken](no-such-file.md)')
        self.cli('update','--source',str(source),'--apply',code=2);self.assertTrue(self.cli('doctor')['healthy'])
    def test_update_rollback_on_swap_failure(self):
        self.install();source=self.candidate();real=kit.os.rename;calls=[]
        def rename(a,b):
            calls.append((a,b))
            if len(calls)==2:raise OSError('Injected swap failure')
            return real(a,b)
        args=kit.parser().parse_args(['update','--repo',str(self.repo),'--source',str(source),'--apply'])
        with patch.object(kit.os,'rename',side_effect=rename):
            with self.assertRaises(OSError):kit.update(args)
        self.assertEqual(len(calls),3);self.assertTrue(self.cli('doctor')['healthy'])
    def test_update_does_not_execute_candidate_code(self):
        self.install();source=self.candidate();marker=self.base/'should-not-exist'
        (source/'scripts/validate_reference_pack.py').write_text('from pathlib import Path\nPath('+repr(str(marker))+').write_text("bad")\n')
        self.cli('update','--source',str(source),'--apply');self.assertFalse(marker.exists())
    @unittest.skipUnless(shutil.which('git'),'Git not installed')
    def test_update_pinned_local_commit(self):
        self.install();source=self.candidate()
        subprocess.run(['git','init','--quiet',str(source)],check=True)
        subprocess.run(['git','-C',str(source),'add','.'],check=True)
        subprocess.run(['git','-C',str(source),'-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','--quiet','-m','fixture'],check=True)
        ref=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
        self.cli('update','--source',str(source),'--ref',ref,'--apply')
        receipt=json.loads((self.repo/'.agents/skills/crm-spec-kit'/kit.RECEIPT).read_text());self.assertEqual(receipt['source_commit'],ref)
    @unittest.skipUnless(shutil.which('git'),'Git not installed')
    def test_clean_clone_preserves_integrity_with_autocrlf(self):
        self.install('--agent','both')
        subprocess.run(['git','init','--quiet',str(self.repo)],check=True)
        subprocess.run(['git','-C',str(self.repo),'add','.'],check=True)
        subprocess.run(['git','-C',str(self.repo),'-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','--quiet','-m','fixture installation'],check=True)
        cloned=self.base/'teammate clone'
        subprocess.run(['git','-c','core.autocrlf=true','clone','--quiet','--no-hardlinks',str(self.repo),str(cloned)],check=True,capture_output=True)
        result=subprocess.run([sys.executable,str(PACK/'scripts/kit.py'),'doctor','--repo',str(cloned)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        data=json.loads(result.stdout);self.assertTrue(data['healthy']);self.assertFalse(data['runtime_verified'])
    def test_admin_lock_is_not_silently_removed(self):
        (self.repo/'.agents/crm-spec-kit-operation-lock').mkdir(parents=True);self.cli('install','--apply',code=2)
        self.assertTrue((self.repo/'.agents/crm-spec-kit-operation-lock').exists())

if __name__=='__main__':unittest.main()
