---
summary: Flag indicating whether the encoder index pulse has been detected.
---
# IndexStat/AuxIndexStat

Flag indicating whether the encoder index pulse has been detected.

## Overview

`IndexStat` indicates whether the encoder index pulse was seen on the most recent control cycle: `0` means not detected, `1` means detected. It is only meaningful when the encoder type ([EncType](../01-general-settings/EncType-AuxEncType.md)) is 1 (digital incremental) or 4 (SIN/COS), as only incremental encoders carry an index mark. It is read-only, axis-scope, and not saved to flash. When the index is detected, the controller latches the feedback position into [IndexPos](IndexPos-AuxIndexPos.md) and raises this flag — commonly used in homing. `AuxIndexStat` is the auxiliary-encoder counterpart.

## How it works

`IndexStat` is re-evaluated every control cycle. At the top of each control interrupt the firmware first assumes no index (`IndexStat = 0`), then tests the index input; if asserted it sets `IndexStat = 1` and captures [IndexPos](IndexPos-AuxIndexPos.md) (from the dedicated index input on a standalone controller, or from the per-axis status bit on central-i). Because the flag is cleared at the start of every cycle, it reflects the *current* cycle only — it is not latched until cleared by the user. A consumer that needs to act on a single index event (such as homing) reads it within the cycle it is set.

| IndexStat | Meaning |
|---|---|
| 0 | Index not detected this control cycle |
| 1 | Index detected this control cycle |

The flag drives two firmware features:

- **Stop on index** ([StopOnIndex](../../16-homing/StopOnIndex.md)): during a jog/joystick move, if `StopOnIndex` is set and `IndexStat` is 1, the profiler issues a stop request and reports motion-reason "index".
- **Homing / commutation:** homing steps reference the index via `IndexStat`/`IndexPos`; for the Hall-plus-index commutation method the firmware waits for `IndexStat` to set the commutation angle to zero.

## AuxIndexStat

`AuxIndexStat` is the auxiliary-encoder counterpart with the same 0/1 meaning. Auxiliary index hardware is only present on single-axis hardware variants; on multi-axis controllers the auxiliary index is not detected (see [the section overview](00-overview.md)).

## Examples

```text
AIndexStat          ; check whether the index was detected this cycle
```

## See also

- [IndexPos](IndexPos-AuxIndexPos.md) — position captured when the index is detected
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; index detection applies for `EncType=1` or `4`
- [StopOnIndex](../../16-homing/StopOnIndex.md) — stop the axis on the next index pulse
- [00-overview](00-overview.md) — index-detection polling and maximum jog speed
