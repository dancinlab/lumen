---
id: H_005
slug: hvm-throughput-floor
title: HVM throughput floor — high-volume manufacturing needs ≥100 WPH, but at the same source 6.5 nm delivers ~14× fewer photons (H_002), so it manages only ~11 WPH, an order of magnitude below the floor
domain: system
status: supported
exploration_method: throughput ∝ source-power model, chained to H_002
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-24
deterministic: true
llm: none
---

# H_005 — HVM throughput floor

## Hypothesis

High-volume manufacturing (HVM) needs a wafer-per-hour (WPH) throughput floor
(~100 WPH; 150–180 cited). At fixed dose, throughput scales with in-band source
power reaching the wafer. Because a 6.5 nm column passes ~14× fewer photons at
the same source (H_002), its effective throughput drops to ~1/14 — about 11 WPH,
an order of magnitude below the floor. The claim: the 6.5 nm wall is not only a
power-budget wall (H_001) but a **throughput** wall — even a working 6.5 nm
exposure is economically dead at the same source.

## Why

- Transcript `state/euv-yt-2KDLZMG8FAs-transcript.md`: HVM needs "적어도 100개
  정도" (≥100 WPH); the LDP path manages "1분의 한 장 만들기도 어려워" → the
  ASML-vs-China gap is framed as ~5만 vs ~500 wafers/month (~100×).
- Completes the H_002 → H_001 chain with the *economic* axis: photons lost in the
  optics (H_002) show up as wafers-not-printed per hour here.

## Variables (pre-registered)

- HVM floor = 100 WPH · ref source = 250 W (H_001 baseline) · ref throughput =
  150 WPH @ 250 W (representative 13.5 nm HVM) · H_002 multiplier (R 0.70→0.55, N=11).

## Run Protocol

- **harness**: `tool/lumen_optics.py` (`hvm_throughput_wph`, `source_power_multiplier`).
- **run script**: `state/h005_hvm_throughput_floor_2026_06_24/run_h005.py`.
- **run cmd**: `python3 state/h005_hvm_throughput_floor_2026_06_24/run_h005.py`
- **artifacts**: `state/h005_hvm_throughput_floor_2026_06_24/result.json`.

## Criteria

- **verdict_rule**: SUPPORTED = all 5 falsifiers PASS; FALSIFIED = any trigger.

## Falsifiers (pre-registered, measurable)

- **F-WPH-1 BASELINE**: 13.5 nm WPH < floor → calibration wrong (incumbent IS in HVM).
- **F-WPH-2 SHORTFALL**: 6.5 nm WPH ≥ floor → no throughput wall (refutes hypothesis).
- **F-WPH-3 MONOTONE**: 13.5 nm WPH ≤ 6.5 nm WPH → photon→throughput link broken.
- **F-WPH-4 POWER-GAP**: power to restore the floor ≤ today's WPH-equivalent → no real gap.
- **F-WPH-5 BOUNDS**: any WPH/power ≤ 0 → ledger bug.

## Honest Limits

- **L1 (linear throughput model)**: WPH ∝ source power assumes fixed dose, scan
  speed, and field overhead; real WPH also depends on stage/scan and dose margin.
- **L2 (ref WPH representative)**: 150 WPH @ 250 W is a representative 13.5 nm HVM
  calibration, not a vendor figure (transcript gives the floor, not the curve).
- **L3 (inherits H_002 limits)**: the 14× factor carries H_002's representative
  R/N (L1–L5). A different R_beuv shifts the shortfall.
- **L4 (same-source framing)**: assumes the 6.5 nm source delivers the same raw
  power as today; a far brighter source (H_001 ceiling / H_004 path) changes the
  arithmetic — this card isolates the optics-throughput coupling.

## Cross-Links

- **transcript**: `state/euv-yt-2KDLZMG8FAs-transcript.md` (100 WPH floor, LDP gap).
- **sister H**: H_002 (photon loss → this throughput loss) · H_001 (power supply) ·
  H_004 (a brighter compact source as the way around this floor).
- **state notes**: `light-source-paths.md` (throughput is the stated wall).
- **harness**: `tool/lumen_optics.hvm_throughput_wph`.

## Verdict

Pre-register-frozen + runnable harness executed 2026-06-24.

```
verdict_class: SUPPORTED
evidence_summary: throughput∝power chained to H_002, 5/5 falsifiers PASS.
  13.5nm @ 250 W = 150.0 WPH  (floor 100)
  6.5nm @ same source = 10.6 WPH  (1/14.2 photons)
  source power to restore floor at 6.5nm = 2366 W
key_finding: at the same source, 6.5 nm prints only ~11 WPH — an order of
             magnitude below the ~100 WPH HVM floor — so the 6.5 nm wall is a
             throughput/economics wall, not just a power-budget one; restoring
             the floor needs ~2.4 kW, beyond the LPP ceiling of H_001.
honest_note: linear throughput model (L1); ref WPH representative (L2); inherits
             H_002 representative R/N (L3); isolates optics→throughput at fixed
             source — a brighter source (H_001 ceiling / H_004) reopens it (L4).
```

### Run verdict (VERBATIM — `python3 run_h005.py` stdout 2026-06-24)

```
H_005 HVM throughput floor (100 WPH) vs 6.5 nm
  13.5nm @ 250 W = 150.0 WPH  (floor 100)
  6.5nm @ same source = 10.6 WPH  (1/14.2 photons)
  source power to restore floor at 6.5nm = 2366 W
  F-WPH-1 BASELINE PASS
  F-WPH-2 SHORTFALL PASS
  F-WPH-3 MONOTONE PASS
  F-WPH-4 POWER-GAP PASS
  F-WPH-5 BOUNDS   PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```

**State output**: `state/h005_hvm_throughput_floor_2026_06_24/result.json`
