---
id: H_037
slug: brightness-lever-falsified
title: Loop cycle-3 breakthrough attempt — FALSIFIED (honest negative) — a high-brightness (low-divergence) electron beam does NOT beat the H_036 bandwidth-collection derating, because the ICS wavelength-angle correlation λ(θ)=λ₀(1+γ²θ²) is radiation kinematics: off-axis photons are genuinely out-of-band regardless of beam quality, so the in-band cone fraction stays ~BW (recovery 1.0×) — the ~50× derating is a FUNDAMENTAL ICS tax, not a beam-fixable one
domain: light-source
status: falsified
exploration_method: break→verify→deepen loop, cycle 3 — test the brightness escape
verification_method: deterministic harness + 3 pre-registered falsifiers (1 triggered)
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
falsifies: the "high-brightness beam recovers the ICS in-band fraction" escape
---
# H_037 — cycle-3 breakthrough attempt: FALSIFIED (honest)
> commons honesty: a failed breakthrough is a result. Reported as FALSIFIED, not tuned to green.
## The tested claim (and why it fails)
- **Claim:** a low-divergence beam lets you collect a larger in-band cone fraction, recovering the ~50× flux derating (H_036).
- **Reality:** in ICS the wavelength-angle correlation **λ(θ)=λ₀(1+γ²θ²)** is *radiation kinematics*. Off-axis photons sit at a different wavelength — genuinely **out of the 2% band** — no matter how good the beam is. The in-band cone fraction is ~BW *independent of beam divergence* (recovery 1.0×).
- **Verdict: FALSIFIED** — the brightness lever does not exist; the bandwidth-collection derating is a **fundamental ICS tax**.
## Falsifiers (1 triggered → FALSIFIED)
- **F-HB-1 BRIGHTNESS-RECOVERS — FAIL (triggered):** the high-brightness beam does NOT recover the in-band fraction (≥2×) — the tested escape is false.
- F-HB-2 KINEMATIC-INVARIANT — PASS (in-band fraction invariant to divergence, confirming the tax is fundamental).
- F-HB-3 BOUNDS — PASS.
## Honest Limits
L1 first-order λ(θ) kinematics (recoil + laser-bandwidth terms only worsen it); L2 this falsifies the *brightness* escape — angle-resolved monochromatization (different wavelength per pixel) is a separate, optics-heavy idea not tested here; L3 a FALSIFIED card is a recorded negative, kept for honesty (it constrains H_038's convergence).
## Verdict
```
verdict_class: FALSIFIED  (2/3 falsifiers PASS; F-HB-1 triggered)
recovery 1.00x (in-band fraction beam-independent) -> the brightness lever does NOT beat the ~50x derating
key_finding: the ICS bandwidth-collection derating is a FUNDAMENTAL kinematic tax, not a beam-quality
             problem -- no high-brightness beam recovers it. Honest negative; feeds the H_038 convergence.
```
**State output**: `state/h037_brightness_lever_falsified_2026_06_25/result.json`
