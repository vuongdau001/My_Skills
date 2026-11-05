"""Scoring arithmetic and evidence boundaries on disposable projects."""
from pathlib import Path
import copy,hashlib,json,subprocess,sys,tempfile,unittest
PACK=Path(__file__).resolve().parents[2]

class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.repo=Path(self.temp.name)
        (self.repo/'.agents').mkdir();(self.repo/'spec').mkdir()
        (self.repo/'.agents/crm-spec-kit.json').write_text(json.dumps(dict(schema_version=1,kit_id='crm-specification-standard',id_namespace='CRM',workstreams=[dict(id='p3',spec_root='spec',sources=[],read_only=[])])))
        self.artifact('STORY-CRM-001','Story','story.md')
        self.artifact('EPIC-CRM-001','Epic','epic.md')
        (self.repo/'spec/review.md').write_text('# Disposable review evidence\n')
        self.doc=self.init()
    def tearDown(self):self.temp.cleanup()
    def artifact(self,identity,kind,name):
        (self.repo/'spec'/name).write_text('# Artifact\n\n```crm-spec-kit\n'+json.dumps(dict(schema_version=1,artifact_id=identity,kind=kind,revision='r1',defined_ids=['REQ-CRM-001'] if kind=='Story' else []))+'\n```\n')
    def cli(self,*args,code=0):
        p=subprocess.run([sys.executable,'-B',str(PACK/'scripts/kit.py'),'score','--repo',str(self.repo),'--workstream','p3',*args],capture_output=True,text=True)
        self.assertEqual(p.returncode,code,p.stdout+p.stderr)
        return json.loads(p.stderr if code==2 else p.stdout)
    def init(self,identity='STORY-CRM-001',kind='Story',path='story.md',scope='manual'):
        return self.cli('--init','--target',identity,'--kind',kind,'--artifact','spec/'+path,'--revision','r1','--scope',scope)
    def ev(self):return dict(path='spec/review.md',revision='review-r1',sha256=hashlib.sha256((self.repo/'spec/review.md').read_bytes()).hexdigest(),locator='Review findings')
    def row(self,item,level=2):
        item.update(applicability='applies',present=level>0,level=level,rationale='Disposable assessment fixture',evidence=[self.ev()])
        if level==3:item['review']=dict(reviewer='Fixture reviewer',mode='specialist',evidence=[self.ev()],checks={f'Q{i:02}':dict(verdict='Đạt',rationale='Fixture evidence') for i in range(1,8)})
        return item
    def allrows(self,level=2):
        for i in self.doc['targets'][0]['items']:self.row(i,level)
    def calc(self,*args,code=0):
        (self.repo/'assessment.json').write_text(json.dumps(self.doc,ensure_ascii=False))
        return self.cli('--assessment','assessment.json',*args,code=code)
    def test_init_is_readonly_full_unknown(self):
        self.assertEqual(len(self.doc['targets'][0]['items']),12)
        self.assertTrue(all(i['level'] is None for i in self.doc['targets'][0]['items']))
        self.assertFalse((self.repo/'assessment.json').exists())
        out=self.calc();self.assertIsNone(out['targets'][0]['summary']['definition_index']);self.assertFalse(out['semantic_approval'])
    def test_exact_arithmetic_and_item_selection(self):
        self.allrows();out=self.calc('--target','STORY-CRM-001','--item','S09')
        self.assertEqual(out['targets'][0]['summary']['definition_index'],dict(lower=66.67,upper=66.67))
        self.assertTrue(out['targets'][0]['focused']);self.assertEqual(out['targets'][0]['summary']['expected'],1)
        self.assertEqual(out['targets'][0]['summary']['gate'],'not_assessed')
    def test_unknown_level_bounds_not_na(self):
        self.allrows();self.doc['targets'][0]['items'][0].update(level=None,present=None)
        s=self.calc()['targets'][0]['summary'];self.assertEqual(s['definition_index'],dict(lower=61.11,upper=69.44));self.assertEqual(s['unknown_levels'],1)
    def test_unknown_applicability_suppresses_index(self):
        self.allrows();self.doc['targets'][0]['items'][0].update(applicability='unknown',level=None,present=None)
        self.assertIsNone(self.calc()['targets'][0]['summary']['definition_index'])
    def test_no_omitted_catalog_row(self):
        self.doc['targets'][0]['items'].pop();self.calc(code=2)
    def test_duplicate_item_and_invalid_level(self):
        self.allrows();self.doc['targets'][0]['items'][0]['level']=True;self.calc(code=2)
        self.doc['targets'][0]['items'][0]['level']=4;self.calc(code=2)
        self.doc['targets'][0]['items'][0]['level']=2;self.doc['targets'][0]['items'][0]['id']='S02';self.calc(code=2)
    def test_stale_target_and_evidence_refused(self):
        self.allrows();(self.repo/'spec/review.md').write_text('changed');self.calc(code=2)
        self.allrows();(self.repo/'spec/story.md').write_text('changed');self.calc(code=2)
    def test_escape_and_wrong_identity(self):
        self.doc['targets'][0]['path']='../escape';self.calc(code=2)
        self.doc=self.init();self.doc['targets'][0]['id']='STORY-CRM-999';self.calc(code=2)
    def test_level3_requires_review_and_checks(self):
        self.allrows(3);self.calc()
        self.doc['targets'][0]['items'][0]['review']['mode']='self-check';self.calc(code=2)
        self.doc['targets'][0]['items'][0]['review']['mode']='specialist'
        self.doc['targets'][0]['items'][0]['review']['checks']['Q01']['verdict']='Không đạt';self.calc(code=2)
    def test_content_blocker_caps_level_but_approval_stays_separate(self):
        self.allrows(3);i=self.doc['targets'][0]['items'][0];i['blockers']=[dict(id='B1',reason='Approval pending',category='approval')]
        out=self.calc();self.assertEqual(out['targets'][0]['summary']['gate'],'blocked');self.assertEqual(out['targets'][0]['summary']['definition_index']['lower'],100)
        i['blockers'][0]['category']='content';self.calc(code=2)
        self.row(i,1);self.assertEqual(self.calc()['targets'][0]['summary']['gate'],'blocked')
    def test_na_requires_evidence_and_cannot_hide_core_item(self):
        self.doc=self.init('EPIC-CRM-001','Epic','epic.md');i=self.doc['targets'][0]['items'][3]
        i.update(applicability='na',rationale='No lifecycle delta',na_confirmation=dict(reviewer='Fixture reviewer',evidence=[self.ev()]))
        self.assertEqual(self.calc()['targets'][0]['summary']['na'],1)
        self.doc['targets'][0]['items'][6].update(copy.deepcopy(i),id='E07');self.calc(code=2)
    def test_rollups_separate_requirements_and_catalogs(self):
        self.allrows();req=self.init('REQ-CRM-001','Requirement','story.md')['targets'][0];self.row(req['items'][0],1);self.doc['targets'].append(req)
        out=self.calc();self.assertEqual(out['rollup']['catalog_obligations']['applicable'],12);self.assertEqual(out['rollup']['canonical_requirements']['applicable'],1)
        self.doc['targets'].append(copy.deepcopy(req));self.calc(code=2)
    def test_scopes_and_revision_collision(self):
        other=copy.deepcopy(self.doc['targets'][0]);other['scope']='import';self.doc['targets'].append(other)
        self.assertEqual(len(self.calc()['targets']),2)
        self.assertEqual(len(self.calc('--target','STORY-CRM-001','--scope','manual')['targets']),1)
        other['revision']='r2';self.calc(code=2)
    def test_zero_level_and_mandatory_story_na(self):
        self.allrows(0)
        s=self.calc()['targets'][0]['summary']
        self.assertEqual(s['definition_index'],dict(lower=0.0,upper=0.0))
        self.assertEqual(s['assessed'],12)
        self.doc=self.init();i=self.doc['targets'][0]['items'][0]
        i.update(applicability='na',rationale='Invalid exemption',na_confirmation=dict(reviewer='Fixture',evidence=[self.ev()]))
        self.calc(code=2)

    def test_command_is_available_in_copied_package_and_readonly(self):
        p=subprocess.run([sys.executable,'-B',str(PACK/'scripts/kit.py'),'install','--repo',str(self.repo),'--agent','codex','--apply'],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        self.allrows();(self.repo/'assessment.json').write_text(json.dumps(self.doc))
        hashes=lambda:{str(p.relative_to(self.repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in self.repo.rglob('*') if p.is_file()}
        before=hashes()
        helper=self.repo/'.agents/skills/crm-spec-kit/scripts/kit.py'
        p=subprocess.run([sys.executable,'-B',str(helper),'score','--repo',str(self.repo),'--workstream','p3','--assessment','assessment.json','--target','STORY-CRM-001','--format','markdown'],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        self.assertIn('66.67-66.67/100',p.stdout)
        self.assertEqual(hashes(),before)

    def test_conflicting_blocker_and_custom_weight_rejected(self):
        self.allrows(1);items=self.doc['targets'][0]['items']
        items[0]['blockers']=[dict(id='B1',reason='One meaning',category='content')]
        items[1]['blockers']=[dict(id='B1',reason='Different meaning',category='content')]
        self.calc(code=2)
        items[1]['blockers']=[];items[0]['weight']=4;self.calc(code=2)

    def add_record(self,kind='Assumption',state='Unverified',target='STORY-CRM-001',path='story.md',trace=None):
        prefix={'Assumption':'ASM','Decision':'DEC','Constraint':'CST'}[kind]
        record=dict(revision='r1',scope='manual',statement='Fixture statement',owner='Fixture owner',evidence=[],trace_links=trace or [])
        if kind=='Assumption':record.update(assumption_state=state,basis='Fixture basis',validation_method='Inspect fixture',review_due=None,if_false='Replan',validation_result='Fixture result')
        if kind=='Decision':record.update(decision_state=state,context='Fixture context',options='A/B',rationale='Fixture',consequences='Fixture',authority='Fixture authority',decided_at='2026-11-05T10:00:00+07:00')
        if kind=='Constraint':record.update(constraint_state=state,constraint_type='technical',verification_method='Inspect fixture',authority='Fixture authority',effective_from='2026-11-05')
        if state in ['Validated','Invalidated','Approved','Rejected','Confirmed']:
            e=self.ev();e['path']='review.md';record['evidence']=[e]
        identity=prefix+'-CRM-001'
        meta=dict(schema_version=2,kind=kind,artifact_id=identity,record=record)
        self.put_meta(prefix.lower()+'.md',meta)
        p=self.repo/'spec'/path
        text=p.read_text();m=json.loads(text.split('```crm-spec-kit\n')[1].split('\n```')[0]);m['trace_links']=[dict(id=identity,path=prefix.lower()+'.md',revision='r1',relation='depends-on')];self.put_meta(path,m)
        self.doc=self.init(target,'Story' if target.startswith('STORY') else 'Epic',path)
        return meta

    def put_meta(self,path,meta):
        (self.repo/'spec'/path).write_text('# Fixture\n\n```crm-spec-kit\n'+json.dumps(meta)+'\n```\n')

    def allocate(self,items):
        for d in self.doc['targets'][0]['record_dependencies']:
            d['items']=items
            d['allocation']=dict(reviewer='Fixture reviewer',rationale='Fixture affected contract item',evidence=[self.ev()])

    def test_unverified_assumption_unmapped_suppresses_index(self):
        self.add_record();self.allrows(3)
        out=self.calc();s=out['targets'][0]['summary']
        self.assertIsNone(s['definition_index']);self.assertEqual(s['confirmed'],0);self.assertEqual(s['gate'],'blocked')
        self.assertEqual(out['targets'][0]['items'][0]['declared_level'],3)
        self.assertEqual(out['targets'][0]['dependency_check']['unresolved'],['ASM-CRM-001'])

    def test_mapped_assumption_caps_only_affected_item_and_focus_keeps_target_blocked(self):
        self.add_record();self.allrows(3);self.allocate(['S07'])
        out=self.calc();items=out['targets'][0]['items'];self.assertEqual(items[6]['level'],1);self.assertEqual(items[5]['level'],3)
        self.assertEqual(out['targets'][0]['summary']['definition_index']['lower'],94.44)
        focused=self.calc('--target','STORY-CRM-001','--item','S06')
        self.assertEqual(focused['targets'][0]['summary']['definition_index']['lower'],100)
        self.assertEqual(focused['targets'][0]['summary']['gate'],'blocked')

    def test_validated_assumption_does_not_need_decision_or_cap(self):
        self.add_record(state='Validated');self.allrows(2)
        out=self.calc();self.assertEqual(out['targets'][0]['dependency_check']['unresolved'],[])
        self.assertEqual(out['targets'][0]['summary']['definition_index']['lower'],66.67)
        self.assertEqual(out['targets'][0]['summary']['gate'],'not_assessed')

    def test_invalidated_and_retired_assumption_still_consumed_blocks(self):
        for state in ['Invalidated','Retired']:
            self.add_record(state=state);self.allrows(2);self.allocate(['S07'])
            out=self.calc();self.assertEqual(out['targets'][0]['items'][6]['level'],1)
            self.assertEqual(out['targets'][0]['summary']['gate'],'blocked')

    def test_pending_decision_and_constraint_are_checked(self):
        for kind,state in [('Decision','Proposed'),('Constraint','Proposed')]:
            self.add_record(kind,state);self.allrows(2);self.allocate(['S07'])
            self.assertEqual(self.calc()['targets'][0]['items'][6]['level'],1)

    def test_record_hash_and_added_dependency_invalidate_old_assessment(self):
        m=self.add_record();self.allrows(2);m['record']['statement']='Changed';self.put_meta('asm.md',m);self.calc(code=2)
        self.doc=self.init();self.allrows(2);self.doc['targets'][0]['record_dependencies']=[];self.calc(code=2)

    def test_missing_mapping_evidence_and_legacy_policy_refused(self):
        self.add_record();self.allrows();self.allocate(['S07'])
        self.doc['targets'][0]['record_dependencies'][0]['allocation']['evidence']=[];self.calc(code=2)
        self.doc['policy']='crm-definition-v1';self.calc(code=2)

    def test_approved_decision_does_not_validate_assumption(self):
        self.add_record()
        # Decision approval is based on an unresolved assumption, so closure remains blocked.
        self.add_record('Decision','Approved',trace=[dict(id='ASM-CRM-001',path='asm.md',revision='r1',relation='derived-from')])
        self.allrows(2);self.allocate(['S07'])
        out=self.calc();self.assertEqual(out['targets'][0]['dependency_check']['unresolved'],['ASM-CRM-001'])
        self.assertEqual(out['targets'][0]['items'][6]['level'],1)

    def test_parent_epic_assumption_reaches_story(self):
        self.add_record(target='EPIC-CRM-001',path='epic.md')
        p=self.repo/'spec/story.md';m=json.loads(p.read_text().split('```crm-spec-kit\n')[1].split('\n```')[0])
        m['trace_links']=[dict(id='EPIC-CRM-001',path='epic.md',revision='r1',relation='parent')];self.put_meta('story.md',m)
        self.doc=self.init();self.allrows(2);self.allocate(['S07'])
        out=self.calc();self.assertEqual(out['targets'][0]['dependency_check']['unresolved'],['ASM-CRM-001'])
        self.assertEqual(out['targets'][0]['items'][6]['level'],1)

    def test_resolved_record_still_needs_pinned_snapshot(self):
        self.add_record(state='Validated');self.allrows(2)
        self.doc['targets'][0]['record_dependencies']=[];self.calc(code=2)

    def test_report_output_is_explicit_scoped_and_never_overwrites(self):
        self.allrows();(self.repo/'spec/reports').mkdir()
        (self.repo/'assessment.json').write_text(json.dumps(self.doc))
        command=[sys.executable,str(PACK/'scripts/kit.py'),'score','--repo',str(self.repo),'--workstream','p3','--assessment','assessment.json','--format','markdown','--output','spec/reports/score.md']
        p=subprocess.run(command,capture_output=True,text=True);self.assertEqual(p.returncode,0,p.stderr)
        text=(self.repo/'spec/reports/score.md').read_text();self.assertEqual(text,p.stdout)
        self.assertIn('Evidence và bước xử lý tiếp',text);self.assertIn('Mức đề xuất | Mức hiệu lực',text)
        p=subprocess.run(command,capture_output=True,text=True);self.assertEqual(p.returncode,2);self.assertEqual((self.repo/'spec/reports/score.md').read_text(),text)
        command[-1]='spec/story.md';p=subprocess.run(command,capture_output=True,text=True);self.assertEqual(p.returncode,2)

    def test_missing_evidence_timezone_and_item_context(self):
        self.allrows();self.doc['targets'][0]['items'][0]['evidence']=[];self.calc(code=2)
        self.allrows();self.doc['snapshot']='2026-11-05';self.calc(code=2)
        self.cli('--assessment','assessment.json','--item','S01',code=2)

if __name__=='__main__':unittest.main()
