---
keyword: JerkInAcc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 720
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
  - 100
  - 1000000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# JerkInAcc

**Definition:**

JerkInAcc sets the jerk applied during the acceleration phase of a third-order (infinite-snap) motion profile, when JerkMode = 1. It controls the rate at which acceleration itself ramps up and down during the acceleration segment. It is an axis-related parameter.

%%
Needs verification
JerkInAcc was not found in the AG300_CTL01Params.c firmware parameter table. Confirm availability and parameter attributes before use.
%%

**See also:**

[JerkInDec](JerkInDec.md), [Jerk](Jerk.md), [JerkMode](../02-motion-configuration/JerkMode.md)
