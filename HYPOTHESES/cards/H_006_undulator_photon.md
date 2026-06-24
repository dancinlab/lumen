---
id: H_006
slug: undulator-photon
title: Accelerator → EUV photons — an undulator turns an LPA electron beam into 13.5 nm at ~0.47 GeV (single-stage LPA reach), and inverse-Compton reaches it at only ~2 MeV, closing the accelerator→light chain (H_004)
domain: light-source
status: supported
exploration_method: standard undulator + inverse-Compton radiation relations
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_006 — accelerator → EUV photons

## Hypothesis

H_004 showed an LPA reaches GeV-class electrons in ~cm. This card closes the
chain to actual light: an undulator radiates `λ = (λ_u/2γ²)(1+K²/2)`, so with a
representative 15 mm / K=1 undulator, 13.5 nm needs only ~0.47 GeV — within a
single-stage LPA. An inverse-Compton route (1 µm laser, `λ_x = λ_L/4γ²`) reaches
13.5 nm at only ~2 MeV. Either mechanism converts the e-beam into EUV photons at
LPA-reachable energy → the accelerator path produces *light*, not just electrons.

## Why

- Fills H_004's L2 gap ("electron energy ≠ EUV photons"): this is the photon stage.
- Two independent mechanisms (undulator, inverse-Compton) → robustness.

## Predictions

- **P1**: undulator 13.5 nm energy ≈ 0.47 GeV ≤ 1 GeV (LPA single-stage).
- **P2**: inverse-Compton 13.5 nm energy ≈ 2 MeV (≪ undulator; low-energy route).

## Variables (pre-registered)

- target 13.5 nm · undulator period 15 mm · K=1 · LPA reach 1 GeV · IC laser 1 µm.

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`undulator_wavelength`,
  `energy_for_undulator_wavelength`, `inverse_compton_wavelength`, `lorentz_gamma`).
- **run script**: `state/h006_undulator_photon_2026_06_24/run_h006.py`.
- **run cmd**: `python3 state/h006_undulator_photon_2026_06_24/run_h006.py`
- **artifacts**: `state/h006_undulator_photon_2026_06_24/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-UND-1 REACH**: undulator energy for 13.5 nm > 1 GeV → not single-stage LPA.
- **F-UND-2 ROUNDTRIP**: undulator λ at derived γ ≠ 13.5 nm (tol) → inconsistency.
- **F-IC-3 LOW-E**: inverse-Compton energy ≥ 100 MeV → not a low-energy alt route.
- **F-IC-4 ROUNDTRIP**: IC λ at derived γ ≠ 13.5 nm (tol) → inconsistency.
- **F-5 BOUNDS**: any energy/wavelength ≤ 0 → ledger bug.

## Honest Limits

- **L1 (wavelength, not flux/brightness)**: this fixes the photon *wavelength*;
  in-band average power, photon flux per shot, and source étendue (which gate HVM,
  cf. H_005) are not modeled here.
- **L2 (representative undulator)**: 15 mm / K=1 is one design point; a shorter
  period or higher K shifts the energy, but the EUV-at-sub-GeV conclusion is robust.
- **L3 (IC trade-off)**: inverse-Compton reaches EUV at far lower energy but with
  lower photon yield per electron and tight laser-electron timing — cheaper energy,
  harder flux (the opposite trade to the undulator).
- **L4 (beam quality assumed)**: energy spread / emittance of real LPA beams
  broaden and weaken undulator lines; ideal-beam figure here.

## Cross-Links

- **sister H**: H_004 (the e-beam this radiates) · H_007 (tuning λ by energy) ·
  H_005 (the flux/throughput axis this does not yet address).
- **harness**: `tool/lumen_optics.py` (electron-beam light section).
- **state notes**: `light-source-paths.md` (compact-LPA path).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: undulator + inverse-Compton relations, 5/5 falsifiers PASS.
  undulator (15 mm, K=1): 13.5 nm at 466.5 MeV (<= 1 GeV LPA reach), roundtrip 13.5000 nm
  inverse-Compton (1 µm): 13.5 nm at 2.20 MeV, roundtrip 13.5000 nm
key_finding: an LPA-class beam makes 13.5 nm EUV two independent ways — undulator
             at ~0.47 GeV (single-stage reach) or inverse-Compton at ~2 MeV — so
             the accelerator path produces light, not just electrons, closing
             H_004's photon-stage gap.
honest_note: fixes wavelength not flux/brightness (L1); representative undulator
             (L2); IC trades energy for yield/timing (L3); ideal-beam (L4).
```

### Run verdict (VERBATIM — `python3 run_h006.py` stdout 2026-06-24)

```
H_006 undulator / inverse-Compton -> EUV photons from an LPA beam
  target 13.5 nm
  undulator (period 15 mm, K=1.0): E = 466.5 MeV  (LPA reach 1000 MeV)
    roundtrip lambda = 13.5000 nm
  inverse-Compton (1 µm laser): E = 2.20 MeV  (roundtrip 13.5000 nm)
  F-UND-1 REACH    PASS
  F-UND-2 ROUNDTRIP PASS
  F-IC-3 LOW-E     PASS
  F-IC-4 ROUNDTRIP PASS
  F-5 BOUNDS       PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h006_undulator_photon_2026_06_24/result.json`
