#!/usr/bin/env python3
"""Check practical retrieval and evidence/link integrity; no network required."""
import json, re, sys
from collections import Counter
from pathlib import Path
sys.dont_write_bytecode = True
from search import ROOT, search, load

CASES = [
 ('ferrofluid glossy spikes reach toward moving attractor', 'attractor-spike-field'),
 ('remaining distance easing same speed 120 hz refresh rate', 'time-based-follow'),
 ('elastic card keeps its momentum when released', 'release-momentum'),
 ('ink dries and re wets on paper', 'wet-dry-ink'),
 ('walking character feet slide on ground', 'planted-foot-ik'),
 ('camera zoom through tiny nested worlds', 'portal-zoom'),
 ('music reactive sculpture with bass and treble', 'band-to-part'),
 ('a field of grass responding to one wind', 'shared-wind'),
 ('kinetic typography from individual letters', 'glyph-choreography'),
 ('interactive telescope image follows optical settings', 'computed-optical-image'),
 ('objects assemble into a product exploded view', 'exploded-assembly'),
 ('seamless loop position and velocity', 'loop-position-velocity'),
 ('a film from messy chaos into organized system', 'chaos-to-organization'),
 ('GPU physics thousands of falling blocks', 'gpu-resident-motion'),
 ('gears keep ticking during exploded inspection', 'phase-coherent-explode'),
 ('particle ring contracts bursts and returns', 'contract-burst-return'),
 ('marbles flip gates to compute a result', 'contact-driven-computation'),
 ('measure joint angles from reference footage', 'measured-joint-motion'),
 ('recognizable dance moves follow musical phase', 'beat-locked-move-library'),
 ('scrubbing stale frames slow decode reversals', 'latest-frame-presentation'),
]
for query, expected in CASES:
    found = [x['id'] for x in search(query, limit=3)]
    assert expected in found, (query, expected, found)
assert search('ink', family='materials')
assert all(p['family']=='materials' for p in search('ink',family='materials'))
assert search('qzxvunknownterm') == []
assert any('moyun' in r['url'].lower() for r in search('ink brush',kind='resources',limit=10))
assert all(r['prompt_signal'] in {'marker-in-retrieved-text','creator-prompt-retrieved'} for r in search('motion',kind='sources',prompt_only=True))

patterns, sources, resources = load('patterns'), load('sources'), load('resources')
coverage = json.loads((ROOT/'references/coverage.json').read_text())
byid={s['id']:s for s in sources}
assert len(byid)==len(sources)==coverage['catalog_records']
assert len({p['id'] for p in patterns})==len(patterns)==coverage['pattern_count']
assert len({p['family'] for p in patterns})==coverage['pattern_families']
assert len(set(s for p in patterns for s in p['sources']))==coverage['pattern_source_posts']
for p in patterns:
    assert all(s in byid for s in p['sources']), p['id']
    assert all(byid[s]['retrieval']=='text-retrieved' for s in p['sources']), p['id']
    text=(ROOT/f"references/patterns/{p['family']}.md").read_text()
    assert f'id="{p["id"]}"' in text, p['id']
    assert len(p['build']) >= 3 and p['check'] and p['prompt']
assert len(resources)==len({r['url'] for r in resources})==coverage['resource_count']
correction=byid['2102796895982878850']
assert 'handmade' in correction['note'].lower(), correction

assert any(r['id']=='2105009470292013286' for r in search('mechanical watch',kind='sources',prompt_only=True))

# Watchable references must resolve existing sources without upgrading unseen media.
visuals=load('visuals')
assert len(visuals)==len({r['id'] for r in visuals})==coverage['visual_comparison_count']
assert sum(r['in_source_catalog'] for r in visuals)==coverage['visual_comparison_catalog_matches']
assert all(r['id'] in byid for r in visuals if r['in_source_catalog'])
assert search('optical camera focus',kind='visuals',limit=1)[0]['id']=='2103044654187081860'
assert sum(r['prompt_partial'] is True for r in visuals)==coverage['visual_comparison_partial_prompt_labels']
assert next(r for r in visuals if r['slug']=='codrops-340299')['model_evidence'].startswith('Attribution caution:')
assert all('prompt' not in r for r in visuals), 'Do not bundle third-party full prompts'

# Validate bundled relative links and explicit atlas anchors. No claims about remote link health.
link_count=0
for file in ROOT.rglob('*.md'):
    for dest in re.findall(r'\]\(([^)]+)\)',file.read_text()):
        if '://' in dest or dest.startswith(('mailto:','#')): continue
        path,_,anchor=dest.partition('#')
        target=(file.parent/path).resolve()
        assert target.is_relative_to(ROOT.resolve()), (file,dest)
        assert target.exists(), (file,dest)
        if anchor and '/patterns/' in str(target):
            assert f'id="{anchor}"' in target.read_text(), (file,dest)
        link_count+=1
print(f'PASS: {len(CASES)} brief retrievals, catalog/evidence invariants, resource search, and {link_count} local links')
