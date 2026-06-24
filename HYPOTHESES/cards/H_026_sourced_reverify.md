---
id: H_026
slug: sourced-reverify
title: Sourced re-verification — published measured values CONFIRM the core inputs (optics R, LPP power, ~0.02% wall-plug, CAPEX) and CORRECT three optimistic links (La/B 0.58→6.5nm wall ~8× not 14×; demonstrated 46.9nm XRL gL~8.3 < 14 saturation → recombination harder; raw LPA spread several% → FEL needs cooling)
domain: system
status: supported
exploration_method: re-run the chain with published measured values (state/sourced-parameters.md)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
---
# H_026 — sourced re-verification
> Goal "실측+검증": ground the representative parameters in published data and report which verdicts hold vs correct. Real-value SSOT: `state/sourced-parameters.md`.
## Key findings
- **CONFIRMED** (representative = published): Mo/Si 70%, LPP 205–250 W, CE 4–5%, rep 50 kHz, scanner ~1.17 MW, **wall-plug ~0.02%** (200 W IF ⇐ ~1 MW, direct anchor), throughput ≥135 WPH, EUV tool $200–400 M.
- **CORRECTED** (data differs, honest, all "harder"): (1) best La/B = 0.58 → 6.5 nm optics multiplier ~8× not 14× (still a wall); (2) demonstrated 46.9 nm Ar XRL gL_max ≈ 8.28 < 14 saturation → recombination route harder than H_017's anchor; (3) raw LPA σγ/γ often several % → the FEL coupling needs cooling not yet routine (strengthens H_024).
## Falsifiers
F-SR-1 optics wall holds (≥2×) at measured 0.58 · F-SR-2 BBU margin ≥10× at measured 10 mA · F-SR-3 demonstrated XRL gL < 14 (correction recorded) · F-SR-4 core inputs confirmed · F-SR-5 bounds.
## Honest Limits
L1 measured values span ranges (best-case used for La/B); L2 corrections are "harder not easier" — they tighten engineering margins, the physics-wall conclusions (flux not a ceiling, CAPEX binding, M8 ~0.5%) hold; L3 economics params remain generic (electricity/Wright not litho-specific).
## Verdict
```
verdict_class: SUPPORTED  (5/5)
6.5nm wall 7.92x at R_beuv=0.58 · BBU margin 50x at 10 mA · 46.9nm XRL gL 8.28<14 (corrected) · core CONFIRMED
key_finding: the campaign's core inputs are REAL (match published), and three optimistic links are
             honestly corrected by data — every correction makes the engineering harder, not easier.
```
**State output**: `state/h026_sourced_reverify_2026_06_25/result.json`
