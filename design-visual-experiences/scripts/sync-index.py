#!/usr/bin/env python3
"""Regenerate compatibility summaries and current counts from canonical local files."""
import argparse
import collections
import json
import sys
sys.dont_write_bytecode = True
from search import ROOT, CORE_FIELDS, load


def outputs():
    path = ROOT/'references/patterns.json'
    registry = json.loads(path.read_text())
    current = {r['id']: r for r in load('patterns')}
    for record in registry:
        card = current[record['id']]
        for key in ['title', *CORE_FIELDS.values()]:
            record[key] = card[key]
    coverage_path = ROOT/'references/coverage.json'
    coverage = json.loads(coverage_path.read_text())
    sources, resources, visuals = load('sources'), load('resources'), load('visuals')
    coverage.update(catalog_records=len(sources), pattern_count=len(registry),
                    pattern_families=len({r['family'] for r in registry}),
                    pattern_source_posts=len({s for r in registry for s in r['sources']}),
                    resource_count=len(resources), visual_comparison_count=len(visuals),
                    visual_comparison_catalog_matches=sum(r['in_source_catalog'] for r in visuals),
                    visual_comparison_partial_prompt_labels=sum(r['prompt_partial'] is True for r in visuals),
                    guide_search_sections=len(load('guides')), composition_search_sections=len(load('compositions')),
                    prompt_availability_counts=dict(sorted(collections.Counter(r['prompt_availability'] for r in sources).items())))
    return {path: registry, coverage_path: coverage}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true', help='Fail on drift without writing')
    args = ap.parse_args()
    stale = []
    for path, value in outputs().items():
        if json.loads(path.read_text()) != value:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    if args.check and stale:
        raise SystemExit('Stale generated summaries: '+', '.join(stale)+'; run scripts/sync-index.py')
    print('PASS: canonical summaries and counts match' if args.check else 'Updated: '+(', '.join(stale) or 'already current'))


if __name__ == '__main__':
    main()
