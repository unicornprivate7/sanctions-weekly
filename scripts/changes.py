#!/usr/bin/env python3
"""Weekly changes: compares data/<week>.json with the previous weekly snapshot, by country and list.
Writes data/changes/<week>.csv, data/changes/<week>.json and release-notes.md. Counts only, no names."""
import csv, json, os, re, sys

week = sys.argv[1]
weeks = sorted(f[:-5] for f in os.listdir('data') if re.fullmatch(r'\d{4}-\d{2}\.json', f))
cur = json.load(open(f'data/{week}.json'))
older = [w for w in weeks if w < week]
prev_week = older[-1] if older else None
prev = json.load(open(f'data/{prev_week}.json')) if prev_week else {}

def pairs(d):
    out = {}
    for c, lists in (d.get('byCountry') or {}).items():
        for l, n in (lists or {}).items():
            out[(c, l)] = out.get((c, l), 0) + int(n or 0)
    return out

a, b = pairs(cur), pairs(prev)
rows = []
for k in sorted(set(a) | set(b)):
    n, p = a.get(k, 0), b.get(k, 0)
    rows.append({'country': k[0], 'list': k[1], 'thisWeek': n, 'previousWeek': p, 'change': n - p})
rows.sort(key=lambda r: (-abs(r['change']), r['country'], r['list']))
os.makedirs('data/changes', exist_ok=True)
with open(f'data/changes/{week}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['country', 'list', 'thisWeek', 'previousWeek', 'change'])
    w.writeheader(); w.writerows(rows)
tot, ptot = int(cur.get('totalNewEntries') or sum(a.values())), int(prev.get('totalNewEntries') or sum(b.values())) if prev_week else 0
summary = {'week': week, 'previousWeek': prev_week, 'period': cur.get('period'), 'totalNewEntries': tot,
           'previousTotalNewEntries': ptot, 'change': tot - ptot, 'rows': rows,
           'license': 'CC BY 4.0, attribution: Unicorn Intelligence (https://intel.unicornprivate.com)'}
json.dump(summary, open(f'data/changes/{week}.json', 'w'), indent=1)
lines = [f'Weekly changes of new entries on official sanctions lists, ISO week {week}' + (f' compared with {prev_week}.' if prev_week else ' (first snapshot, no previous week).'), '',
         f'- New entries this week: {tot}', f'- Previous week: {ptot}', f'- Change: {tot - ptot:+d}', '']
top = [r for r in rows if r['change']][:10]
if top:
    lines += ['| Country | List | This week | Previous week | Change |', '|---|---|---|---|---|']
    lines += [f"| {r['country']} | {r['list']} | {r['thisWeek']} | {r['previousWeek']} | {r['change']:+d} |" for r in top]
else:
    lines.append('No changes by country and list compared with the previous week.')
lines += ['', 'Counts only, no names. Data: CC BY 4.0, Unicorn Intelligence. Daily view: https://intel.unicornprivate.com/sanctions/today/?src=github']
open('release-notes.md', 'w').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
