---
keyword: ForceCmdVal
summary: Sequence of user-defined force references (units) for force mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ForceCmdVal` defines a sequence of user-defined force references, in units, applied in force operation mode. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2, and each value is paired with a holding time from [ForceCmdHTime](ForceCmdHTime.md). The active entry is selected by [ForceCmdIndex](ForceCmdIndex.md), and transitions between entries can be ramped with [ForceCmdSlope](ForceCmdSlope.md).

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
