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

`Begin` starts motion on the axis using the currently selected [MotionMode](../02-motion-configuration/MotionMode.md), the configured targets ([AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)) and the kinematics ([Speed](../03-kinematics-configuration/Speed.md), [Accel](../03-kinematics-configuration/Accel.md), [Decel](../03-kinematics-configuration/Decel.md), [Jerk](../03-kinematics-configuration/Jerk.md)). It is an axis-related command function (it carries no value — the work is done by the firmware `Begin()` handler in `AG300_CTL01Funcs.c:903`).

The handler does three things in order: it runs a chain of **pre-conditions** that reject the command if the axis is not ready, then runs **mode-specific validation and initialization**, and finally **arms the move** by setting bits in [MotionStat](../05-motion-status/MotionStat.md). Motion is ended by [Stop](Stop.md) (controlled) or [Abort](Abort.md) (immediate). A move can also be deferred until a digital-input edge via [BeginDInOn](BeginDInOn.md).

`Begin` is rejected while the axis is already in motion (the keyword carries the `ok_in_motion: false` attribute, enforced by the interpreter, `AG300_CTL01Interpreter.c:1218`). Endless modes — joystick-position and PTP with [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) `= 1` — instead keep the move alive and track new position commands without ending (`AG300_CTL01Profiler.c:1234`).

## How it works

### Pre-condition checks (all modes)

Before any motion-mode handling, `Begin` validates the axis state. The first failing test sets an error code, the command is rejected and no motion starts (`AG300_CTL01Funcs.c:925`–`963`):

| Condition that rejects `Begin` | Error code |
|---|---|
| Motor is off ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) ≠ on) | `MUST_BE_MOTOR_ON_FOR_MOTION` (39) |
| [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0 but outside [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) | `MODREV_IS_OUT_OF_SW_LIM_RANGE` (267) |
| Homing in progress | `CANT_START_MOTION_WHILE_HOMING_IS_ON` (109) |
| Not in position operation mode | `CANT_START_MOTION_WHILE_NOT_IN_POS_MODE` (156) |
| Static brake locked and in use | `CANT_START_MOTION_WHILE_STATIC_BRAKE_IS_LOCKED` (114) |
| Gantry edge transition not ready | `GANTRY_TRANSITION_IN_PROGRESS` |
| Reference already outside software limits and mode is not jog/PTP/velocity-joystick | `CANT_START_MOTION_IF_OUT_OF_POS_LIMITS` (164) |
| [Speed](../03-kinematics-configuration/Speed.md) exceeds [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) in an indirect mode (jog/PTP/PTP-rep/PD-indirect/gear-indirect/ECAM-indirect/joystick-pos-indirect) | `MAXVEL_PROTECTION` (271) |

### Mode-specific validation and initialization

`Begin` then switches on [MotionMode](../02-motion-configuration/MotionMode.md) (`AG300_CTL01Funcs.c:968`). The common point-to-point and jog paths:

- **PTP** ([MotionMode](../02-motion-configuration/MotionMode.md) `= 1`): if [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) ≠ 0 the absolute target is recomputed as `PosRef + RelTrgt`; the target is range-checked against [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) (`FINAL_TARGET_IS_OUTSIDE_OF_POS_LIMITS`, 161) and against the limit switches in the direction of travel (`DO_NOT_ALLOW_MOTION_INTO_RLS_OR_FLS`, 162). The jerk profiler is then seeded with the current [PosRef](../01-kinematics-status/PosRef.md), zero initial velocity, the target, [Speed](../03-kinematics-configuration/Speed.md), [Accel](../03-kinematics-configuration/Accel.md), [Decel](../03-kinematics-configuration/Decel.md) and [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md) (`JerkProfilerInit`, `AG300_CTL01Funcs.c:1040`).
- **PTP-repetitive** ([MotionMode](../02-motion-configuration/MotionMode.md) `= 2`): in addition computes the return target `glAbsTrgtRepetitive` from [RptMode](../02-motion-configuration/RptMode.md) (back-and-forth vs unidirectional), range-checks **both** targets, and resets the repetition counter [RptCounter](../05-motion-status/RptCounter.md) to 0 (`AG300_CTL01Funcs.c:1164`).
- **Jog / velocity-joystick**: rejects a jog whose [Speed](../03-kinematics-configuration/Speed.md) sign drives the axis into an already-active RLS/FLS (`AG300_CTL01Funcs.c:983`).

### Arming the move

For every mode the final step (under interrupts disabled) sets the motion-status bits and resets the per-move state (`AG300_CTL01Funcs.c:993`–`1007` for jog, similarly per case):

| Field set by `Begin` | Value | Meaning |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 0 `IN_MOTION_BIT` | 1 | Axis is in motion — the profiler now owns [PosRef](../01-kinematics-status/PosRef.md) |
| [MotionStat](../05-motion-status/MotionStat.md) bit 9 `IN_WAIT_FOR_INPUT_BIT` | 1 (only if [BeginDInOn](BeginDInOn.md) `= 1`) | Move armed but suspended until a digital-input rising edge |
| [MotionReason](../05-motion-status/MotionReason.md) | 0 (`MOTION_REASON_END_NONE`) | Clears any previous stop reason |
| [InTargetStat](../05-motion-status/InTargetStat.md) | 2 (`IN_TARGET_STATUS_IN_MOTION`) | Settling state set to "in motion" |
| `glMotionSamplesCounter` | 0 | Restarts the [MotionSamples](../05-motion-status/MotionSamples.md) timing |
| friction-compensation flag | 1 | Re-seeds the velocity integral on first motion sample |

Setting `IN_MOTION_BIT` is what actually hands control of [PosRef](../01-kinematics-status/PosRef.md) to the profiler: on the next control cycle the profiler accelerates toward [Speed](../03-kinematics-configuration/Speed.md) using `Accel × AccelFact` and plans its stop with [Decel](../03-kinematics-configuration/Decel.md) (see [Decel](../03-kinematics-configuration/Decel.md) for the deceleration-distance lookahead). When [BeginDInOn](BeginDInOn.md) is set, `IN_WAIT_FOR_INPUT_BIT` holds the axis stationary and the motion-time counter is not incremented until the configured input rises (`AG300_CTL01Profiler.c:502`–`505`).

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

## Changes between versions

In **v5 (central-i)** `Begin` adds two pre-condition checks and supports additional motion modes (`develop:CommonC/AG300_CTL01Funcs.c:1045`):

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| MaxAcc check | none | rejects with `MAXACC_PROTECTION` if [Accel](../03-kinematics-configuration/Accel.md) or [Decel](../03-kinematics-configuration/Decel.md) exceeds [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) (PTP/jog/sine modes) |
| Commutation check | none | rejects with `NOT_ALLOWED_BEFORE_COMMUTATION` if the motor is not yet phased |
| Sine PTP modes | not present | `MOTION_MODE_SINE_PTP` / `MOTION_MODE_SINE_PTP_REP` recognized |
| Position limits / speed | 32-bit (`glRevPLim`, `glSpeed`, …) | 64-bit (`gllRevPLim`, `gllSpeed`, …) |

The bits set by a successful `Begin` ([MotionStat](../05-motion-status/MotionStat.md) bit 0/9, [MotionReason](../05-motion-status/MotionReason.md) `= 0`) are unchanged. **v5 is central-i only.**

## See also

- [MotionMode](../02-motion-configuration/MotionMode.md) — selects the type of motion to start
- [Stop](Stop.md) — controlled stop (uses `Decel`)
- [Abort](Abort.md) — immediate stop
- [BeginDInOn](BeginDInOn.md) — defer `Begin` until a digital-input edge
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — point-to-point targets validated by `Begin`
- [MotionStat](../05-motion-status/MotionStat.md) — bits 0/9 set by `Begin`
- [MotionReason](../05-motion-status/MotionReason.md) — reset to 0 by `Begin`
- [PosRef](../01-kinematics-status/PosRef.md) — the reference the profiler drives once `IN_MOTION_BIT` is set
- [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) — keeps a PTP move alive for on-the-fly retargeting
