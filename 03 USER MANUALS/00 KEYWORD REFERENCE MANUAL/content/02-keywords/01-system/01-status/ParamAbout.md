---
keyword: ParamAbout
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 499
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ParamAbout

**Definition:**

ParamAbout is an axis-related function that returns descriptive information about a specified parameter, including its CAN code, mnemonic name, attribute flags, range, and default value. It is intended for host software and diagnostic tools that need to enumerate or inspect parameter metadata at runtime.

**See also:**

[About](About.md), [Identity](Identity.md), [ParamCS](ParamCS.md)
