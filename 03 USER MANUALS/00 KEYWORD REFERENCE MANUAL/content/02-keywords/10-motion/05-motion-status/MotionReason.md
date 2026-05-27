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

`MotionReason` stores the reason the motion was stopped and is reset to `0` upon a [Begin](../04-motion-command/Begin.md) command. It records the *original* stopping cause: if several stop conditions occur in sequence, only the first is reported. Use it together with [MotionStat](MotionStat.md) to diagnose how and why a move ended.

> **Documentation pending:** `MotionReason` is `implemented: partial`; some reason codes may not yet be fully implemented in all firmware versions.

## How it works

| Value | Function descriptions |
|----|----|
| 0 | Current motion still not ended or motion ended normally. |
| 1 | Motion ended due to Stop command |
| 2 | Motion ended due to Abort command |
| 3 | Motion ended due to StopRep command |
| 4 | Motion ended due to reverse limit switch detection |
| 5 | Motion ended due to forward limit switch detection |
| 6 | Motion ended due to reverse software limit |
| 7 | Motion ended due to forward software limit |
| 8 | Motion ended due to disabled motor |
| 9 | Motion ended due to StopECAM command (for ECAM motions only) |
| 10 | Motion ended due to Stop FIFO command (for FIFO motions only) |
| 11 | Motion ended due to detected index (for Jogging only) |
| 12 | Motion ended due to StopCNCA command (for CNCA motions only) |
| 13 | Motion ended due to timeout at homing |
| 14 | Motion ended due to GoToCurrMode command |
| 15 | Motion ended due to hardstop at homing |
| 16 | Motion ended due to home switch change |
| 17 | Motion ended due to GoToForceMode command |
| 18 | Motion ended due to one member of CNCA was disabled |
| 19 | Motion ended due to one member of CNCA was stopped |
| 20 | Motion ended due to one member of CNCA was aborted |
| 21 | Motion ended due to stop by input signal |
| 22 | Motion ended due to abort by input signal |
| 23 | Motion ended due to one member of CNCA hitting the forward/reverse limit switch |
| 24 | Motion ended due to one member of CNCA hitting the forward/reverse software limit |
| 25 | Motion ended due to one member of CNCB was stopped |
| 26 | Motion ended due to one member of CNCB hit the forward/reverse limit switch |
| 27 | Motion ended due to one member of CNCB hit the forward/reverse software limit |
| 28 | Motion ended due to controlled stop by input signal |
| 29 | Motion ended due to StopVec command |
| 30 | Motion ended due to one member of vector was disabled |
| 31 | Motion ended due to one member of vector was stopped |
| 32 | Motion ended due to one member of vector was aborted |
| 33 | Motion ended due to one member of vector hit the forward/reverse limit switch |
| 34 | Motion ended due to one member of vector hit the forward/reverse software limit |
| 35 | Motion ended due to StopBuff command |
| 36 | Motion ended due to one member of spline buffer was disabled |
| 37 | Motion ended due to one member of spline buffer was stopped |
| 38 | Motion ended due to one member of spline buffer was aborted |
| 39 | Motion ended due to one member of spline buffer hit the forward/reverse limit switch |
| 40 | Motion ended due to one member of spline buffer hit the forward/reverse software limit |

## Examples

```text
AMotionReason       ; read why the last motion stopped
```

If the motion was ended by an abort command, but during deceleration the forward software limit was exceeded, and then the limit switch was encountered, `MotionReason` will have a value of `2`, indicating the original reason to stop and ignoring any following events that could have stopped the motion.

## See also

- [MotionStat](MotionStat.md) — detailed bit-mapped motion status
- [Begin](../04-motion-command/Begin.md) — resets `MotionReason` to 0
- [Stop](../04-motion-command/Stop.md) / [StopRep](../04-motion-command/StopRep.md) — commands that set specific reason codes
