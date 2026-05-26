---
keyword: ProtectMask
summary: Bitfield enabling which hardware protection conditions trigger a fault.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 97
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProtectMask

Bitfield enabling which hardware protection conditions trigger a fault.

## Overview

`ProtectMask` is a bitfield that selects which hardware protection conditions are enabled: setting a bit to 1 enables the corresponding protection (so it will trigger a fault), and clearing it disables that protection. The bit positions correspond to the conditions reported by [HWProtectBits](HWProtectBits.md). It is axis-related, saved to flash, and may be changed at any time.

## Examples

```text
ProtectMask?        ; read which hardware protections are enabled
```

## See also

- [HWProtectBits](HWProtectBits.md) — reports the live state of these protections
