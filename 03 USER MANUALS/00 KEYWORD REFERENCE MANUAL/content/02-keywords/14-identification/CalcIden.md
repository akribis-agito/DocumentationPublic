---
keyword: CalcIden
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 128
attributes:
  access: ro
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CalcIden

**Condition:**

CalcIden is only applicable to sine sweep identification.

**Definition:**

CalcIden is the command that instructs the controller to calculate sinusoidal relation (at [InjectFreq](../../02-keywords/13-injection/InjectFreq.md)) between the internally recorded input and output data. The input and output data must have at least 30 data points and at most 250 data points each.

Once the calculation is complete, controller will return “OK” message and the results are stored in IdenResults.
