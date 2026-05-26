---
keyword: LAmpFullScale
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 229
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LAmpFullScale

**Condition:** 

This keyword is only used when AmpType = 4 (reserved setting).

**Definition:**

LAmpFullScale is a reserved keyword for specific built-in linear amplifier product. It is used to select choice of full-scale current reference (CurrRef) over 10V output.

| LAmpFullScale | Full scale options |
|---------------|--------------------|
| 0             | 0.4A over 10V      |
| 1             | 1.2A over 10V      |
| 2             | 3.0A over 10V      |
