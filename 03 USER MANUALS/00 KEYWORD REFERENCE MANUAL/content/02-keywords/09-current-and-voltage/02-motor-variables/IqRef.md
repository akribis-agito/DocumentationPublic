# IqRef

**Definition:**

IqRef definition varies according to MotorType.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | IqRef equals to IaRef. |
| Three-phase motor (MotorType = 3 or 4) | IqRef equals to CurrRefCtrl after direction correction. It is used in dq0-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | Iq equals to 0. |
