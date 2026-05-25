# Vq

**Condition:**

Vq is only applicable for three-phase motor (MotorType = 3 or 4). Otherwise, Vq is 0.

**Definition:**

Vq is the output of PI controller of the quadrature axis in dq0-domain current control, in terms of internal unit. Vq is 0 if abc-domain current control is used. Please refer to [ControlMode](../../../02-keywords/09-current-and-voltage/02-motor-variables/ControlMode.md) for more information.

For dq0-domain current control, Vd and Vq will form phase voltage commands (Va, Vb, Vc) by inverse Park transform.
