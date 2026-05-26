---
keyword: PDEndTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 414
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
  - 163840
  default: 16
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDEndTime

**Definition:**

PDEndTime is the waiting time in milliseconds, since the pulse-direction counter (PDPos) and generated position reference stops changing, before starting to check for the settling status (InTargetStat).

The timer for PDEndTime resets when PDPos or generated position reference starts changing.
