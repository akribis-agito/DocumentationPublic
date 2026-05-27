---
keyword: MotionStat
summary: Bit-mapped detailed status of the current motion (multiple bits can be set).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 32
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotionStat

Bit-mapped detailed status of the current motion (multiple bits can be set).

## Overview

`MotionStat` reports the detailed status of the current motion as a bitfield: each bit represents a specific motion state and multiple bits can be set at the same time. When the motor is not in motion, `MotionStat = 0`. It complements [MotionReason](MotionReason.md), which records why the previous motion stopped.

## How it works

Each bit reports a motion state when set (`= 1`); when cleared (`= 0`) it represents the opposite.

| MotionStat, bit \# | Motion state if bit is set (= 1). If bit is cleared (= 0), it represents otherwise. |
|----|----|
| 0 | Axis is in motion. |
| 1 | Axis is dwelling (only for point-to-point repetitive motion). See [RptWait](../02-motion-configuration/RptWait.md) and [MotionMode](../02-motion-configuration/MotionMode.md) for more information. |
| 2 | Axis is ending its point-to-point repetitive motion (following [StopRep](../04-motion-command/StopRep.md) command). |
| 3 | [Stop](../04-motion-command/Stop.md) command is requested. |
| 4 | Axis is accelerating. |
| 5 | Axis is decelerating. |
| 6 | Axis is in profile smoothing phase. See [Jerk](../03-kinematics-configuration/Jerk.md) keyword. |
| 7 | Axis is in ECAM stop (following StopECAM command). |
| 8 | Axis is in FIFO stop (following StopFIFO command). |
| 9 | Axis is waiting for input (motion is suspended till the rising edge at user defined input). See [BeginDInOn](../04-motion-command/BeginDInOn.md) for more information. |
| 10 | Axis is one of CNCA member axes. |
| 11 | Axis is now involved in CNCA motion. |
| 12 | Axis is ending its CNCA motion (following StopCNCA command). |
| 13 | Axis is one of CNCB member axes. |
| 14 | Axis is now involved in CNCB motion. |
| 15 | Axis is ending its CNCB motion (following StopCNCB command). |
| 16 | Controlled stop and motor off request due to fault condition is received (e.g. anomaly detection, fault from digital input, etc.). |
| 17 | Axis is ending its spline buffer motion (following StopBuff command). |
| 18 | Axis is ending its vector motion (following StopVec command). |
| 19 | Axis is one of the vector motion axes. |
| 20 | Axis is ending its jog motion as axis is approaching software limit. |

## Examples

```text
MotionStat?         ; read the current motion status word
```

## See also

- [MotionReason](MotionReason.md) — reason the previous motion stopped
- [InTargetStat](InTargetStat.md) — motion and settling state
- [StopRep](../04-motion-command/StopRep.md) — ends repetitive PTP motion (bit 2)
