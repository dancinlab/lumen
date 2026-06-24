---
id: H_021
slug: tabletop-learning-curve
title: The tabletop accelerator wins the CAPEX wall via the M7 learning curve — small, replicable modules ride a Wright's-law curve and cross below LPP tool CAPEX at ~6 units, while a monolithic synchrotron (no replication) stays stuck above
domain: system
status: supported
exploration_method: Wright's-law learning curve on replicable modules
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
from_metalaw: M7 (learning curve) · M9 (amortization)
---

# H_021 — tabletop accelerator wins the CAPEX wall (M7)

> **The affirmative case.** H_020 localized the terminal wall to CAPEX (M7/M9). This card shows the
> compact (tabletop laser-plasma) accelerator is the route that *wins* it — because it is small and
> **replicable**, unlike the synchrotron.

## Hypothesis

The binding economic wall is CAPEX-per-wafer (H_020). A compact-accelerator module starts at a
bespoke unit cost above the LPP tool (~1.5×) but, being small and replicable, mass production rides
a Wright's-law learning curve `C(N) = C1·N^log2(LR)`. At a modest cumulative count (~6 modules, 15%
learning rate) its unit CAPEX crosses below the LPP tool; by ~100 it is ~half. A synchrotron —
monolithic civil works (ring, vault), not module-replicable — cannot ride the curve and stays stuck
at ~4× the EUV tool. So the **tabletop accelerator is the only route that wins the CAPEX terminal wall.**

## Variables (pre-registered, normalized)
- LPP tool = 1.0 · compact first-unit C1 = 1.5 · learning rate 0.85 · synchrotron = 4.0 (no replication).

## Run Protocol
- harness: `tool/lumen_optics.wright_unit_cost` · run: `state/h021_tabletop_learning_curve_2026_06_25/run_h021.py`
- `python3 .../run_h021.py` · artifacts `.../result.json`.

## Falsifiers
- **F-LC-1 CROSSOVER**: no finite N < 100 where compact < LPP → no learning-curve win.
- **F-LC-2 DESCENT**: cost not strictly falling with N → learning curve broken.
- **F-LC-3 BEATS-LPP**: compact at ~10 modules ≥ LPP → win too slow.
- **F-LC-4 SYNCH-STUCK**: synchrotron ≤ LPP or ≤ compact → monolith rides the curve (it can't).
- **F-LC-5 BOUNDS**: any non-positive → ledger bug.

## Honest Limits
- **L1 (learning rate representative)**: 0.85 (15%/doubling) is a typical hardware Wright slope, not
  measured for accelerator modules; a slower rate pushes the crossover N out but does not remove it.
- **L2 (first-unit cost assumed)**: 1.5× LPP is a representative bespoke estimate; the *structure*
  (replicable beats monolithic) is robust, the crossover N moves with C1.
- **L3 (CAPEX only)**: this is the CAPEX axis; OPEX/η (M6) and amortization-across-scanners (M9) are
  separate levers (H_019) — the full win is the conjunction, this card isolates the M7 piece.
- **L4 (replicability assumed)**: assumes the compact module truly mass-produces; bespoke
  laser/plasma engineering could resist standardization (the real risk to the M7 thesis).

## Cross-Links
- from: H_020 (CAPEX is the wall) · meta-law M7/M9. revives: the compact-accelerator route (H_004/H_016).
- vs: synchrotron (H_010, monolithic). harness: `wright_unit_cost`.

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: Wright's-law learning curve, 5/5 falsifiers PASS.
  compact CAPEX (LPP=1.0): N=1 1.50 · N=10 0.87 · N=100 0.51 · crossover ~5.6 modules
  synchrotron 4.0 (monolithic) — never rides the curve
key_finding: the small, replicable tabletop accelerator crosses below LPP tool CAPEX at ~6
             mass-produced modules via the M7 learning curve, while a monolithic synchrotron
             stays stuck at ~4x — so the compact accelerator is the route that WINS the CAPEX
             terminal wall (H_020). The affirmative case that revives the tabletop accelerator.
honest_note: learning rate representative (L1); first-unit cost assumed (L2); CAPEX-only, full win
             is the H_019 conjunction (L3); assumes the module truly mass-produces (L4, the real risk).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_021 tabletop accelerator wins the CAPEX wall via the M7 learning curve
  compact module CAPEX (LPP tool = 1.0): N=1 1.50 · N=10 0.87 · N=100 0.51
  crosses below LPP at ~5.6 modules  (learning rate 0.85)
  synchrotron (monolithic, no replication) = 4.0 — stuck above, never rides the curve
  -> the small, REPLICABLE tabletop accelerator is the route that wins the CAPEX terminal wall
  F-LC-1 CROSSOVER PASS
  F-LC-2 DESCENT   PASS
  F-LC-3 BEATS-LPP PASS
  F-LC-4 SYNCH-STUCK PASS
  F-LC-5 BOUNDS    PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```
**State output**: `state/h021_tabletop_learning_curve_2026_06_25/result.json`
