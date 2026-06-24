---
id: H_003
slug: na-dof-trade
title: NA vs depth-of-focus trade — raising NA improves resolution linearly (×1.67) but shrinks depth-of-focus quadratically (÷2.78), so the focus penalty is strictly steeper than the resolution gain
domain: optics
status: supported
exploration_method: closed-form Rayleigh resolution / DoF relations
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_003 — NA vs depth-of-focus trade

## Hypothesis

Resolution half-pitch ≈ `k1·λ/NA` (falls ∝ 1/NA) while depth-of-focus ≈
`k2·λ/NA²` (falls ∝ 1/NA²). Going NA 0.33 → 0.55 (NXE → High-NA EXE) prints
~1.67× finer but loses ~2.78× of focus depth. The claim: the DoF loss exponent
(NA²) strictly exceeds the resolution gain exponent (NA¹), so every NA increase
buys resolution at a steeper focus cost — the root of the ultra-thin-resist
process pressure (`photochemistry.md`).

## Why

- `optics.md`: the NA↔DoF trade is stated as the driver of resist and process
  constraints. This card proves the asymmetry (linear gain vs quadratic loss).
- Drives `photochemistry.md`: shrinking DoF forces extreme-thin, uniform resist.

## Predictions

- **P1**: res_gain = NA_hi/NA_lo = 1.667×; dof_loss = (NA_hi/NA_lo)² = 2.778×.
- **P2**: dof_loss > res_gain (penalty steeper than gain).

## Variables (pre-registered)

- λ=13.5 nm · NA_lo=0.33 · NA_hi=0.55 · k1=0.3 · k2=0.5 (representative process).

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`resolution_half_pitch`, `depth_of_focus`).
- **run script**: `state/h003_na_dof_trade_2026_06_24/run_h003.py`.
- **run cmd**: `python3 state/h003_na_dof_trade_2026_06_24/run_h003.py`
- **artifacts**: `state/h003_na_dof_trade_2026_06_24/result.json`.

## Criteria

- **verdict_rule**: SUPPORTED = all 5 falsifiers PASS; FALSIFIED = any trigger.

## Falsifiers (pre-registered, measurable)

- **F-DOF-1 RES-GAIN**: res(high NA) ≥ res(low NA) → high NA fails to print finer.
- **F-DOF-2 DOF-LOSS**: DoF(high NA) ≥ DoF(low NA) → high NA fails to shrink DoF.
- **F-DOF-3 QUADRATIC**: dof_loss ≠ (NA_hi/NA_lo)² (tol 1e-9) → the NA² law breaks (structure check).
- **F-DOF-4 PENALTY**: dof_loss ≤ res_gain → penalty not steeper than gain (refutes hypothesis).
- **F-DOF-5 BOUNDS**: any distance ≤ 0 → ledger bug.

## Honest Limits

- **L1 (k1/k2 representative)**: real k1/k2 are process-tuned (resist, illumination,
  OPC); absolute nm values shift with them, but the gain/loss *exponents* (1 vs 2)
  are geometry, not process — the asymmetry is robust.
- **L2 (scalar DoF ignores anamorphic High-NA)**: EXE uses anamorphic (4×/8×) half-
  field optics; a single scalar DoF omits x/y asymmetry and field-stitching.
- **L3 (resolution ≠ printability)**: stochastic defects (`photochemistry.md`) and
  LER set the real floor; this card is the geometric-optics layer only.

## Cross-Links

- **state notes**: `optics.md` (NA↔DoF), `photochemistry.md` (thin-resist pressure).
- **sister H**: H_002 (the other optics-side wall, at shorter λ).
- **harness**: `tool/lumen_optics.py`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: closed-form Rayleigh relations, 5/5 falsifiers PASS.
  resolution 12.27 -> 7.36 nm (gain 1.667x finer)
  depth-of-focus 61.98 -> 22.31 nm (loss 2.778x)
  NA^2 law: dof_loss 2.7778 == (NA_hi/NA_lo)^2 2.7778
key_finding: NA 0.33->0.55 prints 1.67x finer but loses 2.78x of focus depth —
             the DoF penalty (NA^2) is strictly steeper than the resolution gain
             (NA^1), the geometric root of the ultra-thin-resist process wall.
honest_note: k1/k2 representative (L1); scalar DoF omits anamorphic High-NA (L2);
             geometric-optics layer only, stochastics set the real floor (L3).
```

### Run verdict (VERBATIM — `python3 run_h003.py` stdout 2026-06-24)

```
H_003 NA vs depth-of-focus trade
  NA 0.33->0.55 @ 13.5nm
  resolution 12.27 -> 7.36 nm  (gain 1.667x finer)
  depth-of-focus 61.98 -> 22.31 nm  (loss 2.778x)
  NA^2 law check: dof_loss=2.7778 vs (NA_hi/NA_lo)^2=2.7778
  F-DOF-1 RES-GAIN   PASS
  F-DOF-2 DOF-LOSS   PASS
  F-DOF-3 QUADRATIC  PASS
  F-DOF-4 PENALTY    PASS
  F-DOF-5 BOUNDS     PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h003_na_dof_trade_2026_06_24/result.json`
