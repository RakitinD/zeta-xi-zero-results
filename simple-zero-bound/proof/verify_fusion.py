"""Standalone exact replay. Python standard library only; no optimizer or local replay.

python -B -X utf8 verify_fusion.py
python -B -X utf8 verify_fusion.py --all
"""
import sys
sys.dont_write_bytecode=True
if not __debug__:raise RuntimeError('Assertions must be enabled.')
import argparse,json,hashlib,gzip,time
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
ROOT=Path(__file__).resolve().parent
H=Q('210042647916503/312500000000000')
COMP=Q('8269551442741204889710953/12278882618209750000000000')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def local_data():
    p=ROOT/'B/IMPORTED_LOCAL_PAYLOAD.json'
    if not p.exists():p=ROOT/'imported/B/IMPORTED_LOCAL_PAYLOAD.json'
    return read(p)

def rows(m,trim,data):
    assert 250<=m<=750
    result={};n=m-6;B=Q(data['B']);eta=Q(data['triple_target'])
    for case in data['case_order']:
        r=data['rows'][case];p=list(map(Q,r['pressures']));eps=Q(r['target'])
        d=[sum(p[:k+1],Q(0))/B for k in range(6)]
        for a in range(6 if trim else 1):
            for b in range(a,6 if trim else 1):
                if case!='base' and a!=b:continue
                count=n-a-b
                target=(3*(count//3)*eta+(count%3)*eps if case=='base' else count*eps)/n
                coeff=[Q(1)]+[((d[k-a] if k>=a else Q(0))+(d[k-b] if k>=b else Q(0)))/2 for k in range(5)]+[d[5]]
                result[f'{case}_trim_{a}_{b}']=(coeff,target)
    assert len(result)==(69 if trim else 9)
    return result

def profile_point(E,y,m,rho):
    assert E>=0
    tau=Q(7,6);c=1+rho/2
    if E<=tau*c*c:assert y<=E;return
    z=((1+Q(m)/tau)*y-E+m*c*c)/(2*m*c)
    if z>0:assert z*z<=E/tau

def check_certificate(path):
    d=read(path);data=local_data();m=d['m'];n=m-6;rho=Q(d['rho']);R=Q(d['reward']);ts=list(map(Q,d['prices']))
    assert d['h']==str(H) and Q(d['comparator'])==COMP and Q(d['B'])==Q(data['B'])
    assert 0<=rho<=4 and 0<=R<m and len(ts)==6 and min(ts)>=0
    rr=rows(m,d['trim'],data)
    knots=[(Q(k['E']),Q(k['profile_lower'])) for k in d['knots']]
    assert knots[0][0]==0 and all(a[0]<b[0] for a,b in zip(knots,knots[1:]))
    for E,y in knots:profile_point(E,y,m,rho)
    assert len(d['lines'])==len(knots)
    smallest=None
    for i,line in enumerate(d['lines']):
        slope=Q(line['slope']);intercept=Q(line['intercept']);assert slope>=0
        assert line['left_knot']==i
        if i+1<len(knots):
            assert line['right_knot']==i+1
            assert slope*knots[i][0]+intercept==knots[i][1]
            assert slope*knots[i+1][0]+intercept==knots[i+1][1]
        else:assert line['right_knot'] is None and slope==0 and intercept==knots[i][1]
        weights={j:Q(w) for j,w in line['dual_weights'].items()};assert all(j in rr and w>=0 for j,w in weights.items())
        load=[sum(w*rr[j][0][k] for j,w in weights.items()) for k in range(7)]
        cost=[n*slope]+[n*t for t in ts]
        assert all(a<=b for a,b in zip(load,cost))
        value=intercept+sum(w*rr[j][1] for j,w in weights.items())
        assert value==Q(line['certified_value']) and value>=R
        smallest=value-R if smallest is None else min(smallest,value-R)
    # For every E>=0, a covering chord (or the last constant ray) lies below G(E).
    # Every chord line + pressure >= R by a rational Farkas certificate; hence G+pressure >= R.
    P=Q(data['B'])*(2*sum(ts[:5])+(m-11)*ts[5]);assert P==Q(d['pressure'])
    s=Q(d['separator']);pb=Q(d['penalty_upper']);assert H<=s<1 and pb>=0
    mode=d['global_payment_certified']
    if mode=='zero':assert rho==0 and pb==0
    elif mode=='g8elementary':assert pb>=rho*rho/8
    elif mode=='g8':
        # pb >= 4+rho-sqrt(16+8rho), safe sign before squaring.
        t=4+rho-pb
        if t>0:assert t*t<=16+8*rho
    elif mode=='g2':assert pb>=rho*rho*((1-s)/2+s*(s-H)/(2*s-H))/4
    elif mode=='G6_GF02B_PAYMENT':
        N=((2-H)*s-H)/2;A=2*s-H+rho*s
        assert N>0 and A>0 and pb*pb+A*pb>=rho*rho*N/4
    else:raise AssertionError('unknown payment')
    margin=m*H-P-m*pb-(m-R)*s
    assert margin>0 and margin==Q(d['endgame_margin'])
    assert s-COMP==Q(d['strict_gain'])
    return {'path':str(path.relative_to(ROOT)),'status':'PASS_EXACT','m':m,'trim':d['trim'],'payment':mode,'rho':str(rho),'reward':str(R),'separator':str(s),'gain_over_comparator':str(s-COMP),'strict_gain':s>COMP,'chord_and_ray_certificates':len(knots),'minimum_plane_margin':str(smallest),'endgame_margin':str(margin)}

def check_primary_binding():
    base=ROOT/'imported/primary'
    if not base.exists():base=ROOT/'repro/Zeta_Reblocking_Repro'
    d=local_data();p=read(base/'parameters.json')
    assert Q(p['H_floor'])==H and Q(d['B'])==Q(p['B']) and Q(d['triple_target'])==Q(p['triple_target'])
    for name in d['case_order']:
        r=d['rows'][name];c=read(base/f'candidates/{name}.json')
        assert r['window']==c['window'] and Q(r['target'])==Q(c['proposed_target'])
        assert list(map(Q,r['pressures']))==[Q(v,c['position_pressure']['denominator']) for v in c['position_pressure']['numerators']]
        assert [(i,j,Q(v)) for i,j,v in r['pairs']]==[(i,j,Q(v,c['pair_weights']['denominator'])) for i,j,v in c['pair_weights']['entries']]
        assert all(Q(v)>=0 for i,j,v in r['pairs'])
        for span in range(1,7):assert sum(Q(v) for i,j,v in r['pairs'] if j-i==span)==2
    P=Q(p['B'])*(2*sum(map(Q,p['prices'][:5]))+(p['m']-11)*Q(p['prices'][5]))
    assert (p['m']*H-P)/(p['m']-Q(p['R']))==COMP
    # Supplied finite search cap is justified without imposing an energy cap on the theorem.
    assert 744*max(Q(r['target']) for r in d['rows'].values())<=Q(7,6)*9
    return {'status':'PASS_EXACT','rows_compared_to_primary':9,'baseline_reconstructed':str(COMP),'rho_search_cap':'4','universal_local_proofs':'IMPORTED_PINNED_EVIDENCE_NOT_REPLAYED'}

def check_enumeration():
    ledger=read(ROOT/'LEGAL_COMBINATIONS.json');graph=read(ROOT/'MODULE_GRAPH.json')
    compressed=(ROOT/'ALL_RAW_LEGAL_SUBSETS.json.gz').read_bytes()
    assert hashlib.sha256(compressed).hexdigest()==ledger['raw_legal_list']['sha256']
    rawbytes=gzip.decompress(compressed);assert hashlib.sha256(rawbytes).hexdigest()==ledger['raw_legal_list']['uncompressed_sha256']
    raw=read_json_bytes(rawbytes);order=raw['module_order'];assert order==graph['canonical_active_order']
    mods={m['module_id']:m for m in graph['imported_modules'] if m['status'] in ['ACTIVE_EXACT','ACTIVE_CONDITIONAL']}
    assert set(mods)==set(order) and len(order)==26
    pos={k:i for i,k in enumerate(order)};deps=[sum(1<<pos[j] for j in mods[k]['dependencies'] if j in pos) for k in order]
    assert all(d<(1<<i) for i,d in enumerate(deps))
    expected=[];pruned=0
    def walk(i,mask):
        nonlocal pruned
        if i==len(order):expected.append(mask);return
        walk(i+1,mask)
        if mask&deps[i]==deps[i]:walk(i+1,mask|(1<<i))
        else:pruned+=1<<(len(order)-i-1)
    walk(0,0)
    assert expected==raw['legal_masks'] and len(expected)==ledger['raw_legal_count']
    assert pruned==ledger['pruned_by_dependency'] and pruned+len(expected)==ledger['raw_candidate_count']==2**26
    cm=1<<pos['G9_CONDITIONAL_MOMENTS'];cond=sum(bool(mask&cm) for mask in expected)
    assert ledger['surviving_classes'][0]['raw_subsets_mapped']==len(expected)-cond
    assert ledger['surviving_classes'][1]['raw_subsets_mapped']==cond
    return {'status':'PASS_EXACT','raw_candidates':2**26,'legal_subsets':len(expected),'dependency_rejections':pruned,'surviving_numeric_classes':1,'uninstantiable_conditional_classes':1}
def read_json_bytes(x):return json.loads(x)

def check_manifest():
    p=ROOT/'MANIFEST.json'
    if not p.exists():return {'status':'PRE_FREEZE_MANIFEST_NOT_YET_PRESENT'}
    manifest=read(p)
    for f in manifest['files']:
        file=ROOT/f['path'];assert file.stat().st_size==f['bytes'] and sha(file)==f['sha256']
    return {'status':'PASS_SHA256','files':len(manifest['files'])}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--all',action='store_true');args=ap.parse_args();tm=time.time()
    primary=check_primary_binding();enumeration=check_enumeration()
    paths=sorted((ROOT/'certificates').glob('*.json')) if args.all else [ROOT/'certificates/m492_trim_full.json']
    certs=[check_certificate(p) for p in paths]
    if not args.all:assert certs[0]['strict_gain']
    result={'schema':'PGF_C_STANDALONE_REPLAY_V1','status':'PASS_EXACT','primary_binding':primary,'enumeration':enumeration,'certificates':certs,'manifest':check_manifest(),'elapsed_seconds':time.time()-tm,'scope':'Exact local planes, separators, enumeration and supplied hashes. Analytic theorems and the 58,577,037-node full replay remain imported trust inputs.'}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
