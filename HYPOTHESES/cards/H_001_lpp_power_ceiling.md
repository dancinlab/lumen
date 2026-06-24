---
id: H_001
slug: lpp-power-ceiling
title: LPP source-power ceiling — a representative LPP power budget (~250 W class, plausibly scaled to ~1.5 kW) falls short of the ~3.5 kW the 6.5 nm optics demand (H_002) requires
domain: light-source
status: supported
exploration_method: closed-form LPP power budget, chained to H_002 multiplier
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_001 — LPP source-power ceiling

## Hypothesis

LPP (Laser-Produced Plasma) in-band EUV power is `P = f_rep · E_pulse · CE ·
collection`. With representative public-order values the baseline reproduces the
~250 W production class. Pushing every lever to a plausible near-term ceiling
gives ~1.5 kW. The 6.5 nm path needs the baseline times the H_002 mirror-
throughput multiplier (~14×) ≈ 3.5 kW. The claim: ceiling < demand, so LPP
power-scaling **alone** does not reach a stable 6.5 nm source.

## Why

- `light-source-paths.md`: LPP is incumbent (~250 W+), droplet-rate limited;
  "scaling to higher power hard." This card makes that quantitative.
- Supply side of H_002's demand: H_002 says 6.5 nm *needs* ~14× more power;
  H_001 asks whether LPP can *supply* it.

## Variables (pre-registered, representative — see L1)

- baseline: f_rep=50 kHz · E_pulse=0.5 J · CE=0.05 · collection=0.20 → ~250 W
- ceiling: f_rep=100 kHz · E_pulse=1.0 J · CE=0.06 · collection=0.25 → ~1.5 kW
- demand: baseline × H_002 multiplier (R_euv=0.70, R_beuv=0.55, N=11 → 14.19×)

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`lpp_source_power`, `source_power_multiplier`).
- **run script**: `state/h001_lpp_power_ceiling_2026_06_24/run_h001.py`.
- **deterministic**: stdlib only, $0 mac local.
- **run cmd**: `python3 state/h001_lpp_power_ceiling_2026_06_24/run_h001.py`
- **artifacts**: `state/h001_lpp_power_ceiling_2026_06_24/result.json`.

## Criteria

- **verdict_rule**: SUPPORTED = all 5 falsifiers PASS (ceiling < demand, baseline
  realistic, scaling monotone, demand > today); FALSIFIED = any trigger.

## Falsifiers (pre-registered, measurable)

- **F-PC-1 SUPPLY**: ceiling ≥ demand → LPP scaling is NOT the wall (refutes hypothesis).
- **F-PC-2 BASELINE**: baseline ∉ [150, 400] W → model/numbers wrong, not hypothesis.
- **F-PC-3 MONOTONE**: ceiling ≤ baseline → lever-scaling fails to raise power (bug).
- **F-PC-4 BOUNDS**: CE/collection ∉ [0,1] or power < 0 → ledger bug.
- **F-PC-5 GAP-SIGN**: demand ≤ baseline → multiplier ≤ 1 (sanity vs H_002).

## Honest Limits

- **L1 (numbers representative, not vendor-confirmed)**: f_rep/E_pulse/CE/collection
  are public-order estimates chosen so the baseline lands at the ~250 W class;
  real LPP values are vendor-guarded. The verdict is conditional on this budget.
- **L2 (multiplicative budget ignores plasma coupling)**: CE vs droplet size vs
  pre-pulse interact; a four-lever product is a first-order model only.
- **L3 (ceiling is an engineering horizon, not a physical limit)**: a breakthrough
  on any lever (or a new drive scheme) moves the ceiling — `break-walls`: this is
  an "investment/horizon" wall, not a terminal one.
- **L4 (demand inherits H_002 limits)**: the 14× multiplier carries H_002's L1–L5
  (representative R/N, optics-only). A different R_beuv shifts the demand.

## Cross-Links

- **sister H**: H_002 (mirror-throughput wall — the demand this must meet) ·
  H_004 (compact accelerator — an alternative source path if LPP is the wall).
- **harness**: `tool/lumen_optics.lpp_source_power`.
- **state notes**: `light-source-paths.md`, `euv-source-problem.md`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: representative LPP budget, chained to H_002, 5/5 falsifiers PASS.
  baseline = 250.0 W   ceiling = 1500.0 W
  H_002 multiplier = 14.19x -> demand = 3548.4 W
  supply gap = 2048.4 W
key_finding: even with every lever pushed to a plausible near-term ceiling
             (~1.5 kW), LPP falls ~2 kW short of the ~3.5 kW the 6.5 nm optics
             demand requires — LPP power-scaling alone does not reach a stable
             6.5 nm source on this representative budget.
honest_note: numbers are public-order representative (L1); the ceiling is an
             engineering horizon not a physical limit (L3) — a lever breakthrough
             or new drive scheme reopens it (break-walls). Demand inherits H_002's
             representative-R/N limits (L4).
```

### Run verdict (VERBATIM — `python3 run_h001.py` stdout 2026-06-24)

```
H_001 LPP source-power ceiling vs 6.5 nm demand
  baseline = 250.0 W   ceiling = 1500.0 W
  H_002 multiplier = 14.19x -> demand = 3548.4 W
  supply gap (demand - ceiling) = 2048.4 W
  F-PC-1 SUPPLY    PASS
  F-PC-2 BASELINE  PASS
  F-PC-3 MONOTONE  PASS
  F-PC-4 BOUNDS    PASS
  F-PC-5 GAP-SIGN  PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h001_lpp_power_ceiling_2026_06_24/result.json`
