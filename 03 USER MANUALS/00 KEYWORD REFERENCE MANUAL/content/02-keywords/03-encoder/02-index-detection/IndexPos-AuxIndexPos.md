---
summary: Records the latest position at which the encoder index was detected.
---
# IndexPos/AuxIndexPos

Records the latest position at which the encoder index was detected.

## Overview

`IndexPos` records the feedback position captured the last time the encoder index (reference mark) was detected. It is only meaningful when the encoder type ([EncType](../01-general-settings/EncType-AuxEncType.md)) is 1 (digital incremental) or 4 (SIN/COS), since only incremental encoders carry an index mark. It is read-only, axis-scope, and not saved to flash. It is typically used in homing, paired with the detection flag [IndexStat](IndexStat-AuxIndexStat.md). `AuxIndexPos` is the auxiliary-encoder counterpart.

## How it works

The index is sampled once per control cycle. At the start of each control interrupt the firmware clears [IndexStat](IndexStat-AuxIndexStat.md) to 0, then tests the index input for the axis. When the index is asserted, it sets `IndexStat` to 1 and latches the current feedback position into `IndexPos`:

- **Standalone controller:** the index line is read from the encoder index input for each axis. On detection, `IndexStat = 1` and `IndexPos = Pos` (the feedback position from the previous sample).
- **Central-i:** the index is carried as a status bit in the per-axis remote message; when that bit is set the same `IndexStat = 1` / `IndexPos = Pos` capture occurs.

The captured value is the feedback position of the *previous* sample rather than the exact sub-sample position of the edge, so the latched value is accurate to within one control cycle. Because detection is polled once per cycle, the index pulse must remain asserted long enough to be seen — see [the section overview](00-overview.md) for the resulting maximum jog speed.

`IndexPos` feeds homing directly. In the "move to index" homing step the firmware sets the absolute target ([AbsTrgt](../../10-motion/13-motion-mode-ptp/AbsTrgt.md)) to the captured index position, so the axis moves precisely to the latched index location.

## AuxIndexPos

`AuxIndexPos` is the auxiliary-encoder counterpart and behaves identically, latching the auxiliary feedback position on an auxiliary index event. Auxiliary index hardware is only wired on single-axis hardware variants; on multi-axis controllers the auxiliary index is not detected (see the note in [the section overview](00-overview.md)).

## Changes between versions

| | v4 | v5 (central-i) |
|---|---|---|
| Stored width | 32-bit | 64-bit |

In **v5** the index position is held as a 64-bit value, matching the wider position counters used elsewhere in that firmware; **v4** stores a 32-bit value. The keyword value and usage are otherwise unchanged. **v5 is central-i only.**

## Examples

```text
AIndexPos           ; read the position of the last detected index
```

## See also

- [IndexStat](IndexStat-AuxIndexStat.md) — flag indicating whether the index has been detected
- [EncType](../01-general-settings/EncType-AuxEncType.md) — encoder type; index detection applies for `EncType=1` or `4`
- [StopOnIndex](../../16-homing/StopOnIndex.md) — stop the axis on the next index pulse
- [00-overview](00-overview.md) — index-detection polling and maximum jog speed
