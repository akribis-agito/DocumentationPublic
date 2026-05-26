---
keyword: ProductSN
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

**Definition:**

ProductSN is an array that stores the product serial number of the controller. It can be written to flash (with special handling) and read back at any time, and is used to uniquely identify a hardware unit in a production or field-service context.

**See also:**

[Identity](Identity.md), [UnitStat](UnitStat.md)
