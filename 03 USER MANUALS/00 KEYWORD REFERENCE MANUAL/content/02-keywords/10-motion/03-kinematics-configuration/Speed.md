---
keyword: Speed
summary: Target (maximum) velocity for point-to-point and jog motion, in user units per second.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 138
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# Speed

Target (maximum) velocity for point-to-point and jog motion, in user units per second.

## Overview

`Speed` sets the target velocity for motion in user units per second. The axis accelerates up to this speed at the rate set by [Accel](Accel.md) and decelerates to rest at the rate set by [Decel](Decel.md). It is the cruise-velocity kinematic limit the profiler stays within. In jog mode the sign of `Speed` also determines the direction of travel. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
ASpeed=500000        ; target velocity (user units/s)
ASpeed=-500000       ; jog in the negative direction
ASpeed              ; query current value
```

## See also

- [Accel](Accel.md) — acceleration rate toward this speed
- [Decel](Decel.md) — deceleration rate from this speed
- [Jerk](Jerk.md) — S-curve smoothing of the ramps
