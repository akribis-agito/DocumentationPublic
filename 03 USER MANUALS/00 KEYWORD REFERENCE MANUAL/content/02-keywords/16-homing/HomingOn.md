---
keyword: HomingOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 340
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomingOn

HomingOn parameter is cleared to “0” upon power on or reset.

When HomingOn is set to “1”, the controller will start the homing process according to the HomingDef while reporting its status on the HomingStat parameter. HomingOn parameter is cleared by the controller upon completion of the homing process (whether successfully or due to some error).
