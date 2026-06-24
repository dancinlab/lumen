---
id: H_039
slug: band-generalization
title: Generalize the EUV machinery across the spectrum — the undulator/ICS dial λ ∝ 1/γ² makes one accelerator span THz (3.4 MeV) → far-IR (11 MeV) → EUV (511 MeV) → water window (1.08 GeV) → hard X-ray (5.94 GeV), 6.5 orders of magnitude, by dialing electron energy alone; the bands lacking a stable natural emitter (THz gap, EUV, water window, hard X-ray) are precisely the engine's no-incumbent market (meta-law M10), and the campaign's wall structure (dial free, flux the wall, conventional form robust) recurs at every rung
domain: light-source
status: supported
exploration_method: generalize the verified EUV chain across wavelength bands
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
generalizes: H_011 (no wavelength floor) · H_004/006/007 (energy dial) · the whole campaign
---
# H_039 — generalize: EUV is the first instance, not the boundary
> lumen's scope is the source problem. The verified machinery transfers across the spectrum.
## The energy ladder (one undulator, K=1, 18 mm period)
THz gap (300 µm) **3.4 MeV** · far-IR (30 µm) 10.8 MeV · EUV (13.5 nm) **511 MeV** · water window (3 nm) **1.08 GeV** · hard X-ray (0.1 nm) **5.94 GeV** — λ ∝ 1/γ², monotonic, **6.5 orders of magnitude on one machine**.
## What transfers
- **The dial is free at every band** (λ ∝ 1/γ²) — any band is an electron-energy choice + extraction (undulator long-λ/low-E; ICS short-λ by up-shift).
- **The walls transfer too** (honest): flux + extraction tax recur — FEL → slice-spread (needs ERL, H_031/032); ICS → bandwidth tax (fundamental, H_037). So the EUV verdict generalizes: the robust high-average-power form in any no-emitter band is the **conventional accelerator-driven source**; the compact-coherent variant is terminal-thin (H_038).
- **Market = no-incumbent bands** (M10): where a stable emitter exists (far-IR thermal/QCL, visible lasers) the engine has no opening; its market is the THz gap, EUV, water window, hard X-ray, nuclear γ.
## Falsifiers
F-GN-1 monotonic dial · F-GN-2 THz ≤10 MeV · F-GN-3 water window ≤2 GeV · F-GN-4 span ≥4 orders · F-GN-5 every no-emitter band covered (M10) · F-GN-6 bounds.
## Honest Limits
L1 the ladder uses one fixed undulator (K, period) — real machines retune K/period per band, but the λ∝1/γ² scaling and the energy-order are robust; L2 "covered" = the dial reaches the wavelength, NOT that flux/coherence is solved (those walls transfer, per H_031–038); L3 M10 is a market statement (no incumbent), not a claim the engine is built at every band.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
ladder THz 3.4MeV -> EUV 511MeV -> water-window 1.08GeV -> hard-X 5.94GeV · monotonic · 6.5 orders · all no-emitter bands covered
key_finding: the EUV machinery generalizes — one accelerator + undulator/ICS spans THz to hard X-ray by the
             energy dial (6.5 orders), and the no-stable-emitter bands are exactly the engine's market (M10).
             EUV is the 511 MeV rung; the dial-free / flux-wall / conventional-form-robust structure recurs.
honest_note: fixed-undulator ladder (L1); "covered" = dial reaches it, walls still transfer (L2); M10 is a
             market statement not a built claim (L3).
```
**State output**: `state/h039_band_generalization_2026_06_25/result.json`
