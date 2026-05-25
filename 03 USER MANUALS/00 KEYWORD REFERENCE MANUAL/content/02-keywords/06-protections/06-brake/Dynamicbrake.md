# Dynamic brake

Dynamic braking is a technique used to quickly slow down the motor by shorting the motor phases and bleeding the current generated from the back e.m.f. It is a safe way to stop a motor in event that the motor suddenly disables.

##### DynBrakeOn

**Definition:**

DynBrakeOn enables/disables the dynamic braking feature.

| Value | Descriptions |
|-------|--------------|
| 0     | Disabled     |
| 1     | Enabled      |

##### DynBrkRef

**Definition:**

DynBrkRef defines the maximum duty cycle used for dynamic braking. Setting DynBrkRef = 1000 will provide the greatest braking effect. If while braking, the current exceeds the limitation set via ContCL and PeakCL, the controller will internally reduce the duty cycle to bring the current to an acceptable level.

##### DynBrakeSpeed

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

Refer to the detailed explanation regarding the dynamic braking under the [DynBrakeOn](#dynbrakeon) section above.
