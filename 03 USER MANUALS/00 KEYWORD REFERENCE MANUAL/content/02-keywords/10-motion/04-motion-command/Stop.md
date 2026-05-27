---
keyword: Stop
summary: Controlled stop; decelerates the axis to rest using the normal Decel rate.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 132
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
# Stop

Controlled stop; decelerates the axis to rest using the normal `Decel` rate.

## Overview

`Stop` is a command that brings the axis to rest using the normal [Decel](../03-kinematics-configuration/Decel.md) rate, performing a controlled deceleration. This contrasts with [Abort](Abort.md), which decelerates at the faster emergency rate [EmrgDec](../03-kinematics-configuration/EmrgDec.md). It can be issued at any time, including during motion. It is an axis-related command function.

## Examples

```text
AStop                ; controlled stop using the normal Decel rate
```

## See also

- [Abort](Abort.md) — emergency stop using `EmrgDec`
- [Decel](../03-kinematics-configuration/Decel.md) — deceleration rate used by `Stop`
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — emergency deceleration rate
