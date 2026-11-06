"""Exercise shared writing context and Markdown footer compatibility on temporary projects."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
PACK = Path(__file__).resolve().parents[2]
TOOL = PACK / 'scripts/kit.py'
STANDARD = 'references/artifact-writing-standard.md'


class ArtifactWritingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='crm-writing-test-')
        self.repo = Path(self.temp.name) / 'repo'
        self.repo.mkdir()
        self.cli('install', '--workstream', 'p3', '--spec-root', 'spec', '--apply')

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args, code=0):
        p = subprocess.run([sys.executable, '-B', str(TOOL), *args, '--repo', str(self.repo)],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, code, p.stdout + p.stderr)
        return json.loads(p.stderr if code == 2 else p.stdout)

    def hashes(self):
        return {p.relative_to(self.repo).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.repo.rglob('*') if p.is_file()}

    def test_all_functions_deliver_same_standard_without_project_writes(self):
        before = self.hashes()
        functions = json.loads((PACK / 'reference-manifest.json').read_text())['functions']
        expected = (PACK / STANDARD).read_text()
        for function in functions:
            with self.subTest(function=function['id']):
                result = self.cli('context', function['id'], '--workstream', 'p3',
                                  '--target', 'fixture', '--target-kind', function['supported_targets'][0],
                                  '--revision', 'r1', '--format', 'json')
                standards = [f for f in result['files'] if f['path'] == STANDARD]
                self.assertEqual(len(standards), 1)
                self.assertEqual(standards[0]['content'], expected)
                self.assertEqual(standards[0]['sha256'], hashlib.sha256(expected.encode()).hexdigest())
                self.assertIn(STANDARD, result['available_references'])
        self.assertEqual(self.hashes(), before)

    def test_full_and_explicit_reference_do_not_duplicate_shared_standard(self):
        result = self.cli('context', 'crm-define-capability', '--workstream', 'p3', '--full',
                          '--reference', 'CRM-ARTIFACT-WRITING', '--format', 'json')
        paths = [f['path'] for f in result['files']]
        self.assertEqual(paths.count(STANDARD), 1)
        self.assertIn('assets/templates/capability-specification-template.md', paths)

    def test_footer_keeps_record_evidence_and_dependency_gate(self):
        root = self.repo / 'spec'
        source = root / 'source.txt'
        source.write_text('Fixture evidence; no real authority approval.\n')
        decision = dict(schema_version=2, kind='Decision', artifact_id='DEC-CRM-001',
                        record=dict(revision='r1', scope='Fixture command', owner=None,
                                    decision_state='Proposed', statement='Unresolved choice',
                                    context='Fixture need', options='A or B', rationale='Need an authority',
                                    consequences='Blocks selected scope', authority=None, decided_at=None,
                                    evidence=[dict(path='../../source.txt', revision='source-r1',
                                                   sha256=hashlib.sha256(source.read_bytes()).hexdigest())],
                                    trace_links=[]))
        story = dict(schema_version=1, kind='Story', artifact_id='STORY-CRM-001', revision='r1',
                     review_verdict='Chưa kiểm', trace_links=[dict(id='DEC-CRM-001',
                        path='../00-project/02-decisions/decision.md', revision='r1', relation='depends-on')])
        for name, meta in [('00-project/02-decisions/decision.md', decision), ('03-stories/story.md', story)]:
            path = root / name
            path.write_text('# Fixture\n\nReadable business content first.\n\n<details>\n'
                            '<summary>Metadata</summary>\n\n```crm-spec-kit\n'
                            + json.dumps(meta) + '\n```\n\n</details>\n')
        before = self.hashes()
        draft = self.cli('lint', '--workstream', 'p3')
        self.assertTrue(draft['valid'])
        self.assertEqual(draft['trace_link_count'], 1)
        gate = self.cli('lint', '--workstream', 'p3', '--gate', 'readiness',
                        '--target', 'STORY-CRM-001', code=1)
        self.assertFalse(gate['valid'])
        self.assertEqual([r['id'] for r in gate['record_obligations']], ['DEC-CRM-001'])
        self.assertEqual(gate['record_obligations'][0]['state'], 'Proposed')
        self.assertEqual(self.hashes(), before)


if __name__ == '__main__':
    unittest.main()
