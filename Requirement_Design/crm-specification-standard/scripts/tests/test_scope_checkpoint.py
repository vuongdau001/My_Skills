"""Verify checkpoint delivery and read-only context behavior on disposable projects."""
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
CHECKPOINT = 'references/source-scope-and-decomposition-checkpoint.md'
CONSUMERS = {
    'crm-setup-project': 'Project',
    'crm-define-feature': 'Feature',
    'crm-specify-epic': 'Epic',
    'crm-prepare-stories': 'Epic',
    'crm-review-specification': 'Feature',
    'crm-report-status': 'Project',
}


class ScopeCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='crm-scope-checkpoint-')
        self.repo = Path(self.temp.name) / 'repo'
        self.repo.mkdir()
        self.cli('install', '--agent', 'codex', '--workstream', 'p3', '--spec-root', 'spec', '--apply')

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args):
        result = subprocess.run([sys.executable, '-B', str(TOOL), *args, '--repo', str(self.repo)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def hashes(self):
        return {str(path.relative_to(self.repo)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.repo.rglob('*') if path.is_file()}

    def test_relevant_contexts_deliver_checkpoint_without_writing_or_approving_source(self):
        # Intentionally incomplete source: context must not normalize it or invent an allocation.
        source = self.repo / 'function-list.md'
        source.write_text('# Estimation\n\nDeclared count: 12; detailed rows not supplied.\n')
        before = self.hashes()
        expected = (PACK / CHECKPOINT).read_text()
        for function, kind in CONSUMERS.items():
            with self.subTest(function=function):
                context = self.cli('context', function, '--workstream', 'p3', '--target', 'fixture',
                                   '--target-kind', kind, '--revision', 'r1', '--format', 'json')
                matches = [item for item in context['files'] if item['path'] == CHECKPOINT]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]['content'], expected)
                self.assertEqual(matches[0]['sha256'], hashlib.sha256(expected.encode()).hexdigest())
                self.assertNotIn('semantic_approval', context)
        self.assertEqual(self.hashes(), before)

    def test_explicit_reference_full_mode_and_installed_copy_deliver_same_resource_once(self):
        installed = self.repo / '.agents/skills/crm-spec-kit/scripts/kit.py'
        result = subprocess.run(
            [sys.executable, '-B', str(installed), 'context', 'crm-define-feature', '--repo', str(self.repo),
             '--workstream', 'p3', '--full', '--reference', 'CRM-SCOPE-CHECKPOINT', '--format', 'json'],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        context = json.loads(result.stdout)
        resources = [item for item in context['files'] if item['path'] == CHECKPOINT]
        self.assertEqual(len(resources), 1)
        self.assertEqual(resources[0]['content'], (PACK / CHECKPOINT).read_text())
        self.assertIn('assets/templates/feature-specification-template.md', [item['path'] for item in context['files']])


if __name__ == '__main__':
    unittest.main()
