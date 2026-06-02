---
keyword: SpringPHigh
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 594
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# SpringPHigh

**Definition:**

SpringPHigh sets the upper position boundary, in user units, of the spring compensation region. Spring compensation is applied only while the position reference is within the band [SpringPLow](SpringPLow.md) to SpringPHigh; above SpringPHigh no spring current is added. It is an axis-related parameter saved to flash and can be changed at any time.

The default is 10000 user units. The band test compares the shaped, filtered position reference (the commanded profile, not the measured feedback position) against [SpringPLow](SpringPLow.md) and SpringPHigh, with both endpoints included. The boundaries are not range-checked against each other: if SpringPHigh is set below SpringPLow the band is empty and no spring compensation is ever applied.

**See also:**

[SpringPLow](SpringPLow.md), [SpringOn](SpringOn.md), [SpringTable](SpringTable.md), [SpringTableGp](SpringTableGp.md)
