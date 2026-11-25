"""List every parametrised exchange and global parameter in the SiToLub openLCA JSON-LD zip.

Usage:  python scripts/list_formulas.py openlca/SiToLub_parametrised_processes.zip > docs/openlca-formulas.md
"""
import json, re, sys, zipfile
from collections import defaultdict

zf = zipfile.ZipFile(sys.argv[1])
names = zf.namelist()
load = lambda n: json.loads(zf.read(n))

print("# openLCA parameters and formulas\n")
print("Generated from `openlca/SiToLub_parametrised_processes.zip` by `scripts/list_formulas.py`.\n")
print("`amt` stands for the original ecoinvent 3.12 cut-off amount of the exchange.\n")
print("## Global parameters\n\n| Parameter | Default | Formula |\n|---|---|---|")
for n in sorted(x for x in names if x.startswith("parameters/") and x.endswith(".json")):
    p = load(n)
    print(f"| `{p['name']}` | {p.get('value', '')} | {('`' + p['formula'] + '`') if p.get('formula') else ''} |")

groups = defaultdict(set)
for n in sorted(x for x in names if x.startswith("processes/") and x.endswith(".json")):
    p = load(n)
    proc = p["name"].replace(" | SiToLub parametrised", "")
    loc = (p.get("location") or {}).get("name", "")
    for e in p.get("exchanges", []):
        f = e.get("amountFormula")
        if not f:
            continue
        pattern = re.sub(r"^[0-9.eE+-]+ \*", "amt *", f)
        groups[(proc, loc)].add(("input" if e.get("isInput") else "output", e["flow"]["name"], pattern))

print(f"\n## Parametrised processes ({len(groups)})\n")
for (proc, loc), rows in sorted(groups.items()):
    print(f"### {proc} ({loc})\n\n| Direction | Flow | Formula |\n|---|---|---|")
    for d, flow, f in sorted(rows):
        print(f"| {d} | {flow} | `{f}` |")
    print()
