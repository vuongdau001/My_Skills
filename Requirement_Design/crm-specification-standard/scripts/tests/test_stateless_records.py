"""Schema-3 behavior and safe manual ASM-to-DEC conversion on disposable repos."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

PACK = Path(__file__).resolve().parents[2]


class StatelessRecordsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='crm-simple-records-')
        self.repo = Path(self.temp.name)
        (self.repo / '.agents').mkdir()
        cfg = dict(schema_version=1, kit_id='crm-specification-standard', id_namespace='CRM',
                   workstreams=[dict(id='p3', title='P3', spec_root='spec', sources=[], read_only=[],
                                     layout='numbered', record_schema_version=3)])
        (self.repo / '.agents/crm-spec-kit.json').write_text(json.dumps(cfg), encoding='utf-8')
        self.cap = self.put('01-capabilities/cap.md', dict(schema_version=1, kind='Capability',
                            artifact_id='CAP-CRM-001', revision='r1', trace_links=[]))
        self.source = self.repo / 'evidence.md'
        self.source.write_text('# Source\nConfirmed statement from the fixture authority.\n', encoding='utf-8')

    def tearDown(self):
        self.temp.cleanup()

    def put(self, name, meta):
        p = self.repo / 'spec' / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('# ' + meta['artifact_id'] + '\n\n```crm-spec-kit\n' + json.dumps(meta) + '\n```\n', encoding='utf-8')
        return p

    def record(self, kind, state=False, evidence=True):
        prefix = {'Decision':'DEC', 'Assumption':'ASM', 'Constraint':'CST'}[kind]
        row = dict(revision='r1', scope='Fixture', owner=None, statement='A concrete statement', evidence=[], trace_links=[])
        if evidence:
            row['evidence'] = [dict(path='../evidence.md', revision='source-r1',
                                    sha256=hashlib.sha256(self.source.read_bytes()).hexdigest())]
        if state:
            row[{'Decision':'decision_state','Assumption':'assumption_state','Constraint':'constraint_state'}[kind]] = 'Proposed'
        return dict(schema_version=3, kind=kind, artifact_id=prefix+'-CRM-001', revision='r1', record=row, references=[])

    def lint(self, gate='draft'):
        p = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(PACK/'scripts/kit.py'), 'lint',
                            '--repo', str(self.repo), '--workstream', 'p3', '--gate', gate],
                           capture_output=True, text=True, encoding='utf-8')
        self.assertIn(p.returncode, (0, 1), p.stdout+p.stderr)
        return json.loads(p.stdout)

    def test_decision_and_constraint_have_no_state(self):
        for kind in ('Decision','Constraint'):
            self.put('record-'+kind+'.md', self.record(kind))
        result = self.lint('readiness')
        self.assertFalse([i for i in result['issues'] if i['level']=='ERROR'], result)
        self.assertTrue(all('state' not in row for row in result['record_impacts']))

    def test_state_fields_are_rejected_in_schema_three(self):
        for kind in ('Decision','Assumption','Constraint'):
            self.put('record-'+kind+'.md', self.record(kind, state=True))
        self.assertEqual(sum(i['code']=='record-state-removed' for i in self.lint()['issues']), 3)

    def test_assumption_blocks_until_conversion_and_reference_rewrite(self):
        asm = self.put('assumption.md', self.record('Assumption'))
        cap = dict(schema_version=1,kind='Capability',artifact_id='CAP-CRM-001',revision='r1',
                   trace_links=[dict(id='ASM-CRM-001',path='../assumption.md',revision='r1',relation='depends-on')])
        self.put('01-capabilities/cap.md',cap)
        self.assertTrue(self.lint('readiness')['record_obligations'])
        dec = self.put('decision.md', self.record('Decision'))
        asm.unlink()
        self.assertTrue([i for i in self.lint()['issues'] if i['code'] in ('reference-path','broken-link')])
        cap['trace_links']=[dict(id='DEC-CRM-001',path='../decision.md',revision='r1',relation='depends-on')]
        self.put('01-capabilities/cap.md',cap)
        result=self.lint('readiness')
        self.assertFalse([i for i in result['issues'] if i['level']=='ERROR'],result)
        self.assertFalse(result['record_obligations'])

    def test_top_level_state_is_also_rejected(self):
        meta=self.record('Decision')
        meta['decision_state']='Approved'
        self.put('decision.md',meta)
        self.assertTrue([i for i in self.lint()['issues'] if i['code']=='record-state-removed'])

    def test_missing_source_does_not_become_confirmation(self):
        self.put('decision.md',self.record('Decision',evidence=False))
        result=self.lint('readiness')
        self.assertTrue([i for i in result['issues'] if i['code']=='record-obligation'])

    def test_evidence_hash_must_match(self):
        self.put('constraint.md',self.record('Constraint'))
        self.source.write_text('# Changed source\n',encoding='utf-8')
        self.assertTrue([i for i in self.lint()['issues'] if i['code']=='stale-reference'])

    def test_context_intake_does_not_reintroduce_state(self):
        self.put('assumption.md',self.record('Assumption'))
        p=subprocess.run([sys.executable,'-X','utf8',str(PACK/'scripts/kit.py'),'context',
                          'crm-define-capability','--repo',str(self.repo),'--workstream','p3','--format','json'],
                         capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        records=json.loads(p.stdout)['knowledge_intake']['existing_records']
        self.assertTrue(records)
        self.assertTrue(all('declared_state' not in row for row in records))

    def test_meeting_record_is_rejected_in_schema_three_spec(self):
        self.put('meeting.md',dict(schema_version=2,kind='Meeting',artifact_id='MTG-CRM-001',revision='r1',record={}))
        self.assertTrue(any(i['code']=='meeting-input-only' for i in self.lint()['issues']))

    def test_new_meeting_id_is_not_allocated(self):
        p=subprocess.run([sys.executable,'-X','utf8',str(PACK/'scripts/kit.py'),'next-id','MTG',
                          '--repo',str(self.repo)],capture_output=True,text=True,encoding='utf-8')
        self.assertNotEqual(p.returncode,0)
        self.assertIn('input source',p.stdout+p.stderr)

    def test_install_never_creates_meeting_folder_for_current_or_legacy_records(self):
        cfgpath=self.repo/'.agents/crm-spec-kit.json'
        cfg=json.loads(cfgpath.read_text(encoding='utf-8'))
        for schema in (2,3):
            cfg['workstreams'][0]['record_schema_version']=schema
            cfgpath.write_text(json.dumps(cfg),encoding='utf-8')
            p=subprocess.run([sys.executable,'-X','utf8',str(PACK/'scripts/kit.py'),'install',
                              '--repo',str(self.repo),'--workstream','p3','--agent','codex','--apply'],
                             capture_output=True,text=True,encoding='utf-8')
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            self.assertTrue((self.repo/'spec/00-project/02-decisions').is_dir())
            self.assertFalse((self.repo/'spec/00-project/01-meetings').exists())

    def test_directory_source_discovers_new_notes_without_registering_or_writing_them(self):
        directory=self.repo/'sources/inputs/01-meetings'
        directory.mkdir(parents=True)
        cfgpath=self.repo/'.agents/crm-spec-kit.json'
        cfg=json.loads(cfgpath.read_text(encoding='utf-8'))
        cfg['workstreams'][0].update(sources=[dict(id='SRC-MEETINGS',path='sources/inputs/01-meetings')],
                                    read_only=['sources'])
        cfgpath.write_text(json.dumps(cfg),encoding='utf-8')
        def context():
            p=subprocess.run([sys.executable,'-X','utf8',str(PACK/'scripts/kit.py'),'context',
                              'crm-specify-epic','--repo',str(self.repo),'--workstream','p3','--format','json'],
                             capture_output=True,text=True,encoding='utf-8')
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            return json.loads(p.stdout)['knowledge_intake']
        self.assertEqual(len(context()['sources']),1)
        note=directory/'new-note.md';note.write_text('# Meeting\nA tentative choice.\n',encoding='utf-8')
        before={p:p.read_bytes() for p in self.repo.rglob('*') if p.is_file()}
        result=context()
        row=next(s for s in result['sources'] if s['path'].endswith('new-note.md'))
        self.assertEqual(row['source_id'],'SRC-MEETINGS')
        self.assertEqual(row['inspection'],'review-source')
        self.assertEqual(row['sha256'],hashlib.sha256(note.read_bytes()).hexdigest())
        self.assertEqual(row['candidates'],[])
        self.assertFalse(result['existing_records'])
        self.assertEqual(before,{p:p.read_bytes() for p in self.repo.rglob('*') if p.is_file()})

    def test_capability_evidence_pin_detects_changed_meeting_source(self):
        cap=dict(schema_version=1,kind='Capability',artifact_id='CAP-CRM-001',revision='r1',trace_links=[],
                 evidence=[dict(path='../../evidence.md',revision='source-r1',sha256=hashlib.sha256(self.source.read_bytes()).hexdigest())])
        self.put('01-capabilities/cap.md',cap)
        self.assertFalse(any(i['code']=='stale-reference' for i in self.lint()['issues']))
        self.source.write_text('# Changed meeting source\n',encoding='utf-8')
        self.assertTrue(any(i['code']=='stale-reference' for i in self.lint()['issues']))

    def test_score_snapshot_keeps_schema_three_dependencies_without_state(self):
        self.put('decision.md',self.record('Decision'))
        cap=dict(schema_version=1,kind='Capability',artifact_id='CAP-CRM-001',revision='r1',
                 trace_links=[dict(id='DEC-CRM-001',path='../decision.md',revision='r1',relation='depends-on')])
        self.put('01-capabilities/cap.md',cap)
        p=subprocess.run([sys.executable,'-X','utf8',str(PACK/'scripts/kit.py'),'score','--repo',str(self.repo),
                          '--workstream','p3','--init','--target','CAP-CRM-001','--kind','Capability',
                          '--artifact','spec/01-capabilities/cap.md','--revision','r1','--scope','fixture'],
                         capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        records=json.loads(p.stdout)['targets'][0]['record_dependencies']
        self.assertEqual([row['id'] for row in records],['DEC-CRM-001'])
        self.assertTrue(all('state' not in row for row in records))


if __name__=='__main__':
    unittest.main()
