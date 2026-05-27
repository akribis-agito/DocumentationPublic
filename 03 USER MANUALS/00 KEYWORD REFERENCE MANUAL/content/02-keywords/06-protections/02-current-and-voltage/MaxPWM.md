---
keyword: MaxPWM
summary: Limits the maximum PWM duty cycle (and thus the maximum voltage to the motor).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 91
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 1470
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPWM

Limits the maximum PWM duty cycle (and thus the maximum voltage to the motor).

## Overview

For PWM amplifiers, `MaxPWM` limits the maximum duty cycle of the PWM drive — and therefore the maximum voltage applied to the motor. The units are **0.1%**: `1000` represents 100% duty cycle, and `0` represents 0%.

## Examples

With a 48 V bus and default `MaxPWM = 900`, to cap the output at 30% duty cycle (14.4 V) set:

```text
AMaxPWM=300          ; limit to 30% duty cycle -> ~14.4 V on a 48 V bus
```

## See also

- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — bus-voltage limits
