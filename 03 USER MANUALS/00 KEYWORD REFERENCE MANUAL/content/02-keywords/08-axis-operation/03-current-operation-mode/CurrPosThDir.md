---
keyword: CurrPosThDir
summary: Trigger direction for the CurrPosTh position-reference check.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 427
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrPosThDir

Trigger direction for the CurrPosTh position-reference check.

## Overview

`CurrPosThDir` defines the trigger direction for the first condition check (position reference) used to enter current operation mode, together with the threshold [CurrPosTh](CurrPosTh.md). It is used only while the axis is in velocity or position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2 or 3).

## How it works

| CurrPosThDir | Descriptions                                         |
|--------------|------------------------------------------------------|
| \< 0         | First condition is fulfilled if `PosRef` < `CurrPosTh`. |
| 0            | First condition is fulfilled (unconditionally).       |
| \> 0         | First condition is fulfilled if `PosRef` > `CurrPosTh`. |

## Examples

```text
ACurrPosThDir=-1     ; trigger when PosRef < CurrPosTh
ACurrPosTh=50000     ; position-reference threshold
```

## See also

- [CurrPosTh](CurrPosTh.md) — the position-reference threshold
- [Current operation mode](00-overview.md) — full mode-switching conditions
