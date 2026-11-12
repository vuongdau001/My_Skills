"""Epic policy lint and context checks in disposable workstreams."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

KIT = Path(__file__).resolve().parents[2]
EPIC = 'EPIC-CRM-001'
LEGACY_CASE = 'MOD-CRM-001'
STORY = 'STORY-CRM-001'
EPIC_PATH = 'spec/02-epics/epic.md'
BODY = """# Epic

## E01 — Scope

<a id="outside"></a>

## E03 — Use Case

<a id="submit"></a>

<a id="commit"></a>

The system stores the request and returns a receipt.
"""


class EpicUseCaseTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name)
        self.put('.agents/crm-spec-kit.json', json.dumps(dict(
            schema_version=1, kit_id='crm-specification-standard', id_namespace='CRM',
            workstreams=[dict(id=identity, spec_root=root, sources=[], read_only=[])
                         for identity, root in [('p3', 'spec'), ('p4', 'next')]])))

    def put(self, relative, content):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        return path

    def artifact(self, relative, meta, body='# Fixture\n'):
        return self.put(relative, body + '\n```crm-spec-kit\n' + json.dumps(meta) + '\n```\n')

    def epic(self, relative=EPIC_PATH, body=BODY, **overrides):
        meta = dict(schema_version=1, kind='Epic', artifact_id=EPIC, revision='r1',
                    epic_policy='use-case-v1',
                    use_case=dict(level='user-goal', locator='#submit'))
        meta.update(overrides)
        return self.artifact(relative, meta, body)

    def legacy_epic(self, relative=EPIC_PATH, **overrides):
        fields = dict(defined_ids=[LEGACY_CASE],
                      use_case=dict(id=LEGACY_CASE, level='user-goal', locator='#submit'))
        return self.epic(relative, **(fields | overrides))

    def story(self, *, revision='r1', locator='#commit', identity=EPIC, relation='derived-from'):
        self.artifact('spec/03-stories/story.md', dict(
            schema_version=2, kind='Story', artifact_id=STORY, revision='r1',
            trace_links=[dict(id=identity, path='../02-epics/epic.md'+locator,
                              revision=revision, relation=relation)]))

    def cli(self, *args, code=0):
        result = subprocess.run([sys.executable, '-B', str(KIT/'scripts/kit.py'), *args,
                                 '--repo', str(self.repo), '--workstream', 'p3'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def codes(self, *args, code=0):
        return {i['code'] for i in self.cli('lint', *args, code=code)['issues']}

    def test_binding_schema_one_and_two(self):
        for version in (1, 2):
            with self.subTest(version=version):
                self.epic(schema_version=version)
                self.story()
                result = self.cli('lint', '--gate', 'readiness', '--target', STORY)
                self.assertEqual(result['issues'], [])
                self.assertEqual(set(result['gate_scope']['dependency_ids']), {STORY, EPIC})

    def test_binding_requires_one_object_with_valid_id_level_and_owner(self):
        cases = [
            (dict(use_case=None), 'epic-use-case'),
            (dict(use_case=[dict(level='user-goal', locator='#submit')]*2), 'epic-use-case'),
            (dict(use_case=dict(id='REQ-CRM-001', level='user-goal', locator='#submit')), 'epic-use-case-owner'),
            (dict(use_case=dict(level='summary', locator='#submit')), 'epic-use-case'),
            (dict(artifact_id='MOD-CRM-009'), 'epic-use-case'),
            (dict(revision=''), 'epic-use-case'),
            (dict(epic_policy='future'), 'epic-policy'),
        ]
        for fields, expected in cases:
            with self.subTest(fields=fields):
                self.epic(**fields)
                self.assertIn(expected, self.codes(code=1))

    def test_duplicate_binding_key_is_invalid_metadata(self):
        path = self.epic()
        body = path.read_text(encoding='utf-8')
        path.write_text(body.replace('"use_case":', '"use_case": {}, "use_case":'), encoding='utf-8')
        self.assertIn('metadata', self.codes(code=1))

    def test_locator_requires_unique_explicit_anchor_inside_e03(self):
        for body in (
            BODY.replace('<a id="submit"></a>', ''),
            BODY.replace('<a id="outside"></a>', '<a id="submit"></a>'),
            BODY.replace('<a id="submit"></a>', '```text\n<a id="submit"></a>\n```'),
            BODY.replace('## E03', '## E10')
        ):
            with self.subTest(body=body):
                self.epic(body=body)
                self.assertIn('epic-use-case-locator', self.codes(code=1))

    def test_anchors_are_local_but_epic_ids_are_unique_across_workstreams(self):
        self.epic(defined_ids=['MOD-CRM-003'])
        other_epic = 'next/02-epics/other.md'
        self.epic(other_epic, artifact_id='EPIC-CRM-002')
        self.assertEqual(self.codes('--target', EPIC), set())
        self.epic(other_epic)
        self.assertIn('duplicate-id', self.codes('--target', EPIC, code=1))

    def test_existing_model_id_is_readable_and_shares_epic_gate_scope(self):
        self.legacy_epic()
        self.story(identity=LEGACY_CASE)
        result = self.cli('lint', '--gate', 'readiness', '--target', STORY)
        self.assertEqual({i['code'] for i in result['issues']}, {'epic-use-case-legacy-id'})
        self.assertEqual(set(result['gate_scope']['dependency_ids']), {STORY, EPIC, LEGACY_CASE})
        self.story(identity=LEGACY_CASE, locator='#outside')
        self.assertIn('trace-use-case-locator', self.codes('--target', STORY, code=1))

    def test_existing_case_id_must_be_defined_once_and_unambiguous(self):
        for declared in ([], [LEGACY_CASE, LEGACY_CASE]):
            self.legacy_epic(defined_ids=declared)
            self.assertIn('epic-use-case-owner', self.codes(code=1))
        self.legacy_epic()
        self.legacy_epic('next/02-epics/duplicate.md', artifact_id='EPIC-CRM-002')
        self.assertTrue({'duplicate-id', 'duplicate-use-case'} <= self.codes('--target', EPIC, code=1))

    def test_legacy_warns_in_draft_and_only_relevant_gate_is_blocked(self):
        self.artifact(EPIC_PATH, dict(schema_version=1, kind='Epic', artifact_id=EPIC, revision='r1'))
        self.put('spec/02-epics/legacy.md', '# EPIC-CRM-099 · Legacy prose\n')
        self.story(identity=EPIC, relation='parent', locator='')
        self.assertIn('epic-legacy', self.codes())
        self.assertIn('epic-legacy', self.codes('--gate', 'readiness', '--target', STORY, code=1))
        self.assertIn('epic-legacy', self.codes('--gate', 'baseline', '--target', 'EPIC-CRM-099', code=1))
        self.epic()
        self.story()
        self.assertNotIn('epic-legacy', self.codes('--gate', 'baseline', '--target', STORY))
        self.assertIn('epic-legacy', self.codes('--gate', 'baseline', code=1))

    def test_verification_link_includes_epic_in_gate_closure(self):
        self.artifact(EPIC_PATH, dict(schema_version=2, kind='Epic', artifact_id=EPIC, revision='r1'))
        self.artifact('spec/06-baselines/baseline.md', dict(
            schema_version=2, kind='Baseline', artifact_id='BASE-CRM-001', revision='r1',
            trace_links=[dict(id=EPIC, path='../02-epics/epic.md', relation='verifies', revision='r1')]))
        self.assertIn('epic-legacy', self.codes('--gate', 'baseline', '--target', 'BASE-CRM-001', code=1))

    def test_reopen_preserves_id_and_excludes_snapshot_but_rejects_stale_story(self):
        old = self.epic(work_status='done')
        snapshot = self.put('history/epic-r1.md', old.read_text(encoding='utf-8'))
        self.epic(revision='r2', work_status='inprogress')
        self.story()
        self.assertEqual(self.codes('--target', STORY, code=1), {'stale-revision'})
        for locator in ('#outside', ''):
            self.story(revision='r2', locator=locator)
            self.assertEqual(self.codes('--target', STORY, code=1), {'trace-use-case-locator'})
        self.story(revision='r2')
        self.assertEqual(self.codes('--gate', 'baseline', '--target', STORY), set())
        self.assertIn('"revision": "r1"', snapshot.read_text(encoding='utf-8'))

    def test_example_is_structurally_valid_even_if_expected_result_is_missing(self):
        example = KIT/'references/examples/project-code-request-specification.md'
        body = example.read_text(encoding='utf-8')
        draft, removed = body.split('- **Tại 2 · Dữ liệu sai.**', 1)
        incomplete = draft + removed[removed.index('\n'):]
        self.put(EPIC_PATH, incomplete)
        self.assertEqual(self.codes('--gate', 'readiness', '--target', 'EPIC-CRM-001'), set())

    def test_context_loads_policy_for_delivery_workflows(self):
        self.epic()
        workflows = {
            'define-capability': 'Capability', 'specify-epic': 'Epic', 'design-solution': 'Epic',
            'prepare-stories': 'Epic', 'review-specification': 'Epic', 'prepare-baseline': 'Epic',
            'check-readiness': 'Story', 'check-handoff': 'Story', 'check-completion': 'Story',
            'assess-change': 'Epic', 'report-status': 'Epic',
        }
        for workflow, kind in workflows.items():
            with self.subTest(workflow=workflow):
                result = self.cli('context', 'crm-'+workflow, '--target-kind', kind,
                                  '--target', EPIC if kind == 'Epic' else STORY,
                                  '--revision', 'r1', '--format', 'json')
                paths = {file['path'] for file in result['files']}
                self.assertIn('references/epic-use-case-policy.md', paths)
                if workflow == 'specify-epic':
                    self.assertIn('references/models/business-flows-and-use-cases.md', paths)
                    self.assertIn('assets/templates/epic-specification-template.md', paths)
