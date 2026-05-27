---
keyword: StopOnIndex
summary: Enables automatic stop of axis motion on the next encoder index pulse.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 167
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StopOnIndex

Enables automatic stop of axis motion on the next encoder index pulse.

## Overview

`StopOnIndex` enables the index stop function. When set to a non-zero value, the next encoder index pulse causes the axis to halt, which is useful for homing procedures that reference the encoder index position — see the "Jog to index" and "Move to index position" steps in [HomingDef](HomingDef.md). It works analogously to [StopOnHome](StopOnHome.md), which stops on the home digital input instead. It is an axis-scoped parameter, not saved to flash, and can be changed at any time.

## Examples

```text
AStopOnIndex=1       ; halt the axis on the next encoder index pulse
AStopOnIndex        ; 0 = disabled, 1 = enabled
```

## See also

- [StopOnHome](StopOnHome.md) — equivalent stop on the home digital input
- [HomeStat](HomeStat.md) — homing status bit-field
- [HomingDef](HomingDef.md) — homing steps that reference the index
