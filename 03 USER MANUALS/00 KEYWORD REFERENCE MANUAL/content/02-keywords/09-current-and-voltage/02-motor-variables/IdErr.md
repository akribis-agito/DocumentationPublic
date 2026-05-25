# IdErr

**Condition:**

IdErr is only applicable for three-phase motor (MotorType = 3 or 4). Otherwise, IdErr is 0.

**Definition:**

IdErr is the calculated current error in the direct axis, in milliamperes, defined as shown.

$$
IdErr\ \lbrack mA\rbrack\  = \ IdRef\ \lbrack mA\rbrack\  - \ Id\ \lbrack mA\rbrack
$$

It is used in three-phase motor dq0-domain current control.
