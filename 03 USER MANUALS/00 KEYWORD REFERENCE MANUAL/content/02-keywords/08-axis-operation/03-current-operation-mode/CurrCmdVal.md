---
keyword: CurrCmdVal
summary: Sequence of user-defined current references (mA) for current mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 331
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrCmdVal

Sequence of user-defined current references (mA) for current mode.

## Overview

`CurrCmdVal` defines a sequence of user-defined current references, in milliamperes, applied in current operation mode. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 1 or 2, and each value is paired with a holding time from [CurrCmdHTime](CurrCmdHTime.md). The active entry is selected by [CurrCmdIndex](CurrCmdIndex.md), and transitions between entries can be ramped with [CurrCmdSlope](CurrCmdSlope.md).

## Examples

```text
ACurrCmdVal[1]=364   ; first current reference (mA)
ACurrCmdVal[2]=-500  ; second current reference (mA)
```

## See also

- [CurrCmdHTime](CurrCmdHTime.md) — holding time paired with each value
- [CurrCmdIndex](CurrCmdIndex.md) — active table entry
- [CurrCmdSlope](CurrCmdSlope.md) — ramp rate between entries
- [CurrCmdSrc](CurrCmdSrc.md) — selects this table as the source
