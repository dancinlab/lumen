---
id: H_043
slug: ssmb-novel-breakthrough
title: NOVEL breakthrough on the accelerator power wall — Steady-State MicroBunching (SSMB), a third accelerator architecture beyond compact-LPA and single-pass FEL — a storage ring whose beam is micro-bunched at the radiation wavelength every turn, radiating coherently (P~N², ~1e6× over the incoherent ring) and, because the ring reuses the beam continuously, delivering that coherent power CW (high average power ~1 kW at 13-14 nm, ≥10× the HVM floor), with the mechanism proof-of-principle demonstrated (Nature 2021); honest residual: still a ring facility (footprint wall remains) and 13.5 nm kW SSMB undemonstrated
domain: light-source
status: supported
exploration_method: break-walls — a novel third accelerator architecture (reference-matched to the SSMB program)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_042 (accelerator power-vs-footprint wall)
---
# H_043 — NOVEL: Steady-State MicroBunching breaks the accelerator power wall
> The campaign's accelerator families were compact-LPA (wins wavelength, loses power) and single-pass FEL (wins power, but huge + beam-dump). SSMB is a **third architecture** not previously in the lab.
## The novel mechanism (sourced, as-of 2026-06)
- In a storage ring, electrons normally radiate **incoherently** (P ~ N). **Micro-bunch** them at the radiation wavelength (bunch ≪ λ) and they radiate **coherently** (P ~ N²) — a ~**1e6× enhancement**.
- SSMB makes that micro-bunching **steady-state** — present *every turn*. Because the ring **reuses the beam continuously**, the coherent power is delivered **CW** (high *average* power), unlike the single-pass FEL whose beam is dumped after one pass.
- It explicitly targets **~1 kW at 13-14 nm for lithography** (Tsinghua SSMB-EUV; arXiv:2110.08987 / Sci Rep s41598-022-07323-z) — ≥10× the ~100 W HVM floor. The mechanism is **proof-of-principle demonstrated** (Deng/Tang/Chao, *Nature* 2021, at the MLS, Berlin).
## Why it breaks the wall
It is the missing middle: coherent (FEL-class) average power from a **reused ring beam**, so neither the compact-LPA's low power nor the single-pass FEL's huge dumped-beam facility. The accelerator **power** wall (H_008/H_042) is broken by a genuinely novel, demonstrated-mechanism, funded path.
## Falsifiers
F-SS-1 ≥1e6× coherent enhancement (N²) · F-SS-2 steady-state CW reuse vs FEL dump · F-SS-3 ~1 kW ≥ HVM floor · F-SS-4 novel third architecture · F-SS-5 mechanism demonstrated (Nature 2021) · F-SS-6 honest residual (still a ring + 13.5 nm kW undemonstrated).
## Honest Limits
L1 it breaks the **power** wall, NOT the **footprint** wall — SSMB is still a storage ring (~50-100 m), a facility, not tabletop (so it competes with the FEL on footprint, and amortization economics H_021/H_040 still apply); L2 13.5 nm kW SSMB is **undemonstrated** — the 2021 PoP showed the micro-bunching *mechanism*, not litho-power 13.5 nm output; micro-bunching to 13.5 nm precision is the hard open problem; L3 N_coh~1e6 is representative; the real coherent fraction depends on the achievable bunching factor.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
coherent enhancement ~1e6x (P~N^2) · steady-state CW ring reuse · ~1kW @13-14nm = 10x floor · novel third architecture · mechanism demonstrated (Nature 2021) · honest residual (ring footprint + 13.5nm kW undemonstrated)
key_finding: SSMB breaks the accelerator POWER wall with a genuinely novel, demonstrated-mechanism third
             architecture — a storage ring micro-bunched every turn radiates coherently (N^2) and CW (reused
             beam), targeting ~1 kW at 13-14 nm. It is the missing middle between compact-LPA (low power) and
             single-pass FEL (huge dump). Residual: still a ring (footprint), 13.5 nm kW undemonstrated.
honest_note: breaks power not footprint -- still a facility (L1); 13.5nm kW undemonstrated, micro-bunching to
             13.5nm is the hard part (L2); representative coherent fraction (L3).
```
**State output**: `state/h043_ssmb_novel_breakthrough_2026_06_25/result.json`
