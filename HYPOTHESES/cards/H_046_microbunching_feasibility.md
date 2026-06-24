---
id: H_046
slug: microbunching-feasibility
title: Micro-bunching feasibility — the one open milestone (H_045) is physics-ALLOWED, not forbidden; coherent 13.5 nm needs a bunch length below the wavelength, and at the published SSMB-EUV design target σ_z ~ 3 nm the bunching factor b = exp(−½(2πσ_z/λ)²) ≈ 0.38 gives a coherent fraction b² ≈ 0.14, a substantial N² enhancement, so EUV-precision steady-state micro-bunching is hard engineering rather than a forbidding physical floor; honest residual: theory-allowed ≠ demonstrated — few-nm bunching needs a strong laser modulator and low energy spread simultaneously
domain: light-source
status: supported
exploration_method: closed-form feasibility of the single gating milestone (H_045)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
deepens: H_045 (the one open milestone)
---
# H_046 — the milestone is allowed, not forbidden
> H_045 reduced the whole compact-coherent-EUV bet to one milestone: steady-state micro-bunching at 13.5 nm. Is that *physically allowed*, or is there a forbidding floor?
## The closed-form check
Coherent radiation at λ needs the bunch length σ_z below λ; the bunching factor is **b = exp(−½(2πσ_z/λ)²)** and coherent power ~ b²N². At the published **SSMB-EUV design target σ_z ~ 3 nm** (λ = 13.5 nm): b ≈ 0.38 → **b² ≈ 0.14** — a substantial coherent (N²) enhancement survives. No fundamental floor sits above the few-nm target (quantum diffusion sets a sub-nm scale). So the milestone is **physics-ALLOWED**: hard engineering, not forbidden.
## What this resolves
The compact-coherent-EUV risk drops from "maybe impossible" to "demonstrate it." The lab has shown the path is **not forbidden** — the remaining question is experimental (achieve and hold few-nm steady-state bunching), which is where the closed-form lab honestly hands off.
## Falsifiers
F-MB-1 target σ_z < λ (nonzero bunching) · F-MB-2 b² ≥ 0.1 (substantial coherence) · F-MB-3 required σ_z reachable (no forbidding floor) · F-MB-4 EUV-precision bunching undemonstrated (honest) · F-MB-5 bounds.
## Honest Limits
L1 the Gaussian bunching-factor formula is the standard first-order model; real SSMB has slippage, lattice nonlinearity, and collective effects that erode b; L2 "allowed" is *necessary not sufficient* — it shows no hard floor, NOT that the simultaneous strong-modulation + low-spread + ring-stability is achievable; L3 σ_z ~ 3 nm is a published *design target*, not a measured value (the 2021 PoP was at longer wavelength).
## Verdict
```
verdict_class: SUPPORTED  (5/5)
sigma_z 3nm target < 13.5nm; b=0.377 -> b^2=0.142 (>=0.1 substantial); physics-allowed; EUV-precision undemonstrated
key_finding: the single gating milestone is physics-ALLOWED, not forbidden -- at the ~3nm SSMB-EUV design
             bunch length the coherent fraction b^2 ~ 0.14 survives at 13.5nm, a real N^2 enhancement. The
             compact-coherent-EUV risk is hard engineering, not a physical impossibility; the lab hands off
             to experiment (demonstrate few-nm steady-state bunching).
honest_note: first-order Gaussian model, collective effects erode b (L1); allowed = necessary not sufficient
             (L2); 3nm is a design target not a measurement (L3).
```
**State output**: `state/h046_microbunching_feasibility_2026_06_25/result.json`
