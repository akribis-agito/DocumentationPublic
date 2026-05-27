---
keyword: ForceGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 577
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ForceGain

**Definition:**

ForceGain is the proportional gain for standard form PID control in the force loop. Depending on ForcePIVOn, the internal scaling changes as shown.

| ForcePIVOn | Internal scaling |
|------------|------------------|
| 0          | 1E-6             |
| 1          | 1E-3             |
