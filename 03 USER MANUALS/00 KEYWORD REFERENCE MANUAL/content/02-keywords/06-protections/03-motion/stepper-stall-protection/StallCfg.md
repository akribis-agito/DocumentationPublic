---
keyword: StallCfg
summary: Configures the stepper stall-detection mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 513
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallCfg

Configures the stepper stall-detection mode.

## Overview

`StallCfg` enables stepper stall detection and selects what happens on a stall. It is the master switch for the whole stepper stall-protection group ([StallThPcnt](StallThPcnt.md), [StallCnst](StallCnst.md), and the read-only [StallStat](StallStat.md), [StallVal](StallVal.md), [StallTh](StallTh.md)).

## How it works

`StallCfg` gates the per-sample stall logic. When it is `0` the detection block is skipped entirely; otherwise the metric/threshold are computed and a stall is declared when `StallVal < StallTh`:

| Value | Behaviour |
|-------|-----------|
| 0 | Detection disabled; metric and threshold are not evaluated |
| 1 | Detection runs; on stall, [StallStat](StallStat.md) is set and the `StatReg` stall bit is set, but the motor is **not** turned off |
| 2 | Detection runs; on stall, the above status is set **and** the axis is turned off, recording stall fault code `1065` |

On a detected stall the firmware always sets [StallStat](StallStat.md) `= 1` and sets the stall bit of [StatReg](../../../07-status-and-faults/StatReg.md) (bit 31, `0x80000000`). Only in mode 2 does it additionally turn the axis off and log the fault. When the metric recovers, the stall bit is cleared and `StallStat` returns to `0`.

Stall detection only operates on stepper motors driven by the internal amplifier.

## Examples

```text
AStallCfg[1]=2        ; enable stall detection and turn motor off on stall
AStallCfg[1]=1        ; alert-only (set status, keep running)
AStallCfg[1]=0        ; disable
```

## See also

- [StallStat](StallStat.md) — stall status flag set when a stall is detected
- [StallThPcnt](StallThPcnt.md) — stall sensitivity (percent)
- [StallCnst](StallCnst.md) — speed-dependent threshold coefficients
- [StatReg](../../../07-status-and-faults/StatReg.md) — stall bit (bit 31, `0x80000000`) set on stall
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records stall fault code 1065 in mode 2
