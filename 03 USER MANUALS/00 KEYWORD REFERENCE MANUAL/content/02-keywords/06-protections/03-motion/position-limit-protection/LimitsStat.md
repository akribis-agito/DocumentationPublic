---
keyword: LimitsStat
summary: Read-only bitfield reporting reverse/forward limit-switch activation.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 49
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
# LimitsStat

Read-only bitfield reporting reverse/forward limit-switch activation.

## Overview

`LimitsStat` reports the current state of the hardware limit switches as a bitfield. A set bit (`1`) means that limit is active.

| Bit # | 0 | 1 | 2–31 |
|-------|---|---|------|
| Meaning | RLS (reverse limit switch) | FLS (forward limit switch) | Unused |

So `LimitsStat = 1` → RLS active; `LimitsStat = 2` → FLS active.

## Examples

```text
ALimitsStat         ; 1 = RLS active, 2 = FLS active, 3 = both
```

## See also

- [FwdPLim](FwdPLim.md) / [RevPLim](RevPLim.md) — software travel limits
