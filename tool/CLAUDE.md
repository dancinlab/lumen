# tool — shared runnable harness for HYPOTHESES

Repo-root machinery that `HYPOTHESES/` hypothesis cards run against. Anima-parity:
shared, reusable code lives here in `tool/`; per-hypothesis run scripts and their
`result.json` live under `state/<hX>_.../` and import from here.

## Key files

- `lumen_optics.py` — deterministic, stdlib-only (`math`) physics primitives for
  the EUV / sub-13.5 nm source problem:
  - `mirror_chain_throughput(R, N)` — all-reflective column throughput `R**N`.
  - `source_power_multiplier(r_ref, r_new, N)` — power penalty of a lower-R band.
  - `resolution_half_pitch(k1, λ, NA)` / `depth_of_focus(k2, λ, NA)` — the NA↔DoF trade.
  - `lpp_source_power(f_rep, E_pulse, CE, collection)` — LPP in-band power budget.
  - `Falsifier` + `evaluate(metrics, falsifiers)` — pre-registered falsifier ledger.

## Rules

- **No hidden constants / fitting** — every input is explicit and documented so a
  card's falsifiers evaluate against returned numbers.
- **Deterministic** — no randomness, no network, $0 local. Same input → same output.
- **Pure & reusable** — functions here are shared across cards; hypothesis-specific
  parameters belong in the `state/<hX>/run_*.py` script, not here.

## Gotcha

- Import path: run scripts insert `tool/` on `sys.path` via a repo-root-relative
  path, so they run from anywhere (`python3 state/<hX>/run_*.py`).
