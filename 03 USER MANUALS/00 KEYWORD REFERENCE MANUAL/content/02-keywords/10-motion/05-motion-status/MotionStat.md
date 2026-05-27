---
keyword: MotionStat
summary: Bit-mapped detailed status of the current motion (multiple bits can be set).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`MotionStat` reports the detailed status of the current motion as a 32-bit field: each bit represents a specific motion state and multiple bits can be set at the same time. When the motor is not in motion the firmware clears the whole word (`MotionStat = 0`, the `NOT_IN_MOTION` constant), so a non-zero value always means there is an active or stopping motion. It is the per-axis companion to [MotionReason](MotionReason.md) (which records *why* the previous motion stopped) and to [InTargetStat](InTargetStat.md) (which reports the settling state).

The word is rebuilt and stored every control cycle: the control interrupt copies `glMotionStat` into a working value, the `Profiler` updates the bits according to the motion phase, and the result is written back (`AG300_CTL01ControlInterrupt.c:2667`, `:4830`; `AG300_CTL01Profiler.c:375`). At the end of a motion the firmware ANDs the word with `ALL_IN_MOTION_BITS_CLEAR` (`0xFFFC0000` in v4) to clear bits 0–17 in one operation (`AG300_CTL01Profiler.c:461`).

![MotionStat bit layout](motionstat-bitmap.svg)

## How it works

Each bit reports a motion state when set (`= 1`); when cleared (`= 0`) it represents the opposite. Only bits 0–20 are defined; bits 21–31 are reserved and read as 0. The table below is mined directly from the bit constants in `AG300_CTL01ParamsCommon.h:1561–1630` and the set/clear sites in the profiler and control interrupt.

| Bit | Constant | Set mask | Meaning when set (= 1) |
|----|----|----|----|
| 0 | `IN_MOTION_BIT` | 0x00000001 | Axis is in motion. Set at `Begin`; cleared when the motion (and any end-of-smoothing wait) completes. |
| 1 | `IN_WAITING_BIT` | 0x00000002 | Axis is dwelling between repetitions of point-to-point repetitive motion. Set when the previous repetition ends, cleared after [RptWait](../02-motion-configuration/RptWait.md) cycles (`AG300_CTL01Profiler.c:453`, `:926`). Only used when [MotionMode](../02-motion-configuration/MotionMode.md) `= 2`. |
| 2 | `IN_REPETITIVE_STOP_BIT` | 0x00000004 | Axis is ending its repetitive motion following a [StopRep](../04-motion-command/StopRep.md) command. |
| 3 | `IN_STOP_REQUEST_BIT` | 0x00000008 | A [Stop](../04-motion-command/Stop.md) (decelerate-to-stop) has been requested; the profiler ramps the target speed to zero (`AG300_CTL01Profiler.c:557` and many sites). |
| 4 | `IN_ACCELERATION_BIT` | 0x00000010 | Axis is accelerating (profiler speed rising). Bits 4 and 5 are mutually exclusive — set via `IN_ACC_DEC_BITS_CLEAR` then one bit (`AG300_CTL01Profiler.c:807`). |
| 5 | `IN_DECELERATION_BIT` | 0x00000020 | Axis is decelerating (profiler speed falling). |
| 6 | `IN_WAIT_END_SMOOTH_BIT` | 0x00000040 | Axis is in the profile-smoothing tail: the profiler has reached the target but is still flushing the jerk/smoothing filter for `2^Jerk` cycles before the motion is declared finished (`AG300_CTL01Profiler.c:444`). See [Jerk](../03-kinematics-configuration/Jerk.md). |
| 7 | `IN_ECAM_STOP_BIT` | 0x00000080 | Axis is ending its ECAM motion (following a StopECAM command). |
| 8 | `IN_FIFO_STOP_BIT` | 0x00000100 | Axis is ending its FIFO motion (following a StopFIFO command). |
| 9 | `IN_WAIT_FOR_INPUT_BIT` | 0x00000200 | Motion is suspended until a rising edge on the configured digital input. Set by [BeginDInOn](../04-motion-command/BeginDInOn.md); cleared when the edge arrives (`AG300_CTL01Profiler.c:505`). |
| 10 | `CNCA_MEMBER_BIT` | 0x00000400 | Axis is a member of the CNCA group. |
| 11 | `CNCA_INVOLVED_NOW_BIT` | 0x00000800 | Axis is currently involved in an active CNCA motion (`AG300_CTL01Profiler.c:3723`). |
| 12 | `IN_CNCA_STOP_BIT` | 0x00001000 | Axis is ending its CNCA motion (following a StopCNCA command). |
| 13 | `CNCB_MEMBER_BIT` | 0x00002000 | Axis is a member of the CNCB group. |
| 14 | `CNCB_INVOLVED_NOW_BIT` | 0x00004000 | Axis is currently involved in an active CNCB motion (`AG300_CTL01Profiler.c:7146`). |
| 15 | `IN_CNCB_STOP_BIT` | 0x00008000 | Axis is ending its CNCB motion (following a StopCNCB command). |
| 16 | `IN_CONTROLLED_STOP_REQUEST_BIT` | 0x00010000 | A controlled stop with motor-off has been requested due to a fault condition (e.g. anomaly detection, fault from a digital input). Set in the control interrupt, e.g. `AG300_CTL01ControlInterrupt.c:16468`. |
| 17 | `IN_SPLINE_BUFFER_STOP_REQUEST_BIT` | 0x00020000 | Axis is ending its spline-buffer motion (following a [StopBuff](../04-motion-command/StopBuff.md) command). |
| 18 | `IN_VECTOR_STOP_BIT` | 0x00040000 | Axis is ending its vector motion (following a StopVec command). |
| 19 | `VECTOR_MEMBER_BIT` | 0x00080000 | Axis is a member of a vector-motion group. |
| 20 | `IN_MOTION_JOG_SOFTWARE_LIMIT_REACHED` | 0x00100000 | Axis is ending its jog motion because it is approaching a software position limit. **v5 only** (see below). |

Several combined masks are used internally: `IN_MOTION_AND_STOP_BITS_SET` (`0x00010009`, bits 0+3+16) tests "in motion but not yet stopping", and `IN_ANY_STOP_REQUEST_BIT_SET` (`0x00010008`, bits 3+16) tests for either a normal or controlled stop request.

To test a single bit, mask `MotionStat` with the bit value — e.g. "in motion" is `MotionStat & 0x1`, "decelerating" is `(MotionStat & 0x20) >> 5`.

## Changes between versions

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Defined bits | 0–19 | 0–**20** |
| Bit 20 | not defined | **jog software-limit reached** (`IN_MOTION_JOG_SOFTWARE_LIMIT_REACHED`, `0x00100000`) |
| `ALL_IN_MOTION_BITS_CLEAR` | `0xFFFC0000` (clears bits 0–17) | `0xFFE00000` (clears bits 0–20) |

In **v5** a new bit 20 reports that a jog move is ending because it is approaching a software position limit, and the end-of-motion clear mask was widened accordingly (`develop:CommonIncludes/AG300_CTL01ParamsCommon.h:1831`). **v5 is central-i only.**

## Examples

```text
AMotionStat                       ; read the current motion status word
```

Check whether axis A is actively moving (not just stopping) by masking with `0x9` and comparing to `0x1`; detect the deceleration phase with `(AMotionStat & 0x20)`.

## See also

- [MotionReason](MotionReason.md) — reason the previous motion stopped (set when several of these stop bits trigger)
- [InTargetStat](InTargetStat.md) — motion and settling state (independent of these bits)
- [StatReg](../../07-status-and-faults/StatReg.md) — general axis status bitfield (faults, limits, saturations)
- [StopRep](../04-motion-command/StopRep.md) — ends repetitive PTP motion (bit 2)
- [Jerk](../03-kinematics-configuration/Jerk.md) — sets the smoothing-tail length that holds bit 6
