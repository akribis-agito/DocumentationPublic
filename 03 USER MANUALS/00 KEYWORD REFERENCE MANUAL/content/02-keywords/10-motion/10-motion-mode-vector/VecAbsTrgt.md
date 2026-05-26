---
keyword: VecAbsTrgt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 642
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
# VecAbsTrgt

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

The VecAbsTrgt is a status parameter that reports the target distance (from start of motion to its
end) of the vector motion along the vector path. VecAbsTrgt is always positive.

The VecAbsTrgt is not used to define the vector motion. This is done using the RelTrgt or AbsTrgt

of the member axes.
