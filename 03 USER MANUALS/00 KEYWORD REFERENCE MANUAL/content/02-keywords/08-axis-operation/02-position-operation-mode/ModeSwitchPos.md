---
keyword: ModeSwitchPos
summary: Records the position when the axis enters or exits position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 438
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# ModeSwitchPos

Records the position when the axis enters or exits position mode.

## Overview

`ModeSwitchPos` records the position value (`Pos`) at the moment the axis enters or exits position operation mode. Each array element changes only at the corresponding transition, so the values persist between transitions. It is recorded automatically on entry via [GoToPosMode](GoToPosMode.md) or the internal switching algorithm.

## How it works

| Index | Descriptions                                      |
|-------|---------------------------------------------------|
| 1     | Position when axis enters position operation mode |
| 2     | Position when axis exits position operation mode  |

## Examples

```text
AModeSwitchPos[1]   ; position recorded when entering position mode
AModeSwitchPos[2]   ; position recorded when exiting position mode
```

## See also

- [GoToPosMode](GoToPosMode.md) — records the entry position
- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
