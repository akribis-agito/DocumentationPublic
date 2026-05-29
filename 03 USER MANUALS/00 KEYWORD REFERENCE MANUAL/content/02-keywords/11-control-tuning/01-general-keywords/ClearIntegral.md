---
keyword: ClearIntegral
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 412
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ClearIntegral

Command that zeroes the velocity-loop integrator of the addressed axis.

## Overview

`ClearIntegral` resets the accumulated state of the velocity control loop's integral term to zero. It is an axis-scoped command function. It may be issued while the motor is on, but not while the axis is in motion.

## How it works

When the command is received, the velocity-loop integrator of the addressed axis is set to `0` and the command returns success. No other loop state is touched by this command — the position-loop integrator, the current-loop integrators and other loop states are left as they are.

The velocity-loop integrator is the running accumulation built up by the velocity integral gain [VelKi](../04-velocity-control/VelKi.md). Clearing it removes whatever value has accumulated at the instant the command runs. The integrator then resumes accumulating normally from zero on the following control cycles, according to the active gains.

The integrator is also zeroed automatically by the controller whenever the motor is off, so a freshly enabled axis already starts with a cleared velocity integral (see [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md)). `ClearIntegral` provides the same reset on demand while the axis is enabled and stationary.

## Examples

```text
AClearIntegral        ; zero the velocity-loop integrator of axis A
```

### Walk-through: reset the velocity integrator between test moves

A common use is to clear residual integrator state between successive tuning moves so each move starts from the same initial condition. Because `ClearIntegral` rejects calls while the axis is in motion, the sequence is "stop, clear, command".

1. **Make sure the axis is stationary** (the command requires no motion). [MotionStat](../../10-motion/05-motion-status/MotionStat.md) should read `0`:

   ```text
   AMotionStat
   ```

2. **Clear the integrator**:

   ```text
   AClearIntegral
   ```

3. **Verify the clear took effect** by reading the loop's downstream signals on the next sample - for example [CurrRefCtrl](../../09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) will no longer carry any prior integrator contribution. Any anti-windup state captured during the previous move (see the saturation bits in [StatReg](../../07-status-and-faults/StatReg.md)) is also released.

4. **Issue the next command**. The velocity loop will accumulate fresh integral from zero.

> **Scope reminder.** This command touches only the velocity-loop integrator. The position-loop integrator [PosKi](../03-position-control/PosKi.md) and the two current-loop integrators driven by [CurrKi](../06-current-control/CurrKi.md) are untouched - those reset only when the motor is disabled.

## See also

- [VelKi](../04-velocity-control/VelKi.md) — velocity-loop integral gain that drives this integrator
- [PosKi](../03-position-control/PosKi.md) — position-loop integral gain (not affected by this command)
- [CurrKi](../06-current-control/CurrKi.md) — current-loop integral gain (not affected by this command)
- [StatReg](../../07-status-and-faults/StatReg.md) — anti-windup state via bits 21-23
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — loop integrators are zeroed automatically while the motor is off
