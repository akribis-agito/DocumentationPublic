---
keyword: OpenLoopOn
summary: Opens the control loop at a chosen point (none, current, or voltage).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 144
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# OpenLoopOn

Opens the control loop at a chosen point (none, current, or voltage).

## Overview

`OpenLoopOn` opens the control loop at a chosen point, primarily for commissioning and diagnostics. When the loop is opened at the current reference, [OpenLoopCurr](OpenLoopCurr.md) supplies the reference; when opened at the voltage reference, [OpenLoopVolt](OpenLoopVolt.md) supplies it.

## How it works

`OpenLoopOn` cuts the cascade at a chosen point and substitutes a user value for whatever the loops above would have produced. It works independently of [OperationMode](OperationMode.md) and the motor must already be on for any drive to appear.

| OpenLoopOn | Where the loop is cut | Drive source |
|---|---|---|
| 0 | — | All loops closed (normal operation). |
| 1 | At the current reference, just before the current loop | [OpenLoopCurr](OpenLoopCurr.md) becomes the current reference. |
| 2 | At the phase-voltage output, just before PWM modulation | [OpenLoopVolt](OpenLoopVolt.md) sets the amplitude of an injected sinusoid. |

### Current open loop (1)

Each cycle the controller overwrites the current reference with the user value from [OpenLoopCurr](OpenLoopCurr.md). The position, velocity and force loops above are bypassed; only cogging compensation ([UPMVelTable](../../09-current-and-voltage/03-current-compensation/UPMVelTable.md)) is still added on top, and the DC current offset still applies. The current loop itself stays closed and regulates the motor to that reference.

### Voltage open loop (2)

This injects a sinusoid directly onto phase A, with phases B and C held at zero, where the phase advances at the [InjectFreq](../../13-injection/InjectFreq.md) rate. The current loop is bypassed entirely. This mode exists for measuring motor resistance and inductance (R/L) and assumes the frequency is high enough that the motor barely moves and the amplitude small enough not to draw excessive current — hence [OpenLoopVolt](OpenLoopVolt.md) is capped at 20 % PWM.

### Error-protection limits while open

Whenever `OpenLoopOn` is non-zero, the controller swaps the normal position/velocity/force error limits for the wider open-loop limits (`MaxPosErrOL` / `MaxVelErrOL` / `MaxForceErrOL`) and arms all three checks, because the loops are no longer holding the error near zero. Setting `OpenLoopOn = 0` restores the normal limits.

### Safe-by-default on disable

Both drive values are forced to `0` when the motor goes off, and `OpenLoopCurr` is zeroed whenever `OpenLoopOn ≠ 1` while `OpenLoopVolt` is zeroed whenever `OpenLoopOn ≠ 2`, so there is no residual drive when you leave open-loop mode or disable the axis.

## Examples

```text
AOpenLoopOn=1        ; current open loop, drive with OpenLoopCurr
AOpenLoopOn=2        ; voltage open loop, drive with OpenLoopVolt
AOpenLoopOn=0        ; close all loops (normal operation)
```

## See also

- [OpenLoopCurr](OpenLoopCurr.md) — current reference used when OpenLoopOn = 1
- [OpenLoopVolt](OpenLoopVolt.md) — voltage amplitude used when OpenLoopOn = 2
- [OperationMode](OperationMode.md) — selects which loops are active when the loop is closed
- [MotorOn](MotorOn.md) — must be on for open-loop drive to appear; disabling clears both drive values
