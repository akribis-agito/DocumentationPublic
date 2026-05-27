---
keyword: HWProtectBits
summary: Read-only bitfield reporting active hardware protection conditions.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 74
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
# HWProtectBits

Read-only bitfield reporting active hardware protection conditions.

## Overview

`HWProtectBits` is a read-only bitfield reporting the current state of the controller's hardware protection inputs. Each bit corresponds to a specific hardware protection condition (such as over-current, over-voltage, or a hardware enable signal). It is axis-related, updated live, and not saved to flash. Which of these conditions actually trigger a fault is selected by [ProtectMask](ProtectMask.md).

## Examples

```text
AHWProtectBits      ; read the active hardware protection conditions
```

## See also

- [ProtectMask](ProtectMask.md) — enables which protections trigger a fault
