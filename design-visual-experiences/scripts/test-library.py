#!/usr/bin/env python3
"""Check practical retrieval and evidence/link integrity; no network required."""
import json, re, sys
from collections import Counter
from pathlib import Path
sys.dont_write_bytecode = True
from search import ROOT, search, load, words, EXPANSIONS

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
    found = [x['id'] for x in search(query, kind='patterns', limit=3)]
    assert expected in found, (query, expected, found)
assert search('ink', family='materials')
assert all(p['family']=='materials' for p in search('ink',family='materials'))
assert search('qzxvunknownterm') == []
assert any('moyun' in r['url'].lower() for r in search('ink brush',kind='resources',limit=10))
assert all(r['prompt_availability'] == 'content-inspected' for r in search('motion',kind='sources',prompt_only=True))

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
print(f'PASS: {len(CASES)} pattern brief retrievals, catalog/evidence invariants, resource search, and {link_count} local links')

# Task-language queries must reach actual local implementation destinations.
BUILD_CASES = [
 ('introduce components construct assembly tour separated parts restore exact rest pose', 'references/patterns/interaction.md#exploded-assembly'),
 ('room tour camera bookmarks manual walk cutaway return without clipping', 'references/patterns/camera.md#guided-free-exploration'),
 ('classroom lesson advances only after rubbing a match even if the video ends', 'references/action-gated-lessons.md'),
 ('globe stops at an eclipse and resumes without skipping next event', 'references/simulation-event-stops.md'),
 ('puppy accepts a stroke while chasing a toy but sitting and walking cannot run together', 'references/interactive-3d.md#preserve-compatible-actions-inside-a-spatial-scene'),
 ('editable handoff from browser animation to an editor', 'references/editable-motion-handoff.md'),
 ('ink brush dries and makes sound', 'references/compositions.md#an-ink-instrument'),
 ('Generate a reproducible music responsive sculpture from a visitor name', 'references/compositions.md#a-music-responsive-sculpture'),
]
for query, expected in BUILD_CASES:
    found = search(query, limit=5)
    assert expected in [r['path'] for r in found], (query, expected, [r['path'] for r in found])
    assert all((ROOT/r['path'].split('#')[0]).is_file() for r in found)
recipe = search('ink brush dries and makes sound', kind='compositions', limit=1)[0]
assert {'references/patterns/materials.md#distance-spaced-brush',
        'references/patterns/materials.md#wet-dry-ink',
        'references/patterns/sound.md#gesture-instrument'} <= {r['path'] for r in recipe['related']}

# Exact stable IDs and resource topic tags remain valid lookup inputs.
for pattern_id in ['seeded-universe', 'blueprint-rationale']:
    assert search(pattern_id, kind='patterns', limit=1)[0]['id'] == pattern_id
assert search('onboarding', kind='resources')
assert search('receiver map', kind='resources')

# Content inspected, marker only, and code inspected are different evidence states.
for query, expected in [
 ('Small SFX palette matched audition variations', '2104257004474671129'),
 ('origami folding crease', '2104752931710902716'),
 ('original coastline workflow', '2104641083733053881'),
]:
    assert expected in [r['id'] for r in search(query,kind='sources',prompt_only=True)]
assert byid['2104752931710902716']['prompt_completeness'] == 'creator-claims-complete'
assert byid['2104118647274787111']['prompt_availability'] == 'not-established'
assert any(r['prompt_availability']=='lead-only' for r in search('motion',kind='sources',prompt_leads=True,limit=100))
assert all(r['prompt_availability'] in {'content-inspected','lead-only','not-established'} for r in sources)
assert all(r['prompt_completeness'] in {'not-certified','creator-claims-complete'} for r in sources)
assert all(r['prompt_format'] in {'unknown','text','image','linked-text'} for r in sources)

# Source-specific observations cannot be attached to unrelated type cards.
# For each dated evidence link, at least one cited source must occur in that record.
for pattern in [r for r in patterns if r['family']=='type']:
    for target in re.findall(r'\]\((\.\./updates/[^)]+)\)', pattern['evidence']):
        evidence = (ROOT/'references/patterns'/target).resolve().read_text()
        source_ids = set(re.findall(r'https://(?:x|twitter)\.com/[^/]+/status/(\d+)', evidence))
        assert source_ids.intersection(pattern['sources']), (pattern['id'],target,source_ids)

# Stored compatibility summaries must match canonical Markdown instructions.
raw_patterns=json.loads((ROOT/'references/patterns.json').read_text())
for record, card in zip(raw_patterns, patterns):
    assert record['id'] == card['id']
    for field in ['title','mechanism','build','tune','check','prompt','evidence']:
        assert record[field] == card[field], (record['id'],field,'run sync-index.py')
print(f'PASS: {len(BUILD_CASES)} build routes, composition relationships, exact IDs, resource topics, prompt states and scoped typography evidence')

assert search('focal plane ring',kind='visuals',limit=1)[0]['id']=='2103044654187081860'
assert 'foot' in EXPANSIONS[words('footsteps')[0]]
assert 'glyph' in EXPANSIONS[words('letters')[0]]
print('PASS: comparison topic tags and normalized aliases')

# Film briefs must discover the directing guidance alongside existing mechanisms.
FILM_CASES = [
 ('audit remake recreation cut delay action phase stale selection label', 'read-motion-at-native-cadence'),
 ('translate campaign copy longer language aspect ratio reflow moving subject occlusion', 'localization-and-format-variants'),
 ('staged cleanup repair demo intermediate hold folder summary counts', 'parallel-action-and-return-of-control'),
 ('closing product name letters from demonstrated artifacts brand callback', 'branding-and-calls-to-action'),
 ('bounded score percentage overshoot color legend decision state', 'composition-and-finishing'),
 ('avoid generating neutral facial expressions through silhouette lighting and camera angle', 'generated-assets-and-controlled-graphics'),
 ('loading ring points to where new object appears while previous edits remain', 'story-and-agency'),
 ('container motion content stability label drift', 'composition-and-finishing'),
 ('connection jobs preview reveals access contexts persistent composer', 'story-and-agency'),
 ('freeze comedy action explain speed show output resume scene clock', 'parallel-action-and-return-of-control'),
 ('launch title moves out of the way to reveal portrait', 'title-to-image-handoff'),
 ('animate six illustrated characters with a cup lift and drumstick toss', 'illustration-assembly-and-character-performance'),
 ('explain cashback with coins refilling a balance', 'offer-mechanics-and-replenishment'),
 ('product demo explore preview takes then promote chosen render fidelity', 'exploration-before-fidelity'),
 ('analyze motion native cadence consecutive frames acceleration easing', 'read-motion-at-native-cadence'),
 ('agent edits while user makes coffee return control', 'parallel-action-and-return-of-control'),
 ('feature launch video hooks proof pacing', 'hooks-and-proof'),
 ('product demo blur reveal readable closing hold', 'pacing-and-readable-hold-time'),
 ('cinematic image becomes a controllable miniature world', 'object-continuity-and-movement'),
 ('generated footage code motion graphics production layers', 'generated-assets-and-controlled-graphics'),
]
for query, anchor in FILM_CASES:
    assert 'references/feature-launch-films.md#'+anchor in [r['path'] for r in search(query,limit=3)], query
assert search('Higgsfield Layers',kind='resources',limit=1)[0]['url']=='https://x.com/higgsfield/status/2087225671714328813'
assert not any('/research/' in r['path'] for r in load('build')), 'Provenance must not compete with build instructions'
print('PASS: 20 film directing routes, curated video reference discovery and research separation')

# Creative production must be discoverable from production problems, not only its title.
for query, expected in [
 ('generated shot world silhouette visible event viewpoint taste', 'references/creative-production.md#direct-a-shot-instead-of-decorating-a-prompt'),
 ('inner edited sequence footage shrinking into UI source PTS playback', 'references/creative-production.md#decide-the-edit-before-generating-its-ingredients'),
 ('scene contract named cue conflicting track ownership', 'references/creative-production.md#scene-contract-and-engine-helpers'),
 ('longer phrase changed media dimensions stale review hashes approval', 'references/creative-production.md#prove-reuse-and-preserve-review-state'),
]:
    found = [r['path'] for r in search(query, limit=5)]
    assert expected in found, (query, expected, found)
print('PASS: creative direction, edited sequences, scene contracts and reuse review retrieval')
