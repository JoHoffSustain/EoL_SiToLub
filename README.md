# SiToLub Fate Explorer

Interactive Sankey diagram of the use-phase and end-of-life logic of the SiToLub life cycle model.
It shows how 1 kg of lubricant put on the market splits between use losses, formal and informal
collection, and end-of-life treatment routes, depending on application, lubricant class and formulation.

**Live page:** [(https://johoffsustain.github.io/EoL_SiToLub/](https://johoffsustain.github.io/EoL_SiToLub/))

## Model logic

1. **Use losses** per application (Zimmermann et al., 2025; UBA Texte 39/2025).
2. **Fate of losses** by lubricant class (combustion / emission):
   ALL 95/5 · PLL 75/25 · TLL 0/100 · FFL 100/0 (SiToLub assumptions; classes from EU Ecolabel and ATIEL & UEIL, 2025).
3. **Remaining lubricant**: fixed formal collection rate of 82.5 %; informal share split 50/50
   into uncontrolled combustion and emission (no-bias assumption; Pinheiro et al., 2021).
4. **Formal treatment routes**: GEIR EU average (Stahl & Merz, 2020):
   re-refining 60.9 %, fuel conversion 24.0 %, power plant 7.0 %, cement 3.8 %, other use 4.3 %.
5. **Formulation thresholds**:
   - Cl > 499 ppm, F > 499 ppm, Si > 4.99 wt %, biodegradable mass > 3 wt % or glycol > 1 wt %
     → no re-refining; other routes scaled to 100 %.
   - F > 499 ppm or Cl > 1990 ppm → 100 % hazardous waste incineration.

## Files

- `index.html` – the complete app (HTML, CSS and JavaScript in one file, no build step).
- `.nojekyll` – tells GitHub Pages to serve the files as they are.

## Run locally

Open `index.html` in a browser. No server or install needed.

## Acknowledgement

Developed in the SiToLub project, co-funded by the European Union under Grant Agreement No. 101138807.
Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the
European Union or the Health and Digital Executive Agency (HaDEA). Neither the European Union nor the
granting authority can be held responsible for them.
