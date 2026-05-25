# IbRef

**Definition:**

IbRef is the reference current of phase B, in milliamperes.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | IbRef equals to 0. |
| Three-phase motor (MotorType = 3 or 4) | IbRef equals to phase B result of inverse Park transform of IqRef and IdRef. It is used in abc-domain current control. |
| Two-phase stepper motor (MotorType = 6 or 7) | IbRef equals to phase B result after stepper motor calculation and direction correction of CurrRefCtrl. |
