---
keyword: Targets
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 376
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Targets

**Definition:**

Targets is an array that stores a sequence of target positions in user units for multi-target point-to-point motion. The controller moves through the entries in the array sequentially when executing a multi-segment PTP move. It is an axis-related array saved to flash and can be changed at any time.

**See also:**

[AbsTrgt](AbsTrgt.md), [RelTrgt](RelTrgt.md), [Begin](../04-motion-command/Begin.md)
