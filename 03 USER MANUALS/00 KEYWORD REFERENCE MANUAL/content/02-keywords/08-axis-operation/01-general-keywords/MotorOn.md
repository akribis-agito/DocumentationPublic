# MotorOn

**Definition:**

MotorOn is used to enable/disable the motor (by writing) or report the servo status (by reading). MotorOn = 0 corresponds to disabling of the motor while MotorOn = 1 corresponds to enabling of the motor.

When the motor is disabled, no power is applied to the motor and none of the control loop is active.

Motor can be disabled internally due to controller fault (see [ConFlt](../../../02-keywords/07-status-and-faults/ConFlt.md) and [Controller error codes](../../../04-error-codes/controller-error-codes.md)). When axis is enabled, ConFlt is cleared. If the fault state remains, fault will be retriggered and the axis will be disabled again.

Some keywords are only writable or callable when axis is disabled. Please refer to each keyword’s attribute table for more info.
