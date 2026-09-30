#!/usr/bin/env python3
"""Search the bundled pattern, source and resource indexes without network access."""
from pathlib import Path
import argparse, collections, json, math, re
ROOT = Path(__file__).resolve().parents[1]
STOP = set('a an the and or for to of in with make create build want that this from using'.split())
ALIASES = {'sumi': ['ink'], 'watercolor': ['ink','paint'], 'watercolour': ['ink','paint'], 'typography': ['type','glyph'], 'kinetic': ['motion'], 'spring': ['elastic','snap'], 'ik': ['foot','rig'], 'footsteps': ['foot','contact'], 'audio': ['sound'], 'lofi': ['pixel','daylight'], 'weather': ['wind','rain','daylight'], 'morph': ['shape','transition'], 'storytelling': ['story'], 'puppet': ['rig','character'], 'simulation': ['physics'], 'reactive': ['response'], '3d': ['spatial'], 'letters': ['glyph','letter'], 'messy': ['disorder','chaos'], 'organized': ['organization','order'], 'feet': ['foot'], 'walking': ['stance','gait']}
def words(text):
    return [x for x in re.findall(r'\w+', text.lower()) if len(x)>1 and x not in STOP]
def load(kind):
    if kind == 'sources':
        return [json.loads(line) for line in (ROOT/'references/source-catalog.jsonl').read_text().splitlines()]
    filename = {'patterns': 'patterns.json', 'resources': 'resources.json', 'visuals': 'visual-comparisons.json'}[kind]
    return json.loads((ROOT/'references'/filename).read_text())
def search(query, kind='patterns', family=None, limit=6, prompt_only=False):
    records = load(kind)
    if family: records = [r for r in records if r.get('family') == family]
    if prompt_only: records = [r for r in records if r.get('prompt_signal') in {'marker-in-retrieved-text','creator-prompt-retrieved'} or r.get('prompt')]
    if not records: return []
    original=words(query); expanded=list(dict.fromkeys(original+[a for t in original for a in ALIASES.get(t,[])]))
    docs=[collections.Counter(words(json.dumps(r,ensure_ascii=False))) for r in records]
    df=collections.Counter(t for d in docs for t in d); avg=sum(sum(d.values()) for d in docs)/len(docs)
    ranked=[]
    for r,d in zip(records,docs):
        n=sum(d.values()); title=set(words(r.get('title','')+' '+r.get('id',''))); score=0
        for t in expanded:
            tf=d[t]
            if not tf:continue
            idf=math.log(1+(len(docs)-df[t]+.5)/(df[t]+.5))
            score+=(1 if t in original else .45)*idf*(tf*2.2/(tf+1.2*(.25+.75*n/max(avg,1))))
            if t in title:score+=1.5 if t in original else .4
        if score: ranked.append((score,r))
    ranked.sort(key=lambda p:(-p[0],p[1].get('id',p[1].get('url',''))))
    return [dict(r,search_score=round(s,3)) for s,r in ranked[:limit]]
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query');ap.add_argument('--kind',choices=['patterns','sources','resources','visuals'],default='patterns')
    ap.add_argument('--family');ap.add_argument('--limit',type=int,default=6);ap.add_argument('--prompt-only',action='store_true');ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    if args.limit<1 or args.limit>100:ap.error('--limit must be between 1 and 100')
    found=search(args.query,args.kind,args.family,args.limit,args.prompt_only)
    if args.json: print(json.dumps(found,ensure_ascii=False,indent=2));return
    if not found:print('No matching records. Try a physical mechanism or a broader term.');return
    for r in found:
        print('\n'+r['title'])
        if args.kind=='patterns':
            print(f"  Read: references/patterns/{r['family']}.md#{r['id']}")
            print('  Mechanism: '+r['mechanism']);print('  Check: '+r['check'])
            print('  Sources: '+' '.join(r['source_urls']))
        elif args.kind=='sources':
            print('  '+r['url']);print('  Evidence: '+r['retrieval']+'; '+r['visual_review'])
            print('  Prompt signal: '+r['prompt_signal']+' (a marker alone is not proof of a complete prompt)')
            if r.get('visual_reference_url'):print('  Compare videos: '+r['visual_reference_url'])
            if r['pattern_ids']:print('  Patterns: '+', '.join(r['pattern_ids']))
            if r['note']:print('  Note: '+r['note'])
            if r['links']:print('  Linked resources: '+' '.join(r['links']))
            if r['related_creator_posts']:print('  Selected creator follow-ups: '+' '.join(r['related_creator_posts'][:6]))
        elif args.kind=='visuals':
            print('  Compare: '+r['detail_url']);print('  Original: '+r['url'])
            print('  Prompt: '+r['prompt_evidence']);print('  Visual: '+r['visual_review'])
            print('  Model: '+r['model_evidence'])
        else:
            print('  '+r['url']);print('  Evidence: '+r['inspection'])
            if r.get('note'):print('  '+r['note'])
if __name__=='__main__':main()
