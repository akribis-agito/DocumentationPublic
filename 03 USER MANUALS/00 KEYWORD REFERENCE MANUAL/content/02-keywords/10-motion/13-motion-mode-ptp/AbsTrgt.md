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

## How it works

### Validation at Begin

When `Begin` runs in PTP mode the firmware first folds in any relative target (`if (RelTrgt != 0) AbsTrgt = PosRef + RelTrgt`, `AG300_CTL01Funcs.c:1013`), then range-checks the **resulting** `AbsTrgt` against the software travel limits and the active hardware limit switches:

| Check (`AG300_CTL01Funcs.c`) | Effect if it fails |
|---|---|
| `AbsTrgt < RevPLim` or `AbsTrgt > FwdPLim` (`:1017`) | `Begin` rejected — `FINAL_TARGET_IS_OUTSIDE_OF_POS_LIMITS` |
| Moving into a tripped FLS / RLS (`:1025`) | `Begin` rejected — `DO_NOT_ALLOW_MOTION_INTO_RLS_OR_FLS` |

So an out-of-limits `AbsTrgt` does not start a clipped move — it refuses the command.

### Use by the profiler each cycle

Once moving, the PTP profiler (`AG300_CTL01Profiler.c:998`–`1284`) reads `AbsTrgt` every control cycle:

1. It is **re-clamped** to the software limits each cycle (`glAbsTrgt = glFwdPLim` / `glRevPLim`, `:1007`–`1011`), so shrinking a limit mid-move pulls the target in.
2. Direction is decided by comparing the target to the reference at internal 50.14 fixed point: `(AbsTrgt << 14) >= gllPosRef` ⇒ move positive, else negative (`:1078`, `:1134`).
3. The braking point is found from a deceleration-distance square-root lookahead on the remaining distance `(AbsTrgt << 14) − gllPosRef` (`:1090`, `:1133`); with [JerkMode](../03-kinematics-configuration/JerkMode.md) on, the jerk profiler is given `AbsTrgt` directly (`:1170`).
4. Motion ends when `|PosRef − AbsTrgt| ≤ 1` and the profiler velocity is low (`:1239`). At that point the reference is snapped exactly onto the target — `glPosRef = glAbsTrgt` (`:468`) — so there is no residual fractional offset.

### Modes that write AbsTrgt internally

`AbsTrgt` is the common target several modes drive; in these modes you do **not** set it yourself:

| Mode | How `AbsTrgt` is produced |
|---|---|
| Joystick position indirect | `AbsTrgt = selected analog input` each cycle (`AG300_CTL01Profiler.c:1003`) |
| Repetitive PTP | reloaded from the stored repetitive target each segment (`:929`–`936`) |
| Indirect gear motion (`MotionMode = 6`) | `AbsTrgt = PosRefInitial + (MasterPos − MasterPosInitial)` each cycle (`:1671`), then profiled |

### Modulo

If [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0, when the feedback wraps the firmware shifts `AbsTrgt` together with the rest of the reference frame (`AG300_CTL01ControlInterrupt.c:3170`–`3171`), keeping the target consistent with the wrapped `PosRef`.

## Examples

```text
AAbsTrgt=100000      ; set absolute target to 100000 user units
ABegin               ; move there (PTP mode)
AAbsTrgt             ; read the current target
```

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
