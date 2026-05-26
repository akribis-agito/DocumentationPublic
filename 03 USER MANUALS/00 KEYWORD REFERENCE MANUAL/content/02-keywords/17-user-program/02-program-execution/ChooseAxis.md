---
keyword: ChooseAxis
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 563
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ChooseAxis

**Definition:**

ChooseAxis is a per-thread array parameter that selects which physical axis a user-program thread will operate on. Each thread index maps to an axis number, allowing multi-threaded programs to direct axis-specific commands independently. The array size equals the maximum number of concurrent threads.

**See also:**

[Load](Load.md), [Reset](Reset.md)
