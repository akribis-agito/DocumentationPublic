---
keyword: DualStuckVel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 157
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
  - 0
  - 1300000000
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualStuckVel

**Definition:**

DualStuckVel is the maximum absolute velocity difference between the two feedback in dual-loop tolerable by the controller. It is in count/s where the count refers to the main (or position-loop) feedback count.

**Formula:**

$$
Absolute\ velocity\ difference = abs\left( Vel\lbrack 2\rbrack - \frac{AuxVel \bullet DualLoopFact}{65536} \right)
$$
