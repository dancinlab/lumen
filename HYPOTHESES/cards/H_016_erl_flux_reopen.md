---
id: H_016
slug: erl-flux-reopen
title: ERL reopens the flux floor — energy recovery lifts the thermal-limited rep-rate by 1/(1-η) with no thermodynamic cap; ERL+FEL reaches ~167 W (200 W) compact, but ERL alone (2 W) does not — flux is a product engineering wall, not a 2nd-law ceiling
domain: light-source
status: supported
exploration_method: abstraction-lane verdict 'flux is REOPENABLE' first probe (0-D power balance)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
from_metalaw: M4 flux-face · escape ERL
---

# H_016 — ERL reopens the flux floor

> **Campaign-decisive verification.** The abstraction lane (`state/euv-meta-laws.md`, flux-ceiling
> section) concluded the flux face is REOPENABLE (no brightness/Liouville floor for a coherent
> source) and named ERL the highest-leverage escape with this 0-D power-balance as the first probe.
> This card runs it.

## Hypothesis

Average in-band power = Q·f·N_ib·E_γ. ERL (energy-recovery linac) decelerates the spent beam, so
only the un-recovered fraction (1−η) deposits heat → f-ceiling = heat_budget/(E_bunch·(1−η)),
which **diverges as η→1** (no thermodynamic floor). At η=0.9 the rep-rate ceiling rises ≥10×;
combined with FEL-class pulse energy (N_ib gain, H_A2) it reaches the ~167 W HVM floor in a compact
footprint. But ERL alone (spontaneous pulse) falls short → flux is a *product* wall (need f AND
N_ib), an engineering/economic constraint, not a 2nd-law ceiling.

## Variables (pre-registered)

- heat budget 10 kW · E_bunch 0.10 J (1 GeV × 100 pC) · HVM floor 167 W · spont pulse 1 µJ ·
  FEL pulse 100 µJ · η = 0 / 0.90 / 0.95 / 0.999.

## Run Protocol

- harness: `tool/lumen_optics.erl_rep_rate_ceiling`, `average_power`.
- run: `state/h016_erl_flux_reopen_2026_06_25/run_h016.py` · `python3 .../run_h016.py` · `.../result.json`.

## Falsifiers (pre-registered)

- **F-ERL-1 LIFT**: ERL@η=0.9 rep-rate lift < 10× → recovery doesn't reopen f.
- **F-ERL-2 REACH**: ERL+FEL < 167 W → flux floor not reachable compact (would re-establish a wall).
- **F-ERL-3 NECESSARY**: ERL alone ≥ 167 W → flux not a product wall (over-claim; ERL must be insufficient alone).
- **F-ERL-4 MONOTONE**: higher η doesn't raise the ceiling → model bug.
- **F-ERL-5 NO-CEILING**: ceiling stops rising as η→1 → a thermodynamic floor exists (would flip the verdict).

## Honest Limits

- **L1 (0-D power balance)**: ignores BBU/HOM instability, cavity HOM heating, halo losses — the
  real ERL engineering walls. η≥0.9 is an *achieved* ERL regime but not at this charge/energy/EUV combo.
- **L2 (needs FEL too)**: reaching 167 W needs FEL-class N_ib (H_A2), itself beam-quality-fragile
  (H_009/H_013) — H_016 shows ERL is necessary, not sufficient.
- **L3 (reopenable ≠ proven compact)**: confirms no thermodynamic floor; the surviving question is
  *engineering/economic* — can a coherent/ERL source deliver 167 W in a non-stadium volume at
  affordable wall-plug. That is the campaign's mutated terminal question.
- **L4 (representative numbers)**: heat budget, bunch energy, pulse energies are order figures; the
  *structure* (1/(1−η) lift, product wall, no floor) is robust.

## Cross-Links

- from: `state/euv-meta-laws.md` flux-ceiling verdict. attacks: M4 flux-face (rep-rate). needs: H_A2 (FEL N_ib), H_013 (cooling for FEL gain).
- complements: H_B4 (recombination laser — the other source-side escape).

## Verdict

```
verdict_class: SUPPORTED
evidence_summary: 0-D power balance with ERL recovery, 5/5 falsifiers PASS.
  rep-rate ceiling: no-ERL 1e5 Hz -> ERL0.90 1e6 Hz (10x) -> ERL0.95 2e6 Hz
  in-band @ERL0.95: spontaneous 2.0 W vs +FEL 200.0 W (floor 167)
key_finding: ERL lifts the thermal-limited rep-rate by 1/(1-η) with NO thermodynamic
             cap (η->1 diverges), and ERL+FEL reaches 200 W (>167 floor) compact — so
             the flux face is an engineering-reopenable product wall, not a 2nd-law
             ceiling. ERL alone (2 W) is necessary, not sufficient: flux needs f AND N_ib.
honest_note: 0-D balance ignores BBU/HOM/halo walls (L1); needs FEL N_ib too (L2);
             reopenable != proven-compact, terminal question is now engineering/economic (L3);
             representative numbers, robust structure (L4).
```

### Run verdict (VERBATIM — 2026-06-25)

```
H_016 ERL reopens the flux floor (abstraction-lane first probe)
  rep-rate ceiling: no-ERL 1e+05 Hz -> ERL0.90 1e+06 Hz (10x) -> ERL0.95 2e+06 Hz
  in-band power @ERL0.95: spontaneous 2.0 W  vs  +FEL 200.0 W  (floor 167)
  F-ERL-1 LIFT       PASS
  F-ERL-2 REACH      PASS
  F-ERL-3 NECESSARY  PASS
  F-ERL-4 MONOTONE   PASS
  F-ERL-5 NO-CEILING PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h016_erl_flux_reopen_2026_06_25/result.json`
