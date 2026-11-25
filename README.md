# SiToLub LCA tools

Interactive tools and data behind the life cycle assessment in SiToLub (stability simulation of lubricants, deliverable D5.1, Preliminary LCSA report).

**Live page:** https://johoffsustain.github.io/EoL_SiToLub/

| Tool | Path | What it does |
|---|---|---|
| FU Questionnaire | [`functional-units/questionnaire.html`](functional-units/questionnaire.html) | Leads from scope, application and use pattern to the functional unit, reference flow, openLCA parameters and report text |
| FU Explorer | [`functional-units/explorer.html`](functional-units/explorer.html) | Formulas per lubricant class and scope, applied systems (car, machining, deep drawing), parameter map |
| Full Life Cycle Map | [`functional-units/lifecycle-map.html`](functional-units/lifecycle-map.html) | Use case → module → database flow; exchange threshold for corrosion protection |
| Fate Explorer | [`fate-explorer/`](fate-explorer/) | Use-phase losses and end-of-life routes of 1 kg lubricant (Sankey) |

Every tool is a single HTML file with no build step. Open it in a browser, or serve the repository with GitHub Pages.

## Functional units

### Lubricant classes

The classes are base oils, engine, compressor, turbine, gear (ALL/FFL), hydraulic, machining, process oils, greases and other/protection. The FU per class is in [`data/SiToLub_FU_matrix.xlsx`](data/SiToLub_FU_matrix.xlsx).

### Scopes

**Lubricant focus**

| # | Scope | Reference flow |
|---|---|---|
| 1 | Cradle-to-Gate | `m_lube` (declared unit) |
| 2 | Cradle-to-Gate (performance adjusted) | `m_lube · lifetime_lubricant / lifetime_assessed` |
| 3 | Full Life Cycle / Cradle-to-Grave (excl. performance) | `m_lube · total / interval` (same interval for lubricant and benchmark) |

In scope 2 the lifetime can be given directly, as a % change, or from a wear volume: `lifetime_assessed = lifetime_lubricant · wear_volume_lubricant / wear_volume_assessed`.

**Functional focus**

| # | Scope | Reference flow |
|---|---|---|
| 4 | Full Life Cycle (incl. drain intervals, energy consumption, material substitution) | Sum of the modules below |
| 5 | Applied Systems | Parametrised ecoinvent processes (car, metal working) |

### Scope 4 modules

| Module | Formula | Used when the use pattern is |
|---|---|---|
| Lubricant | `m_lube · total / interval`; greases `m_lube + m_relubrication · total / interval` | all |
| Energy | `energy_spec · total + (P_loss − P_loss_benchmark) · hours / eta_conv` (×3.6 for fuel in MJ) | changed, FFL, relubricated |
| Wear | `wear_rate · total` | changed, FFL, relubricated |
| Corrosion | `if(failure_rate · total ≥ exchange_threshold; m_material_protected; failure_rate · total / 100 · m_material_protected)` | protection |
| Downtime | `pieces = production_rate · operating_hours / (1 + production_rate · downtime_per_stop / cleaning_interval)` | per piece |

The energy carrier is fuel for a km basis and electricity otherwise. For fuel, the tailpipe emissions are left out of scope 4.

LCC is calculated only in scopes 4 and 5. It uses `price_lubricant`, `price_energy`, `price_material_wear`, `price_material_protected`, `value_per_piece` and, for the applied systems, `price_vehicle`, `price_metal`, `price_sheet` and `price_machine`.

[`data/SiToLub_scopes_MWF_example.xlsx`](data/SiToLub_scopes_MWF_example.xlsx) takes one metalworking-fluid additive through all five scopes.

## openLCA (scope 5)

The applied systems use copies of ecoinvent 3.12 cut-off processes (RER and RoW) with parameters on the lubricant, energy and lifetime flows:

- passenger car diesel EURO 3, medium and large, with maintenance and production
- metal working machine (8 variants) and metal working averages
- deep drawing (single stroke, automode), where SiToLub adds the lubricant

All global parameters and formulas are listed in [`docs/openlca-formulas.md`](docs/openlca-formulas.md). Parameter names use underscores, because openLCA reads `-` as minus.

**The JSON-LD package is not in this repository.** It contains ecoinvent data, which the ecoinvent licence does not allow to be redistributed. Keep it locally or share it only with ecoinvent licence holders; `.gitignore` blocks `openlca/*.zip`. To refresh the formula list from your local copy:

```
python scripts/list_formulas.py path/to/SiToLub_parametrised_processes.zip > docs/openlca-formulas.md
```

## End-of-life model (Fate Explorer)

1. **Use losses** per application (Zimmermann et al., 2025; UBA Texte 39/2025).
2. **Fate of losses** by lubricant class (combustion / emission): ALL 95/5 · PLL 75/25 · TLL 0/100 · FFL 100/0 (SiToLub assumptions; classes from EU Ecolabel and ATIEL & UEIL, 2025).
3. **Remaining lubricant**: fixed formal collection rate of 82.5 %. The informal share is split 50/50 into uncontrolled combustion and emission (no-bias assumption; Pinheiro et al., 2021).
4. **Formal treatment routes**: GEIR EU average (Stahl & Merz, 2020): re-refining 60.9 %, fuel conversion 24.0 %, power plant 7.0 %, cement 3.8 %, other use 4.3 %.
5. **Formulation thresholds**:
   - Cl > 499 ppm, F > 499 ppm, Si > 4.99 wt %, biodegradable mass > 3 wt % or glycol > 1 wt % → no re-refining; the other routes are scaled to 100 %.
   - F > 499 ppm or Cl > 1990 ppm → 100 % hazardous waste incineration.

## Repository layout

```
index.html                  landing page (GitHub Pages root)
fate-explorer/index.html    end-of-life Sankey
functional-units/           FU questionnaire, explorer, life cycle map
data/                       Excel tables
docs/                       openLCA formula list, figures
scripts/list_formulas.py    writes docs/openlca-formulas.md from the JSON-LD zip
.nojekyll                   GitHub Pages serves the files as they are
```

## Acknowledgement

Developed in the SiToLub project, co-funded by the European Union under Grant Agreement No. 101138807. Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the Health and Digital Executive Agency (HaDEA). Neither the European Union nor the granting authority can be held responsible for them.
