---
id: H_002
slug: beuv-mirror-throughput-wall
title: BEUV (6.5 nm) multilayer-mirror throughput wall — same N-mirror column passes ~14x fewer photons at 6.5 nm than 13.5 nm, forcing a matching source-power increase
domain: optics
status: supported
exploration_method: closed-form public-physics relation (R**N chain)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_002 — BEUV mirror-throughput wall

## Hypothesis

An all-reflective EUV column is a chain of N multilayer mirrors, so optical
throughput scales as `T = R**N` (R = per-mirror reflectivity). Moving from
13.5 nm (Mo/Si, R ≈ 0.70) to 6.5 nm "BEUV" (La/B-based, R ≈ 0.55) with the
**same mirror count** collapses T. To hold constant wafer dose, source power
must rise by `T_euv / T_beuv = (R_euv/R_beuv)**N`. The claim: this multiplier
is large (≫2×) and is therefore a first-order reason the 6.5 nm path is
source-bound, independent of emitter-element or resist changes.

## Why

- `optics.md` (pillar 3): 13.5 nm Mo/Si ~70%/mirror; ~6.5 nm needs La/B
  multilayers with **lower** reflectivity → more loss per mirror → demands far
  more source power. This card makes that statement quantitative and falsifiable.
- `light-source-paths.md`: the 6.5 nm wall is framed as "no clear stable-source
  path." This isolates the optics-side contribution to that wall.
- Cross-links the source problem (`H_001` LPP power ceiling): the multiplier
  here becomes a *demand* that H_001's supply must meet.

## Predictions

- **P1**: `power_multiplier = (0.70/0.55)**11` ≈ 14× (≫2×).
- **P2**: multiplier grows with N (more mirrors → worse penalty).
- **P3**: identical reflectivity → multiplier exactly 1 (negative control).

## Variables

- **R_euv** = 0.70 (Mo/Si @ 13.5 nm, representative)
- **R_beuv** = 0.55 (La/B @ 6.5 nm, representative)
- **N_mirrors** = 11 (collector + illuminator + projection optics box)
- measured: throughput_euv, throughput_beuv, power_multiplier, control, N=7 case.

## Run Protocol

- **harness**: repo-root `tool/lumen_optics.py` (`mirror_chain_throughput`,
  `source_power_multiplier`, `evaluate`).
- **run script**: `state/h002_beuv_mirror_wall_2026_06_24/run_h002.py`.
- **deterministic**: stdlib `math` only, no randomness, $0 mac local.
- **run cmd**: `python3 state/h002_beuv_mirror_wall_2026_06_24/run_h002.py`
- **artifacts**: `state/h002_beuv_mirror_wall_2026_06_24/result.json`.

## Criteria

- **C1 WALL**: power_multiplier ≥ 2×.
- **C2 MONOTONE**: throughput_beuv < throughput_euv.
- **C3 N-SENSITIVITY**: multiplier(N=11) > multiplier(N=7).
- **verdict_rule**: SUPPORTED = all 5 falsifiers PASS; FALSIFIED = any trigger.

## Falsifiers (pre-registered, measurable)

- **F-MW-1 WALL**: power_multiplier < 2× → not a meaningful wall.
- **F-MW-2 MONOTONE**: throughput_beuv ≥ throughput_euv → physics broken.
- **F-MW-3 NEG-CONTROL**: identical R gives multiplier ≠ 1 → harness bug.
- **F-MW-4 N-SENSITIVITY**: multiplier(N=7) ≥ multiplier(N=11) → not N-driven.
- **F-MW-5 BOUNDS**: any throughput ∉ (0,1] → ledger bug.

## Honest Limits

- **L1 (R values representative, not measured)**: reported La/B 6.5 nm
  reflectivities span ~0.40–0.60 across studies; 0.55 is a mid estimate.
  At R_beuv=0.40 the multiplier is far larger; at 0.60, smaller — the *sign*
  (a wall) is robust, the *magnitude* is uncertain.
- **L2 (N representative)**: real scanner reflective-surface counts are
  model-specific / not fully public; N=11 is a representative column.
- **L3 (optics-only slice)**: ignores emitter-element change (Sn→Gd/Tb),
  collector/conversion-efficiency shifts, and resist absorption at 6.5 nm —
  the true system wall is larger and multi-factor; this isolates one term.
- **L4 (power ≠ throughput)**: holding dose constant assumes wafer throughput
  scales linearly with source power; scan-speed and dose margins also matter.
- **L5 (demand ≠ impossibility)**: a 14× power demand is only a "wall" if the
  source cannot supply it — that supply question is H_001, not this card.

## Cross-Links

- **state notes**: `optics.md` (multilayer challenge), `light-source-paths.md`
  (6.5 nm BEUV wall), `photochemistry.md` (6.5 nm chemistry shift).
- **sister H**: H_001 (LPP source-power ceiling — the supply side of this demand).
- **harness**: `tool/lumen_optics.py`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: closed-form R**N chain, 5/5 falsifiers PASS.
  throughput_euv  = 0.0197733   (0.70**11)
  throughput_beuv = 0.00139312  (0.55**11)
  power_multiplier = 14.19x      (N=7 -> 5.41x)
key_finding: at the same 11-mirror column, a 6.5 nm La/B optics (R=0.55) passes
             ~14x fewer photons than a 13.5 nm Mo/Si optics (R=0.70), so source
             power must rise ~14x to hold wafer dose — an optics-side source
             wall that exists BEFORE emitter/resist penalties are added.
honest_note: R and N are representative not measured (L1/L2); optics-only slice
             (L3); a 14x demand is a wall only if the source cannot supply it (L5,
             -> H_001).
```

### Run verdict (VERBATIM — `python3 run_h002.py` stdout 2026-06-24)

```
H_002 BEUV mirror-throughput wall — source-power multiplier
  R_euv=0.7 R_beuv=0.55 N=11
  throughput_euv  = 0.0197733
  throughput_beuv = 0.00139312
  power_multiplier = 14.1935x  (N=7 -> 5.4094x)
  F-MW-1 WALL        PASS
  F-MW-2 MONOTONE    PASS
  F-MW-3 NEG-CONTROL PASS
  F-MW-4 N-SENSITIVITY PASS
  F-MW-5 BOUNDS      PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h002_beuv_mirror_wall_2026_06_24/result.json`
