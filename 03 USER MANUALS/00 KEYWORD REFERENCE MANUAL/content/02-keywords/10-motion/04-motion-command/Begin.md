---
keyword: Begin
summary: Starts motion on the axis according to the current motion mode and target settings.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 131
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
# Begin

Starts motion on the axis according to the current motion mode and target settings.

## Overview

`Begin` starts motion on the axis using the currently selected [MotionMode](../02-motion-configuration/MotionMode.md), the configured targets ([AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)) and the kinematics ([Speed](../03-kinematics-configuration/Speed.md), [Accel](../03-kinematics-configuration/Accel.md), [Decel](../03-kinematics-configuration/Decel.md), [Jerk](../03-kinematics-configuration/Jerk.md)). It is an axis-related command function and carries no value.

The handler does three things in order: it runs a chain of **pre-conditions** that reject the command if the axis is not ready, then runs **mode-specific validation and initialization**, and finally **arms the move** by setting bits in [MotionStat](../05-motion-status/MotionStat.md). Motion is ended by [Stop](Stop.md) (controlled) or [Abort](Abort.md) (immediate). A move can also be deferred until a digital-input edge via [BeginDInOn](BeginDInOn.md).

`Begin` is rejected while the axis is already in motion (the keyword carries the `ok_in_motion: false` attribute, enforced by the interpreter). Endless modes — joystick-position and PTP with [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) `= 1` — instead keep the move alive and track new position commands without ending.

## How it works

### Pre-condition checks (all modes)

Before any motion-mode handling, `Begin` validates the axis state. The first failing test sets an error code, the command is rejected and no motion starts:

| Condition that rejects `Begin` | Error code |
|---|---|
| Motor is off ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) ≠ on) | 39 |
| [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0 but outside [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) | 267 |
| Homing in progress | 109 |
| Not in position operation mode | 156 |
| Static brake locked and in use | 114 |
| Reference already outside software limits and mode is not jog/PTP/velocity-joystick | 164 |
| [Speed](../03-kinematics-configuration/Speed.md) exceeds [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) in an indirect mode (jog/PTP/PTP-rep/PD-indirect/gear-indirect/ECAM-indirect/joystick-pos-indirect) | 271 |

A gantry edge transition that is not yet ready also rejects the command.

### Mode-specific validation and initialization

`Begin` then switches on [MotionMode](../02-motion-configuration/MotionMode.md). The common point-to-point and jog paths:

- **PTP** ([MotionMode](../02-motion-configuration/MotionMode.md) `= 1`): if [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) ≠ 0 the absolute target is recomputed as `PosRef + RelTrgt`; the target is range-checked against [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) (error code 161) and against the limit switches in the direction of travel (error code 162). The jerk profiler is then seeded with the current [PosRef](../01-kinematics-status/PosRef.md), zero initial velocity, the target, [Speed](../03-kinematics-configuration/Speed.md), [Accel](../03-kinematics-configuration/Accel.md), [Decel](../03-kinematics-configuration/Decel.md) and [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md).
- **PTP-repetitive** ([MotionMode](../02-motion-configuration/MotionMode.md) `= 2`): in addition computes the return target from [RptMode](../02-motion-configuration/RptMode.md) (back-and-forth vs unidirectional), range-checks **both** targets, and resets the repetition counter [RptCounter](../05-motion-status/RptCounter.md) to 0.
- **Jog / velocity-joystick**: rejects a jog whose [Speed](../03-kinematics-configuration/Speed.md) sign drives the axis into an already-active RLS/FLS.

### Arming the move

For every mode the final step (under interrupts disabled) sets the motion-status bits and resets the per-move state:

| Field set by `Begin` | Value | Meaning |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 0 (in-motion bit) | 1 | Axis is in motion — the profiler now owns [PosRef](../01-kinematics-status/PosRef.md) |
| [MotionStat](../05-motion-status/MotionStat.md) bit 9 (wait-for-input bit) | 1 (only if [BeginDInOn](BeginDInOn.md) `= 1`) | Move armed but suspended until a digital-input rising edge |
| [MotionReason](../05-motion-status/MotionReason.md) | 0 | Clears any previous stop reason |
| [InTargetStat](../05-motion-status/InTargetStat.md) | 2 | Settling state set to "in motion" |
| motion-samples counter | 0 | Restarts the [MotionSamples](../05-motion-status/MotionSamples.md) timing |
| friction-compensation flag | 1 | Re-seeds the velocity integral on first motion sample |

Setting the in-motion bit (bit 0) is what actually hands control of [PosRef](../01-kinematics-status/PosRef.md) to the profiler: on the next control cycle the profiler accelerates toward [Speed](../03-kinematics-configuration/Speed.md) using `Accel × AccelFact` and plans its stop with [Decel](../03-kinematics-configuration/Decel.md) (see [Decel](../03-kinematics-configuration/Decel.md) for the deceleration-distance lookahead). When [BeginDInOn](BeginDInOn.md) is set, the wait-for-input bit (bit 9) holds the axis stationary and the motion-time counter is not incremented until the configured input rises.

## Examples

```text
ABegin               ; start motion with the current mode and targets
APTPKeepMoving=1     ; allow retargeting on the fly (AbsTrgt can be updated without re-issuing Begin)
```

To run a 100000-unit absolute point-to-point move on axis A: select PTP, set the target and kinematics, then begin.

```text
AMotionMode=1        ; PTP
AAbsTrgt=100000      ; absolute target
ASpeed=50000         ; cruise speed
ABegin               ; start the move
```

### Walk-through: full PTP setup, command, and settling verification

A complete cycle — set kinematics, command the move, poll until settled, then check the stop reason:

```text
AMotorOn=1            ; enable the axis (precondition for Begin)
AMotionMode=1         ; PTP
ASpeed=500000         ; cruise velocity (must be <= MaxVel in indirect modes)
AAccel=1000000        ; leading slope
ADecel=1000000        ; trailing slope
AJerk=0               ; trapezoid; set non-zero for S-curve smoothing
AInTargetTol=50       ; settling window (user units)
AInTargetTime=20      ; minimum dwell (ms)
AAbsTrgt=100000       ; absolute target
ABegin                ; start the move
```

Poll during and after the move:

```text
AMotionStat                   ; bit 0 = in motion; bit 4 accel, bit 5 decel, bit 6 smoothing tail
AInTargetStat                 ; 2 in motion -> 3 settling -> 4 reached
AInTargetStat                 ; once 4, the move is fully settled
AMotionReason                 ; expect 0 (normal end); see MotionReason for non-zero codes
APosErr                       ; final tracking error in user units
```

If `Begin` was *rejected*, no motion bits ever set — inspect [ErrLog](../../07-status-and-faults/ErrLog.md) for the rejection code (e.g. 39 motor off, 161 target out of soft limits, 271 `Speed` over `MaxVel`).

### Edge cases

- **Motor off:** rejected with error 39 (motor must be on for motion).
- **Out-of-range "write":** `Begin` is a function with no value; the keyword carries no payload to validate.
- **Simulation mode (`MotorType` = 5):** allowed; the simulation path still runs the profiler and updates synthetic feedback.
- **ModRev wrap:** allowed; the wrap continues to be applied to the reference during the move.
- **Active fault:** rejected because the motor is off.
- **Already in motion (`ok_in_motion: false`):** the interpreter rejects the command before it reaches the handler.
- **PTP retargeting with `PTPKeepMoving = 1`:** the original move never reports "done"; issuing `Begin` again with a new target is the intended way to retarget — the profiler ramps to the new target without first stopping.
- **`BeginDInOn = 1`:** `Begin` is accepted and bit 9 of [MotionStat](../05-motion-status/MotionStat.md) (wait-for-input) is set; the profiler does not start until the configured digital input rises.
- **Gantry:** the gantry transition-in-progress flag rejects `Begin` until the gantry is ready.
- **Multi-axis modes (CNCA, CNCB, vector, spline-buffer):** `Begin` on a member axis arms the master; the per-mode validation differs from PTP.

## Changes between versions

In **v5 (central-i)** `Begin` adds two pre-condition checks and supports additional motion modes:

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| MaxAcc check | none | rejected if [Accel](../03-kinematics-configuration/Accel.md) or [Decel](../03-kinematics-configuration/Decel.md) exceeds [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) (PTP/jog/sine modes) |
| Commutation check | none | rejected if the motor is not yet phased |
| Sine PTP modes | not present | sine PTP and sine PTP-repetitive modes recognized |
| Position limits / speed | 32-bit | 64-bit |

The bits set by a successful `Begin` ([MotionStat](../05-motion-status/MotionStat.md) bit 0/9, [MotionReason](../05-motion-status/MotionReason.md) `= 0`) are unchanged. **v5 is central-i only.**

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects the type of motion to start
- [Stop](Stop.md) — controlled stop (uses `Decel`)
- [Abort](Abort.md) — immediate stop
- [BeginDInOn](BeginDInOn.md) — defer `Begin` until a digital-input edge
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — point-to-point targets validated by `Begin`
- [MotionStat](../05-motion-status/MotionStat.md) — bits 0/9 set by `Begin`
- [MotionReason](../05-motion-status/MotionReason.md) — reset to 0 by `Begin`
- [PosRef](../01-kinematics-status/PosRef.md) — the reference the profiler drives once the in-motion bit is set
- [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) — keeps a PTP move alive for on-the-fly retargeting
