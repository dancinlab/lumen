---
id: H_010
slug: synchrotron-vs-lpa
title: Synchrotron vs compact LPA — a storage-ring source meets HVM throughput but costs ~4 EUV-tools and ~200× the footprint; the compact LPA inverts it (tiny footprint, flux wall) — the trade is footprint ↔ throughput
domain: light-source
status: supported
exploration_method: footprint / cost / average-power comparison
verification_method: deterministic harness + 4 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_010 — synchrotron vs compact LPA

## Hypothesis

The two accelerator-based EUV routes sit at opposite corners of one trade. A
storage-ring synchrotron (Pohang-class) has ample quasi-CW average power → meets
the HVM throughput floor, but costs ~1.5 B$ (~4 High-NA EUV tools) and a
gymnasium-scale footprint (~200× the compact source). The compact LPA inverts it:
tiny footprint, but the flux wall (H_008). The claim: neither path is free — the
accelerator landscape is a **footprint ↔ throughput** trade, and the lumen
question is which corner is least blocked.

## Why

- Frames the two `light-source-paths.md` accelerator rows against each other with
  the transcript's own numbers (synchrotron ≈ "a generation or two" of EUV cost).
- Tells the design which wall to attack: shrink the synchrotron, or raise LPA flux.

## Variables (pre-registered, representative)

- synchrotron footprint 1e4 m² · LPA 50 m² · synchrotron cost 1.5 B$ · EUV tool
  0.35 B$ · HVM requirement 167 W · synchrotron avg power 500 W · LPA 1 W (H_008).

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`evaluate`, `Falsifier`).
- **run script**: `state/h010_synchrotron_vs_lpa_2026_06_24/run_h010.py`.
- **run cmd**: `python3 state/h010_synchrotron_vs_lpa_2026_06_24/run_h010.py`
- **artifacts**: `state/h010_synchrotron_vs_lpa_2026_06_24/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-SYN-1 FOOTPRINT**: synchrotron/LPA footprint < 100× → no LPA size advantage.
- **F-SYN-2 COST**: synchrotron cost ∉ [1, 10] EUV-tools → transcript framing off.
- **F-SYN-3 TRADE**: NOT (synchrotron meets HVM power AND LPA does not) → no trade.
- **F-SYN-4 BOUNDS**: any ratio ≤ 0 → ledger bug.

## Honest Limits

- **L1 (order-of-magnitude figures)**: footprint, cost, and average powers are
  representative public-order values; the *trade direction* is robust, the exact
  ratios are not vendor figures.
- **L2 (synchrotron throughput optimistic)**: a storage ring feeds many beamlines;
  dedicating enough EUV-band flux to a litho cluster at HVM dose is itself a wall
  not captured by the single avg-power number.
- **L3 (compact-synchrotron middle ground)**: compact storage rings / SR-on-a-chip
  efforts sit between the two corners and could move the trade (break-walls).
- **L4 (footprint vs the fab)**: the transcript note that several synchrotrons may
  exceed the fab's own area is the real economic objection, only sketched here.

## Cross-Links

- **sister H**: H_008 (LPA flux wall = why LPA loses throughput) · H_004 (compact
  gradient = why LPA wins footprint) · H_005 (the WPH floor both are judged by).
- **state notes**: `light-source-paths.md` (synchrotron + compact-LPA rows).
- **transcript**: `euv-yt-2KDLZMG8FAs-transcript.md` (stadium-scale, ~1.5–2 jo cost).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: footprint/cost/power comparison, 4/4 falsifiers PASS.
  footprint: 1e4 m^2 vs 50 m^2 = 200x
  cost: 1.5 B$ = 4.3 High-NA EUV tools
  HVM 167 W: synchrotron meets=True, LPA meets=False
key_finding: the accelerator landscape is a footprint<->throughput trade —
             a storage ring meets HVM power but costs ~4 EUV tools and ~200x the
             footprint; the compact LPA wins footprint but hits the flux wall
             (H_008). Neither corner is free; the design choice is which wall to
             break (shrink the ring, or raise LPA flux).
honest_note: order-of-magnitude figures (L1); synchrotron throughput optimistic —
             beamline sharing not modeled (L2); compact-storage-ring middle ground
             could shift the trade (L3); fab-area objection only sketched (L4).
```

### Run verdict (VERBATIM — `python3 run_h010.py` stdout 2026-06-24)

```
H_010 synchrotron vs compact LPA — footprint <-> throughput trade
  footprint: synchrotron 10000 m^2 vs LPA 50 m^2 = 200x
  cost: synchrotron 1.5 B$ = 4.3 High-NA EUV tools
  HVM power (167 W): synchrotron meets=True  LPA meets=False
  F-SYN-1 FOOTPRINT PASS
  F-SYN-2 COST     PASS
  F-SYN-3 TRADE    PASS
  F-SYN-4 BOUNDS   PASS
VERDICT: SUPPORTED  (4/4 falsifiers PASS)
```

**State output**: `state/h010_synchrotron_vs_lpa_2026_06_24/result.json`
