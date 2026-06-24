---
id: H_009
slug: beam-quality-linewidth
title: Beam energy spread broadens the undulator line — a ~1% LPA energy spread gives ~2% Δλ/λ, filling (and exceeding, 2.24%) the 2% in-band EUV budget and swamping higher harmonics
domain: light-source
status: supported
exploration_method: undulator linewidth = natural ⊕ energy-spread broadening
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_009 — beam quality → undulator linewidth

## Hypothesis

The undulator line has a natural relative width ~1/(nN), but electron energy
spread broadens it by ~2(σγ/γ). LPA beams carry ~1% energy spread, so the line
broadens to ~2% — at or beyond the 2% in-band EUV budget — and at higher
harmonics (narrower natural width) the energy spread fully dominates. The claim:
LPA beam quality, not just rep-rate (H_008), erodes the *in-band* photon fraction,
compounding the flux wall.

## Why

- Quantifies why LPA-undulator in-band flux is worse than the raw average power
  (H_008) suggests: much of the spectrum falls outside the 2% acceptance.
- Beam quality is the second binding LPA constraint after rep-rate.

## Variables (pre-registered)

- σγ/γ = 1% · N = 100 periods · EUV in-band budget = 2% · harmonics n = 1, 3.

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`undulator_natural_linewidth`, `energy_spread_broadening`).
- **run script**: `state/h009_beam_quality_linewidth_2026_06_24/run_h009.py`.
- **run cmd**: `python3 state/h009_beam_quality_linewidth_2026_06_24/run_h009.py`
- **artifacts**: `state/h009_beam_quality_linewidth_2026_06_24/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-BQ-1 DOMINATE**: broadening < natural width → energy spread not the limiter.
- **F-BQ-2 OVERFILL**: total width ≤ 2% budget → no in-band loss (refutes).
- **F-BQ-3 HARMONIC**: broadening ≤ natural(n=3) → harmonics not swamped.
- **F-BQ-4 MONOTONE**: halving σγ/γ does not narrow the line → relation broken.
- **F-BQ-5 BOUNDS**: any width ≤ 0 → ledger bug.

## Honest Limits

- **L1 (quadrature model)**: total = √(natural² + broadening²) is a first-order
  combination; the exact lineshape (and the 2σγ/γ coefficient) depend on undulator
  detail, but the dominance of energy spread at ~1% is robust.
- **L2 (σγ/γ representative)**: ~1% is a typical LPA figure; staged / dechirped LPA
  beams reach <0.1% in research — which would reopen this wall (break-walls).
- **L3 (in-band fraction, not absolute flux)**: this fixes the *fraction* lost to
  bandwidth; absolute photon count is H_008's average-power axis.
- **L4 (monochromator trade)**: a monochromator can recover bandwidth but throws
  away flux — trading H_008's wall for a tighter line, not escaping it.

## Cross-Links

- **sister H**: H_008 (average-power wall this compounds) · H_006/H_007 (the
  undulator whose line this broadens) · H_002 (2% in-band budget origin).
- **harness**: `tool/lumen_optics.py` (undulator linewidth helpers).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: natural ⊕ energy-spread broadening, 5/5 falsifiers PASS.
  sigma_gamma/gamma = 1.0% (N=100)
  n=1: natural 1.00% + spread 2.00% = total 2.24%  (budget 2%)
  n=3: natural 0.33% << spread 2.00%  (harmonic swamped)
key_finding: a ~1% LPA energy spread broadens the undulator line to ~2.24%,
             exceeding the 2% in-band EUV budget and fully swamping higher
             harmonics — so beam quality erodes the in-band photon fraction,
             compounding the H_008 flux wall. Energy spread, not natural width,
             is the limiter.
honest_note: quadrature lineshape model (L1); 1% energy spread representative,
             <0.1% reachable in staged LPA (L2, reopenable); fraction not absolute
             flux (L3); monochromator recovers BW only by discarding flux (L4).
```

### Run verdict (VERBATIM — `python3 run_h009.py` stdout 2026-06-24)

```
H_009 beam energy spread -> undulator linewidth
  sigma_gamma/gamma = 1.0%  (N=100 periods)
  n=1: natural 1.00% (+) spread 2.00% = total 2.24%  (budget 2%)
  n=3: natural 0.33% vs spread 2.00% -> spread swamps harmonic
  F-BQ-1 DOMINATE  PASS
  F-BQ-2 OVERFILL  PASS
  F-BQ-3 HARMONIC  PASS
  F-BQ-4 MONOTONE  PASS
  F-BQ-5 BOUNDS    PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h009_beam_quality_linewidth_2026_06_24/result.json`
