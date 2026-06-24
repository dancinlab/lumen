# lumen

Engineering light sources that nature does not provide stably — starting from EUV
(13.5 nm extreme ultraviolet for semiconductor lithography), generalizing to any
hard-to-generate band where no stable natural emitter exists.

## Structure

```
lumen/
├─ src/              — source code
├─ state/            — all work artifacts (experiments · bench · verification), git-tracked
├─ ARCHITECTURE.json — final architecture SSOT (JSON `children` tree, update-in-place)
├─ architecture.html — human viewer for the JSON (run `python3 serve.py`)
└─ CHANGELOG.md      — history (append-only)
```

## Rules

- Scope is the **source problem**, not one wavelength: EUV is the first instance, not the boundary.
- Artifacts go under `state/` only (commons preserve-state). No scattered report/notes dirs.
- Code/design change → update `ARCHITECTURE.json` in lockstep; log in `CHANGELOG.md`.
- **Research before real measurement (실측전 research).** Before renting compute or running an
  expensive real measurement (DFT / simulation sweep / GPU pod / long bench), do a literature
  research pass FIRST — the answer may already be in the literature, or a cheap proxy may suffice.
  Only spend on real compute after research justifies it.

## Gotchas

- (none yet — fill as the project takes shape)
