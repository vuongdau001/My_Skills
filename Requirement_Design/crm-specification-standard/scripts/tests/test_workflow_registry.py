"""Structural regression tests; no external actions or workflow execution."""
from pathlib import Path
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
PACK = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('reference_validator', PACK / 'scripts/validate_reference_pack.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class WorkflowRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='crm-workflow-registry-')
        self.root = Path(self.temp.name) / 'copied kit'
        shutil.copytree(PACK, self.root, ignore=shutil.ignore_patterns('__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def mutate(self, change):
        path = self.root / 'reference-manifest.json'
        value = json.loads(path.read_text())
        change(value)
        path.write_text(json.dumps(value))

    def assert_error(self, fragment):
        errors, _ = validator.validate(self.root)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_portable_package(self):
        errors, counts = validator.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts['agent_profiles'], 5)
        self.assertEqual(counts['workflow_functions'], 13)

    def test_duplicate_function(self):
        self.mutate(lambda m: m['functions'].append(m['functions'][0]))
        self.assert_error('Function registry inventory mismatch')

    def test_unknown_agent(self):
        self.mutate(lambda m: m['functions'][0].update(agent='missing-agent'))
        self.assert_error('Unknown function agent')

    def test_missing_profile(self):
        (self.root / 'agents/profiles/crm-guide.md').unlink()
        self.assert_error('Missing target')

    def test_missing_workflow(self):
        (self.root / 'workflows/crm-check-handoff.md').unlink()
        self.assert_error('Missing target')

    def test_function_not_routed(self):
        path = self.root / 'SKILL.md'
        path.write_text('\n'.join(line for line in path.read_text().splitlines()
                                   if not line.startswith('| [crm-check-handoff]')))
        self.assert_error('Workflow not linked from entry/onboarding')

    def test_old_short_name(self):
        self.mutate(lambda m: m['functions'][0].update(id='crm-setup'))
        self.assert_error('Invalid function name')

    def test_check_write_scope(self):
        def change(m):
            next(f for f in m['functions'] if f['id']=='crm-check-completion')['write_scope']='scoped-artifacts'
        self.mutate(change)
        self.assert_error('Check workflow write boundary mismatch')

    def test_cross_folder_dependency(self):
        self.mutate(lambda m: m['functions'][0]['references'].append('../other-skill/SKILL.md'))
        self.assert_error('Path outside pack')

    def test_unknown_next_function(self):
        self.mutate(lambda m: m['functions'][0]['next_functions'].append('crm-not-released'))
        self.assert_error('Unknown next function')

    def test_missing_historical_anchor(self):
        path = self.root / 'references/coverage-inventories-and-traceability.md'
        path.write_text(path.read_text().replace('<a id="spec-6"></a>', ''))
        self.assert_error('Missing anchor')

    def test_unregistered_workflow(self):
        (self.root / 'workflows/unregistered.md').write_text('# Unregistered\n')
        self.assert_error('Unregistered document')

    def test_missing_mapping_item(self):
        path = self.root / 'references/catalog-check-model-mapping.md'
        path.write_text('\n'.join(line for line in path.read_text().splitlines() if not line.startswith('| E07 —')))
        self.assert_error('E/S review mapping coverage mismatch')


if __name__ == '__main__':
    unittest.main()
