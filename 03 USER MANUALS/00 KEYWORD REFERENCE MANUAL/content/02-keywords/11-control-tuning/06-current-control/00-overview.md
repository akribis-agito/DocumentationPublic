# Current control

Current loop increases the motor bandwidth above its natural bandwidth. By ensuring the motor bandwidth is higher than outer loop (position, velocity, force, etc.) bandwidth by a factor (recommended: at least 10), it ensures actual motor current can tight follow the outer loop’s generated current reference. This in turns ensures the desired force (or torque) is generated at all times.

The figure below shows the typical, generalised block diagram of current loop control.

<img alt="A diagram of a computer AI-generated content may be incorrect." src="image60.png" style="width:6.26389in;height:2.92431in"/>

For **voice coil or brushed motor**, the controller only has to control 1 phase current (phase A). The figure below shows the typical current control in for such single-phase motor.

![image61.png](../../../assets/image61.png)

For **stepper motor**, current loop is similar to voice coil motor, except the controller has to control 2 separate phase currents (phase A and B). Phase A and B will have the same current loop structure as above.

For **3-phase brushless motor**, the controller has to control 3 current values, with amplifier acting as a power inverter. Ultimately by means of Kirchoff’s current law ($I_{a} + I_{b} + I_{c} = 0$), the controller only needs to control 2 current values ($I_{a}$, $I_{b}$) with the third value inferred from the former 2 (same for voltage).

User can also operate in dq0 space by Park transform, controlling direct and quadrature current values. Selection on which 3-phase current control mode to use is done by [ControlMode](../../../02-keywords/09-current-and-voltage/02-motor-variables/ControlMode.md) keyword.

The following block diagram shows both dq0 and abc domain current controls.

1.  dq0-domain control (vector control, default method)

<img alt="A diagram of a machine AI-generated content may be incorrect." src="image62.png" style="width:7.25419in;height:2.76415in"/>

2.  abc-domain control (individual phase current control)

![image63.png](../../../assets/image63.png)

For more information on the current and voltage terms, please refer to [Current and voltage – Motor variables](../../../02-keywords/09-current-and-voltage/02-motor-variables/00-overview.md).
