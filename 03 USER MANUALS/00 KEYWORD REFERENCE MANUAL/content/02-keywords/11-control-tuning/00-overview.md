# Control tuning

The typical Agito overall position control structure (not dual-loop control) is as below.

![image53.png](../../assets/image53.png)

The profiler will produce user-desired position reference. To ensure the position feedback equals to the desired reference, feedback and feedforwards controls are used.

1.  Feedback control

Position and velocity errors are derived from reference minus feedback. Position and velocity controls (PIV control) then evaluate the control effort needed to drive these errors to minimum values.

2.  Feedforward control

Feedforward evaluates desired control effort from position reference, so that control acts in advance to reduce tracking error.

Current loop will ensure motor current tracks the given current reference, through feedback control.

To improve motion performance, gain scheduling is available for position, velocity and feedforward gains. Input shaping is also available to reduce settling oscillation.

For non-collocated control, dual-loop control can be used to allow 2 separate feedback sources (one for position feedback and one for velocity feedback), in order to eliminate backlash.

In general, this section can be divided into 7 subsections:

1.  General keywords

2.  Dual-loop control

3.  Position control

4.  Velocity control

5.  Feedforwards

6.  Current control

7.  Input-shaping

8.  Force control (TBD)

<span class="mark">Depending on the OperationMode, user has to tune the following section of control keywords.</span>
| OperationMode | Position KW | Velocity KW | Feedforward KW | Current KW | Force KW |
|---|---|---|---|---|---|
| 1 (Current control) | **No** | **No** | **No** | **No** | **No** |
| 2 (Velocity control) |  |  |  | **Yes** |  |
| 3 ( | **Yes** | **Yes** | **Yes** | **Yes** | **No** |
| 4 (Force control) ForcePIVOn = 0 |  |  |  | **Yes** |  |
|  |  |  |  |  |  |
