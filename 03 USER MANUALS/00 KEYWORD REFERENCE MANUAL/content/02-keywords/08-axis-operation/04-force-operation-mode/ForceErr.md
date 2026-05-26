---
keyword: ForceErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 583
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
# ForceErr

**Definition:**

ForceErr is the difference between force reference (ForceRef) and force feedback (Force).

$$
ForceErr\ \lbrack unit\rbrack\  = \ ForceRef\ \lbrack unit\rbrack\  - \ Force\ \lbrack unit\rbrack
$$

It is used in force control loop.
