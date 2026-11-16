"""Clean reset operates only on disposable project fixtures, never live repos."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

PACK = Path(__file__).resolve().parents[2]


class CleanResetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self.cli('install', '--workstream', 'p3', '--spec-root', 'phase-3/spec', '--apply')

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args, code=0):
        p = subprocess.run([sys.executable, str(PACK/'scripts/kit.py'), *args,
                            '--repo', str(self.repo)], capture_output=True, text=True)
        self.assertEqual(p.returncode, code, p.stdout+p.stderr)
        raw = p.stderr if code == 2 else p.stdout
        return json.loads(raw) if raw.lstrip().startswith('{') else {'error':raw}

    def write(self, path, text):
        p = self.repo/path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def config(self, **changes):
        p = self.repo/'.agents/crm-spec-kit.json'
        c = json.loads(p.read_text())
        c.update(changes)
        p.write_text(json.dumps(c))
        return c

    def hashes(self):
        return {str(p.relative_to(self.repo)):hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.repo.rglob('*') if p.is_file() and not p.is_symlink()}

    def seed(self):
        self.write('phase-3/spec/02-epics/old.md', '# EPIC-CRM-042\n')
        self.write('phase-3/spec/00-project/history/old.md.txt', 'old spec')
        self.write('phase-3/spec/07-reports/score.json', '{"old_score":100}')
        self.cli('next-id', 'EPIC', '--reserve', '--owner', 'test', '--apply')

    def apply(self):
        plan = self.cli('reset', '--scope', 'project')
        return self.cli('reset', '--scope', 'project', '--plan-sha256', plan['plan_sha256'], '--apply')

    def test_dry_run_preserves_every_byte(self):
        self.seed()
        before = self.hashes()
        p = self.cli('reset', '--scope', 'project')
        self.assertIn('.agents/crm-spec-kit-id-reservations.json', p['delete_files'])
        self.assertEqual(before, self.hashes())

    def test_reset_removes_all_outputs_reservations_and_restarts_every_prefix(self):
        self.seed()
        self.write('phase-3/spec/AGENTS.md', 'Keep EPIC-CRM-099 example instruction')
        self.write('sources/ba.md', '# EPIC-CRM-200 input source')
        c = self.config()
        c['workstreams'][0]['sources'] = [{'id':'SRC-BA','path':'sources/ba.md'}]
        self.config(**c)
        self.write('old-output/historical-ids.json', '["EPIC-CRM-111"]')
        self.write('old-output/legacy/old.md', 'history')
        self.config(generated_output_paths=['old-output'])
        protected = {n:h for n,h in self.hashes().items() if n.startswith(('.agents/skills/', 'sources/'))
                     or n in ('.agents/crm-spec-kit.json', 'phase-3/spec/AGENTS.md')}
        result = self.apply()
        self.assertFalse(result['archives_created'])
        self.assertFalse((self.repo/'old-output').exists())
        self.assertFalse((self.repo/'phase-3/spec/00-project/history').exists())
        self.assertFalse((self.repo/'.agents/crm-spec-kit-id-reservations.json').exists())
        for prefix in result['next_ids']:
            self.assertEqual(self.cli('next-id', prefix)['id'], f'{prefix}-CRM-001')
        for n,h in protected.items():
            self.assertEqual(self.hashes()[n], h)
        self.assertTrue(self.cli('doctor')['healthy'])
        self.assertTrue(self.cli('lint', '--workstream', 'p3')['valid'])
        self.apply()  # empty reset is safe too

    def test_all_streams_reset_together_no_workstream_counter(self):
        self.cli('install','--workstream','p4','--spec-root','phase-4/spec','--apply')
        self.seed()
        self.write('phase-4/spec/02-epics/x.md','# EPIC-CRM-080')
        self.apply()
        self.assertEqual(self.cli('next-id','EPIC')['id'],'EPIC-CRM-001')
        self.cli('reset','--scope','project','--workstream','p3',code=2)

    def test_apply_requires_exact_unchanged_plan(self):
        self.seed()
        self.cli('reset','--scope','project','--apply',code=2)
        p = self.cli('reset','--scope','project')
        self.write('phase-3/spec/new.md','changed')
        before = self.hashes()
        self.cli('reset','--scope','project','--plan-sha256',p['plan_sha256'],'--apply',code=2)
        self.assertEqual(before,self.hashes())

    def test_source_readonly_tool_overlap_and_traversal_rejected_before_delete(self):
        self.seed()
        c = self.config()
        c['workstreams'][0]['sources'] = [{'id':'SRC-BA','path':'input/ba.md'}]
        c['workstreams'][0]['read_only'] = ['dev']
        self.config(**c)
        for raw in ('input','dev','../escape','.agents','phase-3','.'):
            self.config(generated_output_paths=[raw])
            before=self.hashes()
            self.cli('reset','--scope','project',code=2)
            self.assertEqual(before,self.hashes())

    def test_symlink_and_active_allocation_lock_refused(self):
        self.seed()
        self.write('unrelated.md','keep')
        link=self.repo/'phase-3/spec/link'
        link.symlink_to(self.repo/'unrelated.md')
        before=self.hashes()
        self.cli('reset','--scope','project',code=2)
        self.assertEqual(before,self.hashes())
        link.unlink()
        (self.repo/'.agents/crm-spec-kit-id-lock').mkdir()
        self.cli('reset','--scope','project',code=2)
        self.assertTrue((self.repo/'phase-3/spec/02-epics/old.md').exists())

    def test_installed_copy_can_reset_without_source_kit(self):
        self.seed()
        helper = self.repo/'.agents/skills/crm-spec-kit/scripts/kit.py'
        def copied(*args):
            p = subprocess.run([sys.executable, str(helper), *args,
                                '--repo', str(self.repo)], capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stdout+p.stderr)
            return json.loads(p.stdout)
        preview = copied('reset', '--scope', 'project')
        copied('reset', '--scope', 'project', '--plan-sha256', preview['plan_sha256'], '--apply')
        self.assertEqual(copied('next-id', 'EPIC')['id'], 'EPIC-CRM-001')
        self.assertTrue(copied('doctor')['healthy'])

    def test_unowned_identifiable_history_blocks_reset(self):
        self.write('legacy/historical-ids.json','["EPIC-CRM-001"]')
        before=self.hashes()
        self.cli('reset','--scope','project',code=2)
        self.assertEqual(before,self.hashes())
        self.config(generated_output_paths=['legacy'])
        self.apply()
        self.assertFalse((self.repo/'legacy').exists())


if __name__ == '__main__':
    unittest.main()
