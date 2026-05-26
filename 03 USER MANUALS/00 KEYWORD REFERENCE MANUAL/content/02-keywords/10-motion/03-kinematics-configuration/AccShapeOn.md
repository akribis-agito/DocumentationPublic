---
keyword: AccShapeOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 162
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
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeOn

**Definition:**

AccShapeOn enables the acceleration-shaping feature, which modifies the acceleration profile to reduce vibration by applying a shaped (filtered) acceleration curve. When set to a non-zero value the AccShapeDist and AccShapeFact arrays define the shaping profile. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[AccShapeDist](AccShapeDist.md), [AccShapeFact](AccShapeFact.md), [Accel](Accel.md)
