---
keyword: Begin
summary: Starts motion on the axis according to the current motion mode and target settings.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 131
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Begin

Starts motion on the axis according to the current motion mode and target settings.

## Overview

`Begin` starts motion on the axis using the currently selected [MotionMode](../02-motion-configuration/MotionMode.md) and the configured targets ([AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)) and kinematics. The axis must not already be in motion when `Begin` is issued, unless [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) is enabled to allow retargeting on the fly. A move can also be triggered by a digital input via [BeginDInOn](BeginDInOn.md). Motion is ended by [Stop](Stop.md) or [Abort](Abort.md). It is an axis-related command function.

## Examples

```text
ABegin               ; start motion with the current mode and targets
```

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects the type of motion to start
- [Stop](Stop.md) — controlled stop
- [Abort](Abort.md) — emergency stop
- [BeginDInOn](BeginDInOn.md) — trigger `Begin` from a digital input
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — absolute target position
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — relative target position
