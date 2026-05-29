---
keyword: AbsTrgt
summary: Absolute target position (user units) for the next point-to-point move.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 134
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# AbsTrgt

Absolute target position (user units) for the next point-to-point move.

## Overview

`AbsTrgt` sets the absolute target position, in user units, that the trajectory profiler drives the position reference toward in point-to-point (PTP) motion. When a [Begin](../04-motion-command/Begin.md) is issued in PTP mode ([MotionMode](../02-motion-configuration/MotionMode.md) `= 0`), the axis moves so that the reference [PosRef](../01-kinematics-status/PosRef.md) ends exactly at `AbsTrgt`. It is the absolute counterpart of [RelTrgt](RelTrgt.md), which specifies a relative distance. It is not saved to flash and can be changed at any time, including during a move when [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) is enabled.

`AbsTrgt` is more than a user setpoint: it is also the internal target that several other motion modes write into each cycle, so it is the single "where do I want the reference to be" variable for all profiled-position motion.

![AbsTrgt vs RelTrgt geometry](abstrgt-vs-reltrgt.svg)

## How it works

### Validation at Begin

When `Begin` runs in PTP mode the controller first folds in any relative target (if [RelTrgt](RelTrgt.md) is non-zero, `AbsTrgt = PosRef + RelTrgt`), then range-checks the **resulting** `AbsTrgt` against the software travel limits and the active hardware limit switches:

| Check | Effect if it fails |
|---|---|
| `AbsTrgt < RevPLim` or `AbsTrgt > FwdPLim` | `Begin` rejected — final target outside the software position limits ([instruction error code](../../../04-error-codes/instruction-error-codes.md) 161) |
| Moving into a tripped FLS / RLS | `Begin` rejected — motion direction is into an active limit switch ([instruction error code](../../../04-error-codes/instruction-error-codes.md) 162) |

So an out-of-limits `AbsTrgt` does not start a clipped move — it refuses the command.

### Use by the profiler each cycle

Once moving, the PTP profiler reads `AbsTrgt` every control cycle:

1. It is **re-clamped** to the software limits ([RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) / [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)) each cycle, so shrinking a limit mid-move pulls the target in.
2. Direction is decided by comparing the target to the reference [PosRef](../01-kinematics-status/PosRef.md): if the target is at or above the reference the axis moves positive, otherwise negative.
3. The braking point is found from a deceleration-distance lookahead on the remaining distance to the target; with [JerkMode](../03-kinematics-configuration/JerkMode.md) on, the jerk profiler is driven toward `AbsTrgt` directly.
4. Motion ends when the reference has reached the target (`|PosRef − AbsTrgt| ≤ 1`) and the profiler velocity is low. At that point the reference is snapped exactly onto the target, so there is no residual fractional offset.

### Modes that write AbsTrgt internally

`AbsTrgt` is the common target several modes drive; in these modes you do **not** set it yourself:

| Mode | How `AbsTrgt` is produced |
|---|---|
| Joystick position indirect | `AbsTrgt = selected analog input` each cycle |
| Repetitive PTP | reloaded from the stored repetitive target each segment |
| Indirect gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 6`) | `AbsTrgt` tracks the master position offset each cycle, then is profiled |

### Modulo

If [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0, when the feedback wraps the controller shifts `AbsTrgt` together with the rest of the reference frame, keeping the target consistent with the wrapped `PosRef`.

## Examples

```text
AAbsTrgt=100000      ; set absolute target to 100000 user units
ABegin               ; move there (PTP mode)
AAbsTrgt             ; read the current target
```

### Walk-through: set up a PTP move with custom kinematics and verify settling

A complete PTP cycle — configure profile, command the move, poll for settling, then read the stop reason:

```text
AMotionMode=1        ; point-to-point
ASpeed=500000        ; cruise velocity
AAccel=1000000       ; leading slope
ADecel=1000000       ; trailing slope
AJerk=0              ; trapezoid (set non-zero for S-curve smoothing)
AAbsTrgt=100000      ; absolute target (user units)
ABegin               ; start the move
```

While the move runs:

```text
AMotionStat                   ; bit 0 set = in motion; bit 5 set during decel; bit 6 during smoothing tail
AInTargetStat                 ; 2 in motion, 3 settling, 4 target reached
```

After the move:

```text
AInTargetStat                 ; expect 4 (target reached) once |PosErr| <= InTargetTol for InTargetTime
AMotionReason                 ; expect 0 (normal end); non-zero = something stopped it (see MotionReason)
APosErr                       ; final position error in user units
```

If [InTargetStat](../05-motion-status/InTargetStat.md) does not reach 4, either [InTargetTol](../05-motion-status/InTargetTol.md) is too tight (the dwell counter keeps resetting) or the loop is unsettled. If [MotionReason](../05-motion-status/MotionReason.md) is non-zero, the move was cut short — codes 4–7 point at limits, 1–3 at user commands, and the rest at the clusters shown on the [MotionReason](../05-motion-status/MotionReason.md) page.

## Changes between versions

In **v5 (central-i)** `AbsTrgt` is a 64-bit integer with the larger range shown in the frontmatter, matching the 64-bit position pipeline; the validation and profiler use are unchanged. **v5 is central-i only**, so on standalone `AbsTrgt` remains the v4 32-bit value.

## See also

- [RelTrgt](RelTrgt.md) — relative target distance (folded into `AbsTrgt` at `Begin`)
- [Targets](Targets.md) — flash-stored target array for user programs
- [Begin](../04-motion-command/Begin.md) — validates and starts the PTP move
- [PosRef](../01-kinematics-status/PosRef.md) — the reference that the profiler drives to `AbsTrgt`
- [Speed](../03-kinematics-configuration/Speed.md) — cruise velocity toward the target
- [MotionMode](../02-motion-configuration/MotionMode.md) — modes that consume or generate `AbsTrgt`
- [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) — retarget on the fly while moving
