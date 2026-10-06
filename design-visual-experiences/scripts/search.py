#!/usr/bin/env python3
"""Find local build guidance; use explicit kinds for source/resource/comparison research."""
from pathlib import Path
import argparse
import collections
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
STOP = set('a an the and or for to of in with make create build want that this from using is it as by on at be into when then only one use should can'.split())
ALIASES = {'sumi': ['ink'], 'watercolor': ['ink', 'paint'], 'watercolour': ['ink', 'paint'], 'typography': ['type', 'glyph'], 'kinetic': ['motion'], 'spring': ['elastic', 'snap'], 'ik': ['foot', 'rig'], 'footsteps': ['foot', 'contact'], 'audio': ['sound'], 'lofi': ['pixel', 'daylight'], 'weather': ['wind', 'rain', 'daylight'], 'morph': ['shape', 'transition'], 'storytelling': ['story'], 'puppet': ['rig', 'character'], 'simulation': ['physics'], 'reactive': ['response'], 'responsive': ['response'], '3d': ['spatial'], 'letters': ['glyph', 'letter'], 'messy': ['disorder', 'chaos'], 'organized': ['organization', 'order'], 'feet': ['foot'], 'walking': ['stance', 'gait'], 'reproducible': ['seeded', 'replay'], 'repeatable': ['seeded', 'replay']}
# Evidence/history and alternate browsing views are deliberately outside build search.
RESEARCH = {'atlas', 'examples', 'source-cards', 'principles', 'toolkits', 'evidence', 'research-coverage', 'inspected-sources', 'visual-comparisons', 'motion-recipes', 'briefs-and-review'}
SECTION_GUIDES = {'composition-choreography', 'creative-production', 'feature-launch-films', 'production', 'interactive-3d', 'build-patterns', 'principles', 'diagnosis'}
CORE_FIELDS = {'Mechanism': 'mechanism', 'Build': 'build', 'Tune': 'tune', 'Failure check': 'check', 'Adapted prompt': 'prompt', 'Evidence': 'evidence'}


def words(text):
    tokens = [x for x in re.findall(r'\w+', text.lower()) if len(x) > 1 and x not in STOP]
    # Small, predictable plural normalization; do not turn physics into physic or glass into glas.
    return [x[:-3]+'y' if len(x) > 4 and x.endswith('ies') else
            x[:-1] if len(x) > 3 and x.endswith('s') and not x.endswith(('ss', 'us', 'is', 'ics')) and x not in {'canvas', 'lens'} else x
            for x in tokens]


EXPANSIONS = {words(key)[0]: words(' '.join(values)) for key, values in ALIASES.items()}


def slug(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def plain(text):
    """Keep visible words; URLs, markup and schema labels must not affect rank."""
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'https?://\S+', '', text)
    return re.sub(r'<[^>]+>|[*`#]', '', text).strip()


def card_fields(text):
    result = {}
    matches = list(re.finditer(r'^\*\*([^*]+):\*\*\s*', text, re.M))
    for i, match in enumerate(matches):
        key = CORE_FIELDS.get(match[1])
        if not key:
            continue
        value = text[match.end():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
        result[key] = re.findall(r'^\d+\. (.+)$', value, re.M) if key == 'build' else value
    return result


def patterns():
    """JSON owns identity/source membership; Markdown owns the implementation."""
    records = json.loads((ROOT/'references/patterns.json').read_text())
    texts = {}
    for record in records:
        family = record['family']
        if family not in texts:
            texts[family] = (ROOT/f'references/patterns/{family}.md').read_text()
        marker = f'<a id="{record["id"]}"></a>'
        section = texts[family].split(marker, 1)[1].split('<a id=', 1)[0]
        record.update(card_fields(section))
        record['title'] = re.search(r'^## (.+)$', section, re.M)[1]
        record.update(kind='patterns', path=f'references/patterns/{family}.md#{record["id"]}')
    return records


def operational(text):
    """Exclude evidence-only sections from relevance, without hiding them at the destination."""
    text = re.sub(r'^## (?:Evidence|Source|Reference|Inspection|Attribution)[^\n]*\n.*?(?=^## |\Z)', '', text, flags=re.M | re.S)
    return '\n'.join(line for line in text.splitlines() if not re.match(r'^\*\*(?:Evidence|Source|Attribution)[.:]', line))


def section_records(path, kind):
    text = path.read_text()
    title = re.search(r'^# (.+)$', text, re.M)[1]
    relative = path.relative_to(ROOT).as_posix()
    if path.stem not in SECTION_GUIDES and kind != 'compositions':
        body = operational(text)
        return [dict(id=path.stem, kind=kind, title=title, path=relative, body=body)]
    headings = list(re.finditer(r'^## (.+)$', text, re.M))
    records = []
    used = collections.Counter()
    for i, match in enumerate(headings):
        heading = match[1]
        anchor = slug(heading)
        count = used[anchor]
        used[anchor] += 1
        if count:
            anchor += f'-{count}'
        if re.match(r'Contents|Evidence|Source|Reference|Inspection|Attribution', heading):
            continue
        body = operational(text[match.end():headings[i+1].start() if i+1 < len(headings) else len(text)])
        if not body.strip():
            continue
        records.append(dict(id=f'{path.stem}:{anchor}', kind=kind, title=heading, path=f'{relative}#{anchor}', body=body))
    return records


def guides():
    return [r for p in sorted((ROOT/'references').glob('*.md'))
            if p.stem not in RESEARCH | {'compositions'}
            for r in section_records(p, 'guides')]


def load(kind):
    if kind == 'patterns':
        return patterns()
    if kind == 'guides':
        return guides()
    if kind == 'compositions':
        return section_records(ROOT/'references/compositions.md', kind)
    if kind == 'build':
        return patterns() + guides() + load('compositions')
    if kind == 'sources':
        return [json.loads(line) for line in (ROOT/'references/source-catalog.jsonl').read_text().splitlines()]
    filename = {'resources': 'resources.json', 'visuals': 'visual-comparisons.json'}[kind]
    return json.loads((ROOT/'references'/filename).read_text())


def searchable(record, kind):
    if kind in {'build', 'patterns', 'guides', 'compositions'}:
        fields = [record.get(k, '') for k in ('mechanism', 'tune', 'check', 'body')]
        return plain(' '.join(fields + record.get('build', []) + record.get('terms', [])))
    keys = {'sources': ('title', 'terms', 'note', 'category'),
            'resources': ('title', 'note', 'topics', 'kind'),
            'visuals': ('title', 'terms', 'prompt_evidence')}[kind]
    return plain(' '.join(' '.join(record.get(k, [])) if isinstance(record.get(k), list) else str(record.get(k, '')) for k in keys))


def related_paths(record):
    """Expose the recipe's existing relationships, not invented compatibility scores."""
    origin = (ROOT/record['path'].split('#')[0]).parent
    seen = set()
    result = []
    for label, dest in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', record.get('body', '')):
        if '://' in dest or dest.startswith('#'):
            continue
        filename, _, anchor = dest.partition('#')
        path = (origin/filename).resolve()
        if not path.is_relative_to(ROOT.resolve()) or not path.exists():
            continue
        local = path.relative_to(ROOT.resolve()).as_posix() + (f'#{anchor}' if anchor else '')
        if local not in seen:
            seen.add(local)
            result.append(dict(title=label, path=local))
    return result


def search(query, kind='build', family=None, limit=6, prompt_only=False, prompt_leads=False):
    records = load(kind)
    if family:
        records = [r for r in records if r.get('family') == family]
    if prompt_only:
        # Adapted prompts on patterns are original examples; this filter concerns retrieved sources.
        records = [r for r in records if r.get('prompt_availability') == 'content-inspected']
    elif prompt_leads:
        records = [r for r in records if r.get('prompt_availability') in {'content-inspected', 'lead-only'}]
    if not records:
        return []
    original = words(query)
    expanded = list(dict.fromkeys(original + [a for t in original for a in EXPANSIONS.get(t, [])]))
    docs = [collections.Counter(words(searchable(r, kind) + ' ' + r['title'] + ' ' + r.get('id', ''))) for r in records]
    df = collections.Counter(t for d in docs for t in d)
    avg = sum(sum(d.values()) for d in docs)/len(docs)
    ranked = []
    for r, d in zip(records, docs):
        n = sum(d.values())
        title = set(words(r['title'] + ' ' + r.get('id', '')))
        score = 20 if query.strip().lower() == r.get('id', '').lower() else 0
        for term in expanded:
            tf = d[term]
            if not tf:
                continue
            idf = math.log(1+(len(docs)-df[term]+.5)/(df[term]+.5))
            score += (1 if term in original else .45)*idf*(tf*2.2/(tf+1.2*(.25+.75*n/max(avg, 1))))
            if term in title:
                score += 1.5 if term in original else .4
        if score:
            ranked.append((score, r))
    ranked.sort(key=lambda pair: (-pair[0], pair[1].get('id', pair[1].get('url', ''))))
    results = []
    for score, record in ranked[:limit]:
        result = dict(record, search_score=round(score, 3))
        body = result.pop('body', None)
        if body is not None:
            lines = [plain(line) for line in body.splitlines() if plain(line) and not line.startswith(('**Combine:', '#'))]
            result['summary'] = lines[0][:500] if lines else ''
            result['related'] = related_paths(record)
        results.append(result)
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query')
    ap.add_argument('--kind', choices=['build', 'patterns', 'guides', 'compositions', 'sources', 'resources', 'visuals'], default='build')
    ap.add_argument('--family')
    ap.add_argument('--limit', type=int, default=6)
    prompt = ap.add_mutually_exclusive_group()
    prompt.add_argument('--prompt-only', action='store_true', help='Sources whose prompt content was inspected; not a completeness claim')
    prompt.add_argument('--prompt-leads', action='store_true', help='Also include marker-only prompt leads')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    if args.limit < 1 or args.limit > 100:
        ap.error('--limit must be between 1 and 100')
    if (args.prompt_only or args.prompt_leads) and args.kind != 'sources':
        ap.error('Prompt filters require --kind sources; pattern prompts are original adaptations')
    found = search(args.query, args.kind, args.family, args.limit, args.prompt_only, args.prompt_leads)
    if args.json:
        print(json.dumps(found, ensure_ascii=False, indent=2))
        return
    if not found:
        print('No matching records. Try a mechanism or browse references/atlas.md; proceed from the brief if no reference helps.')
        return
    for r in found:
        print('\n'+r['title'])
        if r.get('path'):
            print(f"  Read ({r['kind']}): {r['path']}")
            if r['kind'] == 'patterns':
                print('  Mechanism: '+r['mechanism'])
                print('  Check: '+r['check'])
                print('  Sources: '+' '.join(r['source_urls']))
            else:
                print('  Use: '+r['summary'])
                for related in r.get('related', [])[:5]:
                    print(f"  Related: {related['title']} → {related['path']}")
        elif args.kind == 'sources':
            print('  '+r['url'])
            print('  Evidence: '+r['retrieval']+'; '+r['visual_review'])
            print('  Prompt: '+r['prompt_availability']+'; completeness: '+r['prompt_completeness'])
            print('  Inspection note: '+r['prompt_signal'])
            if r.get('visual_reference_url'):
                print('  Compare videos: '+r['visual_reference_url'])
            if r['pattern_ids']:
                print('  Patterns: '+', '.join(r['pattern_ids']))
            if r['note']:
                print('  Note: '+r['note'])
            if r['links']:
                print('  Linked resources: '+' '.join(r['links']))
            if r['related_creator_posts']:
                print('  Selected creator follow-ups: '+' '.join(r['related_creator_posts'][:6]))
        elif args.kind == 'visuals':
            print('  Compare: '+r['detail_url'])
            print('  Original: '+r['url'])
            print('  Prompt: '+r['prompt_evidence'])
            print('  Visual: '+r['visual_review'])
            print('  Model: '+r['model_evidence'])
        else:
            print('  '+r['url'])
            print('  Evidence: '+r['inspection'])
            if r.get('note'):
                print('  '+r['note'])


if __name__ == '__main__':
    main()
