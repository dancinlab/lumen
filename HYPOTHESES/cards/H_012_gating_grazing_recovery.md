---
id: H_012
slug: gating-grazing-recovery
title: Spectral gating + grazing-incidence in-band recovery — converting 4 of 11 surfaces to grazing reflectors and gating out-of-band shots lifts wafer in-band flux ~8× over a normal-incidence ungated baseline at 6.5 nm (promotes abstract H_A4)
domain: optics
status: supported
exploration_method: mixed grazing/normal column throughput × gated in-band fraction
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
promoted_from: H_A4
---

# H_012 — gating + grazing-incidence in-band recovery

> **Promotion of 🜂 H_A4** (brainstorm shortlist) to a verified, runnable hypothesis — the runnable
> subset (throughput × in-band fraction) is now numerically tested. H_A4 stays as the broader
> abstract idea; H_012 is its falsifiable core.

## Hypothesis

A *recovery* lever, not a new source: (1) replace the collection/transport surfaces with
**grazing-incidence** reflectors (R≈0.9 at shallow angle) instead of near-normal multilayers whose
R collapses to ~0.55 at 6.5 nm (H_002); (2) **gate** out-of-band shots so only ≤2%-line pulses
reach the wafer, raising the in-band fraction (H_009). With only 4 of 11 surfaces converted and a
0.8 gating duty, wafer-level in-band flux rises ~8× over a fixed normal-incidence ungated baseline —
past the ≥5× bar H_A4 predicted.

## Why

- Cheapest, least-exotic of the flux-wall breakthroughs (every part exists): attacks the optics
  (H_002) and in-band (H_009) losses without a brighter source.
- Demand/recovery side complement to the supply-side H_008 walls.

## Variables (pre-registered, representative)

- N_total=11 · N_graze=4 · R_graze=0.90 · R_normal=0.55 · in-band ungated 0.70 / gated 0.98 ·
  gating duty 0.80.

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`column_throughput_mixed`, `mirror_chain_throughput`).
- **run script**: `state/h012_gating_grazing_recovery_2026_06_25/run_h012.py`.
- **run cmd**: `python3 state/h012_gating_grazing_recovery_2026_06_25/run_h012.py`
- **artifacts**: `state/h012_gating_grazing_recovery_2026_06_25/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-RC-1 RECOVER**: recovery ratio < 5× → not a meaningful recovery (refutes H_A4 bar).
- **F-RC-2 GRAZING**: R_graze ≤ R_normal → no optics gain.
- **F-RC-3 GATING**: gated in-band ≤ ungated → gating useless.
- **F-RC-4 MONOTONE**: more grazing surfaces don't raise throughput → model bug.
- **F-RC-5 BOUNDS**: any throughput ∉ (0,1] → ledger bug.

## Honest Limits

- **L1 (grazing suits collection, not high-NA imaging)**: only the ~4 collection/transport surfaces
  are realistically convertible; grazing optics struggle with the high-NA projection imaging — that
  is why N_graze=4, not 11. Converting more is physically unjustified here.
- **L2 (in-band fractions representative)**: 0.70/0.98 are stand-ins for the H_009 line overlap; the
  *direction* (gating helps) is robust, the magnitude moves with the real spectrum.
- **L3 (gating duty is a real cost)**: discarding 20% of shots wastes source power — already folded
  into the 0.8 duty; a worse source spectrum lowers duty and the ratio.
- **L4 (recovery, not generation)**: this multiplies *delivered* flux; it does not lift the source's
  average power (H_008) — it makes the scarce watts count, a complement not a substitute.

## Cross-Links

- **promotes**: H_A4 (abstract). **recovers against**: H_002 (optics), H_009 (line).
- **complements**: H_008 (still need source average power). harness: `column_throughput_mixed`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-25.

```
verdict_class: SUPPORTED
evidence_summary: mixed grazing/normal column × gated in-band, 5/5 falsifiers PASS.
  baseline (all-normal R=0.55, ungated) = 0.000975
  enhanced (4 grazing R=0.9 + 7 normal, gated×0.8 duty) = 0.00783
  recovery ratio = 8.03x
key_finding: gating + grazing recovers ~8x more wafer-level in-band flux than a
             normal-incidence ungated column at 6.5 nm (≥5x bar cleared) with only
             4 of 11 surfaces grazing — the cheapest, least-exotic flux-wall lever,
             promoting abstract H_A4 to a verified result.
honest_note: grazing only suits collection not high-NA imaging (L1, why N_graze=4);
             in-band fractions representative (L2); gating duty is a real 20% cost
             (L3); recovery multiplies delivered flux, does not generate it (L4).
```

### Run verdict (VERBATIM — `python3 run_h012.py` stdout 2026-06-25)

```
H_012 spectral gating + grazing-incidence in-band recovery (promotes H_A4)
  baseline (all-normal R=0.55, ungated) = 0.000975186
  enhanced (4 grazing R=0.9 + 7 normal, gated×duty) = 0.00783114
  recovery ratio = 8.03x  (more-grazing -> 0.0209693)
  F-RC-1 RECOVER   PASS
  F-RC-2 GRAZING   PASS
  F-RC-3 GATING    PASS
  F-RC-4 MONOTONE  PASS
  F-RC-5 BOUNDS    PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h012_gating_grazing_recovery_2026_06_25/result.json`
