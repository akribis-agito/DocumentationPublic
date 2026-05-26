---
keyword: ProductSN
summary: Array storing the unit's product serial number (persisted to flash).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 468
attributes:
  access: rw
  scope: non-axis
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
---
# ProductSN

Array storing the unit's product serial number (persisted to flash).

## Overview

`ProductSN` is a three-element array that stores the product serial number of the controller. It is written to flash (with special handling) and can be read back at any time, uniquely identifying a hardware unit in production or field-service contexts. Because it is saved to flash, the serial number persists across power cycles.

## Examples

```text
ProductSN[0]?       ; read the first word of the product serial number
```

## See also

- [Identity](Identity.md) — controller identification and features
- [UnitStat](UnitStat.md) — unit hardware/firmware health
