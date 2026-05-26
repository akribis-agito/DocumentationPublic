---
keyword: MotorOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 130
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
# MotorOn

**Definition:**

MotorOn is used to enable/disable the motor (by writing) or report the servo status (by reading). MotorOn = 0 corresponds to disabling of the motor while MotorOn = 1 corresponds to enabling of the motor.

When the motor is disabled, no power is applied to the motor and none of the control loop is active.

Motor can be disabled internally due to controller fault (see [ConFlt](../../../02-keywords/07-status-and-faults/ConFlt.md) and [Controller error codes](../../../04-error-codes/controller-error-codes.md)). When axis is enabled, ConFlt is cleared. If the fault state remains, fault will be retriggered and the axis will be disabled again.

Some keywords are only writable or callable when axis is disabled. Please refer to each keyword’s attribute table for more info.
