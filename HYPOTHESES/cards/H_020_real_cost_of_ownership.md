---
id: H_020
slug: real-cost-of-ownership
title: Real-units cost-of-ownership settles M8-vs-LPP — with public-order figures the energy + waste-heat (M8) term is ~0.5% of LPP cost-of-ownership; the binding economic wall is CAPEX + maintenance (M7/M9), NOT the M8 thermodynamic floor
domain: system
status: supported
exploration_method: real-units cost-of-ownership (the H_019 open question, sourced)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
settles: H_019 / meta-law M8 open question
---

# H_020 — real-units cost-of-ownership (settles M8-vs-LPP)

> **Closes the campaign's last flagged unknown.** H_019 showed (normalized) that economics is a
> conjunction reopenable down to the M8 waste-heat floor, but left "does M8 sit above or below LPP's
> all-in cost?" open. This card answers it with public-order figures.

## Hypothesis

Populate the cost-of-ownership model with representative public-order numbers (2nd-gen EUV tool
~$350M, maintenance ~1/4 tool/yr, ~1 MW wall-plug, $0.10/kWh). The claim: the **M8 term** (energy
generation + waste-heat cooling) is **a small single-digit-% of cost-of-ownership** — CAPEX +
maintenance dominate. So the M8 thermodynamic floor, though a true ceiling, is **economically
negligible**, and the binding economic wall is CAPEX (M7 learning curve / M9 amortization).

## Variables (pre-registered, public-order representative — see L1)

- CAPEX $350M (transcript) · amortize 5 yr · maintenance 1/4 tool/yr (transcript) · wall-plug 1 MW ·
  utilization 0.7 · $0.10/kWh · cooling COP 4.

## Run Protocol

- harness: `tool/lumen_optics.evaluate` · run: `state/h020_real_cost_of_ownership_2026_06_25/run_h020.py`
- `python3 .../run_h020.py` · artifacts `.../result.json`.

## Falsifiers (pre-registered)

- **F-M8-1 NEGLIGIBLE**: energy+waste-heat ≥ 5% of CoO → M8 is economically material.
- **F-M8-2 CAPEX-DOMINANT**: CAPEX+maintenance ≤ 80% of CoO → CAPEX not the binding wall.
- **F-M8-3 ORDERING**: energy ≥ maintenance or ≥ CAPEX → cost hierarchy wrong.
- **F-M8-4 BOUNDS**: fractions ∉ (0,1) or CoO ≤ 0 → ledger bug.
- **F-M8-5 M8-REAL**: energy term = 0 → the M8 floor would be denied (it is real, just small).

## Honest Limits

- **L1 (public-order, not vendor figures)**: every number is representative public-order knowledge
  (CAPEX/maintenance from the transcript; wall-plug/$/kWh/COP textbook orders) — not a vendor cost
  model. The *finding* (energy ≪ CAPEX, ~0.5%) is robust across plausible ranges; exact % is not.
- **L2 (maintenance fraction range)**: the transcript gives ~1/4–1/3 tool/yr; 1/4 used (conservative).
  At 1/3 the energy fraction is even smaller — the conclusion strengthens.
- **L3 (settles LPP, informs others)**: this is the *incumbent* (LPP) cost structure. A coherent/ERL
  source shifts CAPEX (bespoke, M7) and η (M6), but its energy term is also small vs CAPEX — so the
  economic battle is CAPEX/amortization for every route, confirming H_019's M7/M9 emphasis.
- **L4 (excludes ecosystem/moat/ramp)**: ASML lock-in, ramp risk, and €/kWh regional spread unmodeled.

## Cross-Links

- settles: H_019 / meta-law **M8** open question. inputs: transcript `euv-yt-2KDLZMG8FAs-transcript.md`.
- refines: `state/euv-meta-laws.md` economic verdict (M8 is the true ceiling but not the binding wall).

## Verdict

```
verdict_class: SUPPORTED
evidence_summary: public-order cost-of-ownership, 5/5 falsifiers PASS.
  CAPEX/yr $70.0M · maintenance/yr $87.5M · energy/yr $0.77M (gen 0.61 + cooling/M8 0.15) · CoO $158.3M
  M8 (energy+heat) = 0.48% of CoO · CAPEX+maint = 99.5%
key_finding: the M8 waste-heat thermodynamic floor is REAL but economically negligible (~0.5% of
             LPP cost-of-ownership); the binding economic wall is CAPEX + maintenance (M7 learning
             curve / M9 amortization). This settles the campaign's last open unknown: M8 sits ~200x
             below LPP all-in cost, so it is NOT the decision wall — CAPEX is.
honest_note: public-order representative numbers, finding robust / exact % not (L1); maintenance
             1/4 conservative, 1/3 strengthens it (L2); settles LPP, CAPEX-dominance holds for all
             routes (L3); excludes ecosystem/moat/ramp (L4).
```

### Run verdict (VERBATIM — `python3 run_h020.py` stdout 2026-06-25)

```
H_020 real-units cost-of-ownership — M8 vs LPP (settles H_019 open question)
  CAPEX/yr   = $  70.0M   maintenance/yr = $  87.5M
  energy/yr  = $  0.77M   (gen $0.61M + cooling/M8 $0.15M)
  CoO/yr     = $ 158.3M
  M8 (energy+heat) = 0.48% of CoO  ·  CAPEX+maint = 99.5%
  -> M8 thermodynamic floor is REAL but economically negligible; CAPEX/maint (M7/M9) is the wall
  F-M8-1 NEGLIGIBLE  PASS
  F-M8-2 CAPEX-DOMINANT PASS
  F-M8-3 ORDERING    PASS
  F-M8-4 BOUNDS      PASS
  F-M8-5 M8-REAL     PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h020_real_cost_of_ownership_2026_06_25/result.json`
