---
id: H_045
slug: risk-localization
title: Risk localization (continuation capstone) — the compact SSMB-Compton path addresses all four mapped walls (wavelength via the free dial + Compton at MeV; beam quality via Compton slice-spread-immunity; footprint via the 7 MeV metre-scale ring; power via SSMB coherent-N² CW), so the entire next-generation compact-coherent-EUV question reduces to ONE measurable milestone — the steady-state micro-bunching factor achievable at ~13.5 nm precision; the mechanism is proof-of-principle demonstrated (Nature 2021) at longer wavelength, and EUV-precision bunching is the single unproven binding step the whole path is gated on
domain: system
status: supported
exploration_method: continuation capstone — localize the residual risk after H_043/044
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
localizes: H_033/H_043/H_044 (the compact SSMB-Compton synthesis)
---
# H_045 — the whole bet reduces to one milestone
> After breaking power (H_043) and footprint (H_044), what single thing still has to work?
## The four walls — addressed
- **wavelength** ✅ free dial λ~1/γ² (H_011) + Compton reaches 13.5 nm at MeV (H_033)
- **beam quality** ✅ Compton is slice-spread-immune (H_033) — no FEL slice wall
- **footprint** ✅ 7 MeV → ~1 m ring (H_044)
- **power** ✅ SSMB steady-state micro-bunching → coherent (N²) CW (H_043)
## The one open wall 🎯
All four rest on **one mechanism**: steady-state micro-bunching at **~EUV-wavelength precision**. The 2021 proof-of-principle demonstrated the mechanism (at longer wavelength); pushing the bunching to **13.5 nm precision** is the **single unproven, binding step**. So the entire next-gen compact-coherent-EUV question reduces to **one measurable milestone**: the bunching factor at 13.5 nm. The whole path is gated on it.
## Why this is the honest terminus of the loop
Every other wall is solved or reopened; the residual is concentrated, not diffuse. That makes the research question *crisp* — "can you achieve and hold steady-state micro-bunching at 13.5 nm?" — and *measurable*, rather than a vague "is compact EUV possible?". This is where the closed-form lab honestly hands off to experiment.
## Falsifiers
F-RL-1 ≥4 walls addressed · F-RL-2 exactly one open residual · F-RL-3 mechanism demonstrated (Nature 2021) · F-RL-4 reduces to one measurable milestone · F-RL-5 EUV-precision bunching undemonstrated (honest gate) · F-RL-6 every wall classified.
## Honest Limits
L1 "addressed" means each wall has a verified reopening mechanism in the lab, NOT a built device — the milestone gates the whole stack; L2 micro-bunching at 13.5 nm precision may itself hide sub-problems (quantum diffusion, ring dynamics, jitter) — "one milestone" is the *headline* gate, not a proof it is a single experiment; L3 this localizes the COMPACT SSMB-Compton path's risk; the funded near-term answer remains the conventional ERL FEL (H_030).
## Verdict
```
verdict_class: SUPPORTED  (6/6)
4 walls addressed (wavelength/beam-quality/footprint/power) · 1 open (EUV-precision micro-bunching) · mechanism demonstrated longer-lambda (Nature 2021) · EUV-precision undemonstrated
key_finding: the compact-coherent-EUV question reduces to ONE measurable milestone -- the steady-state
             micro-bunching factor at ~13.5 nm precision. Wavelength, beam quality, footprint, and power are
             each addressed by a verified reopening; the entire bet is concentrated on one unproven step,
             where the closed-form lab honestly hands off to experiment.
honest_note: 'addressed' = verified mechanism not built device (L1); the one milestone may hide sub-problems
             (L2); localizes the compact path, the funded near-term answer stays the conventional ERL FEL (L3).
```
**State output**: `state/h045_risk_localization_2026_06_25/result.json`
