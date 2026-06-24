---
id: H_011
slug: wavelength-reach
title: Accelerator wavelength reach — no theoretical short-λ floor; λ ~ 1/E² walks EUV→water-window→X-ray, single-stage LPA (≤1 GeV) hits ~3 nm and a few stages (≤2 GeV) hit ~1 nm. The wall is flux/beam-quality, not wavelength
domain: light-source
status: supported
exploration_method: undulator λ ~ 1/γ² ladder vs electron energy
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_011 — accelerator wavelength reach

## Hypothesis

For an accelerator source the photon wavelength is a continuous function of
electron energy (`λ ∝ 1/γ² ∝ 1/E²`), so there is **no theoretical short-
wavelength floor** — raising energy walks EUV → water-window → soft X-ray → hard
X-ray. With a 15 mm / K=1 undulator: single-stage LPA (≤1 GeV, H_004) reaches
~3 nm; a few staged modules (≤2 GeV) reach ~1 nm; ~5 GeV reaches 0.1 nm. The
claim answers "how low can the tabletop accelerator go?": arbitrarily low in
*wavelength* — the binding wall is flux/average-power (H_008) and beam quality
(H_009), which worsen as λ shrinks, not the wavelength itself.

## Why

- Directly answers the user question (이론상 몇 nm까지?) and the
  `light-source-paths.md` open question on least-blocked sub-13.5 nm.
- Reframes the wall: unlike LPP (locked to emitter element + multilayer), the
  accelerator's limit is energy reach and brightness, not the band.

## Predictions

- **P1**: λ(2 GeV)/λ(1 GeV) = 0.25 (inverse-square).
- **P2**: 3 nm ≤ 1 GeV; 1 nm ≤ 2 GeV; 0.1 nm at ~5.4 GeV (all finite).

## Variables (pre-registered)

- undulator 15 mm / K=1 (same as H_006/H_007) · energies 0.5/1/2/5/10 GeV ·
  targets 3 / 1 / 0.1 nm · single-stage 1 GeV · few-stage 2 GeV.

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`undulator_wavelength`, `lorentz_gamma`,
  `energy_for_undulator_wavelength`).
- **run script**: `state/h011_wavelength_reach_2026_06_24/run_h011.py`.
- **run cmd**: `python3 state/h011_wavelength_reach_2026_06_24/run_h011.py`
- **artifacts**: `state/h011_wavelength_reach_2026_06_24/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-WR-1 MONOTONE**: λ(10 GeV) ≮ λ(1 GeV) ≮ λ(0.5 GeV) → a floor exists.
- **F-WR-2 INVERSE-SQUARE**: λ(2 GeV)/λ(1 GeV) ≠ 0.25 (tol) → 1/E² law broken.
- **F-WR-3 SINGLE-STAGE**: 3 nm energy > 1 GeV → not single-stage reachable.
- **F-WR-4 FEW-STAGE**: 1 nm energy > 2 GeV → soft X-ray not few-stage reachable.
- **F-WR-5 BOUNDS**: any λ/energy ≤ 0 or non-finite → ledger bug.

## Honest Limits

- **L1 (wavelength reach ≠ usable source)**: this is the *wavelength* a beam can
  radiate; whether it is a usable litho source is gated by flux (H_008), beam
  quality (H_009), and downstream optics/resist (H_002/H_003) — all worse at short λ.
- **L2 (undulator design point)**: 15 mm / K=1 sets the absolute energies; a
  shorter period or higher K shifts them, but the no-floor / 1-E² conclusion is
  design-independent.
- **L3 (staging idealized)**: "few-stage ≤2 GeV" assumes clean LPA staging
  (coupling, jitter, energy spread not modeled here — H_009 is the quality axis).
- **L4 (litho-relevant band is narrow)**: only ~13.5 down to a few nm is
  lithographically interesting now; the X-ray/γ reach is physical headroom, not a
  litho target — stated for completeness, not as a node goal.

## Cross-Links

- **sister H**: H_004 (energy reach) · H_006/H_007 (undulator + tuning) ·
  H_008/H_009 (the real walls that cap usable short-λ).
- **state notes**: `light-source-paths.md` (sub-13.5 nm question).
- **harness**: `tool/lumen_optics.py` (electron-beam light section).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: undulator 1/E^2 ladder, 5/5 falsifiers PASS.
  0.5 GeV -> 11.750 nm | 1 GeV -> 2.938 nm | 2 GeV -> 0.734 nm | 5 GeV -> 0.118 nm | 10 GeV -> 0.029 nm
  3 nm = 0.99 GeV | 1 nm = 1.71 GeV | 0.1 nm = 5.42 GeV | lambda(2)/lambda(1) = 0.2500
key_finding: there is no theoretical short-wavelength floor for an accelerator
             source — lambda ~ 1/E^2 walks EUV->water-window->X-ray continuously.
             Single-stage LPA (<=1 GeV) reaches ~3 nm, a few stages (<=2 GeV)
             reach ~1 nm. The binding wall is flux/beam-quality (H_008/H_009),
             not the wavelength.
honest_note: wavelength reach != usable source — flux/quality/downstream all
             worsen at short λ (L1); undulator design point sets absolute energies
             (L2); staging idealized (L3); litho-relevant band is narrow (L4).
```

### Run verdict (VERBATIM — `python3 run_h011.py` stdout 2026-06-24)

```
H_011 accelerator wavelength reach (15 mm undulator, K=1)
   0.5 GeV ->   11.750 nm
     1 GeV ->    2.938 nm
     2 GeV ->    0.734 nm
     5 GeV ->    0.118 nm
    10 GeV ->    0.029 nm
  energy needed: 3 nm=0.99 GeV | 1 nm=1.71 GeV | 0.1 nm=5.42 GeV
  1/E^2 check: lambda(2GeV)/lambda(1GeV) = 0.2500 (expect 0.25)
  F-WR-1 MONOTONE    PASS
  F-WR-2 INVERSE-SQUARE PASS
  F-WR-3 SINGLE-STAGE PASS
  F-WR-4 FEW-STAGE   PASS
  F-WR-5 BOUNDS      PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h011_wavelength_reach_2026_06_24/result.json`
