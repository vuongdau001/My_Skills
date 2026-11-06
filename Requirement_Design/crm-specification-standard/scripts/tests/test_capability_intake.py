"""Compatibility and read-only input intake for the Capability workflows."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

KIT = Path(__file__).resolve().parents[2]
CAPABILITY = 'CAP-CRM-001'


class CapabilityIntakeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name)
        self.put('.agents/crm-spec-kit.json', json.dumps(dict(
            schema_version=1, kit_id='crm-specification-standard', id_namespace='CRM',
            workstreams=[dict(id='p3', spec_root='spec', layout='numbered', read_only=[],
                              sources=[dict(id='SRC-WORKSHOP', path='input/workshop.md'),
                                       dict(id='SRC-NOTES', path='input/notes.md'),
                                       dict(id='SRC-MISSING', path='input/missing.md')])])))
        self.capability_path = 'spec/01-capabilities/current.md'

    def put(self, path, text):
        file = self.repo/path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding='utf-8')
        return file

    def put_metadata(self, path, **meta):
        return self.put(path, '# Fixture\n\n```crm-spec-kit\n'+json.dumps(meta)+'\n```\n')

    def cli(self, *args, code=0):
        command = [sys.executable, '-B', str(KIT/'scripts/kit.py'), *args, '--repo', str(self.repo)]
        if args[0] != 'next-id':
            command.extend(['--workstream', 'p3'])
        run = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(run.returncode, code, run.stdout + run.stderr)
        return json.loads(run.stderr if code == 2 else run.stdout)

    def context(self, workflow='crm-define-capability', kind='Capability', *args):
        return self.cli('context', workflow, '--format', 'json', '--target-kind', kind,
                        '--target', 'p3' if kind == 'Project' else CAPABILITY, '--revision', 'r1', *args)

    def test_capability_routes_and_uses_new_layout(self):
        current = self.context()
        self.assertEqual(current['function'], 'crm-define-capability')
        self.assertEqual(current['target_kind'], 'Capability')
        self.assertEqual(current['workstream']['artifact_paths']['capabilities'], '01-capabilities')

    def test_capability_metadata_scoring_and_id(self):
        self.put_metadata(self.capability_path, schema_version=1, kind='Capability',
                          artifact_id=CAPABILITY, revision='r1')
        self.assertTrue(self.cli('lint')['valid'])
        self.assertEqual(self.cli('next-id', 'CAP')['id'], 'CAP-CRM-002')
        assessment = self.cli('score', '--init', '--artifact', self.capability_path, '--kind', 'Capability',
                              '--target', CAPABILITY, '--revision', 'r1', '--scope', 'fixture')
        self.assertEqual(assessment['targets'][0]['kind'], 'Capability')
        self.assertEqual([row['id'] for row in assessment['targets'][0]['items']],
                         [f'C{n:02}' for n in range(1, 9)])
        self.put('assessment.json', json.dumps(assessment))
        self.assertEqual(self.cli('score', '--assessment', 'assessment.json')['targets'][0]['kind'], 'Capability')

    def test_earlier_names_and_prefix_are_rejected(self):
        self.put_metadata(self.capability_path, schema_version=1, kind='Feature',
                          artifact_id='FEAT-CRM-001', revision='r1')
        self.assertEqual({i['code'] for i in self.cli('lint', code=1)['issues']}, {'kind', 'id-format'})
        self.put_metadata(self.capability_path, schema_version=1, kind='Capability',
                          artifact_id='EPIC-CRM-001', revision='r1')
        self.assertIn('capability-id', {i['code'] for i in self.cli('lint', code=1)['issues']})
        self.assertIn('Unknown function', self.cli('context', 'crm-define-feature', code=2)['error'])
        self.assertIn('Unsupported target', self.cli('context', 'crm-define-capability',
                                                      '--target-kind', 'Feature', code=2)['error'])
        self.assertIn('Unknown prefix', self.cli('next-id', 'FEAT', code=2)['error'])

    def test_setup_and_direct_define_share_records_and_source_candidates(self):
        self.put_metadata('spec/00-project/constraints.md', schema_version=2, kind='Project',
                          records=[dict(id='CST-CRM-001', kind='Constraint', revision='r2',
                                        scope='Import', constraint_state='Confirmed')])
        workshop = self.put_metadata('input/workshop.md', schema_version=2, kind='Project',
                                     records=[
                                         dict(id='DEC-CRM-001', kind='Decision', revision='r1',
                                              scope='Customer', decision_state='Approved'),
                                         dict(id='ASM-CRM-001', kind='Assumption', revision='r1',
                                              scope='Customer', assumption_state='Unverified'),
                                     ])
        self.put('input/notes.md', '# Notes\nBA-D7 records a tentative decision.\n')
        self.put('input/handoff.md', '# Handoff\nThe uploaded file size must be limited.\n')
        files_before = {p: p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}
        setup = self.context('crm-setup-project', 'Project', '--input', 'input/handoff.md')
        define = self.context('crm-define-capability', 'Capability', '--input', 'input/handoff.md')
        intake = setup['knowledge_intake']
        self.assertEqual(intake, define['knowledge_intake'])
        self.assertEqual([(r['id'], r['revision']) for r in intake['existing_records']],
                         [('CST-CRM-001', 'r2')])
        sources = {s['path']: s for s in intake['sources']}
        self.assertEqual(sources['input/workshop.md']['source_id'], 'SRC-WORKSHOP')
        self.assertEqual(sources['input/workshop.md']['sha256'], hashlib.sha256(workshop.read_bytes()).hexdigest())
        self.assertEqual([(r['id'], r['declared_state']) for r in sources['input/workshop.md']['candidates']],
                         [('DEC-CRM-001', 'Approved'), ('ASM-CRM-001', 'Unverified')])
        self.assertEqual(sources['input/notes.md']['inspection'], 'review-source')
        self.assertEqual(sources['input/handoff.md']['candidates'], [])
        self.assertEqual(sources['input/missing.md']['inspection'], 'missing')
        self.assertEqual({p: p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}, files_before)
        for bundle in (setup, define):
            self.assertIn('references/knowledge-records-and-evidence.md', {f['path'] for f in bundle['files']})

    def test_input_is_repo_relative_and_limited_to_intake_workflows(self):
        result = self.cli('context', 'crm-setup-project', '--input', '../out.md', code=2)
        self.assertIn('Traversal forbidden', result['error'])
        result = self.cli('context', 'crm-review-specification', '--input', 'input/workshop.md', code=2)
        self.assertIn('--input is available', result['error'])
