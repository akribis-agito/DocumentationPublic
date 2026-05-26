---
keyword: Pos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 2
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Pos

**Definition:**

Pos reports the encoder feedback, in terms of main user unit (configurable by UsrUnits). Since Pos is used for position loop feedback in non-gantry mode. its definition will change depending on the gantry mode and dual-loop condition.

| Conditions | Default control (non-gantry mode) Dual-loop control (non-gantry mode) Gantry mode (regardless of dual-loop condition) | Pseudo dual-loop control (non-gantry mode) |
|---|---|---|
| Definition | Main encoder reading after the modulo operation block. **Unit: Main encoder count** | Auxiliary encoder reading after decoding but scaled up to main encoder unit.<br> $$Pos = AuxPos \bullet \frac{DualLoopFact}{65536}$$ **Unit: Main encoder count** |

Pos can be set to any desired value at any time via [SetPosition](../../../02-keywords/10-motion/03-kinematics-configuration/SetPosition.md) function (instead of setting Pos directly). Its value is reset to 0 upon power up.
