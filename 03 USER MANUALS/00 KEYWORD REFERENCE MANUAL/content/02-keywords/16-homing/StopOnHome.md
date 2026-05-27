---
keyword: StopOnHome
summary: Enables automatic stop of axis motion when the home digital input is asserted.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 169
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
# StopOnHome

Enables automatic stop of axis motion when the home digital input is asserted.

## Overview

`StopOnHome` enables the home-switch stop function. When set to a non-zero value, the axis automatically halts when the home digital input is asserted during a move. It is typically used in homing procedures that reference the home switch — see the "Jog until a change in the Home discrete input" step in [HomingDef](HomingDef.md) — and works analogously to [StopOnIndex](StopOnIndex.md), which stops on the encoder index pulse instead. It is an axis-scoped parameter, not saved to flash, and can be changed at any time.

## Examples

```text
AStopOnHome=1        ; halt the axis when the home input is detected
AStopOnHome         ; 0 = disabled, 1 = enabled
```

## See also

- [StopOnIndex](StopOnIndex.md) — equivalent stop on the encoder index pulse
- [HomeStat](HomeStat.md) — homing status bit-field
- [HomingDef](HomingDef.md) — homing steps that reference the home input
