---
keyword: BeginOnToPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 587
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
# BeginOnToPos

**Definition:**

BeginOnToPos is a one-time flag, which if set, will instruct the controller to perform a point-to-point motion upon entering position operation mode. After the motion, BeginOnToPos is cleared.

The target position is defined by RetractTarget or RelTrgt, while velocity is defined by RetractSpeed. This flag only works for GoToPosMode command and internal switching algorithm. It will not work if OperationMode is changed manually.
