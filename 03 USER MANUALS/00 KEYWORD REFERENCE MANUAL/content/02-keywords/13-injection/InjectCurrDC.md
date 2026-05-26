---
keyword: InjectCurrDC
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 126
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
  - -32000
  - 32000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectCurrDC

**Condition:**

InjectCurrDC is only applicable for injection at current command (InjectPoint = 0), in direct injection mode (see InjectType for more information).

**Definition:**

InjectCurrDC is the offset of the current injection value, in terms of mA.
