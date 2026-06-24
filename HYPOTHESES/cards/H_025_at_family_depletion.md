---
id: H_025
slug: at-family-depletion
title: @-family depletion census — the @-combination space is mapped and dry; of 4 families exactly ONE clears all walls (the accelerator-coherent spine, H_022), the other three fall on distinct walls, and the supply(3 primitives)+demand(1 multiplier) taxonomy is complete → depletion
domain: system
status: supported
exploration_method: fleet-full @-frontier census + depletion judgement
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
closes: goal "tabletop accelerator + @ combination wall-breakthrough + deepen-to-depletion"
---

# H_025 — @-family depletion census (the goal's terminus)

> Closes the standing goal "tabletop accelerator + @ combination wall-breakthrough **and deepen
> after breakthrough until depletion**." A fleet-full fan-out enumerated the @-partner families;
> this card freezes the census and the depletion declaration.

## Hypothesis

Any @-partner must either **make EUV photons** (supply — which splits exhaustively by extraction
physics into three primitives: e-beam→radiator, atomic gain, upconversion) or **change how many are
needed** (demand — a multiplier). Of 4 censused families exactly ONE clears all walls (the
accelerator-coherent spine, H_022); the other three are partial, each falling on a DISTINCT wall
(flux / RLS-defect / CAPEX-redundant). The supply+demand taxonomy being complete, remaining @ ideas
are variants → the @-space is **dry (depletion)**.

## Variables (pre-registered)
- 4-family census (verdict + distinct failure wall) · supply primitives {ebeam-radiator, atomic-gain,
  upconversion} + demand multiplier {requirement-reduction} = taxonomy size 4.

## Run Protocol
- harness: `tool/lumen_optics.evaluate` · run: `state/h025_at_family_depletion_2026_06_25/run_h025.py`
- `python3 .../run_h025.py` · `.../result.json`.

## Falsifiers
- **F-DP-1 SPINE-CLEARS**: the accelerator-coherent spine doesn't clear all walls → no breakthrough.
- **F-DP-2 SINGLE-CLEARER**: ≠1 family clears all → a second independent path exists (not converged).
- **F-DP-3 DISTINCT-WALLS**: partials don't fall on distinct walls → enumeration not orthogonal.
- **F-DP-4 TAXONOMY-COMPLETE**: supply+demand taxonomy ≠ 4 or < 4 families → space not mapped.
- **F-DP-5 DEPLETION**: not (one clearer ∧ orthogonal failures ∧ complete taxonomy) → not depleted.

## Honest Limits
- **L1 (census, not exhaustive search)**: 4 representative families from a fleet-full sweep; an
  unforeseen mechanism could in principle appear, but the supply/demand dichotomy is exhaustive by
  construction (a photon source either generates or the demand changes).
- **L2 (depletion = of the @-COMBINATION space)**: this declares the *partner-family* enumeration dry,
  NOT that the spine is built — the real engineering (cooling stage, module mass-production, start-to-end
  sim) remains, outside what closed-form hypotheses verify.
- **L3 (verdicts inherit their cards' limits)**: source-coherent's flux-fail rests on undemonstrated
  13.5 nm gain (H_017 L1); demand-side's RLS wall is representative (H_B5). The taxonomy is robust; the
  per-family magnitudes are order-of-magnitude.

## Cross-Links
- closes: the standing goal. spine: H_022. deepened by: H_023, H_024. census: `state/at-frontier-census.md`.
- exogenous binding wall remains CAPEX/M7 (H_021); M8 waste-heat ~0.5% (H_020).

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: 4-family census + depletion judgement, 5/5 falsifiers PASS.
  clears-all: 1 (accelerator-coherent spine) · partials: 3 on 3 distinct walls (flux/rls-defect/capex-redundant)
  taxonomy: 3 supply primitives + 1 demand multiplier = 4 (mapped)
key_finding: the @-combination space is mapped and DRY — exactly one family (the H_022
             accelerator-coherent spine) clears all walls, the other three fall on distinct walls, and
             the supply+demand taxonomy is complete, so further @-enumeration yields only variants.
             Depletion reached: the goal "breakthrough + deepen-to-depletion" is met. The route is the
             tabletop accelerator's ERL+FEL combination; the binding work is now CAPEX/M7 + a cooling
             stage, not more @-search.
honest_note: representative census not exhaustive but supply/demand dichotomy is exhaustive (L1);
             depletion of the @-SPACE, not "spine built" — engineering remains (L2); per-family
             magnitudes order-of-magnitude (L3).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_025 @-family depletion census — the @-combination space is mapped and dry
  accelerator-coherent (ERL+FEL/IC)          clears-all-walls   wall=none
  source-coherent (recombination laser)      partial            wall=flux
  demand-side (resist+gating+grazing)        partial            wall=rls-defect
  exotic (plasma-mirror/HHG/channeling)      partial            wall=capex-redundant
  clears-all: 1 (spine) · partials: 3 on 3 distinct walls
  taxonomy: 3 supply primitives + 1 demand multiplier = 4 (mapped)
  -> DEPLETION: no second independent all-wall path; @-space is dry (further @ = variants)
  F-DP-1 SPINE-CLEARS    PASS
  F-DP-2 SINGLE-CLEARER  PASS
  F-DP-3 DISTINCT-WALLS  PASS
  F-DP-4 TAXONOMY-COMPLETE PASS
  F-DP-5 DEPLETION       PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```
**State output**: `state/h025_at_family_depletion_2026_06_25/result.json`
