---
summary: Zeroes the axis position error by snapping the position reference onto the feedback (v5 central-i).
keyword: ZeroPosErr
availability:
  standalone: []
  central-i:
  - v5
can_code: 669
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
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
# ZeroPosErr

Zeroes the axis position error by snapping the position reference onto the current feedback.

## Overview

`ZeroPosErr` is a command function (central-i, v5 only) that **clears the accumulated position error** [PosErr](../01-kinematics-status/PosErr.md) by setting the position reference [PosRef](../01-kinematics-status/PosRef.md) equal to the current feedback [Pos](../01-kinematics-status/Pos.md). This is the opposite of [SetPosition](SetPosition.md), which relabels the coordinate (moving `Pos` and `PosRef` together and *preserving* `PosErr`): `ZeroPosErr` leaves the coordinate where the feedback is and brings the reference to it, so the error becomes zero.

The typical use is to relieve a standing position error when the load is stuck or pressing against an object — the reference is pulled to where the motor actually is so the servo stops fighting the obstruction.

![SetPosition vs ZeroPosErr](setpos-vs-zeroerr.svg)

## How it works

`ZeroPosErr` does nothing when the motor is off (the reference already tracks the feedback in that state). When the motor is on, it samples the current feedback `Pos` and writes it into the **entire reference chain** — `PosRef`, the shaped and shaped-filtered references and all of their 64-bit history, plus the high-precision reference accumulator — leaving `Pos` unchanged. The result is `PosRef = Pos`, i.e. `PosErr = 0`. As in [SetPosition](SetPosition.md), it temporarily forces [Jerk](Jerk.md) to `0` to re-seed the smoothing buffer and resets the reference filter history.

If the axis is in motion when `ZeroPosErr` is issued, the controller first performs an [Abort](../04-motion-command/Abort.md)-style immediate end of motion, then zeroes the error. It assumes the motor is not actually moving at that moment; issuing it on a moving axis behaves like an abort.

### Conditions

- Allowed only in **position operation mode** ([OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md)).
- **Not allowed during multi-axis motion** — CNCA, CNCB, vector or spline-buffer modes are rejected; only simple single-axis motion modes are permitted.
- The same checks as [SetPosition](SetPosition.md) apply: encoder error mapping off, auto-gain off, the (resulting) position within the software limits, and input shaping off while the motor is on.

### Edge cases

- **Motor off:** the command is a no-op (the reference already tracks the feedback).
- **Out-of-range:** the resulting `PosRef = Pos` is checked against `[RevPLim, FwdPLim]` via the shared [SetPosition](SetPosition.md) conditions; if `Pos` happens to be outside the limits the command is rejected.
- **Simulation mode (`MotorType` = 5):** `Pos` is forced to follow `PosRef`, so `PosErr` is already zero and the operation is benign.
- **ModRev wrap:** if a wrap happens during the operation, the wrap shifts both sides together; the resulting `PosRef = Pos` is preserved.
- **Active fault:** the axis is disabled (motor off), so the command is a no-op.
- **In-motion behaviour:** the in-progress single-axis move is **aborted** (no ramp), then `PosRef` is snapped to `Pos`. Multi-axis motion modes are rejected. The user is responsible for ensuring the load is not actually moving; if it is, the snap will produce a step in `PosErr` and likely a fault.
- **Other motion modes:** allowed only for simple single-axis modes (jog/PTP/PD/gear/ECAM/joystick/FIFO/slave); CNCA/CNCB/vector/spline rejected.

## Examples

```text
AZeroPosErr          ; clear axis A's position error (set PosRef = Pos)
```

## Changes between versions

`ZeroPosErr` exists only in **v5 (central-i)**. In v4 the CAN code (669) is an unused placeholder, so the function is not available on the standalone product or on v4 central-i.

## See also

- [SetPosition](SetPosition.md) — redefine the coordinate (preserves `PosErr`) rather than zero the error
- [PosErr](../01-kinematics-status/PosErr.md) — the error this command zeroes
- [Pos](../01-kinematics-status/Pos.md) / [PosRef](../01-kinematics-status/PosRef.md) — `ZeroPosErr` sets `PosRef = Pos`
- [Abort](../04-motion-command/Abort.md) — `ZeroPosErr` aborts an in-progress single-axis move first
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — must be position control
