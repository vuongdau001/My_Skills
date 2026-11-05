"""Evidence-pinned definition maturity; read-only arithmetic, never semantic approval."""
from datetime import datetime
import copy
import os
import json
import re

POLICY = 'crm-definition-v2'
CATALOGS = {'Feature':('F',8), 'Epic':('E',16), 'Story':('S',12), 'Requirement':('definition',1)}
CORE = {'E01','E02','E03','E05','E06','E07','E10','E13','E14','E15','E16'}

def criteria(kind):
    prefix,count = CATALOGS[kind]
    return [f'{prefix}{i:02}' for i in range(1,count+1)] if kind != 'Requirement' else ['definition']


def run(api, args):
    error = api['KitError']
    def require(ok, message):
        if not ok: raise error(message)
    def string(x): return isinstance(x,str) and bool(x.strip())
    repo = args.repo.resolve()
    cfg = api['load_config'](repo,args.config)
    ws = api['select_stream'](cfg,args.workstream)
    root = api['relative'](repo,ws['spec_root'])
    def pin(value, label):
        require(isinstance(value,dict),label+': expected reference object')
        p = api['relative'](repo,value.get('path'))
        require(p.is_file(),label+': missing reference file')
        require(string(value.get('revision')),label+': revision required')
        require(bool(re.fullmatch('[a-f0-9]{64}',str(value.get('sha256','')))),label+': SHA256 required')
        require(api['digest'](p)==value['sha256'],label+': stale hash; reassess current revision')
        return p
    def evidence(refs,label):
        require(isinstance(refs,list) and bool(refs),label+': evidence required')
        for ref in refs:
            pin(ref,label)
            require(string(ref.get('locator')),label+': evidence locator required')
    def identity(t):
        require(isinstance(t,dict),'Target must be an object')
        require(t.get('kind') in CATALOGS,'Unsupported scoring kind')
        require(string(t.get('scope')),'Explicit target scope required')
        require(bool(re.fullmatch(api['id_pattern'](),str(t.get('id','')))),'Invalid target ID')
        p = pin(t,'target '+t['id'])
        require(p.is_relative_to(root),'Target must be inside selected workstream spec_root')
        meta = api['metadata'](p.read_text(encoding='utf-8'))
        require(bool(meta),'Target requires structured artifact metadata')
        owned = [meta.get('artifact_id')] + meta.get('defined_ids',[])
        require(t['id'] in owned,'Target ID not defined in pinned artifact')
        if t['kind'] != 'Requirement':
            require(meta.get('kind')==t['kind'],'Target kind mismatch')
        else:
            require(t['id'].split('-')[0] in {'REQ','BR','MOD'},'Requirement scoring expects canonical REQ/BR/MOD ID')
        if meta.get('revision'):
            require(t['revision']==meta['revision'],'Declared revision differs from artifact metadata')
        return p
    require(not(args.item and not args.target),'--item requires --target')
    require(not(args.scope and not args.target),'--scope requires --target')
    if args.init:
        require(not args.output,'--init emits JSON stdout; --output is for Markdown reports')
        require(not args.assessment and args.artifact and args.target and args.kind and args.revision and args.scope,
                '--init requires --artifact --target --kind --revision --scope, without --assessment')
        require(not args.item,'--init always creates the full catalog')
        p=api['relative'](repo,args.artifact)
        t=dict(id=args.target,kind=args.kind,path=args.artifact,revision=args.revision,
               sha256=api['digest'](p),scope=args.scope)
        identity(t)
        t['record_dependencies']=[dict(r,items=None) for r in api['support']('score_dependencies').snapshot(api,args,args.target)]
        t['items']=[dict(id=i,applicability='unknown',present=None,level=None,rationale='',evidence=[],blockers=[]) for i in criteria(args.kind)]
        return dict(schema_version=1,policy=POLICY,workstream=ws['id'],snapshot=api['now'](),
                    inventory=dict(revision=args.revision,scope='Selected artifact only',complete=False),targets=[t])
    require(args.assessment and not any([args.artifact,args.kind,args.revision]),'Use --assessment for calculation; authoring arguments require --init')
    data=api['read_json'](api['relative'](repo,args.assessment))
    require(isinstance(data,dict) and data.get('schema_version')==1 and data.get('policy')==POLICY,'Unsupported assessment schema/policy; v2 requires dependency snapshot: regenerate --init and reassess')
    require(data.get('workstream')==ws['id'],'Assessment workstream mismatch')
    try:
        timestamp=datetime.fromisoformat(data.get('snapshot','').replace('Z','+00:00'))
        require(timestamp.tzinfo is not None,'snapshot requires timezone')
    except (ValueError,TypeError):raise error('snapshot must be an ISO timestamp with timezone')
    inv=data.get('inventory')
    require(isinstance(inv,dict) and string(inv.get('revision')) and string(inv.get('scope')) and type(inv.get('complete')) is bool,'Inventory revision/scope/complete required')
    targets=data.get('targets')
    require(isinstance(targets,list) and bool(targets),'Nonempty targets list required')
    seen=set(); revisions={}; outputs=[]; selected=[]; blocker_defs={}; dependency_cache={}
    for original in targets:
        t=copy.deepcopy(original)
        identity(t)
        key=(t['id'],t['scope'])
        require(key not in seen,'Duplicate target/scope; do not silently deduplicate')
        seen.add(key)
        require(t['id'] not in revisions or revisions[t['id']]==(t['revision'],t['sha256']),'Mixed revisions for same logical ID')
        revisions[t['id']]=(t['revision'],t['sha256'])
        if t['kind']=='Requirement':
            require(sum(x.get('id')==t['id'] for x in targets)==1,'Canonical requirement must occur once in inventory')
        items=t.get('items')
        require(isinstance(items,list) and all(isinstance(i,dict) for i in items),'items must be object list')
        expected=criteria(t['kind']);ids=[i.get('id') for i in items]
        require(len(ids)==len(expected) and set(ids)==set(expected),'Full catalog required; use --item to filter results, not to omit assessment rows')
        for i in items:
            label=t['id']+'/'+i['id'];app=i.get('applicability');level=i.get('level')
            require(app in ('applies','na','unknown'),label+': invalid applicability')
            require(i.get('present') is None or type(i['present']) is bool,label+': present must be boolean/null')
            require(level is None or type(level) is int and 0<=level<=3,label+': level must be integer 0..3 or null')
            blockers=i.get('blockers',[])
            require(isinstance(blockers,list),label+': blockers must be list')
            for b in blockers:
                require(isinstance(b,dict) and string(b.get('id')) and string(b.get('reason')) and b.get('category') in ('content','approval','delivery'),label+': blocker id/reason/category required')
                require(b['id'] not in blocker_defs or blocker_defs[b['id']]==b,label+': conflicting definitions for shared blocker ID')
                blocker_defs[b['id']]=b
            if app!='applies':
                require(level is None and i.get('present') is None,label+': N/A/unknown must not carry score/presence')
            require(type(i.get('weight',1)) is int and i.get('weight',1)==1,label+': scoring policy uses equal weights only')
            if app=='na':
                require(not (t['kind']=='Epic' and i['id'] in CORE),label+': mandatory Epic catalog item cannot be N/A')
                require(t['kind']=='Epic',label+': only conditional Epic items may be wholly N/A; use applicable refs/delta for Feature/Story')
                require(not blockers,label+': N/A cannot hide blockers')
                c=i.get('na_confirmation',{})
                require(string(i.get('rationale')) and string(c.get('reviewer')),label+': N/A rationale/reviewer required')
                evidence(c.get('evidence'),label+' N/A')
            if level is not None:
                require(string(i.get('rationale')),label+': score rationale required')
                if level==0:require(i.get('present') is False,label+': level 0 requires present=false')
                else:
                    require(i.get('present') is True,label+': positive level requires present=true')
                    evidence(i.get('evidence'),label)
                if level>=2:require(not any(b['category']=='content' for b in blockers),label+': unresolved content blocker caps level at 1')
                if level==3:
                    review=i.get('review',{})
                    require(string(review.get('reviewer')) and review.get('mode') in ('specialist','independent'),label+': level 3 needs specialist/independent review declaration, not AI self-check')
                    evidence(review.get('evidence'),label+' review')
                    checks=review.get('checks',{})
                    require(isinstance(checks,dict) and set(checks)=={f'Q{n:02}' for n in range(1,8)},label+': Q01-Q07 review disposition required')
                    for check in checks.values():
                        require(isinstance(check,dict) and check.get('verdict') in ('Đạt','N/A') and string(check.get('rationale')),label+': unresolved quality check; not confirmed level 3')
        for i in items:
            i['declared_level']=i['level']
        dependency=api['support']('score_dependencies').integrate(api,args,t,require,evidence,dependency_cache)
        t['_dependency_check']=dependency
        chosen=[i for i in items if not args.item or i['id']==args.item]
        if args.target and t['id']!=args.target or args.scope and t['scope']!=args.scope:continue
        require(bool(chosen),'Item does not belong to selected target catalog')
        selected.append((t,chosen))
    require(bool(selected),'No matching target/scope')
    def summarize(rows):
        applies=[i for i in rows if i['applicability']=='applies']
        pending=sum(i['applicability']=='unknown' for i in rows)
        assessed=[i for i in applies if i['level'] is not None]
        unknown=len(applies)-len(assessed);n=len(applies);total=sum(i['level'] for i in assessed)
        bounds=None if not n or pending else dict(lower=round(100*total/(3*n),2),upper=round(100*(total+3*unknown)/(3*n),2))
        blockers={b['id']:b for i in rows for b in i.get('blockers',[])}
        return dict(expected=len(rows),applicable=n,applicability_unknown=pending,na=sum(i['applicability']=='na' for i in rows),
                    present=sum(i.get('present') is True for i in applies),presence_unknown=sum(i.get('present') is None for i in applies),
                    assessed=len(assessed),assessment_coverage_pct=round(100*len(assessed)/n,2) if n else None,
                    unknown_levels=unknown,levels={str(k):sum(i['level']==k for i in assessed) for k in range(4)},
                    confirmed=sum(i['level']==3 for i in assessed),definition_index=bounds,
                    blockers=list(blockers.values()),gate='blocked' if blockers else 'not_assessed')
    for t,items in selected:
        summary=summarize(items)
        if t['_dependency_check']['blockers']:
            summary['gate']='blocked'
        if t['_dependency_check']['impact_allocation_unknown']:
            summary['definition_index']=None
        outputs.append(dict(id=t['id'],kind=t['kind'],scope=t['scope'],revision=t['revision'],sha256=t['sha256'],
                            declared_summary=summarize([dict(i,level=i['declared_level']) for i in items]),summary=summary,items=items,dependency_check=t['_dependency_check'],focused=bool(args.item)))
    # Distinct ledgers: catalog obligations are not requirements, nor business value.
    catalog=[i for t,rows in selected if t['kind']!='Requirement' for i in rows]
    req=[i for t,rows in selected if t['kind']=='Requirement' for i in rows]
    result=dict(valid=True,policy=POLICY,workstream=ws['id'],snapshot=data['snapshot'],inventory=inv,
                report_scope='focused item' if args.item else 'selected targets' if args.target else 'assessment inventory',targets=outputs,
                rollup=dict(catalog_obligations=summarize(catalog),canonical_requirements=summarize(req)),
                semantic_approval=False,authority_verified=False,project_completeness_verified=False,
                dependency_policy='Current typed ASM/DEC/CST closure checked and pinned; unresolved mapped items capped at 1; unmapped impact suppresses index',
                note='Equal-weight ordinal definition index, not percent correct/effort/value. Unknown applicability suppresses index. Bounds cover known applicable inventory only. No gate/approval granted; evidence hashes validate bytes, not truth or reviewer authority. Inventory completeness is a declaration, not a discovered fact. No source artifacts modified; --output explicitly saves a new report.')
    for name,kind in [('catalog_obligations',False),('canonical_requirements',True)]:
        if any(t['_dependency_check']['blockers'] for t,_ in selected if (t['kind']=='Requirement')==kind):
            result['rollup'][name]['gate']='blocked'
    for name,kind in [('catalog_obligations',False),('canonical_requirements',True)]:
        if any(t['_dependency_check']['impact_allocation_unknown'] for t,_ in selected if (t['kind']=='Requirement')==kind):
            result['rollup'][name]['definition_index']=None
    if args.format=='json':
        require(not args.output,'--output requires --format markdown')
        return result
    lines=['# Báo cáo mức hoàn thiện phân tích','',
           'Báo cáo tách điểm đề xuất với điểm hiệu lực sau kiểm dependency. Kết quả là chỉ số mức hoàn thiện trên phạm vi đã khai báo, không là % yêu cầu đúng hoặc % sản phẩm hoàn thành.',
           '', '## Bối cảnh đánh giá', '',
           f'- **Policy / workstream:** {POLICY} / {ws["id"]}.',
           f'- **Snapshot:** {data["snapshot"]}.',
           f'- **Inventory:** {inv["scope"]} / {inv["revision"]}.',
           f'- **Khai báo đầy đủ:** {inv["complete"]}; chưa được tool xác minh.',
           '- **Người thực hiện/chế độ (khai báo):** '+str(data.get('assessment_context','Chưa khai báo; không tự là independent review')), '',
           '## Kết quả chính','']
    lines.extend(['| Artifact | Điểm đề xuất | Điểm hiệu lực | Gate |','|---|---|---|---|'])
    def display_index(s):
        d=s['definition_index']
        return f'{d["lower"]}-{d["upper"]}/100' if d else 'Unknown/N/A'
    for out in outputs:
        s=out['summary']
        lines.append('| '+' | '.join(str(x).replace('|','/').replace('\n',' ') for x in [out['id'],display_index(out['declared_summary']),display_index(s),s['gate']])+' |')
    lines.extend(['','Gate not_assessed không có nghĩa Ready. Mức 3 cần review evidence; record này không tự cấp approval.',''])
    for out in outputs:
        s=out['summary'];index=s['definition_index']
        lines.extend([f'## {out["id"]}', '',
            f'- **Phạm vi / revision:** {out["scope"]} / {out["revision"]}.',
            f'Chỉ số hiệu lực: {index["lower"]}-{index["upper"]}/100' if index else 'Chỉ số: Unknown/N/A — cần xác định applicability, inventory hoặc phạm vi ảnh hưởng dependency',
            '',f'- **Đã đánh giá:** {s["assessed"]}/{s["applicable"]}.',
            f'- **Mức 3 / applicability Unknown / N/A:** {s["confirmed"]} / {s["applicability_unknown"]} / {s["na"]}.',
            f'- **Gate:** {s["gate"]}.',
            '','| Hạng mục | Applicability | Mức đề xuất | Mức hiệu lực |','|---|---|---|---|'])
        for i in out['items']:
            clean=lambda v:str(v).replace('|','/').replace('\n',' ')
            lines.append('| '+' | '.join(map(clean,[i['id'],i['applicability'],i['declared_level'] if i['declared_level'] is not None else 'Unknown',i['level'] if i['level'] is not None else 'Unknown']))+' |')
        lines.extend(['','### Kiểm tra dependency ASM/DEC/CST',out['dependency_check']['coverage']])
        if not out['dependency_check']['records']:
            lines.append('Không tìm thấy ASM/DEC/CST trong typed dependency closure; không chứng minh đã hết giả định/câu hỏi. Cần kiểm queue/prose và allocation bằng review.')
        for r in out['dependency_check']['records']:
            lines.append(f'- **{r["id"]}:** {r["kind"]}, {r["state"]}, revision {r["revision"]}.')
        if out['dependency_check']['records']:
            lines.extend(['','<details>','<summary>Nguồn và hash của record dependencies</summary>',''])
            for r in out['dependency_check']['records']:
                lines.extend([f'- {r["id"]}: {r["path"]}',f'  Revision: {r["revision"]}; SHA-256: {r["sha256"]}'])
            lines.extend(['','</details>',''])
        for b in out['dependency_check']['blockers']:lines.append(f'- **Dependency còn chặn — {b["id"]}:** {b["reason"]}')
        if out['dependency_check']['impact_allocation_unknown']:
            lines.append('**Việc tiếp theo:** phân bổ ảnh hưởng tới catalog items, có rationale/review evidence. Chưa cấp chỉ số khi phạm vi ảnh hưởng còn Unknown.')
        lines.extend(['','### Evidence và bước xử lý tiếp'])
        for i in out['items']:
            lines.extend(['',f'#### {i["id"]}', '', '**Lý do đánh giá:** '+(i.get('rationale','') or 'Cần xác định applicability/nội dung và ghi rationale.')])
            for adjustment in i.get('score_adjustments',[]):lines.append('**Điều chỉnh điểm:** '+adjustment)
            if i.get('evidence'):
                lines.extend(['','<details>','<summary>Evidence và phiên bản</summary>',''])
                for e in i['evidence']:lines.extend([f'- Nguồn: {e["path"]}',f'  Revision: {e["revision"]}; locator: {e["locator"]}',f'  SHA-256: {e["sha256"]}'])
                lines.extend(['','</details>',''])
            for b in i.get('blockers',[]):lines.append(f'- **Cần xử lý {b["id"]} ({b["category"]}):** {b["reason"]}; sau đó đánh giá lại revision bị ảnh hưởng.')
        for b in s['blockers']:lines.append(f'- **Blocker {b["id"]} ({b["category"]}):** {b["reason"]}')
        lines.append('')
    lines.extend(['## Tổng hợp theo ledger',''])
    for name,summary in result['rollup'].items():
        lines.extend([f'### {name}', '',f'- **Áp dụng / mức 3:** {summary["applicable"]} / {summary["confirmed"]}.',
                      f'- **Chỉ số mức hoàn thiện:** {display_index(summary)}.',f'- **Gate:** {summary["gate"]}.',''])
    lines.extend(['## Giới hạn kết luận','',
                  'Chỉ số dùng thang thứ bậc với trọng số bằng nhau, không đo % đúng, effort hoặc giá trị. Applicability Unknown làm chỉ số chưa được cấp; khoảng điểm chỉ bao phủ inventory đã biết là áp dụng.', '',
                  'Báo cáo không cấp gate hoặc approval. Hash chỉ xác minh byte, không chứng minh nội dung đúng hay reviewer có thẩm quyền. Tính đầy đủ của inventory là khai báo, không phải fact được tool tự phát hiện.', '',
                  'Không sửa source artifacts. Chỉ lưu report mới khi có --output; không ghi đè kết quả cũ.'])
    report='\n'.join(lines)+'\n'
    if args.output:
        output=api['relative'](repo,args.output)
        reports=api['relative'](root,api['artifact_paths'](ws)['reports'])
        require(output.is_relative_to(reports) and output.suffix=='.md','--output must be a new Markdown file inside configured reports directory')
        api['check_write_boundaries'](repo,cfg,[output])
        meta=dict(schema_version=1,kind='Report',review_verdict='Chưa kiểm',references=[os.path.relpath(api['relative'](repo,args.assessment),output.parent).replace(os.sep,'/')])
        report+='\n<details>\n<summary>Metadata cho công cụ</summary>\n\n```crm-spec-kit\n'+json.dumps(meta,ensure_ascii=False,indent=2)+'\n```\n\n</details>\n'
        with output.open('x',encoding='utf-8') as f:f.write(report)
    return report
