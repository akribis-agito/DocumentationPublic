---
keyword: BuffCycles
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 548
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
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffCycles

**Definition:**

BuffCycles sets the number of times the spline buffer trajectory is repeated. Setting it to zero causes continuous repetition until StopBuff is issued. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[BuffCalc](BuffCalc.md), [BuffPos](BuffPos.md), [BuffStatus](BuffStatus.md), [StopBuff](../04-motion-command/StopBuff.md)
