---
id: H_004
slug: compact-accelerator
title: Compact plasma-wakefield accelerator as a light-source enabler — a GV/m Dawson gradient (96 GV/m @ 1e18 cm⁻³) is ~3200× conventional RF, reaching 1 GeV in ~1 cm vs ~33 m, the enabling step toward a tabletop EUV source
domain: light-source
status: supported
exploration_method: closed-form Dawson wave-breaking field, reference-matched to demiurge
verification_method: deterministic harness + 5 pre-registered falsifiers (incl. reference parity)
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_004 — compact accelerator as a light-source enabler

## Hypothesis

A laser-plasma (wakefield) accelerator sustains the Dawson cold wave-breaking
field `E_0 = m_e c ω_p / e`, which at n_e = 1e18 cm⁻³ is ~96 GV/m — thousands of
times the ~30 MV/m of conventional RF. So it reaches a lithography-relevant
electron energy (≈1 GeV, the energy class an undulator / inverse-Compton stage
needs for EUV/X-ray photons) in **cm not tens of metres**. The claim: this
compactness is the enabling step that makes an accelerator-based EUV source a
candidate path alongside LPP — "no CERN required."

> This card tests the **accelerator compactness** only. Turning the electron
> beam into EUV photons (undulator / inverse-Compton, beam quality, average
> power) is explicitly downstream — a sister hypothesis, not this card (L2).

## Why

- Reframes `light-source-paths.md`'s synchrotron/FEL row: the wall there is
  facility scale + throughput. A plasma-wakefield stage attacks the *scale* term
  by replacing km-class RF with a cm-class plasma.
- The "if we had a CERN accelerator…" question: a tabletop laser-plasma
  accelerator is the compact substitute. Physics is **reference-matched** to
  `dancinlab/demiurge` cern-accelerator (already built + PIC-verified).

## Predictions

- **P1**: E_0(1e18 cm⁻³) = 96.159 GV/m (parity with demiurge anchor).
- **P2**: gradient ratio E_0 / RF(30 MV/m) ≈ 3200× (≥100×).
- **P3**: length to 1 GeV — LPA ~1 cm vs RF ~33 m, ≥100× shorter.

## Variables (pre-registered)

- n_e = 1e18 cm⁻³ · RF_gradient = 30 MV/m (SCRF class) · target = 1 GeV.
- reference anchor: demiurge `wakefield_e0_gv_m` = 96.15919872735485 GV/m.

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`plasma_omega`, `wavebreak_field`,
  `accelerator_length`) — formulas reference-matched to
  `hexa-lang/stdlib/cern/plasma_wakefield.hexa`.
- **run script**: `state/h004_compact_accelerator_2026_06_24/run_h004.py`.
- **run cmd**: `python3 state/h004_compact_accelerator_2026_06_24/run_h004.py`
- **artifacts**: `state/h004_compact_accelerator_2026_06_24/result.json`.

## Criteria

- **verdict_rule**: SUPPORTED = all 5 falsifiers PASS (incl. demiurge parity);
  FALSIFIED = any trigger.

## Falsifiers (pre-registered, measurable)

- **F-CA-1 PARITY**: |E_0 − demiurge_ref| > 1e-6 GV/m → harness diverges from the
  verified reference (reference-match check).
- **F-CA-2 GRADIENT**: E_0/RF < 100× → wakefield gradient not a step-change.
- **F-CA-3 COMPACT**: RF/LPA length ratio < 100× → no real compactness.
- **F-CA-4 MONOTONE**: lower density giving ≥ E_0 → ω_p(n_e) scaling broken.
- **F-CA-5 BOUNDS**: any quantity ≤ 0 / non-finite → ledger bug.

## Honest Limits

- **L1 (E_0 is the wave-breaking ceiling, not the sustained field)**: real LWFA
  accelerating gradient is regime-dependent — demiurge's own 2-D PIC sweep gives
  E_z = 1.7 / 73.6 / 405 GV/m for a0 = 0.5 / 2 / 4. Using E_0 = 96 GV/m as the
  characteristic gradient is mid-range (blowout reaches ~0.77 E_0 at a0=2), not a
  guaranteed operating point.
- **L2 (electron energy ≠ EUV photons)**: reaching 1 GeV is necessary, not
  sufficient — undulator / inverse-Compton photon generation, conversion
  efficiency, and average power are downstream and unaddressed here.
- **L3 (single-stage ideal)**: dephasing + pump depletion cap a single LWFA stage;
  the "~1 cm" is a single-stage geometric figure, real high-energy needs staging.
- **L4 (RF gradient representative)**: 30 MV/m is SCRF class; normal-conducting RF
  reaches ~100 MV/m, shrinking the ratio to ~960× — still a step-change.
- **L5 (HVM throughput / rep-rate / wall-plug unaddressed)**: the industrial wall
  (average power, kHz rep-rate, efficiency, stability) is the same class of
  question H_001/H_002 raise for LPP — this card is the gradient layer only.

## Cross-Links

- **reference**: `dancinlab/demiurge` cern-accelerator
  (`hexa-lang/stdlib/cern/plasma_wakefield.hexa` · cold-linear closed-form +
  1-D/2-D PIC parity · E_0 anchor 96.159 GV/m). lumen reuses the physics and
  adds the **light-source compactness** axis (transcend-axis beyond parity).
- **sister H**: H_001 (LPP wall — the path this offers an alternative to) ·
  H_002 (optics demand any source, incl. this one, must still meet).
- **state notes**: `light-source-paths.md` (synchrotron/FEL row), `euv-source-problem.md`.
- **harness**: `tool/lumen_optics.py` (accelerator section).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24. Reference parity
exact (|Δ| = 0).

```
verdict_class: SUPPORTED
evidence_summary: Dawson E_0 reference-matched to demiurge, 5/5 falsifiers PASS.
  E_0 = 96.15920 GV/m  (demiurge ref 96.15920, |Δ| = 0.00)
  gradient ratio vs RF(30 MV/m) = 3205x
  length to 1 GeV: LPA = 1.04 cm vs RF = 33.3 m (3205x shorter)
key_finding: a plasma-wakefield gradient is ~3200x conventional RF, reaching a
             1 GeV (undulator/IC-relevant) beam in ~1 cm instead of ~33 m — the
             compactness that makes a tabletop accelerator-driven EUV source a
             candidate path ("no CERN required"). E_0 matches the verified
             demiurge reference to machine precision.
honest_note: E_0 is the wave-breaking ceiling not the sustained field (L1, real
             E_z regime-dependent 1.7-405 GV/m); electron energy ≠ EUV photons —
             undulator/IC + average power are downstream (L2); single-stage ideal
             (L3); HVM throughput wall unaddressed (L5).
```

### Run verdict (VERBATIM — `python3 run_h004.py` stdout 2026-06-24)

```
H_004 compact plasma-wakefield accelerator as light-source enabler
  n_e=1e+18 cm^-3  omega_p=5.6415e+13 rad/s
  E_0 = 96.15920 GV/m  (demiurge ref 96.15920, |Δ|=0.00e+00)
  gradient ratio vs RF(30 MV/m) = 3205x
  length to 1 GeV:  LPA=1.04 cm  vs  RF=33.3 m  (3205x shorter)
  F-CA-1 PARITY    PASS
  F-CA-2 GRADIENT  PASS
  F-CA-3 COMPACT   PASS
  F-CA-4 MONOTONE  PASS
  F-CA-5 BOUNDS    PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h004_compact_accelerator_2026_06_24/result.json`
