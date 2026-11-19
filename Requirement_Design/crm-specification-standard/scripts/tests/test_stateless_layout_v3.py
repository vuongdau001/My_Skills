"""Verify retired workflows/categories do not return through install or update."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

PACK=Path(__file__).resolve().parents[2]

class StatelessLayoutV3Tests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.repo=Path(self.temp.name).resolve()

    def cli(self,*args,code=0):
        p=subprocess.run([sys.executable,'-B',str(PACK/'scripts/kit.py'),*args,'--repo',str(self.repo)],text=True,capture_output=True)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr)
        return json.loads(p.stderr if code==2 else p.stdout)

    def install(self):return self.cli('install','--agent','codex','--workstream','p3','--spec-root','spec','--apply')

    def test_new_install_only_scaffolds_current_categories_and_no_hook(self):
        result=self.install();paths=result['artifact_paths']
        self.assertEqual(set(paths),{'project','capabilities','epics','stories','tasks','reviews','prototypes'})
        self.assertEqual(paths['prototypes'],'06-prototypes')
        self.assertEqual(json.loads((self.repo/'.agents/crm-spec-kit.json').read_text())['workstreams'][0]['layout_version'],3)
        for name in ['06-baselines','07-reports','08-pilot','09-prototypes','history','archive']:
            self.assertFalse((self.repo/'spec'/name).exists(),name)
        self.assertFalse((self.repo/'.git/hooks/commit-msg').exists())

    def test_old_workstream_preserves_prototype_path_and_existing_outputs(self):
        self.install();cfg=self.repo/'.agents/crm-spec-kit.json';data=json.loads(cfg.read_text())
        data['workstreams'][0].pop('layout_version');cfg.write_text(json.dumps(data))
        old=self.repo/'spec/07-reports/current.md';old.parent.mkdir();old.write_text('Existing untracked project content')
        config_before=cfg.read_bytes();content_before=old.read_bytes()
        self.cli('install','--agent','codex','--workstream','p3','--apply')
        context=self.cli('context','crm-setup-project','--workstream','p3','--format','json')
        self.assertEqual(context['workstream']['artifact_paths']['prototypes'],'09-prototypes')
        self.assertEqual(config_before,cfg.read_bytes());self.assertEqual(content_before,old.read_bytes())
        doctor=self.cli('doctor','--agent','codex')
        self.assertTrue(doctor['healthy'])
        self.assertIn('retired-categories',{c['code'] for c in doctor['checks']})
        plan=self.cli('plan-layout','--workstream','p3')
        self.assertEqual(plan['candidate_config']['workstreams'][0]['layout_version'],3)
        self.assertIn('spec/07-reports', {v['path'] for v in plan['retired_categories']})
        self.assertTrue(any(m['from']=='spec/09-prototypes' and m['to']=='spec/06-prototypes' for m in plan['moves']))
        self.assertEqual(config_before,cfg.read_bytes());self.assertEqual(content_before,old.read_bytes())

    def test_retired_functions_and_baseline_gate_are_rejected(self):
        self.install()
        for function in ['crm-prepare-baseline','crm-report-status','crm-run-pilot']:
            self.assertIn('Unknown function',self.cli('context',function,'--workstream','p3',code=2)['error'])
        p=subprocess.run([sys.executable,'-B',str(PACK/'scripts/kit.py'),'lint','--repo',str(self.repo),'--workstream','p3','--gate','baseline'],capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
        self.assertIn('invalid choice',p.stderr)
        self.assertIn('retired',self.cli('next-id','BASE',code=2)['error'])

    def test_every_workflow_context_delivers_commit_and_current_state_rules_once(self):
        self.install()
        functions=json.loads((PACK/'reference-manifest.json').read_text())['functions']
        self.assertEqual(len(functions),10)
        for f in functions:
            c=self.cli('context',f['id'],'--workstream','p3','--format','json','--full')
            paths=[row['path'] for row in c['files']]
            for expected in ['references/current-state-and-history.md','references/commit-message-policy.md']:
                self.assertEqual(paths.count(expected),1,(f['id'],expected))

    def test_removed_override_requires_explicit_config_migration(self):
        self.install();cfg=self.repo/'.agents/crm-spec-kit.json';data=json.loads(cfg.read_text())
        data['workstreams'][0]['artifact_paths']={'reports':'07-reports'};cfg.write_text(json.dumps(data))
        before=cfg.read_bytes()
        self.assertIn('artifact_paths',self.cli('context','crm-setup-project','--workstream','p3',code=2)['error'])
        self.assertEqual(before,cfg.read_bytes())

if __name__=='__main__':unittest.main()
