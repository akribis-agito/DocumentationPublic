---
keyword: MotionReason
summary: Records why the last motion stopped, encoded as a numeric reason code.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 43
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# MotionReason

Records why the last motion stopped, encoded as a numeric reason code.

## Overview

`MotionReason` stores the reason the last motion stopped, as a numeric code (the firmware `MOTION_REASON_*` enumeration in `AG300_CTL01ParamsCommon.h:1662–1702`). It is reset to `0` (`MOTION_REASON_END_NONE`) when a new motion starts (`Begin`/homing/profiler restart, e.g. `AG300_CTL01ControlLoops.c:3009`, `AG300_CTL01Controller.c:2411`). It records the *original* stopping cause: the firmware writes the code at the moment a stop is first requested and the same move keeps decelerating, so if several stop conditions occur in sequence, only the first is reported. Use it together with [MotionStat](MotionStat.md) to diagnose how and why a move ended.

> **Documentation pending:** `MotionReason` is `implemented: partial`; some reason codes may not yet be fully implemented in all firmware versions.

## How it works

Each code is written by a distinct stop path. Codes 4–7 come from the profiler's limit handling (hardware RLS/FLS and software [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) checks, `AG300_CTL01Profiler.c:558`, `:566`, `:577`), homing codes 13/15/16 come from `AG300_CTL01Homing.c`, and the CNCA/CNCB/vector/spline "one member …" codes (18–40) are written when a group-member axis stops, aborts, or hits a limit. The value table is the firmware enumeration verbatim:

| Value | Constant | Function descriptions |
|----|----|----|
| 0 | `MOTION_REASON_END_NONE` | Current motion still not ended, or motion ended normally. |
| 1 | `MOTION_REASON_END_STOP` | Motion ended due to Stop command. |
| 2 | `MOTION_REASON_END_ABORT` | Motion ended due to Abort command. |
| 3 | `MOTION_REASON_END_STOP_REP` | Motion ended due to StopRep command. |
| 4 | `MOTION_REASON_END_RLS` | Motion ended due to reverse limit switch detection. |
| 5 | `MOTION_REASON_END_FLS` | Motion ended due to forward limit switch detection. |
| 6 | `MOTION_REASON_END_REV_PLIM` | Motion ended due to reverse software limit. |
| 7 | `MOTION_REASON_END_FWD_PLIM` | Motion ended due to forward software limit. |
| 8 | `MOTION_REASON_END_MOTOR_OFF` | Motion ended due to disabled motor. |
| 9 | `MOTION_REASON_END_STOP_ECAM` | Motion ended due to StopECAM command (for ECAM motions only). |
| 10 | `MOTION_REASON_END_STOP_FIFO` | Motion ended due to StopFIFO command (for FIFO motions only). |
| 11 | `MOTION_REASON_END_INDEX` | Motion ended due to detected index (for jogging only). |
| 12 | `MOTION_REASON_END_STOP_CNCA` | Motion ended due to StopCNCA command (for CNCA motions only). |
| 13 | `MOTION_REASON_HOMING_TIMEOUT` | Motion ended due to timeout at homing. |
| 14 | `MOTION_REASON_END_GO_TO_CURR` | Motion ended due to GoToCurrMode command. |
| 15 | `MOTION_REASON_HOMING_HARD_STOP` | Motion ended due to hardstop at homing. |
| 16 | `MOTION_REASON_END_HOME_CHANGE` | Motion ended due to home switch change. |
| 17 | `MOTION_REASON_END_GO_TO_FORCE` | Motion ended due to GoToForceMode command. |
| 18 | `..._CNC_ONE_MEMBER_WENT_MOTOR_OFF` | Motion ended due to one member of CNCA being disabled. |
| 19 | `..._CNC_ONE_MEMBER_WAS_STOPPED` | Motion ended due to one member of CNCA being stopped. |
| 20 | `..._CNC_ONE_MEMBER_WAS_ABORTED` | Motion ended due to one member of CNCA being aborted. |
| 21 | `MOTION_REASON_END_STOP_BY_INPUT` | Motion ended due to stop by input signal. |
| 22 | `MOTION_REASON_END_ABORT_BY_INPUT` | Motion ended due to abort by input signal. |
| 23 | `..._CNCA_ONE_MEMBER_HIT_RLS_FLS` | Motion ended due to one member of CNCA hitting the forward/reverse limit switch. |
| 24 | `..._CNCA_ONE_MEMBER_HIT_REV_FWD_PLIM` | Motion ended due to one member of CNCA hitting the forward/reverse software limit. |
| 25 | `MOTION_REASON_END_STOP_CNCB` | Motion ended due to StopCNCB command / one member of CNCB stopped. |
| 26 | `..._CNCB_ONE_MEMBER_HIT_RLS_FLS` | Motion ended due to one member of CNCB hitting the forward/reverse limit switch. |
| 27 | `..._CNCB_ONE_MEMBER_HIT_REV_FWD_PLIM` | Motion ended due to one member of CNCB hitting the forward/reverse software limit. |
| 28 | `..._CONTROLLED_STOP_BY_INPUT` | Motion ended due to controlled stop by input signal. |
| 29 | `MOTION_REASON_END_STOP_VEC` | Motion ended due to StopVec command. |
| 30 | `..._VEC_ONE_MEMBER_WENT_MOTOR_OFF` | Motion ended due to one member of vector being disabled. |
| 31 | `..._VEC_ONE_MEMBER_WAS_STOPPED` | Motion ended due to one member of vector being stopped. |
| 32 | `..._VEC_ONE_MEMBER_WAS_ABORTED` | Motion ended due to one member of vector being aborted. |
| 33 | `..._VEC_ONE_MEMBER_HIT_RLS_FLS` | Motion ended due to one member of vector hitting the forward/reverse limit switch. |
| 34 | `..._VEC_ONE_MEMBER_HIT_REV_FWD_PLIM` | Motion ended due to one member of vector hitting the forward/reverse software limit. |
| 35 | `..._END_STOP_SPLINE_BUFFER` | Motion ended due to StopBuff command. |
| 36 | `..._SPLINE_BUFFER_ONE_MEMBER_WENT_MOTOR_OFF` | Motion ended due to one member of spline buffer being disabled. |
| 37 | `..._SPLINE_BUFFER_ONE_MEMBER_WAS_STOPPED` | Motion ended due to one member of spline buffer being stopped. |
| 38 | `..._SPLINE_BUFFER_ONE_MEMBER_WAS_ABORTED` | Motion ended due to one member of spline buffer being aborted. |
| 39 | `..._SPLINE_BUFFER_ONE_MEMBER_HIT_RLS_FLS` | Motion ended due to one member of spline buffer hitting the forward/reverse limit switch. |
| 40 | `..._SPLINE_BUFFER_ONE_MEMBER_HIT_REV_FWD_PLIM` | Motion ended due to one member of spline buffer hitting the forward/reverse software limit. |

(Constants prefixed `...` share the `MOTION_REASON_END_` prefix; see `AG300_CTL01ParamsCommon.h:1662–1702`.)

## Changes between versions

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Highest reason code | 40 | **41** |
| Value 41 | not defined | **`MOTION_REASON_END_FWD_OR_REV_PLIM`** — motion ended at a forward *or* reverse software position limit (a single combined code). |

In **v5** a combined software-limit reason code 41 was added (`develop:CommonIncludes/AG300_CTL01ParamsCommon.h:1896`; written in `develop:CommonC/AG300_CTL01Profiler.c:935`). Codes 0–40 are unchanged. **v5 is central-i only.**

## Examples

```text
AMotionReason       ; read why the last motion stopped
```

If the motion was ended by an abort command, but during deceleration the forward software limit was exceeded, and then the limit switch was encountered, `MotionReason` will have a value of `2`, indicating the original reason to stop and ignoring any following events that could have stopped the motion.

## See also

- [MotionStat](MotionStat.md) — detailed bit-mapped motion status
- [Begin](../04-motion-command/Begin.md) — resets `MotionReason` to 0
- [Stop](../04-motion-command/Stop.md) / [Abort](../04-motion-command/Abort.md) / [StopRep](../04-motion-command/StopRep.md) — commands that set reason codes 1 / 2 / 3
- [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) / [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) — software limits behind reason codes 6 / 7
