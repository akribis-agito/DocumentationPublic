---
keyword: OpenLoopOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 144
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OpenLoopOn

**Definition:**

OpenLoopOn is used to open the control loop at a chosen point, as shown.

| OpenLoopOn | Descriptions |
|---|---|
| 0 | **No open loop** All control loops are closed. |
| 1 | **Current open loop** Control loops are cut-off/opened at the current reference input (just before the current loop). |
| 2 | **Voltage open loop** Control loops are cut-off/opened at the voltage reference input (just before the space vector modulation for PWM drive). |
