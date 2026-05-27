---
keyword: VecEmrgDec
summary: Emergency vector deceleration applied to all member axes on a stop or fault.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 638
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecEmrgDec

Emergency vector deceleration applied to all member axes on a stop or fault.

## Overview

`VecEmrgDec` sets the emergency deceleration rate, in user units per second squared, applied to all axes participating in vector motion when a stop or fault is triggered. It is typically set higher than the normal [VecDecel](VecDecel.md) to halt the vector move as quickly as possible while keeping the path coordinated. It is the rate used by the [StopVec](StopVec.md) command. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
VecEmrgDec=100000   ; emergency vector deceleration (user units/s^2, default)
VecEmrgDec?         ; read the current value
```

## See also

- [VecDecel](VecDecel.md) — normal (controlled) vector deceleration
- [StopVec](StopVec.md) — command that decelerates using this rate
