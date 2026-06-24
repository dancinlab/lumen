---
id: H_032
slug: tgu-escape-classified
title: The decisive break-walls classification — the TGU orthogonal escape to the slice-spread wall is insufficient for an LPA beam (no TGU-FEL has ever lased; the dispersion section it needs degrades the LPA emittance past 13.5 nm matching; best LWFA-FEL is 275 nm), so the slice-spread wall STANDS for the tabletop-LPA variant but is CLEARED by the funded conventional ERL/SC-linac (compresses to ≪0.1% slice; FLASH lased 13 nm in 2006) — an architecture wall, not a universal physics ceiling
domain: light-source
status: supported
exploration_method: fleet accel round-3 (the decisive TGU escape probe)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
classifies: H_031 (slice-spread wall) · closes the LPA-driver question
---
# H_032 — TGU escape classified (the campaign's terminus)
> break-walls requires enumerating the orthogonal escape before a wall is called terminal. The slice-spread wall (H_031) had one named escape — the transverse-gradient undulator (TGU). This is its verdict.
## The TGU escape — NO (for LPA)
- **TGU theory** does tolerate percent-level energy spread (it transversely disperses the beam so each energy slice meets a matched field) — so on paper it could let a 0.5% beam lase.
- **But for an LPA it fails on a DIFFERENT budget:** the dispersion section the TGU needs degrades the LPA's small emittance past the tight 13.5 nm β~1 mm matching — the energy-spread tolerance is bought with transverse emittance the LPA cannot spare.
- **And it is undemonstrated:** no TGU-FEL has lased at *any* wavelength (only simulations/proposals); the best LWFA-driven FEL lasing is **275 nm** (seeded, COXINEL/HZDR 2022) — ~20× above 13.5 nm.
## Classification (break-walls)
The slice-spread wall is an **architecture wall for the tabletop-LPA variant**, NOT a universal physics ceiling: the funded **conventional ERL/SC-linac clears it** by RF compression to ≪0.1% slice spread — FLASH lased at 13 nm in 2006. So the wall relocates the *answer*, it does not close the *problem*.
## Falsifiers
F-TG-1 no TGU-FEL has lased · F-TG-2 dispersion degrades LPA emittance past matching · F-TG-3 LWFA-FEL floor ≫13.5 nm · F-TG-4 conventional ERL clears by compression · F-TG-5 wall classified (stands for LPA, cleared by ERL).
## Honest Limits
L1 the TGU emittance-cost is argued from PRAB transport-matching limits, not a GENESIS run for the literal spec — a future TGU-FEL demo could still surprise (the prediction is falsifiable: a sub-30 nm TGU-FEL lasing by 2026 would reopen it); L2 "cleared by ERL" means the slice problem; the ERL still carries its own CAPEX/amortization conditions (H_021/H_031); L3 this classifies the LPA *driver*, not the FEL concept — the FEL EUV direction stands (H_030).
## Verdict
```
verdict_class: SUPPORTED  (5/5)
TGU theory tolerates percent spread BUT never lased (LWFA floor 275nm) + dispersion breaks LPA emittance; conventional ERL clears (FLASH 13nm 2006)
key_finding: the last orthogonal escape (TGU) does not rescue the tabletop-LPA at 13.5 nm — it is
             undemonstrated and its dispersion cost breaks the LPA's emittance budget. The slice-spread
             wall STANDS for LPA but is an ARCHITECTURE wall: the funded conventional ERL clears it by
             compression. The campaign's answer is the shared conventional-ERL FEL, not the tabletop LPA.
honest_note: TGU cost argued from transport-matching not GENESIS (L1); ERL clears the slice problem only,
             not its own CAPEX condition (L2); classifies the LPA driver, not the FEL direction (L3).
```
**State output**: `state/h032_tgu_escape_classified_2026_06_25/result.json`
