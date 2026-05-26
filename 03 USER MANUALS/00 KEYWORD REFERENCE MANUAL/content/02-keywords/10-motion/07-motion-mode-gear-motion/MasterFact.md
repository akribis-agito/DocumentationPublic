---
keyword: MasterFact
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 120
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
  - -16777215
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterFact

**Definition:**

MasterFact is the numerator used in the scaling ratio applied onto the delta of master variable. Once the gear motion is started, the final change in profiler position reference (if [MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) = 5) or target position (AbsTrgt if [MotionMode](../../../02-keywords/10-motion/02-motion-configuration/MotionMode.md) = 6) is as shown.

$$
\mathrm{\Delta}_{ProfilerPosRef/AbsTrgt} = \mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}\ 
$$
