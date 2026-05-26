---
keyword: GoToPosMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 336
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GoToPosMode

**Definition:**

GoToPosMode command instructs the controller to enter position operation mode in a graceful manner. Position value (Pos) upon receipt of command is recorded in ModeSwitchPos keyword.

Through BeginOnToPos flag, user may choose to immediately start a point-to-point motion to target position (set by RetractTarget or RelTrgt) at a defined speed (RetractSpeed) upon receipt of GoToPosMode command.

**Note:**

GoToPosMode cannot be used if axis is in velocity operation mode (OperationMode = 1).
