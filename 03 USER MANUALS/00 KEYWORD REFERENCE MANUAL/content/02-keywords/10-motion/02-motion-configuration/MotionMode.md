---
keyword: MotionMode
summary: Selects the type of motion performed when Begin is issued.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 141
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -1
  - 19
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - -1
    - 21
---
# MotionMode

Selects the type of motion performed when `Begin` is issued.

## Overview

`MotionMode` determines the type of motion that will be performed when the [Begin](../04-motion-command/Begin.md) command is issued. It is the master selector for the axis motion engine, choosing between jog, point-to-point, repetitive, pulse-and-direction, gear, ECAM, and other modes. The mode also dictates which kinematic and target keywords are relevant (for example, repetitive mode uses [RptMode](RptMode.md), [RptCycles](RptCycles.md) and [RptWait](RptWait.md)). It cannot be changed until the current motion ends.

## How it works

`Begin` reads `MotionMode` and branches on its value. A value of `-1` (invalid selection) is rejected with an error, and each valid value runs its own setup before setting the in-motion bit (bit 0) of [MotionStat](../05-motion-status/MotionStat.md). The modes fall into two families:

- **Indirect** modes — the controller's own profiler generates the trajectory subject to [Speed](../03-kinematics-configuration/Speed.md)/[Accel](../03-kinematics-configuration/Accel.md)/[Decel](../03-kinematics-configuration/Decel.md): jog, PTP, PTP-repetitive, PD-indirect, gear-indirect, ECAM-indirect, joystick-position-indirect. `Begin` rejects these if `|Speed| > MaxVel`.
- **Direct** modes — the reference is driven directly by the user's position/velocity commands (pulse-and-direction direct, gear direct, ECAM direct, FIFO, slave, CNCA/CNCB, vector, spline buffer, joystick-velocity).

The following table shows the types of motion described by `MotionMode`.

| MotionMode | Descriptions |
|---|---|
| -1 | **Invalid selection.** This is the default value of MotionMode. |
| 0 | **Jog motion** The motor will accelerate to reach the constant speed specified by Speed and maintain at such speed until Stop command is received. The jog direction is determined by the sign of Speed keyword. **Related keywords:** Speed, Accel, Decel, JerkMode, JerkInAcc, JerkInDec |
| 1 | **Point to point motion** If RelTrgt = 0, axis moves to the position defined by AbsTrgt. Otherwise, axis moves relative to the initial position according to RelTrgt. The motion profile generated will stay within the maximum kinematic limits of Speed, Accel, Decel, and optionally JerkInAcc and JerkInDec. **Related keywords:** RelTrgt, AbsTrgt, Speed, Accel, Decel, JerkMode, JerkInAcc, JerkInDec |
| 2 | **Point to point repetitive motion** If RelTrgt = 0, axis moves to the position defined by AbsTrgt and then moves back to the initial position. Otherwise, axis moves relative to the initial position according to RelTrgt and then moves back to the initial position. Repetitive motion will continue indefinitely until either StopRep is commanded or RptCounter equals to user defined RptCycles. Axis will dwell for RptWait in between each motion. The motion profile generated will stay within the maximum kinematic limits of Speed, Accel, Decel, and optionally JerkInAcc and JerkInDec. **Related keywords:** RelTrgt, AbsTrgt, Speed, Accel, Decel, JerkMode, JerkInAcc, JerkInDec |
| 3 | **Pulse and direction (PD) motion – direct mode** Axis will follow the profile generated from the pulse-direction inputs. Please refer to Motion mode – Pulse and direction for more information. |
| 4 | **Pulse and direction (PD) motion - indirect mode** Axis will follow the second order profile generated from the pulse-direction inputs, subject to limitations by the specified acceleration and speed values. Please refer to Motion mode – Pulse and direction for more information. |
| 5 | **Gear motion – direct mode** Axis will follow the profile which tracks proportionally to the master variable. Please refer to Motion mode – Gear motion for more information. |
| 6 | **Gear motion – indirect mode** Axis will follow the second order motion profile (subject to limitations by the specified acceleration and speed values), where the generated profile tracks proportionally to the change in master variable. Please refer to Motion mode – Gear motion for more information. |
| 7 | **Electronic cam (ECAM) motion - direct mode** Axis will undergo perpetual relative motion, in which the relative position reference (relative to its initial position upon the Begin command) depends on a master variable. The relative position reference is obtained at every controller cycle from a customisable array that maps to a user-defined and evenly spaced master position range. It is analogous to mechanical cam-follower motion. Please refer to Motion mode – ECAM motion for more information. |
| 8 | **Electronic cam (ECAM) motion - indirect mode** This motion mode is reserved for internal use. |
| 9 | FIFO motion |
| 10 | **Direct slave motion** Axis A's position reference is driven directly from the change in axis B's position reference each control cycle, scaled by [MasterFact](../07-motion-mode-gear-motion/MasterFact.md). This is a separate, narrower mechanism from gear motion (it does not use `GearMaster`, `MasterPos` or `MasterFilt`). Available on multi-axis builds only. Please refer to [MotionMode10](../07-motion-mode-gear-motion/MotionMode10.md) for more information. |
| 11 | CNCA motion |
| 12 | Joystick position direct mode |
| 13 | Joystick position indirect mode |
| 14 | Joystick velocity direct mode |
| 15 | Joystick velocity indirect mode |
| 16 | Vector motion |
| 17 | CNCB motion |
| 18 | Spline buffer |
| 19 | FIFO position tracking |

## Changes between versions

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Range | −1 … 19 | −1 … **21** |
| Mode 20 | not defined | **sine point-to-point profile** |
| Mode 21 | not defined | **sine point-to-point profile (repetitive)** |

v5 adds two sine-profile point-to-point modes. **v5 is central-i only.**

## Examples

```text
AMotionMode=1        ; point-to-point motion
AMotionMode=2        ; repetitive point-to-point motion
AMotionMode         ; query current mode
```

## See also

- [Begin](../04-motion-command/Begin.md) — starts motion in the selected mode
- [JerkMode](JerkMode.md) — profiler order (modes 1 and 2)
- [RptMode](RptMode.md) — repetition direction (mode 2)
- [RptCycles](RptCycles.md) — number of repetitions (mode 2)
- [RptWait](RptWait.md) — dwell between repetitions (mode 2)
- [MotionStat](../05-motion-status/MotionStat.md) — which status bits each mode sets (see the mode-bits map there)
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — targets for PTP modes (1 and 2)
