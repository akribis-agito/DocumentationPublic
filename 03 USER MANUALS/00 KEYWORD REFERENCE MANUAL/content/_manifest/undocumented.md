# Undocumented keywords

This list is the set of mnemonics present in `Params.c` (LTS/v4 ∪ develop/v5) that have **no
controller-keyword doc page**, after the v5 gap-fill pass.

**Genuine documentation gaps: none.** Every controller firmware keyword now has a page.

The keywords below are **intentionally excluded** — they are host/PC-tool–driven or internal
tokens, not controller keywords a customer programs against:

| Keyword | Category | Reason excluded |
| --- | --- | --- |
| DownloadDraw, DrawErase, DrawExecTime, DrawIdle, DrawInfo, DrawMemories, DrawMode, DrawParams, DrawRunBack, DrawSignals, DrawStat | DrawControl subsystem | Driven by the PC-tool DrawControl feature; document as part of a DrawControl feature guide rather than the keyword reference. |
| ScopeAbout, ScopeGap, ScopeOn, ScopeParams, ScopeStatus, ScopeUpload | Scope recording subsystem | New high-rate "Scope" recording path used by the PC tool; document with the recording feature. |
| Print | User-program output | Host/UPL-compiler print directive. |
| AnyVariable | DrawControl indirect read | Host-side indirect-variable token. |
| GPTemp | Internal | General-purpose scratch/temporary. |
| ZDoNotUse, ZZZZZZZZZZZZZ | Sentinels | Table placeholders / terminators; not real keywords. |
| MyPlayground | Internal | Development scratch keyword. |
| CiOfflineSend | Duplicate spelling | Same can_code-502 command as the documented `CIOfflineSend` (the firmware table carries both spellings across product blocks). |

Notes:
- `UPMCalcCoeff` and `UPMRptRange` are documented under `03-special-features/upm/` (the older
  simple-style UPM family), not under `02-keywords/`, so a `02-keywords`-only scan will still
  report them as "undocumented" — they are in fact documented.
- The `keyword-docgen` manifest generator matches docs by exact filename stem under
  `02-keywords/` only, so it over-reports keywords documented in combined `A-B.md` files, in
  `03-special-features/`, or in `05-legacy-keywords/`. This hand-maintained list reflects the
  true state.
