# EncDir/AuxEncDir

**Condition:**

EncDir is only used when EncType is not 4 (i.e. not SIN/COS encoder). For EncType = 4, please refer to [SinCosSetup](../../../02-keywords/03-encoder/01-general-settings/SinCosSetup-AuxSinCosSet.md) to configure the encoder direction.

**Definition:**

EncDir configures the direction of the encoder reading. The controller increments/decrements the position (Pos) by the delta of raw position feedback at every controller cycle (hardware interrupt). If EncDir = 0, controller will increment the delta. If EncDir = 1, controller will decrement the delta.

In the setup process, it is important to configure EncDir to get the desired direction first before performing the motor phasing.
