---
id: H_022
slug: combination-breakthrough
title: Combination breakthrough — tabletop accelerator + ERL + FEL + cooling + module-array clears the flux floor (200 W), the CAPEX wall (0.87 < LPP), and wavelength tunability ALL at once; each lever is necessary (drop one, a wall reappears)
domain: system
status: supported
exploration_method: stack the verified levers (H_004 x H_016 x H_A2 x H_013 x H_021)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
goal: tabletop accelerator + @ combination wall-breakthrough
---

# H_022 — combination breakthrough (the goal realized)

> **Goal: "tabletop accelerator + @ combination wall-breakthrough."** This capstone stacks the
> verified levers into one compact-EUV-source system and shows it breaks every wall the campaign
> found — simultaneously — and that each lever is load-bearing.

## Hypothesis

No single lever wins; the *combination* does. Stack: a tabletop laser-plasma accelerator (H_004,
compact GV/m gradient) + **ERL** (H_016, rep-rate ceiling ÷(1−η)) + **FEL** (H_A2, ~100× photons/
bunch) + **cooling** (H_013, energy spread for FEL gain) + **module array** (H_021, M7 learning
curve). The claim: this stack clears the **flux floor** (~200 W ≥ 167), the **CAPEX wall** (~0.87 <
LPP at 10 modules), and keeps **wavelength tunability** (H_007, 13.5→3 nm) — all at once. And each
lever is **necessary**: drop FEL → 2 W (flux wall); drop the array → 1.5× (CAPEX wall).

## Variables (pre-registered)
- flux: heat 10 kW · E_bunch 0.10 J · η_rec 0.95 · FEL pulse 100 µJ vs spontaneous 1 µJ.
- capex: compact C1 1.5 · learning rate 0.85 · N=10 modules vs N=1.
- wavelength: tunable (H_007 capability).

## Run Protocol
- harness: `tool/lumen_optics.py` (`erl_rep_rate_ceiling`, `average_power`, `wright_unit_cost`).
- run: `state/h022_combination_breakthrough_2026_06_25/run_h022.py` · `python3 .../run_h022.py` · `.../result.json`.

## Falsifiers
- **F-CMB-1 FLUX**: stack < 167 W → flux wall not cleared.
- **F-CMB-2 CAPEX**: stack CAPEX ≥ LPP → CAPEX wall not cleared.
- **F-CMB-3 FEL-NECESSARY**: dropping FEL still ≥ 167 W → FEL not load-bearing.
- **F-CMB-4 ARRAY-NECESSARY**: single module < LPP → array not load-bearing.
- **F-CMB-5 ALL-WALLS**: not all of {flux, capex, wavelength} clear together → no combination breakthrough.
- **F-CMB-6 BOUNDS**: any non-positive → ledger bug.

## Honest Limits
- **L1 (system integration on paper, not built)**: this multiplies *separately verified, representative*
  relations; co-integrating ERL + FEL + cooling + array on one machine has cross-couplings (e.g. FEL
  needs the cooled low-spread beam H_013; ERL recirculation must preserve FEL beam quality) not modeled
  as joint constraints here — the real engineering risk.
- **L2 (inherits each lever's limits)**: carries H_016 L1 (BBU/HOM, addressed by H_018), H_A2 (LPA-FEL
  fragility), H_013 L1 (cooling stage undesigned), H_021 L4 (module replicability) — the weakest link governs.
- **L3 (representative numbers)**: the stack uses the same order figures as its source cards; the
  *structure* (combination clears all, each necessary) is the finding, not the exact 200 W / 0.87.
- **L4 (economics is the conjunction)**: CAPEX-clear here is the M7 piece; full economic win also needs
  M6 efficiency + M9 amortization (H_019) — this card asserts the physical+CAPEX walls, not the full $/wafer.

## Cross-Links
- realizes goal: tabletop accelerator + @ combination. stacks: H_004 · H_016 · H_A2 · H_013 · H_021 · H_007.
- the affirmative synthesis of the whole campaign (H_001–H_021).

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: stacked verified levers, 6/6 falsifiers PASS.
  FLUX  200 W >= 167 (cleared) · CAPEX 0.87 < 1.0 (cleared) · WAVELENGTH tunable (cleared)
  necessity: drop FEL -> 2 W (wall) · drop array -> 1.50 (wall)
key_finding: the compact-accelerator COMBINATION (LPA + ERL + FEL + cooling + module array) breaks
             every campaign wall at once — flux, CAPEX, and wavelength — and each lever is necessary.
             The tabletop accelerator, revived, is the route that clears all walls in combination;
             no single lever does. The affirmative synthesis of the campaign.
honest_note: paper-level system integration, cross-couplings unmodeled (L1, the real risk); inherits
             each lever's limits, weakest link governs (L2); representative numbers, structure is the
             finding (L3); CAPEX-clear is the M7 piece, full $/wafer needs M6+M9 too (L4).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_022 combination breakthrough — tabletop accelerator + ERL + FEL + cooling + array
  FLUX : full stack 200 W >= 167 floor  (CLEARED)
  CAPEX: full stack 0.87 < 1.0 LPP     (CLEARED)
  WAVELENGTH: 13.5/6.5/5/3 nm tunable (H_007)               (CLEARED)
  necessity: drop FEL -> 2 W (wall) · drop array -> 1.50 (wall)
  -> ALL WALLS CLEARED simultaneously: True  (each lever necessary)
  F-CMB-1 FLUX       PASS
  F-CMB-2 CAPEX      PASS
  F-CMB-3 FEL-NECESSARY PASS
  F-CMB-4 ARRAY-NECESSARY PASS
  F-CMB-5 ALL-WALLS  PASS
  F-CMB-6 BOUNDS     PASS
VERDICT: SUPPORTED  (6/6 falsifiers PASS)
```
**State output**: `state/h022_combination_breakthrough_2026_06_25/result.json`
