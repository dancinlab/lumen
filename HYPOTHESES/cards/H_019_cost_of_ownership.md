---
id: H_019
slug: cost-of-ownership
title: Cost-of-ownership conjunction — a compact coherent/ERL source beats LPP $/wafer-layer ONLY when efficiency η≥~4× LPP (M6) AND amortized across M≥~3 scanners (M9); neither lever alone suffices, and the M8 waste-heat OPEX floor never vanishes
domain: system
status: supported
exploration_method: economic prediction Q3 (state/euv-meta-laws.md M6-M9) made runnable
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
from_metalaw: M6 (η-coupling) · M9 (amortization) · M8 (waste-heat floor) · prediction Q3
---

# H_019 — cost-of-ownership conjunction (Q3)

> **Fleet loop, third closure.** The economic abstraction peel (`state/euv-meta-laws.md` M6–M9)
> named Q3 the cheapest terminal probe — cheaper than any physics card. This runs it.

## Hypothesis

After flux is reopened (H_016), the terminal question is economic: does a compact coherent/ERL
source beat LPP on $/wafer-layer? Model normalized cost = CAPEX_unit/N_scanners + OPEX_base/η_ratio
(LPP = 1.0). The claim: the win is a **conjunction** — it needs efficiency η ≥ ~4× LPP (M6) AND
amortization across M ≥ ~3 scanners (M9); efficiency alone (1 scanner) or amortization alone
(no η gain) each LOSE. And the M8 waste-heat OPEX floor (OPEX/η) never vanishes even as scanners→∞.

## Variables (pre-registered, normalized)
- LPP=1.0 · coherent CAPEX_unit=1.2 · OPEX_base=0.6 · win case (η×4, M=3) · η-only (η×4, M=1) · amort-only (η×1, M=3).

## Run Protocol
- harness: `tool/lumen_optics.cost_of_ownership` · run: `state/h019_cost_of_ownership_2026_06_25/run_h019.py`
- `python3 .../run_h019.py` · artifacts `.../result.json`.

## Falsifiers
- **F-COO-1 WIN**: both levers don't beat LPP → no economic path.
- **F-COO-2 ETA-INSUFFICIENT**: efficiency alone (M=1) beats LPP → amortization not needed.
- **F-COO-3 AMORT-INSUFFICIENT**: amortization alone (η=1) beats LPP → efficiency not needed.
- **F-COO-4 CONJUNCTION**: win not strictly below both single-lever cases → not a conjunction.
- **F-COO-5 M8-FLOOR**: cost as N→∞ ≠ the OPEX/η floor → the 2nd-law waste-heat floor is misstated.

## Honest Limits
- **L1 (normalized order-of-magnitude)**: CAPEX/OPEX shares and the η/M thresholds are coordinate
  estimates (🜂 economics peel), not vendor figures; the *structure* (conjunction + M8 floor) is the
  finding, not the exact break-even η or M.
- **L2 (M8 floor is the true ceiling)**: the win shrinks but never crosses the OPEX/η_max waste-heat
  asymptote — whether that asymptote sits below LPP's all-in cost is the one unverified unknown.
- **L3 (model, not a market)**: ignores ecosystem lock-in, ASML moat, ramp risk, and €/kWh regional spread.

## Cross-Links
- from: `state/euv-meta-laws.md` M6/M9/M8, prediction Q3. inputs: H_016 (ERL η), H_017 (recombination route), H_014 (no-SPF η).

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: normalized cost-of-ownership, 5/5 falsifiers PASS.
  LPP=1.0 · BOTH(η×4,M=3)=0.55 WIN · η-only=1.35 LOSE · amort-only=1.00 LOSE
  M->inf asymptote 0.150 = M8 OPEX floor 0.150 (never 0)
key_finding: a compact coherent/ERL source beats LPP $/wafer-layer ONLY as a conjunction of
             efficiency (η≥~4x, M6) AND scanner-amortization (M≥~3, M9) — neither lever alone wins —
             and the M8 waste-heat OPEX floor never vanishes. The economic terminal question is
             reopenable down to that M8 asymptote, settled by this spreadsheet not by more physics.
honest_note: normalized order-of-magnitude, structure is the finding not the exact thresholds (L1);
             M8 asymptote-vs-LPP is the one unknown (L2); ignores ecosystem/moat/ramp (L3).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_019 cost-of-ownership conjunction (economic Q3, normalized LPP=1.0)
  LPP baseline = 1.00
  coherent BOTH (eta x4, M=3) = 0.55  -> WIN
  coherent eta-only (M=1)   = 1.35  -> LOSE
  coherent amort-only (eta=1) = 1.00  -> LOSE
  M->inf asymptote = 0.150 = M8 OPEX floor 0.150 (never 0)
  F-COO-1 WIN            PASS
  F-COO-2 ETA-INSUFFICIENT PASS
  F-COO-3 AMORT-INSUFFICIENT PASS
  F-COO-4 CONJUNCTION    PASS
  F-COO-5 M8-FLOOR       PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```
**State output**: `state/h019_cost_of_ownership_2026_06_25/result.json`
