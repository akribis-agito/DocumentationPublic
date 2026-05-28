# Homing

Agito controller supports built-in, programmable homing process. Homing process is controlled by two parameters: HomingOn and HomingDef. The status of the Homing process is reported at the HomingStat parameter.

The Homing process consists of steps. The maximum number of homing steps is 20 steps. The number of steps, instructions for each step and instructions’ parameters are defined by the HomingDef.

Most of the homing steps include built-in error detection mechanism. When an error is detected during the homing process, the process is aborted, HomingOn is cleared and HomingStat is properly set to reflect the error status.

**Note:**

Upon entering the homing process, the axis kinematics (speed, acceleration, deceleration and emergency deceleration) are temporarily saved. They are restored when the homing process is completed. This is required since the homing process may change these parameters.
