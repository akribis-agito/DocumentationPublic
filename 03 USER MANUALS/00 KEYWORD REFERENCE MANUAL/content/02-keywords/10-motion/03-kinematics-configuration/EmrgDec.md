---
keyword: EmrgDec
summary: Emergency deceleration rate applied on Abort or fault, in user units per second squared.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 140
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# EmrgDec

Emergency deceleration rate applied on `Abort` or fault, in user units per second squared.

## Overview

`EmrgDec` sets the emergency deceleration rate applied when an [Abort](../04-motion-command/Abort.md) or a fault condition halts motion. It is normally set higher than the regular [Decel](Decel.md) rate so the axis stops as quickly as possible. A controlled [Stop](../04-motion-command/Stop.md) uses `Decel`, whereas `Abort` uses `EmrgDec`. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
AEmrgDec=1000000     ; emergency deceleration (user units/s^2)
AEmrgDec            ; query current value
```

## See also

- [Decel](Decel.md) — normal deceleration rate
- [Accel](Accel.md) — acceleration rate
- [Abort](../04-motion-command/Abort.md) — command that uses this rate
