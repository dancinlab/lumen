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
Framing claim                     lumen verdict (19 verified hypotheses)
─────────────────────────         ───────────────────────────────────────
"no alternative beyond EUV"   →   wavelength has NO floor (H_011: λ ~ 1/E²)
                              →   the wall is FLUX, and flux is NOT a physics
                                  ceiling (H_016: reopenable via ERL+FEL)
                              →   the terminal wall is economic, reopenable down
                                  to the M8 waste-heat floor (H_019)
```

- **Wavelength is free.** A compact laser-plasma accelerator + undulator tunes
  13.5 / 6.5 / 5 / 3 nm by an electron-energy dial (H_004/H_006/H_007/H_011) —
  no emitter-element swap (Sn→Gd/Lu/La) + multilayer swap (Mo/Si→La/B) needed.
- **The wall is flux (average power), not wavelength** (H_008/H_005), and flux has
  **no brightness/Liouville ceiling for a coherent source** (H_016) — only
  efficiency + waste-heat (the M8 floor) survive.
- **Front-runner: ERL+FEL** (de-risked, ~200 W compact); **dark horse: a
  recombination EUV laser** (H_017, intrinsically narrow, undulator-free).
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

**Status:** 19 verified 🟢 (all deterministic, 4–5/5 falsifiers PASS) + 10 abstract 🜂.
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
coordinates (🜂), not claims. The one true ceiling found is **M8** — the 2nd-law
waste-heat OPEX floor; whether it sits above or below LPP's all-in cost is the single
remaining decision-relevant unknown.
