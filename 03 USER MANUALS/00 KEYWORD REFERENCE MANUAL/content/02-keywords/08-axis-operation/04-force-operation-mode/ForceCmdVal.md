---
keyword: ForceCmdVal
summary: Sequence of user-defined force references (units) for force mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 571
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceCmdVal

Sequence of user-defined force references (units) for force mode.

## Overview

`ForceCmdVal` defines a sequence of user-defined force references, in units, applied in force operation mode. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2, and each value is paired with a holding time from [ForceCmdHTime](ForceCmdHTime.md). The active entry is selected by [ForceCmdIndex](ForceCmdIndex.md), and the transition into each value is ramped at [ForceCmdSlope](ForceCmdSlope.md).

The array holds **20 usable entries, indexed 1 to 20**. Index `[0]` is unused (the table is 1-indexed to match the command syntax).

## How it works

While `ForceCmdSrc = 1` or `2`, each cycle the generator reads the entry at [ForceCmdIndex](ForceCmdIndex.md) and ramps the raw force reference toward `ForceCmdVal[ForceCmdIndex]` at [ForceCmdSlope](ForceCmdSlope.md) units/second (`AG300_CTL01ControlLoops.c:1155`). Once the raw reference equals the target value, the holding timer [ForceCmdCntr](ForceCmdCntr.md) begins counting against [ForceCmdHTime](ForceCmdHTime.md). When the hold time elapses, [ForceCmdIndex](ForceCmdIndex.md) advances to the next entry (`AG300_CTL01ControlLoops.c:1314`).

The sequence end is governed entirely by [ForceCmdHTime](ForceCmdHTime.md): a `0` hold time exits force mode and returns to position mode at that entry; a negative hold time holds that value indefinitely. If the index reaches the last array element (20) with a positive hold time, the axis holds that last value indefinitely rather than rolling over (`AG300_CTL01ControlLoops.c:1320`). See [Force operation mode](00-overview.md) for fully worked sequence examples.

## Examples

```text
AForceCmdVal[1]=340  ; first force reference (units)
AForceCmdVal[2]=-260 ; second force reference (units)
```

## See also

- [ForceCmdHTime](ForceCmdHTime.md) — holding time paired with each value
- [ForceCmdIndex](ForceCmdIndex.md) — active table entry
- [ForceCmdSlope](ForceCmdSlope.md) — ramp rate between entries
- [ForceCmdSrc](ForceCmdSrc.md) — selects this table as the source
