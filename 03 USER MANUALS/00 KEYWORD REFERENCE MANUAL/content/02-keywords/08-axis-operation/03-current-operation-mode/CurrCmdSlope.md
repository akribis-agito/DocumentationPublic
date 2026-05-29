---
keyword: CurrCmdSlope
summary: Ramp rate (mA/s) toward each current-command table entry.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 568
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# CurrCmdSlope

Ramp rate (mA/s) toward each current-command table entry.

## Overview

`CurrCmdSlope` defines the slope for the transition from the starting `CurrRef` value to the active [CurrCmdVal](CurrCmdVal.md) entry, in milliamperes per second. It is applicable only when [CurrCmdSrc](CurrCmdSrc.md) = 1 or 2. The holding timer [CurrCmdCntr](CurrCmdCntr.md) only begins counting from 0 once the ramp completes. The array is indexed 1 to 20, paired one-for-one with the `CurrCmdVal` / `CurrCmdHTime` entries.

## How it works

Each control cycle the controller adds (or subtracts, depending on whether `CurrRef` is below or above the target) an increment of `CurrCmdSlope[index] x sample_time` to `CurrRef`, moving it toward `CurrCmdVal[index]`:

- The fractional part of each per-cycle increment is carried over in an internal remainder accumulator, so the effective ramp rate is exact even when the per-cycle step is below 1 mA.
- While `CurrRef` is still ramping (not yet equal to the target), [CurrCmdCntr](CurrCmdCntr.md) is forced to 0; only once `CurrRef` exactly equals `CurrCmdVal[index]` does the holding timer start incrementing.
- When the ramp reaches or overshoots the target in a cycle, `CurrRef` is snapped to `CurrCmdVal[index]` and the remainder accumulator is cleared.

Because the slope is applied independently per entry, the rate into each `CurrCmdVal` step can differ. On standalone/v4 the minimum value is 1 (a slope of 0 is not allowed, which guarantees the ramp always progresses); central-i v5 lowers the minimum to a near-zero value, so fractional sub-1 mA/s slopes are allowed (see [Changes between versions](#changes-between-versions)).

## Examples

```text
ACurrCmdSlope[3]=700 ; ramp into entry 3 at 700 mA/s
```

Worked example — if `CurrCmdIndex` = 2, `CurrCmdCntr` = `CurrCmdHTime[2]` (end of the current entry), `CurrRef` = `CurrCmdVal[2]` = 340, `CurrCmdVal[3]` = -500, and `CurrCmdSlope[3]` = 700, then the ramp from 340 mA to -500 mA starts and completes in 1.2 seconds.

### Edge cases

- **Index 0** — invalid; valid indices are `CurrCmdSlope[1]`–`CurrCmdSlope[20]`. `CurrCmdSlope[0]` does not exist.
- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 1 or [CurrCmdSrc](CurrCmdSrc.md) ∉ {1, 2}) — the slope is **not consulted**; stored but unused.
- **Out of range** — `0` and negative values are rejected. On standalone/v4 the minimum is `1` to guarantee progress; central-i v5 lowers the minimum to a near-zero value, allowing fractional sub-1 mA/s slopes.
- **Large slope** — values that would produce a per-cycle step larger than the remaining distance to the target cause `CurrRef` to snap to the target on the next cycle; the holding timer starts immediately.
- **Reload mid-ramp** — writing a new slope on the active entry changes the rate from the next cycle; the remainder accumulator is preserved so there is no discontinuity.
- **Save** — flash-saveable.
- **Platform** — v5 stores as `float32` with no upper limit; v4 stores as `int32` up to `2 147 483 647`.

## Changes between versions

central-i v5 stores `CurrCmdSlope` as a 32-bit float. This both removes the fixed upper range limit and lowers the minimum from 1 to a near-zero value, so fractional sub-1 mA/s slopes become possible (standalone/v4: 32-bit integer, range 1 to 2147483647).

## See also

- [CurrCmdVal](CurrCmdVal.md) — target current values
- [CurrCmdHTime](CurrCmdHTime.md) — holding times per entry
- [CurrCmdCntr](CurrCmdCntr.md) — timer that starts after the ramp
