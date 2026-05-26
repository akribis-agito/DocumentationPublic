---
keyword: PeakTime
summary: Maximum time allowed at peak current; sets the I²t time constant.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 53
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 3000
  default: 500
  scaling: 1.0
  implemented: final
overrides: {}
---
# PeakTime

Maximum time allowed at peak current; sets the I²t time constant.

## Overview

`PeakTime` defines the maximum time the drive may spend at the peak current. Together with [ContCL](ContCL.md) and [PeakCL](PeakCL.md) it sets the time constant of the I²t protection (see the [I²t mechanism diagram on ContCL](ContCL.md)).

If the motor's trip time is rated at a trip current different from the peak current, compute the equivalent peak-current time from the motor's trip-curve formula before setting `PeakTime`.

## Examples

```text
PeakTime=500        ; time allowed at peak current
```

## See also

- [ContCL](ContCL.md) — continuous current limit (and I²t diagram)
- [PeakCL](PeakCL.md) — peak current limit
