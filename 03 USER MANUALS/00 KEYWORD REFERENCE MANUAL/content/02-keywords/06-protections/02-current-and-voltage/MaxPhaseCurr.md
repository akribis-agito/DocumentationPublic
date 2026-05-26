---
keyword: MaxPhaseCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 98
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
  - 76000
  default: 76000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPhaseCurr

**Definition:**

MaxPhaseCurr defines the maximum allowable motor phase current in mA. If absolute value of any phase current exceeds MaxPhaseCurr for more than 0.25ms, axis is disabled, and an error code is thrown to ConFlt.

**Note:**

For single-phase motor/voice-coil, MotorCurr is monitored. For three-phase motor, Ia, Ib and Ic are monitored. Ic is inferred from Ia and Ib.
