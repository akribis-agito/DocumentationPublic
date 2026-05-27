---
keyword: StallThPcnt
summary: Stepper stall threshold as a percentage (10–90%, default 50%).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 512
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
  - 10
  - 90
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# StallThPcnt

Stepper stall threshold as a percentage (10–90%, default 50%).

## Overview

`StallThPcnt` sets, as a percentage (valid 10–90, default 50), what fraction of the expected healthy metric counts as a stall. It is the user-facing sensitivity knob for stepper stall detection: it directly scales the computed threshold [StallTh](StallTh.md) against which the live metric [StallVal](StallVal.md) is compared.

## How it works

Each control sample the firmware multiplies the speed-dependent expected-metric fit by `StallThPcnt/100` when forming [StallTh](StallTh.md) (firmware `CommonC/AG300_CTL01ControlLoops.c:2526`):

```c
ThFiltInput = (StallThPcnt * ldPosRefBitShifted) * 0.01 * 0.001
              * (StallCnst[1]*ldPosRefBitShifted + StallCnst[2]) - 10000;
```

The `* 0.01` term is the `/100` that turns the percentage into a fraction. A stall is then declared when `StallVal < StallTh`.

Because `StallTh` rises with `StallThPcnt`:

- **Higher `StallThPcnt`** raises the threshold, so it is easier for `StallVal` to fall below it → **more sensitive** (and more prone to false trips).
- **Lower `StallThPcnt`** lowers the threshold → **less sensitive** (the metric must collapse further before a stall is flagged).

The valid range is 10–90 % (firmware `STALLTHPCNT_MIN`/`MAX`), default 50 %.

## Examples

```text
AStallThPcnt[1]=50    ; threshold at 50% of the expected healthy metric
AStallThPcnt[1]       ; read back
```

## See also

- [StallTh](StallTh.md) — the resulting (read-only) threshold this percentage scales
- [StallCnst](StallCnst.md) — the speed-dependent fit that the percentage scales
- [StallVal](StallVal.md) — metric compared against `StallTh`
- [StallCfg](StallCfg.md) — stall-detection mode (enables this protection)
