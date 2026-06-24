---
id: H_008
slug: accelerator-flux-wall
title: Accelerator-source flux wall — at present LPA rep rates the undulator's average in-band EUV power is ~10³–10⁵× below the ~167 W that 100 WPH HVM needs; the compact path is flux-limited, not wavelength-limited
domain: light-source
status: supported
exploration_method: average-power budget (rep-rate × pulse energy) vs HVM requirement
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_008 — accelerator-source flux wall

## Hypothesis

H_004/H_006/H_007 show the compact accelerator reaches the right *wavelength*
cheaply. This card states the honest counter-wall: HVM needs ~167 W in-band for
100 WPH (H_005), but an LPA-undulator average power = rep-rate × per-pulse EUV
energy. At today's ~kHz LPA rep rates (~µJ/pulse) that is ~mW — a 10³–10⁵× gap.
The compact accelerator path is **flux/average-power limited**, not wavelength
limited; rep-rate is the binding constraint (LPP runs at 50–100 kHz; LPA does not).

## Why

- Balances the chain: H_004/H_006/H_007 are rosy on wavelength/compactness; the
  real reason LPA-driven EUV is not in fabs is average power, so it must be stated.
- Couples to H_005 (throughput) and H_009 (energy spread further cuts in-band flux).

## Variables (pre-registered, representative — see L1)

- HVM 100 WPH → ~167 W (H_005 calibration) · LPA now 1 kHz × 1 µJ · pushed 100 kHz.

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`power_for_throughput`, `average_power`).
- **run script**: `state/h008_accelerator_flux_wall_2026_06_24/run_h008.py`.
- **run cmd**: `python3 state/h008_accelerator_flux_wall_2026_06_24/run_h008.py`
- **artifacts**: `state/h008_accelerator_flux_wall_2026_06_24/result.json`.

## Falsifiers (pre-registered, measurable)

- **F-FLX-1 WALL**: LPA avg power ≥ HVM requirement → no flux wall (refutes).
- **F-FLX-2 SEVERE**: gap < 100× → not an order-of-magnitude wall.
- **F-FLX-3 REP-LEVER**: ~100× rep-rate alone clears the requirement → trivial fix.
- **F-FLX-4 MONOTONE**: higher rep rate ≤ lower → power model broken.
- **F-FLX-5 BOUNDS**: any power ≤ 0 → ledger bug.

## Honest Limits

- **L1 (per-pulse EUV energy representative)**: 1 µJ/shot in-band is an order-of-
  magnitude figure; real LPA-undulator yields vary, but the gap (10³–10⁵×) is so
  large the conclusion (a wall) is robust to plausible values.
- **L2 (rep-rate is the live frontier)**: high-average-power / high-rep LPA is an
  active research direction; this card is a snapshot wall (break-walls: investment/
  horizon class, reopenable), not a physical ceiling.
- **L3 (single-undulator)**: multi-undulator / recirculation / FEL gain could lift
  per-shot photon yield; not modeled.
- **L4 (couples to H_009)**: energy-spread broadening (H_009) reduces the *in-band*
  fraction further, so the effective gap is worse than this average-power figure.

## Cross-Links

- **sister H**: H_005 (the WPH→power requirement) · H_009 (in-band fraction) ·
  H_010 (synchrotron meets this power; LPA does not) · H_004/H_006/H_007 (the
  wavelength/compactness wins this wall qualifies).
- **harness**: `tool/lumen_optics.py` (`average_power`, `power_for_throughput`).

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: average-power budget vs HVM requirement, 5/5 falsifiers PASS.
  HVM requires ~167 W in-band (100 WPH)
  LPA now (1 kHz x 1 µJ) = 1.0 mW  (gap 166667x)
  LPA pushed (100 kHz)   = 0.1 W   (gap 1667x)
key_finding: the compact-accelerator EUV source is flux/average-power limited —
             ~10^3–10^5x below the HVM requirement at present and even pushed rep
             rates — so its real wall is brightness/rep-rate, NOT wavelength
             (which H_004/H_006/H_007 already win). Honest counterweight.
honest_note: per-pulse EUV energy representative (L1); rep-rate is the live
             research frontier so this is a reopenable horizon wall (L2);
             multi-stage/FEL gain not modeled (L3); H_009 makes it worse (L4).
```

### Run verdict (VERBATIM — `python3 run_h008.py` stdout 2026-06-24)

```
H_008 accelerator-source flux / average-power wall
  HVM requires ~167 W in-band (for 100 WPH)
  LPA now (1e+03 Hz x 1 µJ) = 1.000 mW  (gap 166667x)
  LPA pushed (1e+05 Hz) = 0.100 W  (gap 1667x)
  F-FLX-1 WALL     PASS
  F-FLX-2 SEVERE   PASS
  F-FLX-3 REP-LEVER PASS
  F-FLX-4 MONOTONE PASS
  F-FLX-5 BOUNDS   PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h008_accelerator_flux_wall_2026_06_24/result.json`
