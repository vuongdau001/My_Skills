"""Behavioral checks on disposable projects; no writes to the CRM pilot."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
PACK = Path(__file__).resolve().parents[2]
TOOL = PACK/'scripts/kit.py'
NUMBERED = ['00-project','01-features','02-epics','03-stories','04-tasks','05-reviews','06-baselines','07-reports','08-pilot']
LEGACY = ['00-project','features','epics','stories','tasks','reviews','baselines','reports','pilot']


class LayoutAndRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='crm-17-test-')
        self.repo = Path(self.temp.name)/'repo'
        self.repo.mkdir()
        self.root = self.repo/'spec'

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args, code=0):
        p = subprocess.run([sys.executable,'-B',str(TOOL),*args,'--repo',str(self.repo)],capture_output=True,text=True)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr)
        return json.loads(p.stderr if code==2 else p.stdout)

    def config(self, **fields):
        ws = dict(id='p3',title='P3',spec_root='spec',sources=[],read_only=[])
        ws.update(fields)
        cfg = dict(schema_version=1,kit_id='crm-specification-standard',id_namespace='CRM',workstreams=[ws])
        p = self.repo/'.agents/crm-spec-kit.json'
        p.parent.mkdir(exist_ok=True)
        p.write_text(json.dumps(cfg))
        return p

    def put(self, rel, meta=None, body=''):
        p = self.root/rel
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text('# Fixture\n\n'+('```crm-spec-kit\n'+json.dumps(meta,ensure_ascii=False)+'\n```\n' if meta else '')+body)
        return p

    def hashes(self):
        return {p.relative_to(self.repo).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.repo.rglob('*') if p.is_file() and not p.is_symlink()}

    def record(self, kind='Assumption', state=None, identity=None, **fields):
        prefix = dict(Meeting='MTG',Decision='DEC',Assumption='ASM',Constraint='CST')[kind]
        base = dict(revision='r1',scope='Contact linking',owner=None,evidence=[],trace_links=[])
        if kind=='Assumption':
            base.update(assumption_state=state or 'Unverified',statement='An existing provider can be reused',basis='Unverified source',validation_method='Inspect provider contract',review_due=None,if_false='Replan integration')
        elif kind=='Decision':
            base.update(decision_state=state or 'Proposed',statement='Chosen behavior',context='User need',options='A or B',rationale='Reason',consequences='Trade-off')
        elif kind=='Constraint':
            base.update(constraint_state=state or 'Proposed',statement='Required interface',constraint_type='technical',verification_method='Contract inspection')
        else:
            base.update(meeting_state=state or 'Draft',event_type='chat',occurred_at=None,participants=[],summary='Recorded discussion',actions=[])
        base.update(fields)
        return dict(schema_version=2,kind=kind,artifact_id=identity or prefix+'-CRM-001',record=base,references=[])

    def evidence(self, containing):
        source = self.root/'00-project/source.md'
        source.parent.mkdir(parents=True,exist_ok=True)
        source.write_text('# Evidence\n\nSource excerpt.\n')
        return dict(path=Path(os.path.relpath(source,containing.parent)).as_posix(),revision='source-r1',sha256=hashlib.sha256(source.read_bytes()).hexdigest())

    def trace(self, containing, target, identity, relation='depends-on', revision='r1', pin=False):
        value = dict(id=identity,path=Path(os.path.relpath(target,containing.parent)).as_posix(),revision=revision,relation=relation)
        if pin:
            value['sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
        return value

    def story(self, trace=None, identity='STORY-CRM-001', rel='03-stories/story.md'):
        return self.put(rel,dict(schema_version=1,kind='Story',artifact_id=identity,revision='r1',trace_links=trace or []))

    def lint(self, *args, code=0):
        return self.cli('lint','--workstream','p3',*args,code=code)

    def codes(self, result):
        return {i['code'] for i in result['issues']}

    def test_partial_scope_allocation_keeps_shared_controls(self):
        self.config(layout='numbered')
        epic=self.put('02-epics/epic.md',dict(schema_version=1,kind='Epic',artifact_id='EPIC-CRM-001',revision='r1'))
        manual_path=self.root/'03-stories/manual.md'
        manual=self.story([self.trace(manual_path,epic,'EPIC-CRM-001','parent')],rel='03-stories/manual.md')
        import_path=self.root/'03-stories/import.md'
        imported=self.story([self.trace(import_path,epic,'EPIC-CRM-001','parent')],identity='STORY-CRM-002',rel='03-stories/import.md')
        decision_path=self.root/'00-project/import-decision.md'
        self.put('00-project/import-decision.md',self.record(kind='Decision',scope='Import only',trace_links=[self.trace(decision_path,imported,'STORY-CRM-002','applies-to')]))
        result=self.lint('--gate','readiness','--target','STORY-CRM-001')
        self.assertNotIn('DEC-CRM-001',result['gate_scope']['dependency_ids'])
        result=self.lint('--gate','readiness','--target','STORY-CRM-002',code=1)
        self.assertIn('record-obligation',self.codes(result))
        shared_path=self.root/'00-project/shared-decision.md'
        self.put('00-project/shared-decision.md',self.record(kind='Decision',identity='DEC-CRM-002',scope='All entry paths',trace_links=[self.trace(shared_path,epic,'EPIC-CRM-001','applies-to')]))
        result=self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)
        self.assertIn('DEC-CRM-002',result['gate_scope']['dependency_ids'])
        self.assertIn('record-obligation',self.codes(result))
        self.assertNotIn('DEC-CRM-001',result['gate_scope']['dependency_ids'])

    def test_numbered_default_scaffold_for_all_adapters(self):
        for agent in ('codex','antigravity','claude'):
            with self.subTest(agent=agent):
                result=self.cli('install','--agent',agent,'--workstream','p3','--spec-root','spec','--apply')
                self.assertEqual(result['artifact_paths']['epics'],'02-epics')
                for d in NUMBERED:
                    self.assertTrue((self.root/d).is_dir())
                self.assertTrue((self.root/'00-project/02-decisions').is_dir())
                self.assertFalse((self.root/'epics').exists())
                self.assertTrue(self.cli('doctor','--agent',agent)['healthy'])

    def test_legacy_config_unchanged_on_install_and_doctor(self):
        cfg=self.config();before=cfg.read_bytes()
        self.cli('install','--agent','codex','--apply')
        self.assertEqual(cfg.read_bytes(),before)
        self.assertTrue(all((self.root/d).is_dir() for d in LEGACY))
        self.assertFalse((self.root/'02-epics').exists())
        self.assertFalse((self.root/'00-project/02-decisions').exists())
        self.assertTrue(self.cli('doctor','--agent','codex')['healthy'])
        self.cli('install','--layout','numbered','--apply',code=2)
        self.assertEqual(cfg.read_bytes(),before)

    def test_explicit_legacy_for_new_stream(self):
        self.cli('install','--layout','legacy','--apply')
        self.assertTrue((self.root/'epics').is_dir())
        self.assertTrue((self.root/'00-project/01-meetings').is_dir())

    def test_custom_paths_context_doctor_and_lint_inference(self):
        self.config(layout='numbered',artifact_paths={'stories':'delivery/user-stories'})
        self.cli('install','--apply')
        self.assertTrue((self.root/'delivery/user-stories').is_dir())
        self.put('delivery/user-stories/legacy.md')
        self.assertIn('legacy-metadata',self.codes(self.lint()))
        context=self.cli('context','crm-prepare-stories','--target','EPIC-CRM-001','--target-kind','Epic','--revision','r1','--format','json')
        self.assertEqual(context['workstream']['artifact_paths']['stories'],'delivery/user-stories')
        self.assertTrue(self.cli('doctor')['healthy'])

    def test_invalid_layouts_paths_and_overlaps_rejected(self):
        for fields in ({'layout':'unknown'},{'artifact_paths':{'wrong':'x'}},{'artifact_paths':{'stories':'../escape'}},
                       {'artifact_paths':{'stories':'features/nested'}},{'artifact_paths':{'stories':'.agents'}},
                       {'artifact_paths':{'stories':'/absolute'}}):
            with self.subTest(fields=fields):
                self.config(**fields)
                self.cli('lint',code=2)

    def test_symlink_custom_path_cannot_escape_repo(self):
        self.config(artifact_paths={'stories':'outside'})
        self.root.mkdir()
        (self.root/'outside').symlink_to(self.repo.parent,target_is_directory=True)
        self.cli('install','--apply',code=2)

    def test_numbered_and_mixed_layout_do_not_hide_metadata_warnings(self):
        self.config()
        self.put('epics/a.md');self.put('02-epics/b.md')
        warnings=[i for i in self.lint()['issues'] if i['code']=='legacy-metadata']
        self.assertEqual(len(warnings),2)

    def test_plan_layout_preserves_every_byte_and_reports_inbound_links_and_pins(self):
        cfg=self.config()
        epic=self.put('epics/e.md',dict(schema_version=1,kind='Epic',artifact_id='EPIC-CRM-001'))
        self.put('stories/s.md',dict(schema_version=1,kind='Story',artifact_id='STORY-CRM-001',references=['../epics/e.md']))
        self.put('baselines/b.md',dict(schema_version=1,kind='Baseline'),str(hashlib.sha256(epic.read_bytes()).hexdigest()))
        (self.repo/'README.md').write_text('[Epic](spec/epics/e.md)\n')
        before=self.hashes();result=self.cli('plan-layout','--to','numbered')
        self.assertEqual(before,self.hashes())
        self.assertFalse(result['automatic_apply_supported'])
        self.assertEqual(result['candidate_config']['workstreams'][0]['layout'],'numbered')
        self.assertNotIn('layout',json.loads(cfg.read_text())['workstreams'][0])
        self.assertTrue(any(r['suggested_link']=='../02-epics/e.md' for r in result['link_rewrites']))
        self.assertTrue(any(r['path']=='README.md' for r in result['link_rewrites']))
        self.assertTrue(result['locator_or_hash_impacts'])
        self.assertIn('spec/baselines/b.md',result['historical_records_to_preserve'])
        self.assertEqual(result['snapshot_sha256'],self.cli('plan-layout')['snapshot_sha256'])

    def test_plan_reports_collision_and_symlink_without_merging(self):
        self.config();self.put('epics/e.md');self.put('02-epics/existing.md')
        (self.root/'epics/link').symlink_to(self.root/'epics/e.md')
        before=self.hashes();result=self.cli('plan-layout')
        self.assertEqual(before,self.hashes())
        self.assertGreaterEqual(len(result['blockers']),2)

    def test_plan_has_no_apply_flag(self):
        p=subprocess.run([sys.executable,str(TOOL),'plan-layout','--repo',str(self.repo),'--apply'],capture_output=True)
        self.assertNotEqual(p.returncode,0)
        self.assertFalse(list(self.repo.iterdir()))

    def test_new_prefixes_are_allocated_across_streams_and_reservations(self):
        self.config();self.put('00-project/notes.md',body='MTG-CRM-007 ASM-CRM-009 CST-CRM-004')
        for prefix,expected in [('MTG','008'),('ASM','010'),('CST','005')]:
            self.assertEqual(self.cli('next-id',prefix)['id'],prefix+'-CRM-'+expected)
        r=self.cli('next-id','ASM','--reserve','--owner','BA','--apply')
        self.assertTrue(r['reserved']);self.assertEqual(self.cli('next-id','ASM')['id'],'ASM-CRM-011')

    def test_draft_records_supported_without_fabricating_approval(self):
        self.config()
        for kind in ('Meeting','Decision','Assumption','Constraint'):
            self.put('00-project/'+kind+'.md',self.record(kind))
        before=self.hashes();result=self.lint()
        self.assertEqual(before,self.hashes());self.assertTrue(result['valid'])
        self.assertEqual(result['definitions'],4)
        self.assertIn('record-obligation',self.codes(result))
        self.assertFalse(result['semantic_approval'])

    def test_register_record_ownership_and_duplicate_detection(self):
        self.config();meta=self.record();row=dict(meta['record'],id='ASM-CRM-001',kind='Assumption')
        p=self.put('00-project/register.md',dict(schema_version=2,kind='Project',records=[row]))
        self.assertEqual(self.lint()['definitions'],1)
        self.put('00-project/duplicate.md',meta)
        self.assertIn('duplicate-id',self.codes(self.lint(code=1)))
        (self.root/'00-project/duplicate.md').unlink()
        self.put('00-project/register.md',dict(schema_version=2,kind='Project',records=[row,row]))
        self.assertIn('duplicate-record',self.codes(self.lint(code=1)))

    def test_legacy_decision_remains_readable(self):
        self.config();self.put('00-project/legacy.md',dict(schema_version=1,kind='Decision',artifact_id='DEC-CRM-001',decision_state='Approved'))
        self.assertTrue(self.lint()['valid'])

    def test_schema2_approval_requires_fields_and_evidence(self):
        self.config();self.put('00-project/decision.md',self.record('Decision','Approved'))
        codes=self.codes(self.lint(code=1))
        self.assertTrue({'record-field','record-time','record-evidence'}<=codes)

    def test_approved_decision_pinned_to_actual_source(self):
        self.config();p=self.root/'00-project/decision.md'
        meta=self.record('Decision','Approved',authority='Business owner (fixture)',decided_at='2026-11-04T10:00:00+07:00',evidence=[self.evidence(p)])
        self.put('00-project/decision.md',meta)
        self.assertTrue(self.lint()['valid'])
        (self.root/'00-project/source.md').write_text('Changed source')
        self.assertIn('stale-reference',self.codes(self.lint(code=1)))

    def test_meeting_confirmed_requires_real_event_metadata_and_actions(self):
        self.config();p=self.root/'00-project/meeting.md'
        meta=self.record('Meeting','Confirmed',occurred_at='2026-11-04T10:00:00+07:00',participants=['BA'],actions=[dict(description='Clarify permissions',owner=None,due=None)],evidence=[self.evidence(p)])
        self.put('00-project/meeting.md',meta);self.assertTrue(self.lint()['valid'])
        meta['record']['participants']=[];meta['record']['actions']=[{}]
        self.put('00-project/meeting.md',meta)
        self.assertTrue({'meeting-participants','meeting-action'}<=self.codes(self.lint(code=1)))

    def test_confirmed_constraint_requires_authority_and_source(self):
        self.config();p=self.root/'00-project/constraint.md'
        self.put('00-project/constraint.md',self.record('Constraint','Confirmed'))
        self.assertIn('record-evidence',self.codes(self.lint(code=1)))
        self.put('00-project/constraint.md',self.record('Constraint','Confirmed',authority='Contract owner (fixture)',effective_from='2026-11-04',evidence=[self.evidence(p)]))
        self.assertTrue(self.lint()['valid'])

    def test_assumption_obligation_blocks_gate_but_not_draft_then_validation_unblocks(self):
        self.config();p=self.put('00-project/a.md',self.record())
        story=self.root/'03-stories/story.md'
        self.story([self.trace(story,p,'ASM-CRM-001')])
        self.assertTrue(self.lint()['valid'])
        self.assertIn('record-obligation',self.codes(self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)))
        self.put('00-project/a.md',self.record(state='Validated',owner='BA',validation_result='Provider inspected',evidence=[self.evidence(p)]))
        self.assertTrue(self.lint('--gate','readiness','--target','STORY-CRM-001')['valid'])

    def test_invalidated_assumption_and_risk_acceptance_are_not_validation(self):
        self.config();p=self.put('00-project/a.md',self.record(state='Invalidated',owner='BA',validation_result='Provider absent',evidence=[self.evidence(self.root/'00-project/a.md')],risk_acceptance='Approved'))
        s=self.root/'03-stories/story.md';self.story([self.trace(s,p,'ASM-CRM-001')])
        self.assertIn('record-obligation',self.codes(self.lint('--gate','baseline','--target','STORY-CRM-001',code=1)))

    def test_gate_target_closure_excludes_unrelated_open_record(self):
        self.config();self.put('00-project/a.md',self.record());self.story()
        self.assertTrue(self.lint('--gate','readiness','--target','STORY-CRM-001')['valid'])
        self.assertIn('record-obligation',self.codes(self.lint('--gate','readiness',code=1)))

    def test_reverse_applies_to_and_transitive_parent_dependencies(self):
        self.config();s=self.story()
        epic=self.put('02-epics/e.md',dict(schema_version=1,kind='Epic',artifact_id='EPIC-CRM-001',revision='r1'))
        self.story([self.trace(s,epic,'EPIC-CRM-001',relation='parent')])
        a=self.root/'00-project/a.md';meta=self.record(trace_links=[self.trace(a,epic,'EPIC-CRM-001',relation='applies-to')])
        self.put('00-project/a.md',meta)
        self.assertIn('record-obligation',self.codes(self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)))

    def test_revision_id_ownership_anchor_and_hash_mismatches_detected(self):
        self.config();a=self.put('00-project/a.md',self.record())
        s=self.root/'03-stories/story.md'
        for change,code in [({'revision':'r0'},'stale-revision'),({'id':'ASM-CRM-999'},'trace-unresolved'),({'path':'../00-project/a.md#missing'},'reference-anchor'),({'sha256':'0'*64},'stale-reference')]:
            with self.subTest(change=change):
                link=self.trace(s,a,'ASM-CRM-001');link.update(change);self.story([link])
                self.assertIn(code,self.codes(self.lint(code=1)))
        other=self.put('00-project/other.md')
        self.story([self.trace(s,other,'ASM-CRM-001')])
        self.assertIn('trace-owner',self.codes(self.lint(code=1)))

    def test_evidence_escape_and_external_access_not_faked(self):
        self.config();p=self.root/'00-project/d.md'
        meta=self.record('Decision','Approved',authority='Owner',decided_at='2026-11-04T10:00:00+07:00',evidence=[dict(path='https://example.invalid/notes',revision='r1',sha256='0'*64)])
        self.put('00-project/d.md',meta)
        self.assertIn('external-evidence-unverified',self.codes(self.lint()))
        self.assertIn('gate-evidence-unverified',self.codes(self.lint('--gate','baseline','--target','DEC-CRM-001',code=1)))
        meta['record']['evidence'][0]['path']='../../../../escape.md';self.put('00-project/d.md',meta)
        self.assertIn('reference-path',self.codes(self.lint(code=1)))

    def test_legacy_prose_revision_needs_hash_for_gate(self):
        self.config();a=self.put('02-epics/e.md',dict(schema_version=1,kind='Epic',artifact_id='EPIC-CRM-001'))
        s=self.root/'03-stories/story.md';self.story([self.trace(s,a,'EPIC-CRM-001')])
        self.assertIn('revision-unverified',self.codes(self.lint()))
        self.assertIn('gate-evidence-unverified',self.codes(self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)))
        self.story([self.trace(s,a,'EPIC-CRM-001',pin=True)])
        self.assertTrue(self.lint('--gate','readiness','--target','STORY-CRM-001')['valid'])

    def test_supersession_is_preserved_and_obsolete_dependency_is_blocked(self):
        self.config();old=self.root/'00-project/old.md';new=self.root/'00-project/new.md'
        old_meta=self.record('Decision','Superseded',trace_links=[self.trace(old,new,'DEC-CRM-002',relation='superseded-by')])
        new_meta=self.record('Decision','Approved',identity='DEC-CRM-002',authority='Business',decided_at='2026-11-04T10:00:00+07:00',evidence=[self.evidence(new)],trace_links=[self.trace(new,old,'DEC-CRM-001',relation='supersedes')])
        self.put('00-project/old.md',old_meta);self.put('00-project/new.md',new_meta)
        self.assertTrue(self.lint('--gate','baseline')['valid'])
        s=self.root/'03-stories/story.md';self.story([self.trace(s,old,'DEC-CRM-001')])
        self.assertIn('record-obligation',self.codes(self.lint('--gate','baseline','--target','STORY-CRM-001',code=1)))

    def test_supersession_cycle_and_missing_replacement_detected(self):
        self.config();self.put('00-project/old.md',self.record('Decision','Superseded'))
        self.assertIn('supersession-missing',self.codes(self.lint(code=1)))
        old=self.root/'00-project/old.md';new=self.root/'00-project/new.md'
        self.put('00-project/old.md',self.record('Decision','Superseded',trace_links=[self.trace(old,new,'DEC-CRM-002',relation='superseded-by')]))
        self.put('00-project/new.md',self.record('Decision','Superseded',identity='DEC-CRM-002',trace_links=[self.trace(new,old,'DEC-CRM-001',relation='superseded-by')]))
        self.assertIn('supersession-cycle',self.codes(self.lint(code=1)))

    def test_record_prefix_must_match_kind_and_schema2_requires_record(self):
        self.config();self.put('00-project/a.md',self.record(identity='DEC-CRM-001'))
        self.assertIn('record-id',self.codes(self.lint(code=1)))
        self.put('00-project/a.md',dict(schema_version=2,kind='Decision',artifact_id='DEC-CRM-001'))
        self.assertIn('record-required',self.codes(self.lint(code=1)))

    def test_new_kind_with_legacy_schema_is_rejected_without_rewrite(self):
        self.config();meta=self.record();meta['schema_version']=1;p=self.put('00-project/a.md',meta);before=p.read_bytes()
        self.assertIn('record-schema',self.codes(self.lint(code=1)))
        self.assertEqual(before,p.read_bytes())

    def test_undefined_gate_target_fails(self):
        self.config();self.story()
        self.assertIn('gate-target',self.codes(self.lint('--target','STORY-CRM-999',code=1)))

    def test_gate_target_reports_transitive_record_impacts(self):
        self.config();a=self.put('00-project/a.md',self.record())
        e=self.root/'02-epics/e.md'
        self.put('02-epics/e.md',dict(schema_version=1,kind='Epic',artifact_id='EPIC-CRM-001',revision='r1',trace_links=[self.trace(e,a,'ASM-CRM-001')]))
        s=self.root/'03-stories/story.md';self.story([self.trace(s,e,'EPIC-CRM-001',relation='parent')])
        result=self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)
        self.assertEqual(result['record_obligations'][0]['affected_ids'],['EPIC-CRM-001','STORY-CRM-001'])
        self.assertEqual(set(result['gate_scope']['dependency_ids']),{'ASM-CRM-001','EPIC-CRM-001','STORY-CRM-001'})

    def test_pending_decision_and_proposed_constraint_block_linked_story(self):
        self.config();s=self.root/'03-stories/story.md'
        for kind,identity in [('Decision','DEC-CRM-001'),('Constraint','CST-CRM-001')]:
            p=self.put('00-project/'+kind+'.md',self.record(kind))
            self.story([self.trace(s,p,identity)])
            result=self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)
            self.assertEqual(result['record_obligations'][0]['id'],identity)

    def test_unrelated_external_evidence_does_not_block_selected_story(self):
        self.config();self.story()
        self.put('00-project/d.md',self.record('Decision','Approved',authority='Owner',decided_at='2026-11-04T10:00:00+07:00',evidence=[dict(path='https://example.invalid/source',revision='r1',sha256='0'*64)]))
        self.assertTrue(self.lint('--gate','readiness','--target','STORY-CRM-001')['valid'])

    def test_register_link_resolves_exact_record_revision(self):
        self.config();meta=self.record()
        a=self.put('00-project/register.md',dict(schema_version=2,kind='Project',records=[dict(meta['record'],id='ASM-CRM-001',kind='Assumption')]))
        s=self.root/'03-stories/story.md';self.story([self.trace(s,a,'ASM-CRM-001')])
        self.assertNotIn('revision-unverified',self.codes(self.lint()))

    def test_schema1_structured_payload_is_not_silently_ignored(self):
        self.config();meta=self.record('Decision');meta['schema_version']=1
        self.put('00-project/d.md',meta)
        self.assertIn('record-schema',self.codes(self.lint(code=1)))

    def test_typed_external_target_is_not_treated_as_verified_definition(self):
        self.config();self.story([dict(id='DEC-CRM-001',path='https://example.invalid/decision',revision='r1',relation='depends-on')])
        self.assertIn('trace-external',self.codes(self.lint(code=1)))

    def test_cross_stream_record_ids_and_obligations_are_resolved(self):
        cfg=self.config();data=json.loads(cfg.read_text());data['workstreams'].append(dict(id='p4',title='P4',spec_root='p4/spec',sources=[],read_only=[]));cfg.write_text(json.dumps(data))
        foreign=self.repo/'p4/spec/00-project/a.md';foreign.parent.mkdir(parents=True)
        foreign.write_text('# Foreign\n```crm-spec-kit\n'+json.dumps(self.record())+'\n```\n')
        s=self.root/'03-stories/story.md';self.story([self.trace(s,foreign,'ASM-CRM-001')])
        self.assertIn('record-obligation',self.codes(self.lint('--gate','readiness','--target','STORY-CRM-001',code=1)))
        self.assertEqual(self.cli('next-id','ASM')['id'],'ASM-CRM-002')

    def test_plan_snapshot_changes_for_binary_and_inbound_document_changes(self):
        self.config();self.put('epics/e.md');binary=self.root/'epics/diagram.bin';binary.write_bytes(b'v1')
        inbound=self.repo/'README.md';inbound.write_text('[Epic](spec/epics/e.md)\n')
        one=self.cli('plan-layout')['snapshot_sha256'];binary.write_bytes(b'v2')
        two=self.cli('plan-layout')['snapshot_sha256'];self.assertNotEqual(one,two)
        inbound.write_text('[Epic](spec/epics/e.md)\nNew discussion\n')
        self.assertNotEqual(two,self.cli('plan-layout')['snapshot_sha256'])

    def test_internal_scaffold_symlink_is_not_followed(self):
        self.config();self.root.mkdir();(self.root/'real').mkdir()
        (self.root/'stories').symlink_to(self.root/'real',target_is_directory=True)
        before=self.hashes();self.cli('install','--apply',code=2)
        self.assertEqual(before,self.hashes())


if __name__=='__main__':
    unittest.main()
