"""Prototype gate and E08 behavior on disposable workstreams."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

KIT = Path(__file__).resolve().parents[2]
EPIC = 'EPIC-CRM-001'
SCOPE = 'contact-create'
SCENARIO = 'SCN-CONTACT-CREATE'
SCREEN = 'SCR-CONTACT-CREATE'
CASE = 'MOD-CRM-001'


class PrototypeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name)
        self.epic = 'spec/02-epics/contact.md'
        self.review = 'spec/05-reviews/contact.md'
        self.bundle = 'spec/09-prototypes/customer-contact/'
        self.manifest = self.bundle + 'manifest.json'
        self.asset = self.bundle + 'assets/style.css'
        self.config()

    def config(self, enabled=True):
        workstream = dict(id='p3', spec_root='spec', layout='numbered', sources=[], read_only=[])
        if enabled:
            workstream['prototype_gate'] = True
        self.put_json('.agents/crm-spec-kit.json', dict(schema_version=1, kit_id='crm-specification-standard',
                                                        id_namespace='CRM', workstreams=[workstream]))

    def put(self, path, content):
        file = self.repo/path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding='utf-8')

    def put_json(self, path, data):
        self.put(path, json.dumps(data, ensure_ascii=False))

    def put_meta(self, path, **fields):
        body = '# Fixture\n\n'
        if fields.get('epic_policy') == 'use-case-v1':
            body += '## E03 — Use Case\n\n<a id="create"></a>\n\n'
        self.put(path, body + '```crm-spec-kit\n' + json.dumps(dict(schema_version=1, **fields), ensure_ascii=False) + '\n```\n')

    def hash(self, path):
        return hashlib.sha256((self.repo/path).read_bytes()).hexdigest()

    def cli(self, *args, code=0):
        command = [sys.executable, '-B', str(KIT/'scripts/kit.py'), *args, '--repo', str(self.repo), '--workstream', 'p3']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def gate(self, target=EPIC, code=0):
        return self.cli('lint', '--gate', 'baseline', '--target', target, code=code)

    def fixture(self, state='required', *, revision='r1', scenario_ref=CASE+'#create'):
        selection = dict(applicability=state, scope=SCOPE, review=self.review.removeprefix('spec/'))
        if state == 'required':
            selection['manifest'] = self.manifest.removeprefix('spec/')
            files = {'scenarios.md': '# Fixture\n', 'app/index.html': '<title>Contact</title>',
                     'screens/create.html': '<h1>Create</h1>', 'assets/style.css': 'body { color: black; }'}
            for name, content in files.items():
                self.put(self.bundle + name, content)
            self.put_json(self.manifest, dict(schema_version=1, entrypoint='app/index.html',
                allocations=[dict(epic_id=EPIC, epic_revision=revision, scope=SCOPE, scenarios=[SCENARIO])],
                screens=[dict(id=SCREEN, path='screens/create.html')],
                scenarios=[dict(id=SCENARIO, screens=[SCREEN], refs=['BR-CRM-001', scenario_ref])],
                files={name: self.hash(self.bundle + name) for name in files}))
        else:
            selection['reason'] = 'Backend changes only'
        self.put_meta(self.epic, kind='Epic', artifact_id=EPIC, revision='r1', prototype=selection,
                      epic_policy='use-case-v1', defined_ids=[CASE],
                      use_case=dict(id=CASE, level='user-goal', locator='#create'))
        evidence = dict(scope=SCOPE, epic_sha256=self.hash(self.epic), reviewer='Fixture reviewer',
                        observed_at='2026-11-05T10:00:00+07:00')
        if state == 'required':
            evidence.update(manifest_sha256=self.hash(self.manifest), observed_scenarios=[SCENARIO])
            self.put_meta(self.review, kind='Review', review_verdict='Đạt', prototype_walkthrough=evidence)
        else:
            self.put_meta(self.review, kind='Review', review_verdict='N/A', na_reason=selection['reason'],
                          prototype_walkthrough=evidence)

    def test_draft_and_legacy_stay_available_without_prototype(self):
        self.put_meta(self.epic, kind='Epic', artifact_id=EPIC, revision='r1')
        self.cli('lint')
        result = self.gate(code=1)
        self.assertEqual({i['code'] for i in result['issues']}, {'prototype-gate', 'epic-legacy'})
        self.config(enabled=False)
        self.assertEqual(self.gate(code=1)['issues'][0]['code'], 'epic-legacy')
        self.cli('lint')

    def test_baseline_requires_trace_to_epic(self):
        self.fixture()
        package = 'spec/06-baselines/contact.md'
        self.put_meta(package, kind='Baseline', artifact_id='BASE-CRM-001', revision='r1')
        self.gate('BASE-CRM-001', code=1)
        self.put_meta(package, kind='Baseline', artifact_id='BASE-CRM-001', revision='r1',
                      trace_links=[dict(id=EPIC, path='../02-epics/contact.md', revision='r1', relation='depends-on')])
        self.gate('BASE-CRM-001')

    def test_use_case_allocation_checks_locator_and_revision(self):
        self.fixture(scenario_ref=CASE+'#missing')
        self.assertIn('valid E03 locators', self.gate(code=1)['issues'][0]['message'])
        self.fixture(revision='r0')
        self.assertIn('Epic ID, revision and scope', self.gate(code=1)['issues'][0]['message'])

    def test_walkthrough_pins_runtime_assets(self):
        self.fixture()
        self.assertFalse(self.gate()['semantic_approval'])
        self.put(self.asset, 'body { color: blue; }')
        self.assertIn('Stale prototype file pin', self.gate(code=1)['issues'][0]['message'])

    def test_na_is_reviewed_and_bound_to_epic_bytes(self):
        self.fixture('not_applicable')
        self.gate()
        with (self.repo/self.epic).open('a', encoding='utf-8') as file:
            file.write('\nDraft changed.\n')
        self.assertIn('Epic bytes', self.gate(code=1)['issues'][0]['message'])

    def test_score_caps_effective_e08_when_prototype_is_stale(self):
        self.fixture()
        doc = self.cli('score', '--init', '--artifact', self.epic, '--target', EPIC, '--kind', 'Epic',
                       '--revision', 'r1', '--scope', SCOPE)
        item = next(item for item in doc['targets'][0]['items'] if item['id'] == 'E08')
        item.update(applicability='applies', level=2, present=True, rationale='Fixture',
                    evidence=[dict(path=self.review, revision='r1', sha256=self.hash(self.review), locator='Results')])
        self.put_json('assessment.json', doc)
        args = ('score', '--assessment', 'assessment.json', '--target', EPIC, '--item', 'E08')
        self.assertEqual(self.cli(*args)['targets'][0]['items'][0]['level'], 2)
        self.put(self.asset, 'body { color: blue; }')
        target = self.cli(*args)['targets'][0]
        self.assertEqual(target['items'][0]['declared_level'], 2)
        self.assertEqual(target['items'][0]['level'], 1)
        self.assertEqual(target['summary']['gate'], 'blocked')

    def test_context_exposes_reuse_and_user_input_before_authoring(self):
        context = self.cli('context', 'crm-specify-epic', '--target', EPIC, '--target-kind', 'Epic',
                           '--revision', 'r1', '--format', 'json')
        standard = next(file for file in context['files'] if file['path'].endswith('prototype-workflow-and-epic-gate.md'))
        self.assertIn('nhắc người dùng cung cấp chỉ dẫn và mẫu', standard['content'])
        self.assertIn('Tái dùng file', standard['content'])
        self.assertEqual(context['workstream']['artifact_paths']['prototypes'], '09-prototypes')
