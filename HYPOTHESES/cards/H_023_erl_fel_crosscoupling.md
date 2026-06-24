---
id: H_023
slug: erl-fel-crosscoupling
title: ERL↔FEL cross-coupling holds but is the combination's tightest link — the cooled beam (0.85%) sits inside the FEL Pierce bandwidth (rho~1%, margin 1.18×) and the post-FEL beam (1.31%) inside the ERL acceptance (2%, margin 1.52×); FEL beam-quality is the binding cross-coupling
domain: light-source
status: supported
exploration_method: co-existence check of the H_022 levers on one beam (deepens L1)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
deepens: H_022 L1 (cross-couplings unmodeled)
---

# H_023 — ERL↔FEL cross-coupling (deepening the weakest link)

> H_022 *multiplied* separately-verified levers; its L1 flagged that they must also **co-exist on one
> beam**. This card checks the two real couplings and finds the binding one.

## Hypothesis

Two couplings the combination must satisfy: (1) the FEL gain condition σγ/γ < ρ — the **cooled** beam
(H_013, 0.85%) must sit inside the Pierce bandwidth, which at the high-current LPA regime is ρ~1%;
(2) the ERL must energy-recover the **post-FEL** beam, whose spread broadens by ~ρ, within its energy
acceptance (~2%). Claim: both hold, but the **FEL beam-quality** coupling has the tightest margin —
it is the binding cross-coupling of the combination (not flux, not CAPEX), and deeper cooling buys margin.

## Variables (pre-registered)
- cooled σγ/γ 0.85% (H_013) · FEL ρ 1% (high-current LPA) · FEL-saturation spread ~1% · ERL acceptance 2%.

## Run Protocol
- harness: `tool/lumen_optics.evaluate` · run: `state/h023_erl_fel_crosscoupling_2026_06_25/run_h023.py`
- `python3 .../run_h023.py` · `.../result.json`.

## Falsifiers
- **F-CC-1 FEL-GAIN**: cooled σ ≥ ρ → FEL gain dies (cross-coupling wall).
- **F-CC-2 ERL-ACCEPT**: post-FEL spread ≥ ERL acceptance → recovery dies.
- **F-CC-3 FEL-TIGHTEST**: FEL margin ≥ ERL margin → FEL not the binding coupling.
- **F-CC-4 POSITIVE-MARGIN**: either margin ≤ 1 → combination inconsistent.
- **F-CC-5 BOUNDS**: any non-positive → ledger bug.

## Honest Limits
- **L1 (ρ is regime-dependent — the real risk)**: ρ~1% assumes the high-current LPA-FEL regime; a
  lower-ρ scheme would make σ<ρ FAIL (the cooled 0.85% would exceed it) — the FEL-gain coupling would
  then be a genuine wall. The margin (1.18×) is thin and ρ-conditional.
- **L2 (1-D coupling model)**: ignores transverse emittance, slippage, and CSR; a full start-to-end
  sim is the real test. This is the first-order co-existence check, not a machine design.
- **L3 (resolves H_022 L1 partially)**: confirms the two scalar couplings are consistent; the joint
  multi-constraint optimization (and whether deeper cooling costs flux, H_013 L4) remains open.

## Cross-Links
- deepens: H_022 (combination). couples: H_013 (cooling) ↔ H_A2 (FEL) ↔ H_016 (ERL).
- the FEL-beam-quality margin is the @-variant target (source-coherent routes, H_017, sidestep it).

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: two-coupling co-existence check, 5/5 falsifiers PASS.
  FEL gain: cooled 0.85% < rho 1.0% (margin 1.18x) · ERL recovery: post-FEL 1.31% < 2.0% (margin 1.52x)
  binding coupling = FEL beam-quality (1.18x < ERL 1.52x)
key_finding: the H_022 levers co-exist on one beam — the cooled beam sits inside the FEL Pierce
             bandwidth and the post-FEL beam inside the ERL acceptance — but the FEL beam-quality
             coupling is the tightest link (margin 1.18x), the combination's binding constraint.
             Deeper cooling (H_013) buys margin; source-coherent @-routes (H_017) sidestep it.
honest_note: rho is regime-dependent — at low rho the FEL-gain coupling becomes a real wall (L1, the
             thin 1.18x is ρ-conditional); 1-D model, start-to-end sim is the real test (L2); resolves
             H_022 L1 only partially (L3).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_023 ERL<->FEL cross-coupling (deepening H_022 weakest link)
  FEL gain: cooled 0.85% < rho 1.0%  -> margin 1.18x  (OK)
  ERL recovery: post-FEL 1.31% < acceptance 2.0%  -> margin 1.52x  (OK)
  binding cross-coupling = FEL beam-quality (margin 1.18x < ERL 1.52x)
  -> combination is consistent, but FEL beam-quality is the tightest link (deeper cooling buys margin)
  F-CC-1 FEL-GAIN      PASS
  F-CC-2 ERL-ACCEPT    PASS
  F-CC-3 FEL-TIGHTEST  PASS
  F-CC-4 POSITIVE-MARGIN PASS
  F-CC-5 BOUNDS        PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```
**State output**: `state/h023_erl_fel_crosscoupling_2026_06_25/result.json`
