---
id: H_007
slug: sub13-tunability
title: Sub-13.5 nm tunability by electron energy — the SAME undulator reaches 13.5 / 6.5 / 5 / 3 nm across a ~2.1× energy dial (466→990 MeV, all ≤1 GeV LPA reach), so shorter wavelength is a knob, not an emitter-element + mirror-multilayer swap
domain: light-source
status: supported
exploration_method: undulator gamma ~ 1/sqrt(lambda) scaling
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_007 — sub-13.5 nm tunability by electron energy

## Hypothesis

The undulator fundamental scales as `γ ∝ 1/√λ`, so the same undulator tunes to
shorter wavelengths purely by raising electron energy. For a 15 mm / K=1
undulator, the EUV→BEUV ladder 13.5 / 6.5 / 5 / 3 nm maps to 466 / 672 / 766 /
990 MeV — a ~2.1× energy dial, all within single-stage LPA reach (H_004). The
claim: for an accelerator source, going sub-13.5 nm is a **knob** (electron
energy), not the LPP wall of swapping the emitter element (Sn→Gd/Lu/La) *and* the
mirror multilayer (Mo/Si→La/B). This is lumen's central "stable sub-13.5 nm
source" target attacked from a different axis.

## Why

- Transcript `euv-yt-2KDLZMG8FAs-transcript.md`: shorter λ (6.5/5/3 nm) is
  "theoretically possible" but "no clear source"; candidates Gd/Lu/La each imply a
  new emitter + new multilayer. This card shows the accelerator route sidesteps
  both — wavelength follows electron energy continuously.
- Directly answers `light-source-paths.md` open question (least-blocked sub-13.5 nm).

## Predictions

- **P1**: E(λ) = E(13.5) · √(13.5/λ); E(3 nm)/E(13.5 nm) ≈ 2.12×.
- **P2**: all four targets reachable at ≤ 1 GeV (single-stage LPA).

## Variables (pre-registered)

- targets 13.5/6.5/5/3 nm · undulator 15 mm / K=1 (same as H_006) · LPA reach 1 GeV.

## Run Protocol

- **harness**: `tool/lumen_optics.energy_for_undulator_wavelength`.
- **run script**: `state/h007_sub13_tunability_2026_06_24/run_h007.py`.
- **run cmd**: `python3 state/h007_sub13_tunability_2026_06_24/run_h007.py`
- **artifacts**: `state/h007_sub13_tunability_2026_06_24/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-TUN-1 SPAN**: any target (incl. 3 nm) needs > 1 GeV → outside single-stage LPA.
- **F-TUN-2 SQRT-LAW**: E(λ)/E(13.5) ≠ √(13.5/λ) (tol) → scaling broken.
- **F-TUN-3 MONOTONE**: 3 nm energy ≤ 13.5 nm energy → shorter-λ not higher-E.
- **F-TUN-4 DIAL**: E(3 nm)/E(13.5 nm) > 3× → not a modest dial (regime change).
- **F-TUN-5 BOUNDS**: any energy ≤ 0 → ledger bug.

## Honest Limits

- **L1 (wavelength reach, not source viability)**: shows the *wavelength* is a
  dial; brightness, in-band flux, beam quality, and HVM throughput (H_005) at
  3 nm are unaddressed — reaching the wavelength ≠ a production source.
- **L2 (representative undulator)**: a different period/K shifts the absolute
  energies; 3 nm at ≤1 GeV is tight for 15 mm/K=1 and moves with the design.
- **L3 (shorter λ stresses everything downstream)**: optics (H_002 multilayer),
  resist (H_003 thin-film), and stochastics worsen as λ falls — this card only
  removes the *source-element* barrier, not the rest of the column.
- **L4 (ideal beam)**: real LPA energy spread broadens the undulator line, blurring
  the clean λ↔E mapping.

## Cross-Links

- **sister H**: H_004 (the accelerator) · H_006 (the photon stage) · H_002/H_003
  (downstream walls that any sub-13.5 nm source still meets).
- **transcript**: `euv-yt-2KDLZMG8FAs-transcript.md` (6.5/5/3 nm, Gd/Lu/La).
- **harness**: `tool/lumen_optics.energy_for_undulator_wavelength`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: gamma ~ 1/sqrt(lambda) ladder, 5/5 falsifiers PASS.
  13.5 nm -> 466.5 MeV | 6.5 nm -> 672.3 MeV | 5.0 nm -> 766.5 MeV | 3.0 nm -> 989.5 MeV
  dial 13.5->3 nm = 2.12x energy (<= 1 GeV LPA reach), sqrt-law holds
key_finding: one undulator spans 13.5->3 nm with a ~2.1x electron-energy dial,
             all within single-stage LPA reach — for an accelerator source,
             shorter wavelength is a continuous knob, not the LPP double-swap of
             emitter element (Sn->Gd/Lu/La) plus mirror multilayer (Mo/Si->La/B).
honest_note: fixes wavelength not source viability/flux (L1); representative
             undulator, 3nm tight at 15mm/K=1 (L2); downstream optics/resist
             walls still worsen with λ (L3); ideal beam (L4).
```

### Run verdict (VERBATIM — `python3 run_h007.py` stdout 2026-06-24)

```
H_007 sub-13.5 nm tunability by electron energy (same undulator)
   13.5 nm ->   466.5 MeV
    6.5 nm ->   672.3 MeV
    5.0 nm ->   766.5 MeV
    3.0 nm ->   989.5 MeV
  dial 13.5->3 nm = 2.12x energy  (LPA reach 1000 MeV)
  sqrt-law (gamma ~ 1/sqrt(lambda)) holds: True
  F-TUN-1 SPAN     PASS
  F-TUN-2 SQRT-LAW PASS
  F-TUN-3 MONOTONE PASS
  F-TUN-4 DIAL     PASS
  F-TUN-5 BOUNDS   PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h007_sub13_tunability_2026_06_24/result.json`
