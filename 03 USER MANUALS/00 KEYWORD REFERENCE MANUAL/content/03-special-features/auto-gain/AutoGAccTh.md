---
keyword: AutoGAccTh
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 353
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# AutoGAccTh

**Definition:**

AutoGAccTh sets the acceleration threshold in user units per second squared below which motion data is excluded from the auto-gain identification process. It filters out low-excitation segments that may produce unreliable inertia estimates. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGVelTh](AutoGVelTh.md), [AutoGOn](AutoGOn.md), [AutoGMinLen](AutoGMinLen.md)
