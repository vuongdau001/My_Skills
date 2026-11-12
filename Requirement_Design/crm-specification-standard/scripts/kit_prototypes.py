"""Read-only prototype evidence checks for opt-in workstreams."""
from datetime import datetime
import re

RUNTIME_DIRS = ('app', 'screens', 'assets', 'fixtures')


def validate(api, root, dirs, path, epic, scope=None):
    def fail(message):
        raise api['KitError'](message)

    def text(value):
        return isinstance(value, str) and bool(value.strip())

    def object_file(parent, raw, suffix):
        path = regular_file(parent, raw)
        if path.suffix != suffix:
            fail(f'Expected {suffix} file: {raw}')
        return path

    def regular_file(parent, raw):
        path = api['relative'](parent, raw)
        if path.relative_to(parent).as_posix() != raw or not path.is_file():
            fail(f'Expected a canonical, regular relative file: {raw}')
        return path

    def obj(value):
        return value if isinstance(value, dict) else {}

    def rows(data, field):
        value = data.get(field)
        if not isinstance(value, list) or not value or not all(isinstance(row, dict) for row in value):
            fail(f'{field} must be a nonempty list of objects')
        return value

    def ids(value, label):
        if not isinstance(value, list) or not value or not all(text(item) for item in value):
            fail(f'{label} must be a nonempty list of IDs')
        if len(set(value)) != len(value):
            fail(f'{label} contains duplicate IDs')
        return set(value)

    def index(data, field, prefix):
        result = {}
        for row in rows(data, field):
            identity = row.get('id')
            if not isinstance(identity, str) or not re.fullmatch(prefix + r'-[A-Z0-9]+(?:-[A-Z0-9]+)*', identity):
                fail(f'Invalid {field} ID: {identity}')
            if identity in result:
                fail(f'Duplicate {field} ID: {identity}')
            result[identity] = row
        return result

    def bundle(manifest_path, epic, selection):
        manifest = obj(api['read_json'](manifest_path))
        if type(manifest.get('schema_version')) is not int or manifest['schema_version'] != 1:
            fail('Unsupported prototype manifest schema_version')
        parent = manifest_path.parent
        entrypoint = manifest.get('entrypoint')
        entry = object_file(parent, entrypoint, '.html')
        if not entry.is_relative_to(parent/'app'):
            fail('Prototype entrypoint must be under app/')
        pins = manifest.get('files')
        if not isinstance(pins, dict):
            fail('Prototype manifest requires a files map of bundle-relative SHA256 pins')
        inventory = {'scenarios.md'}
        for directory in RUNTIME_DIRS:
            location = parent/directory
            if location.is_symlink() or (location.exists() and not location.is_dir()):
                fail(f'Expected an ordinary directory: {directory}')
            for file in location.rglob('*'):
                if file.is_symlink():
                    fail(f'Prototype runtime symlink: {file.relative_to(parent)}')
                if file.is_file():
                    inventory.add(file.relative_to(parent).as_posix())
        if inventory != set(pins):
            fail('Prototype files map must pin scenarios.md and all runtime files under app/, screens/, assets/, fixtures/')
        for raw, sha in pins.items():
            if api['digest'](regular_file(parent, raw)) != sha:
                fail(f'Stale prototype file pin: {raw}')
        screens = index(manifest, 'screens', 'SCR')
        for row in screens.values():
            screen_path = object_file(parent, row.get('path'), '.html')
            if screen_path.relative_to(parent).as_posix() not in pins:
                fail('Screen path must be a pinned HTML file')
        scenarios = index(manifest, 'scenarios', 'SCN')
        for row in scenarios.values():
            if ids(row.get('screens'), 'Scenario screens') - screens.keys():
                fail('Scenario references an unknown screen ID')
            ids(row.get('refs'), 'Scenario requirement or contract refs')
        allocations = rows(manifest, 'allocations')
        for row in allocations:
            if ids(row.get('scenarios'), 'Allocation scenarios') - scenarios.keys():
                fail('Allocation references an unknown scenario ID')
        matches = [row for row in allocations if row.get('epic_id') == epic['artifact_id']
                   and row.get('epic_revision') == epic['revision'] and row.get('scope') == selection['scope']]
        if len(matches) != 1:
            fail('Manifest needs exactly one allocation for the selected Epic ID, revision and scope')
        allocated = set(matches[0]['scenarios'])
        epic_policy = api['support']('epics')
        if epic.get('epic_policy') == epic_policy.POLICY:
            anchors = epic_policy.case_anchors(api, path.read_text(encoding='utf-8'))
            binding = obj(epic.get('use_case'))
            locator = binding.get('locator')
            if binding.get('level') != 'user-goal' or not text(locator) or locator not in anchors:
                fail('Prototype allocation requires a valid Epic Use Case binding')
            epic_id = epic['artifact_id']
            reference_ids = {epic_id}
            legacy_id = epic_policy.legacy_case_id(epic)
            if legacy_id:
                reference_ids.add(legacy_id)
            for scenario in sorted(allocated):
                locators = set()
                for ref in scenarios[scenario]['refs']:
                    identity, separator, anchor = ref.partition('#')
                    if identity in reference_ids:
                        locators.add(separator + anchor)
                if not locators or not locators <= anchors:
                    fail(f'{scenario} must reference {epic_id} at valid E03 locators')
        return allocated

    selection = obj(epic.get('prototype'))
    state = selection.get('applicability')
    if state not in ('required', 'not_applicable') or not text(selection.get('scope')) or not text(epic.get('revision')):
        fail('Epic requires revision, prototype.scope and prototype.applicability (required or not_applicable)')
    if scope is not None and scope != selection['scope']:
        fail('Prototype scope does not match the assessed scope')
    if not text(selection.get('review')):
        fail('Epic requires a Prototype walkthrough review path for the selected scope')
    review_path = object_file(root, selection['review'], '.md')
    if not review_path.is_relative_to(root/dirs['reviews']):
        fail('Prototype review record must be under the workstream reviews directory')
    review = obj(api['metadata'](review_path.read_text(encoding='utf-8')))
    evidence = obj(review.get('prototype_walkthrough'))
    if review.get('kind') != 'Review' or evidence.get('scope') != selection['scope'] or evidence.get('epic_sha256') != api['digest'](path):
        fail('Prototype review must match the selected scope and Epic bytes')
    if not text(evidence.get('reviewer')) or not text(evidence.get('observed_at')):
        fail('Prototype review requires reviewer and observed_at')
    try:
        timestamp = datetime.fromisoformat(evidence['observed_at'])
    except ValueError:
        fail('Prototype review observed_at must be an ISO timestamp with timezone')
    if timestamp.tzinfo is None:
        fail('Prototype review observed_at must include a timezone')
    if state == 'not_applicable':
        if not text(selection.get('reason')) or review.get('review_verdict') != 'N/A' or not text(review.get('na_reason')):
            fail('No UI impact requires a documented reason and reviewed N/A evidence')
        return state
    manifest_path = object_file(root, selection.get('manifest'), '.json')
    if (manifest_path.name != 'manifest.json' or manifest_path.parent.parent != root/dirs['prototypes']):
        fail('Expected a journey manifest at prototypes/<journey>/manifest.json')
    expected = bundle(manifest_path, epic, selection)
    if review.get('review_verdict') != 'Đạt' or evidence.get('manifest_sha256') != api['digest'](manifest_path):
        fail('A passing walkthrough must pin the current prototype manifest bytes')
    observed = ids(evidence.get('observed_scenarios'), 'Observed scenarios')
    if observed != expected:
        fail('Walkthrough scenarios must match the selected Epic allocation')

    return state


def audit(api, repo, root, ws, dirs, docs, scope, issue):
    if not ws.get('prototype_gate') or scope['gate'] != 'baseline':
        return

    error = api['KitError']
    selected = scope['target']
    candidates = []
    for path, source in docs.items():
        try:
            meta = api['metadata'](source) or {}
        except error:
            continue  # The general Markdown lint already reports malformed metadata.
        if meta.get('kind') != 'Epic' and not path.is_relative_to(root/dirs['epics']):
            continue
        identity = meta.get('artifact_id')
        if selected and identity not in scope['dependency_ids']:
            continue
        if not selected and meta.get('work_status') == 'cancel':
            continue
        if meta.get('kind') == 'Epic' or re.search(r'\bEPIC-CRM-\d{3,}\b', path.name):
            candidates.append((path, meta))
    if selected and not candidates:
        issue('ERROR', 'prototype-gate', ws['spec_root'],
              'Prototype baseline check needs a local Epic target or a baseline trace dependency on a local Epic')
    for path, epic in candidates:
        try:
            if epic.get('kind') != 'Epic' or not isinstance(epic.get('artifact_id'), str):
                raise error('Prototype gate requires structured Epic metadata with artifact_id')
            validate(api, root, dirs, path, epic)
        except (error, OSError, UnicodeError) as exc:
            issue('ERROR', 'prototype-gate', path.relative_to(repo).as_posix(), str(exc))
