---
id: H_018
slug: erl-bbu-threshold
title: ERL beam-breakup is not the binding wall — an ERL+FEL EUV source needs ~0.2 mA average current, ~100× below the demonstrated HOM-damped BBU threshold (~20 mA); the binding ERL limit is heat/wall-plug, not instability
domain: light-source
status: supported
exploration_method: BBU threshold current vs required current
verification_method: deterministic harness + 4 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
from_metalaw: M4 flux-face · ERL escape (H_016) instability check
---

# H_018 — ERL beam-breakup is not the binding wall

> Closes a flagged risk of the ERL escape (H_016): does beam-breakup (BBU) instability cap the
> recirculating current before it reaches the EUV operating point? No.

## Hypothesis

ERL recirculating current is limited by transverse beam-breakup (BBU) above a threshold I_th. An
ERL+FEL EUV source (Q=100 pC, f=2 MHz for 167 W, H_016) needs only ~0.2 mA average current — ~100×
below demonstrated HOM-damped BBU thresholds (~20 mA). So BBU is not the binding ERL wall; the
binding limit is heat removal / wall-plug (H_016), consistent with the flux-face being an
engineering/economic question.

## Variables (pre-registered)
- Q 100 pC · f 2 MHz · BBU threshold (HOM-damped) 20 mA · without damping 1 mA.

## Run Protocol
- harness: `tool/lumen_optics.evaluate` · run: `state/h018_erl_bbu_threshold_2026_06_25/run_h018.py`
- `python3 .../run_h018.py` · artifacts `.../result.json`.

## Falsifiers
- **F-BBU-1 BELOW**: required current ≥ BBU threshold → BBU caps the ERL (refutes).
- **F-BBU-2 MARGIN**: margin < 10× → not comfortably stable.
- **F-BBU-3 DAMPING**: HOM damping doesn't raise the threshold → the lever is wrong.
- **F-BBU-4 BOUNDS**: any non-positive → ledger bug.

## Honest Limits
- **L1 (threshold representative)**: BBU thresholds depend on cavity HOM spectrum, optics, and
  damping detail; ~20 mA is an order figure from the ERL literature, not this exact machine.
- **L2 (other instabilities exist)**: BBU is one mode; CSR microbunching, ion trapping, and
  HOM heating are separate ERL walls not covered here.
- **L3 (confirms the bottleneck is elsewhere)**: ruling out BBU does not solve the ERL — it
  localizes the binding wall to heat/wall-plug (H_016) and economics (next abstraction peel).

## Cross-Links
- checks: H_016 (ERL escape). binding wall localizes to heat/wall-plug → economic peel.

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: BBU threshold vs required current, 4/4 falsifiers PASS.
  current needed (Q x f) = 0.20 mA · BBU threshold 20 mA · margin 100x
  HOM damping lifts threshold 20x (1->20 mA)
key_finding: BBU instability is NOT the binding ERL wall at EUV-relevant current (~0.2 mA, ~100x
             margin) — the binding limit is heat removal / wall-plug, localizing the terminal
             question to engineering/economics, consistent with H_016.
honest_note: threshold representative (L1); other instabilities exist (L2); ruling out BBU localizes
             but does not solve the ERL wall (L3).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_018 ERL beam-breakup (BBU) is not the binding wall at EUV current
  current needed (Q x f) = 0.20 mA
  BBU threshold (HOM-damped) = 20 mA  -> margin 100x
  HOM damping lifts threshold 20x (1->20 mA)
  -> binding ERL limit is heat/wall-plug (H_016), not BBU instability
  F-BBU-1 BELOW  PASS
  F-BBU-2 MARGIN PASS
  F-BBU-3 DAMPING PASS
  F-BBU-4 BOUNDS PASS
VERDICT: SUPPORTED  (4/4 falsifiers PASS)
```
**State output**: `state/h018_erl_bbu_threshold_2026_06_25/result.json`
