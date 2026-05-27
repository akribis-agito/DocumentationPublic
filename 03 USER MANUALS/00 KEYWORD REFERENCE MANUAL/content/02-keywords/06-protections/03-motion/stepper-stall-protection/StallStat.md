---
keyword: StallStat
summary: Read-only stepper stall status flag (0 = no stall, 1 = stalled).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 514
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallStat

Read-only stepper stall status flag (0 = no stall, 1 = stalled).

## Overview

`StallStat` is a read-only flag reporting the stepper stall-detection result: `0` = no stall (`STALL_DETECTION_NOT_OCCURED`), `1` = stall detected (`STALL_DETECTION_OCCURED`). It is the status output of the stall-protection group enabled by [StallCfg](StallCfg.md).

## How it works

When [StallCfg](StallCfg.md) is non-zero, the firmware compares the live metric against the threshold every control sample and sets `StallStat` accordingly (firmware `CommonC/AG300_CTL01ControlLoops.c:2531`):

```c
if (StallVal < StallTh)
{
    StallStat = STALL_DETECTION_OCCURED;     // 1
    if (StallCfg == STALL_DETECTION_ON_WITH_MOTOR_OFF)
        MotorOffAndAddToErrorLog(axis, CON_FLT_STALL_DETECTED_AND_MOTOR_OFF, true);
    StatReg |= STAT_REG_STALL_SET;           // bit 31
}
else
{
    StatReg &= STAT_REG_STALL_CLEAR;
    StallStat = STALL_DETECTION_NOT_OCCURED; // 0
}
```

So `StallStat` is set whenever the filtered metric [StallVal](StallVal.md) drops below the computed threshold [StallTh](StallTh.md), in **both** alert-only (`StallCfg = 1`) and motor-off (`StallCfg = 2`) modes. It mirrors bit 31 of [StatReg](../../../07-status-and-faults/StatReg.md) (`STAT_REG_STALL`, `0x80000000`). When the metric recovers above the threshold the flag clears automatically. With detection disabled (`StallCfg = 0`) the flag is not updated; it is reset to `0` when the motor goes off (`AG300_CTL01ControlLoops.c:2697`).

## Examples

```text
AStallStat[1]         ; 0 = no stall, 1 = stall detected
```

## See also

- [StallCfg](StallCfg.md) — enables detection and whether a stall also turns the motor off
- [StallVal](StallVal.md) / [StallTh](StallTh.md) — the metric and threshold whose comparison sets this flag
- [StatReg](../../../07-status-and-faults/StatReg.md) — bit 31 (`0x80000000`) mirrors this flag
