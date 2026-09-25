---
keyword: PushEvSelect
summary: Per-axis bitmask of the push-event types to send.
availability:
  standalone: []
  central-i:
  - v5
can_code: 908
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvSelect

Per-axis bitmask of the push-event types to send.

## Overview

`PushEvSelect` chooses which [push-event](00-overview.md) types the controller detects on each axis. It applies to event types whose scope is **axis**. Controller-wide types are selected in [PushEvSelSys](PushEvSelSys.md). Nothing is sent unless [PushEvEnable](PushEvEnable.md) is also 1.

The keyword is an axis-related array of two 32-bit masks. It is saved to flash with [Save](../02-operation/Save.md). The default is 0, so no type is selected.

| Index | Event types |
|---|---|
| `[1]` | types 1-32: type *k* is bit *k*−1 |
| `[2]` | types 33-64: type *k* is bit *k*−33 |

Arrays are 1-indexed; `PushEvSelect[0]` does not exist.

## Event types

| Type | Bit | Mask in `[1]` | Name |
|---|---|---|---|
| `1` | 0 | `1` | Profile ended — the axis stopped being commanded to move. See the [overview](00-overview.md#event-types) for its data fields |

Type 1 is the only type in this release. Bits for other types are stored but have no effect. Because each index is a signed 32-bit value, a mask with bit 31 set (type 32 or type 64) is written as a negative number.

## Examples

```text
APushEvSelect[1]=1   ; axis A: send Profile ended
CPushEvSelect[1]=1   ; axis C: the same
APushEvSelect[1]=0   ; axis A: send nothing
APushEvSelect[1]     ; read axis A's mask for types 1-32
```

## See also

- [Push Events overview](00-overview.md) — the event catalogue and packet format
- [PushEvEnable](PushEvEnable.md) — master switch
- [PushEvSelSys](PushEvSelSys.md) — the equivalent mask for controller-wide event types
