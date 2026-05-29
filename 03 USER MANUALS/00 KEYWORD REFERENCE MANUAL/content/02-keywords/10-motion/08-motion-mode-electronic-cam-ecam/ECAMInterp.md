---
keyword: ECAMInterp
summary: Reserved internal ECAM keyword (not implemented).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 308
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# ECAMInterp

Reserved internal ECAM keyword (not implemented).

## Overview

`ECAMInterp` is a reserved keyword in the ECAM motion group, intended to select the interpolation mode used between cam-table entries. It is an array of 10 cam patterns, one element per pattern. Its valid range is fixed at `[0, 0]`, so the only accepted value is `0`.

The interpolation between successive [GenData](../../20-arrays/GenData.md) entries is currently always **linear** — the controller blends the two neighbouring table values by the fractional master position (see [ECAMGap](ECAMGap.md) for the mapping). No alternative interpolation mode is selectable.

The linear blend is carried at finer-than-one-sample resolution rather than stepping from one table entry to the next, so the follower reference advances smoothly between cam points. Because the follower velocity (and the velocity/acceleration feedforward derived from it) is the per-cycle change of that reference, this sub-sample blend is what keeps the commanded velocity continuous across table points instead of jumping at each entry. It is also why two consecutive cam-table entries may not differ by more than the internal per-sample limit (see [ECAMGap](ECAMGap.md)): the limit bounds how fast the reference can change in one control cycle.

> **Documentation pending:** `ECAMInterp` is currently reserved and not implemented (`implemented: not_implemented`). It accepts only `0`; no value-dependent behaviour is defined.

## Examples

```text
AECAMInterp[1]      ; read the (reserved) interpolation mode for cam pattern 1
```

## See also

- [ECAMGap](ECAMGap.md) — master-to-index mapping and the linear interpolation applied
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
