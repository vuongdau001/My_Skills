"""Reuse lint record graph; pin it and allocate impact without inferring semantics."""
from argparse import Namespace


def snapshot(api,args,identity):
    audit=api['lint'](Namespace(repo=args.repo,config=args.config,workstream=args.workstream,gate='readiness',target=identity))
    errors=[x for x in audit['issues'] if x['level']=='ERROR' and x['code'] not in {'record-obligation', 'epic-legacy'}]
    if errors:
        raise api['KitError']('Dependency audit failed; resolve lint errors before scoring: '+str(errors[:5]))
    blocked={r['id'] for r in audit['record_obligations']}
    records=[]
    for r in audit['record_impacts']:
        if r['kind'] not in {'Assumption','Decision','Constraint'}:continue
        records.append(dict(id=r['id'],kind=r['kind'],state=r['state'],revision=r['revision'],path=r['path'],
                            sha256=api['digest'](args.repo.resolve()/r['path']),unresolved=r['id'] in blocked))
    return sorted(records,key=lambda r:r['id'])


def integrate(api,args,target,require,evidence,cache):
    identity=target['id']
    if identity not in cache:cache[identity]=snapshot(api,args,identity)
    current=cache[identity]
    recorded=target.get('record_dependencies')
    require(isinstance(recorded,list),'record_dependencies required; regenerate --init and reassess policy v2')
    require(all(isinstance(r,dict) for r in recorded),'record_dependencies must be objects')
    ids=[r.get('id') for r in recorded]
    require(len(ids)==len(set(ids)) and set(ids)=={r['id'] for r in current},identity+': dependency closure changed; regenerate snapshot and reassess')
    rows={r['id']:r for r in recorded};unknown=[];blockers=[]
    for actual in current:
        r=rows[actual['id']]
        require(all(r.get(k)==v for k,v in actual.items()),identity+': stale record dependency '+actual['id'])
        items=r.get('items')
        require(items is None or isinstance(items,list) and bool(items) and all(isinstance(i,str) for i in items) and len(items)==len(set(items)),actual['id']+': impact items must be nonempty unique IDs or null')
        if items is not None:
            require(set(items)<={i['id'] for i in target['items']},actual['id']+': impact item outside target catalog')
            allocation=r.get('allocation',{})
            require(isinstance(allocation,dict) and isinstance(allocation.get('rationale'),str) and allocation['rationale'].strip() and allocation.get('reviewer'),actual['id']+': impact allocation rationale/reviewer required')
            evidence(allocation.get('evidence'),actual['id']+' allocation')
        if not actual['unresolved']:continue
        b=dict(id='record:'+actual['id'],reason=actual['kind']+' '+actual['id']+' is '+str(actual['state']),category='content')
        blockers.append(b)
        if items is None:
            unknown.append(actual['id']);continue
        for item in target['items']:
            if item['id'] not in items:continue
            require(item['applicability']!='na',actual['id']+': unresolved dependency cannot be allocated to N/A')
            item.setdefault('blockers',[]).append(b)
            item.setdefault('score_adjustments',[]).append(b['reason'])
            if item['level'] is not None and item['level']>1:item['level']=1
    if unknown:
        for item in target['items']:
            item['level']=None
            item.setdefault('score_adjustments',[]).append('Unknown impact allocation: '+', '.join(unknown))
    return dict(records=current,unresolved=[r['id'] for r in current if r['unresolved']],
                impact_allocation_unknown=unknown,blockers=blockers,
                coverage='Declared typed links only; prose assumptions/missing links require reviewer inventory check',
                gate='blocked' if blockers else 'not_assessed')
