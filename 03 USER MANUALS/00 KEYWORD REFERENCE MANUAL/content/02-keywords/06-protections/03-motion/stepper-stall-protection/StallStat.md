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

`StallStat` is a read-only flag reporting the stepper stall-detection result: `0` = no stall, `1` = stall detected. It is the status output of the stall-protection group enabled by [StallCfg](StallCfg.md).

## How it works

When [StallCfg](StallCfg.md) is non-zero, the firmware compares the live metric against the threshold every control sample and sets `StallStat` accordingly:

```text
if StallVal < StallTh
    StallStat = 1
    if StallCfg = 2 (motor-off mode)
        turn the axis off and log the stall fault
    set the StatReg stall bit (bit 31)
else
    clear the StatReg stall bit
    StallStat = 0
```

So `StallStat` is set whenever the filtered metric [StallVal](StallVal.md) drops below the computed threshold [StallTh](StallTh.md), in **both** alert-only ([StallCfg](StallCfg.md) = 1) and motor-off ([StallCfg](StallCfg.md) = 2) modes. It mirrors bit 31 of [StatReg](../../../07-status-and-faults/StatReg.md) (`0x80000000`). When the metric recovers above the threshold the flag clears automatically. With detection disabled ([StallCfg](StallCfg.md) = 0) the flag is not updated; it is reset to `0` when the motor goes off.

### Edge cases

- **Motor off:** the detection block does not run; `StallStat`, [StallVal](StallVal.md), and [StallTh](StallTh.md) are all reset to `0`.
- **Non-stepper / external amplifier:** the metric is not generated, so `StallStat` stays at `0` regardless of [StallCfg](StallCfg.md).
- **Untuned [StallCnst](StallCnst.md):** if the speed-fit coefficients are at defaults, `StallTh` does not track speed correctly and `StallStat` may toggle unpredictably.
- **Mode 2 (motor-off):** the axis is disabled with [ConFlt](../../../07-status-and-faults/ConFlt.md) code 1065; `StallStat` clears on re-enable (along with the [StatReg](../../../07-status-and-faults/StatReg.md) bit 31).

## Examples

```text
AStallStat[1]         ; 0 = no stall, 1 = stall detected
```

## See also

- [StallCfg](StallCfg.md) — enables detection and whether a stall also turns the motor off
- [StallVal](StallVal.md) / [StallTh](StallTh.md) — the metric and threshold whose comparison sets this flag
- [StatReg](../../../07-status-and-faults/StatReg.md) — stall bit (bit 31, `0x80000000`) mirrors this flag
