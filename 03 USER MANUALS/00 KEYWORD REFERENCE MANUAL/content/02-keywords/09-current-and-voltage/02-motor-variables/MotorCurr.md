# MotorCurr

**Definition:**

MotorCurr is the total feedback current vector amplitude of motor, in milliamperes.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | 
$$
MotorCurr\ \lbrack mA\rbrack\  = \ Ia\ \lbrack mA\rbrack
$$ |
| Three-phase motor (MotorType = 3 or 4) | 
$$
MotorCurr\ \lbrack mA\rbrack\  = \ sign(Iq) \bullet \sqrt{{Iq}^{2} + {Id}^{2}}\ \lbrack mA\rbrack
$$ |
| Two-phase stepper motor (MotorType = 6 or 7) | 
$$
MotorCurr\ \lbrack mA\rbrack\  = \ \sqrt{{Ia}^{2} + {Ib}^{2}}\ \lbrack mA\rbrack
$$ |
