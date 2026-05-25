# IaRef

**Definition:**

IaRef is the reference current of phase A, in milliamperes.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | IaRef equals to CurrRefCtrl after direction correction. |
| Three-phase motor (MotorType = 3 or 4) | IaRef equals to phase A result of inverse Park transform of IqRef and IdRef. It is used in abc-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | IaRef equals to phase A result after stepper motor calculation and direction correction of CurrRefCtrl. |
