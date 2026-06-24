---
id: H_013
slug: energy-spread-cooling
title: Energy-spread cooling splits the M4 brightness wall — cooling σγ/γ 1.0%→0.85% pushes the undulator line from 2.24% to 1.97% (inside the 2% budget, quality wall BEATEN) while average power is unchanged (flux wall STUBBORN)
domain: light-source
status: supported
exploration_method: abstraction-lane prediction P4 (state/euv-meta-laws.md) made runnable
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
from_metalaw: M4 (Liouville/brightness) · escape E4 · prediction P4
---

# H_013 — energy-spread cooling splits the M4 brightness wall

> **Fleet loop closure.** The abstraction lane (`state/euv-meta-laws.md`) peeled H_009/H_008 to
> meta-law **M4** (Liouville brightness bound), named escape **E4** (dissipative cooling breaks the
> conservative-optics assumption), and cast prediction **P4**. This card makes P4 runnable.

## Hypothesis

M4 says phase-space density is conserved under conservative forces, so Δλ/λ ≈ 2(σγ/γ) is fixed by
the injector. **But Liouville forbids only lossless optics** — a dissipative cooling stage
(radiative / laser / optical-stochastic) is non-conservative and shrinks σγ/γ. Cooling a ~1% LPA
beam to ≤0.866% (the critical σ* where the total undulator line equals the 2% budget) pushes the
line from 2.24% to 1.97% — **inside** the in-band budget. Crucially, cooling touches phase space,
**not** rep-rate or charge, so the H_008 average-power gap is unchanged. The claim: M4 splits into
a *quality* sub-wall (beatable by cooling) and a *flux* sub-wall (not) — which is the single most
decision-relevant fact for whether the accelerator route can reach HVM.

## Why

- Tests the abstraction lane's highest-leverage escape (E4/P4) — the smallest hard margin in the
  whole law-set (2.24% vs 2%) and the only M4 face a non-conservative mechanism can move.
- Cleanly separates "beatable" from "stubborn" so the campaign knows which wall is terminal.

## Variables (pre-registered)

- undulator N=100 (natural 1%) · in-band budget 2% · σγ/γ before 1.0% / after 0.85% ·
  flux side: LPA 1 kHz × 1 µJ (H_008, unchanged by cooling).

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`undulator_natural_linewidth`, `energy_spread_broadening`, `average_power`).
- **run script**: `state/h013_energy_spread_cooling_2026_06_25/run_h013.py`.
- **run cmd**: `python3 state/h013_energy_spread_cooling_2026_06_25/run_h013.py`
- **artifacts**: `state/h013_energy_spread_cooling_2026_06_25/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-QW-1 BEFORE-FAIL**: uncooled (1%) line ≤ 2% → no quality wall to beat.
- **F-QW-2 AFTER-PASS**: cooled line > 2% → cooling fails to beat the quality wall (refutes).
- **F-QW-3 THRESHOLD**: σ* not in (cooled, uncooled) → the critical-σ crossing is wrong.
- **F-QW-4 FLUX-STUBBORN**: cooling changes average power → the split is not real (would mean cooling magically adds photons).
- **F-QW-5 BOUNDS**: cooled line not strictly narrower / non-positive → ledger bug.

## Honest Limits

- **L1 (cooling stage assumed, not designed)**: this proves the *target* σ* and the split; it does
  NOT design the cooling element (radiative damping is slow at low energy; laser/optical-stochastic
  cooling of LPA beams is research-stage). Reaching 0.85% is the open engineering wall.
- **L2 (quadrature lineshape)**: inherits H_009's √(natural² + broadening²) model.
- **L3 (split is the finding, not a solution)**: beating the quality wall does NOT print a wafer —
  the flux wall (H_008, ~10³–10⁵×) is untouched and remains the terminal accelerator-route question.
- **L4 (cooling may cost flux)**: real cooling can scrape charge / lengthen the machine — a second-
  order coupling to flux not modeled here.

## Cross-Links

- **from**: `state/euv-meta-laws.md` M4 / E4 / P4 (abstraction lane).
- **sister H**: H_009 (the line it narrows) · H_008 (the flux wall it does NOT move) · H_A2 (SASE,
  also threatened by σγ/γ).
- **harness**: `tool/lumen_optics.py` (undulator linewidth + average_power).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-25.

```
verdict_class: SUPPORTED
evidence_summary: undulator line vs cooled σγ/γ + unchanged flux, 5/5 falsifiers PASS.
  natural 1.00% · critical σ* = 0.866%
  σ 1.00% -> line 2.24% (> 2%: quality WALL)
  σ 0.85% -> line 1.97% (<= 2%: quality BEATEN)
  flux 1.000 mW before = after (flux WALL stubborn)
key_finding: the M4 brightness wall splits — energy-spread cooling (1.0%→0.85%) pushes
             the undulator line inside the 2% in-band budget (quality sub-wall beatable),
             while average power is untouched (flux sub-wall, H_008, stubborn). Tells the
             campaign the quality wall is engineering-reopenable and the flux wall is the
             terminal accelerator-route question.
honest_note: proves the target σ*, does not design the cooling stage (L1, the real wall);
             quadrature lineshape (L2); beating quality ≠ printing — flux untouched (L3);
             cooling may cost flux second-order (L4).
```

### Run verdict (VERBATIM — `python3 run_h013.py` stdout 2026-06-25)

```
H_013 energy-spread cooling splits the M4 brightness wall (from P4)
  natural line (N=100) = 1.00%  · critical sigma* = 0.866%
  sigma 1.00% -> line 2.24%  (> 2% budget: quality WALL)
  sigma 0.85% -> line 1.97%  (<= budget: quality BEATEN)
  flux unchanged: 1.000 mW before = after  (flux WALL stubborn, H_008)
  F-QW-1 BEFORE-FAIL PASS
  F-QW-2 AFTER-PASS  PASS
  F-QW-3 THRESHOLD   PASS
  F-QW-4 FLUX-STUBBORN PASS
  F-QW-5 BOUNDS      PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h013_energy_spread_cooling_2026_06_25/result.json`
