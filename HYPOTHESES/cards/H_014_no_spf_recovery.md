---
id: H_014
slug: no-spf-recovery
title: No-SPF in-band recovery — an intrinsically narrow source drops the spectral-purity filter a broadband LPP needs, recovering ~43% in-band power; narrow is required (broadband exceeds the out-of-band tolerance) — promotes abstract H_B1
domain: light-source
status: supported
exploration_method: SPF transmission audit (narrow vs broadband)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
promoted_from: H_B1
---

# H_014 — no-SPF in-band recovery

> **Promotion of 🜂 H_B1.** The runnable core (SPF transmission audit) is now verified.

## Hypothesis

A broadband LPP keeps a spectral-purity filter (SPF) that throws away ~30% of in-band power to
block out-of-band/IR. An intrinsically narrow source (recombination laser, H_B4) has negligible
out-of-band content, so it can drop the SPF and recover that power — ~43% (= 1/0.70) more delivered
in-band at equal raw source power. The recovery *requires* a narrow line: a broadband source without
an SPF exceeds the wafer/optics out-of-band tolerance.

## Why

- Cheapest near-term system-level flux recovery — no brighter source, just stop discarding photons.
- Couples the source-side escape (H_B4 narrow laser) to a concrete delivered-power gain.

## Variables (pre-registered, representative)

- SPF transmission 0.70 · broadband OOB 0.15 · narrow OOB 0.001 · OOB tolerance 0.02.

## Run Protocol

- **harness**: `tool/lumen_optics.spf_recovery`.
- **run script**: `state/h014_no_spf_recovery_2026_06_25/run_h014.py`.
- **run cmd**: `python3 state/h014_no_spf_recovery_2026_06_25/run_h014.py`
- **artifacts**: `state/h014_no_spf_recovery_2026_06_25/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-SPF-1 RECOVER**: recovery < 1.25× → not a meaningful in-band recovery.
- **F-SPF-2 NARROW-REQ**: narrow can't skip SPF OR broadband can → the recovery doesn't need a narrow line.
- **F-SPF-3 MONOTONE**: worse SPF loss doesn't raise recoverable power → model bug.
- **F-SPF-4 NO-FREE-LUNCH**: recovery > 1/transmission → over-claim.
- **F-SPF-5 BOUNDS**: recovery ≤ 1 or transmission ∉ (0,1] → ledger bug.

## Honest Limits

- **L1 (SPF loss representative)**: ~30% is an order figure; the *direction* is robust, the magnitude
  varies with the actual filter stack.
- **L2 (recovery, not generation)**: like H_012 this multiplies *delivered* flux; it does not lift the
  source's average power (H_008) — it stops discarding the watts you already make.
- **L3 (depends on a narrow source existing)**: the whole gain is conditional on H_B4 (a narrow EUV
  laser) being real — itself unverified.
- **L4 (OOB tolerance representative)**: the 2% OOB tolerance is a stand-in for real spectral-purity
  spec; a stricter spec narrows which sources qualify.

## Cross-Links

- **promotes**: H_B1. **depends on**: H_B4 (narrow source). **complements**: H_012 (also recovery), H_008 (still need power).
- harness: `spf_recovery`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-25.

```
verdict_class: SUPPORTED
evidence_summary: SPF transmission audit, 5/5 falsifiers PASS.
  broadband SPF transmission 0.70 -> narrow recovers 1.429x (43%)
  narrow OOB 0.001 <= tol 0.02 (skip SPF); broadband OOB 0.15 > tol (must keep)
key_finding: an intrinsically narrow source recovers ~43% in-band power by dropping
             the spectral-purity filter a broadband LPP cannot — a cheap near-term
             system-level gain, conditional on a narrow source (H_B4) existing.
             Recovery, not generation (flux wall H_008 untouched).
honest_note: SPF loss representative (L1); recovery not generation (L2); conditional
             on H_B4 (L3); OOB tolerance representative (L4).
```

### Run verdict (VERBATIM — `python3 run_h014.py` stdout 2026-06-25)

```
H_014 no-SPF in-band recovery (promotes H_B1)
  broadband SPF transmission 0.7 -> narrow recovers 1.429x (43%)
  narrow OOB 0.001 <= tol 0.02: skip SPF = True
  broadband OOB 0.15 > tol: must keep SPF = True
  F-SPF-1 RECOVER    PASS
  F-SPF-2 NARROW-REQ PASS
  F-SPF-3 MONOTONE   PASS
  F-SPF-4 NO-FREE-LUNCH PASS
  F-SPF-5 BOUNDS     PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h014_no_spf_recovery_2026_06_25/result.json`
