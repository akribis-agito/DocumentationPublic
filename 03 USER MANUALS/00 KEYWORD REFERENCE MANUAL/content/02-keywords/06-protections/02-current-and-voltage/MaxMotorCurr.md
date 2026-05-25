# MaxMotorCurr

**Definition:**

MaxMotorCurr defines the maximum allowable motor current ([MotorCurr](../../../02-keywords/09-current-and-voltage/02-motor-variables/MotorCurr.md)) in mA. If absolute value of MotorCurr exceeds MaxMotorCurr for more than 0.25ms, axis is disabled, and an error code is thrown to ConFlt.

**Note:**

For three-phase motor, MotorCurr is equal to amplitude of motor current phasor.
