---
keyword: ComtAng
summary: Read-only instantaneous commutation (electrical) angle of the motor, in degrees scaled by 100.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 73
attributes:
  access: ro
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
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ComtAng

Read-only instantaneous commutation (electrical) angle of the motor, in degrees scaled by 100.

## Overview

`ComtAng` reports the instantaneous commutation angle (the motor electrical angle) used by the controller to drive the phase currents of a DC brushless motor. The value is expressed in degrees scaled by 100 and wraps between a lower limit of 0 and an upper limit of 35999 (i.e. 0.00°–359.99°).

Commutation keeps the applied current vector offset from the magnetic field so that force/torque is produced efficiently as the motor moves. `ComtAng` is the angle the controller is currently using; it is established by the commutation process configured through [ComtMode](ComtMode.md) and monitored through [ComtStatus](ComtStatus.md). The angle source depends on the configured method (for example Hall sensors via [HallsAngle](HallsAngle.md) / [HallsValue](HallsValue.md), or encoder-based feedback). Being read-only, axis-scope, and not flash-saved, it can be queried at any time, including while the motor is on or in motion.

## Examples

```text
AComtAng            ; query the instantaneous commutation angle (deg x100)
```

## See also

- [ComtMode](ComtMode.md) — commutation settings that determine how the angle is established
- [ComtStatus](ComtStatus.md) — reports the commutation process status
- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state
- [HallsValue](HallsValue.md) — current raw Hall sensor state
