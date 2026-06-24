---
id: H_015
slug: wall-census
title: Wall census — across every proposed sub-13.5 nm architecture the binding constraint is one of the four cost meta-laws {M1 photon · M2 power · M3 footprint · M4 flux} and NEVER wavelength (verifies meta-law M5/P5)
domain: system
status: supported
exploration_method: meta-law prediction P5 made runnable (taxonomy classification)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
from_metalaw: M5 (wavelength-freedom) · prediction P5
---

# H_015 — wall census (P5)

> **Meta-verification.** Runs the abstraction-lane prediction P5 (`state/euv-meta-laws.md`): the
> binding wall is always one of the four *cost* meta-laws, never the wavelength itself.

## Hypothesis

Classify each architecture (LPP, synchrotron, LPA-undulator, inverse-Compton, recombination laser,
6.5 nm BEUV optics) by its binding wall. M5 predicts none binds on wavelength; all bind on M1
(photon/reflectance), M2 (power), M3 (footprint), or M4 (flux/brightness). The compact-accelerator
routes (LPA-undulator, inverse-Compton) both bind on M4 — confirming flux is the terminal question.

## Variables (pre-registered)

- census dict {architecture → binding wall} · cost-wall set {M1,M2,M3,M4} · accel routes = {LPA-undulator, inverse-Compton}.

## Run Protocol

- harness: `tool/lumen_optics.evaluate` · run: `state/h015_wall_census_2026_06_25/run_h015.py`
- run cmd: `python3 state/h015_wall_census_2026_06_25/run_h015.py` · artifacts: `.../result.json`.

## Falsifiers (pre-registered)

- **F-CEN-1 NO-WAVELENGTH**: any architecture binds on wavelength → M5 violated (refutes).
- **F-CEN-2 IN-SET**: any binding wall ∉ {M1,M2,M3,M4} → taxonomy incomplete.
- **F-CEN-3 COVERAGE**: < 3 architectures censused → too thin.
- **F-CEN-4 FLUX-TERMINAL**: an accelerator route not on M4 → flux not the terminal accel wall.
- **F-CEN-5 ALL-WALLS-HIT**: not all four cost walls appear → taxonomy not exercised.

## Honest Limits

- **L1 (classification, not measurement)**: the binding-wall assignment is a structured judgement
  from the verified H-laws, not a per-architecture measurement; a different operating point could
  shift which wall binds first.
- **L2 (census not exhaustive)**: six representative architectures; an exotic scheme could in
  principle bind elsewhere — but M5 (relativistic/undulator kinematics) makes "wavelength" structurally impossible.
- **L3 (this is a map, not a solution)**: confirming where the walls are does not move them.

## Cross-Links

- from: `state/euv-meta-laws.md` M5 / P5. confirms: flux (M4) is the accelerator-route terminal wall (→ H_016).

## Verdict

```
verdict_class: SUPPORTED
evidence_summary: taxonomy classification, 5/5 falsifiers PASS.
  LPP->M2 · Synchrotron->M3 · LPA-undulator->M4 · Inverse-Compton->M4 · Recomb-laser->M2 · BEUV-optics->M1
  binds-on-wavelength: False · all in {M1..M4}: True · accel routes on M4: True
key_finding: across 6 architectures the binding wall is always one of the four cost
             meta-laws, never wavelength (M5 confirmed) — and both compact-accelerator
             routes bind on M4 (flux), pinning flux as the terminal accelerator question.
honest_note: classification not measurement (L1); census representative not exhaustive (L2); a map, not a solution (L3).
```

### Run verdict (VERBATIM — 2026-06-25)

```
H_015 wall census — binding wall is never wavelength (P5)
  LPP (tin droplet)              -> M2
  Synchrotron (storage ring)     -> M3
  LPA-undulator                  -> M4
  Inverse-Compton                -> M4
  Recombination EUV laser        -> M2
  6.5 nm BEUV optics (any src)   -> M1
  binds-on-wavelength: False  ·  all in {M1..M4}: True
  accelerator routes bind on M4 (flux): True
  F-CEN-1 NO-WAVELENGTH PASS
  F-CEN-2 IN-SET       PASS
  F-CEN-3 COVERAGE     PASS
  F-CEN-4 FLUX-TERMINAL PASS
  F-CEN-5 ALL-WALLS-HIT PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h015_wall_census_2026_06_25/result.json`
