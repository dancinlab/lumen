# lumen

Engineering stable light sources for bands nature does not supply — starting from
**EUV (13.5 nm)** for semiconductor lithography, generalizing to any hard-to-generate
wavelength lacking a stable natural emitter. The scope is the **source problem**, not
one wavelength: EUV is the first instance, not the boundary.

## The answer (current campaign conclusion)

> *"Is there really no path beyond 13.5 nm EUV?"* — the framing question (from a
> Korean EUV analysis, Prof. Kwon Seok-jun) said there is "no clear technical
> alternative." lumen's verified-hypothesis lab reached a different conclusion:

**The next-generation source problem is not a wavelength impossibility — it is an
engineering / volume problem, reopenable down to one thermodynamic floor.**

```
Framing claim                     lumen verdict (32 verified hypotheses)
─────────────────────────         ───────────────────────────────────────
"no alternative beyond EUV"   →   wavelength has NO floor (H_011: λ ~ 1/E²)
                              →   the wall is FLUX, and flux is NOT a physics
                                  ceiling (H_016: reopenable via ERL+FEL)
                              →   the terminal wall is economic, reopenable down
                                  to the M8 waste-heat floor (H_019)
```

- **Wavelength has no *physics* floor** (H_011: λ ~ 1/E²) — an accelerator + undulator
  tunes 13.5 / 6.5 / 5 / 3 nm by an electron-energy dial (H_004/H_006/H_007), no
  emitter-element swap (Sn→Gd/Lu/La) + multilayer swap (Mo/Si→La/B) needed. **But the dial
  is bounded by beam *slice energy spread*** (H_031/032): only a beam compressed to ≪0.1%
  slice lases at 13.5 nm — which a conventional ERL achieves (FLASH, 2006) but a raw ~0.5%
  LPA beam does not (demonstrated LPA-FEL floor ~25 nm). **Breakthrough (H_033):** that
  slice-spread wall is *FEL-specific* — **inverse-Compton scattering** sidesteps it (no gain
  condition), reaching 13.5 nm with only **~2.2 MeV** (≈455× less beam energy), slice spread
  merely broadening the line; the compact path reopens, the wall relocating to *flux*
  (reopenable, H_016). Honest residual: ICS-EUV at litho power is undemonstrated.
- **The wall is flux (average power), not wavelength** (H_008/H_005), and flux has
  **no brightness/Liouville ceiling for a coherent source** (H_016) — only
  efficiency + waste-heat (the M8 floor) survive.
- **The answer: an accelerator-driven FEL EUV source — and, after a full real-data
  reference-match (H_030/031/032), its funded and physically-coherent form is a SHARED
  CONVENTIONAL energy-recovery linac (ERL) FEL amortized across many scanners (the
  xLight/KEK shape), NOT the tabletop laser-plasma (LPA) module-array first emphasized.**
  Why the relocation: (1) the funded driver is a conventional ERL — zero funded programs
  use an LPA driver (H_030); (2) the win is **M9-amortization** (one ~$260 M / 10 kW source
  → ~$26 M/scanner at fan-out ~10, ~8× < LPP; it *inverts* at N=1), not the **M7
  module-learning** curve, whose cryomodule Wright slope is shallow ~0.95 (H_031); (3) the
  wavelength "dial" is bounded by **slice energy spread** — a real ~0.5% LPA beam sits ~5×
  over the FEL gain criterion, single-pass cooling is undemonstrated, dechirping is not
  cooling, and the last orthogonal escape (a transverse-gradient undulator) is undemonstrated
  and breaks the LPA emittance budget (H_032); demonstrated LPA-FEL floor ~25–27 nm, never
  13.5 nm. The conventional ERL clears that slice wall by RF compression (FLASH lased 13 nm,
  2006). The LPA combination (H_022) stays a coherent **longer-horizon** variant; the concept
  itself is not novel (Nakajima 2014).
- **Economics is a conjunction** (H_019): a compact coherent source beats LPP
  $/wafer-layer only with efficiency η ≥ ~4× *and* amortization across ≥ ~3
  scanners — neither lever alone — and never below the M8 waste-heat floor.

## How the lab works (HYPOTHESES system)

Modeled on anima's `UNIVERSE/`: **pre-register → falsify → run → verbatim verdict**,
with all shared physics in a single deterministic harness.

```
[ HYPOTHESES/cards/H_*.md ] ─pre-registered + ≥5 falsifiers─▶ [ tool/lumen_optics.py ]
        │                                                            │ deterministic, stdlib-only
        └── registry [ HYPOTHESES/REGISTRY.jsonl ] ◀─verbatim verdict─┴─▶ [ state/hX/run.py → result.json ]
```

- `HYPOTHESES/REGISTRY.jsonl` — one JSON line per hypothesis (id · tier · verdict · artifacts).
- `HYPOTHESES/cards/H_*.md` — verified `H_0xx` (🟢, run to verdict) and abstract
  `H_A*/H_B*` (🜂, unverified conjecture with a falsifiable prediction, **tier-separated**).
- `tool/lumen_optics.py` — shared physics harness (mirror throughput, NA↔DoF, LPP
  power, undulator/inverse-Compton, ERL, cost-of-ownership, falsifier ledger).
- `state/` — per-hypothesis runs + result.json, pillar notes, brainstorms, meta-laws.

**Status:** 33 verified 🟢 (all deterministic, 4–6/5 falsifiers PASS) + 10 abstract 🜂. Key inputs
are **sourced against published data** (`state/sourced-parameters.md`, H_026): the core values are
real (optics R, LPP power, ~0.02% wall-plug, EUV-tool CAPEX), with three optimistic links honestly
corrected (all "harder, not easier"). The three self-found weaknesses (integration, the thin FEL
margin, module replicability) are each attacked by ≥3 independent break-walls lenses (H_027/028/029)
— reopenable, not terminal, though not retired (each lens names an escape, not a build).
The abstraction lane peeled meta-laws **M1–M9** (`state/euv-meta-laws.md`); the fleet
loop closed three times (a frozen meta-law prediction → a verified hypothesis: P4→H_013,
flux-verdict→H_016, Q3→H_019).

## Run it

```bash
python3 state/<hX>_<slug>_<date>/run_*.py     # run any hypothesis (deterministic, $0 local)
python3 serve.py                              # view ARCHITECTURE.json in a browser
```

## Layout

```
lumen/
├─ HYPOTHESES/          — verification lab (REGISTRY.jsonl + cards/ + CLAUDE.md)
├─ tool/                — shared runnable physics harness (lumen_optics.py)
├─ state/               — per-hypothesis runs · pillar notes · meta-laws · brainstorms
├─ ARCHITECTURE.json    — design SSOT (JSON tree · architecture.html viewer)
└─ CHANGELOG.md         — history (append-only)
```

## Honesty note

Verified `H_0xx` are closed-form public-physics relations with representative
parameters (each card lists its honest limits); they bound *requirements and
scaling*, not vendor performance. Abstract `H_A*/H_B*` and meta-laws are unverified
coordinates (🜂), not claims.

**Funded-reality reference-match (H_030, the strongest honesty check):** the
accelerator-driven FEL EUV direction is **real and funded** — xLight (≤$150M CHIPS LOI,
2028 prototype, one source → ~20 scanners) and KEK (10 kW ERL EUV-FEL) — validating
lumen's direction. But three honest corrections land: the funded **driver is a
conventional ERL, not the tabletop LPA** this campaign emphasized; the funded **economic
lever is M9-amortization (shared source across scanners), not the M7 module-array**; and
**13.5 nm-on-LPA + single-pass cooling are undemonstrated** (LPA-FEL floor ~25 nm). The
concept predates lumen (Nakajima 2014) — the synthesis is **not novel**. The robust
restatement of the answer is **xLight-shaped (a shared conventional-ERL FEL amortized
across many scanners)**, with the tabletop-LPA + module-array + cooling form as the
longer-horizon, less-proven variant.

**Where the terminal wall actually sits (settled, H_020):** the one true *physical*
ceiling is **M8** (the 2nd-law waste-heat floor) — but with real-units cost-of-ownership
it is only **~0.5% of LPP cost-of-ownership**, economically negligible. The binding wall
is **CAPEX-per-wafer** — attacked by **M7** (learning curve / mass-produced modules) and
**M9** (amortization across scanners). Not wavelength, not flux, not waste-heat: the
next-generation source problem is, at bottom, a **CAPEX / volume** question.
