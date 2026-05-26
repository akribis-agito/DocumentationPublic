---
keyword: ModeSwitchPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 438
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ModeSwitchPos

**Definition:**

ModeSwitchPos records the position value (Pos) when axis exits or enters position operation mode. The array element will only change upon the transition.

| Index | Descriptions                                      |
|-------|---------------------------------------------------|
| 1     | Position when axis enters position operation mode |
| 2     | Position when axis exits position operation mode  |
