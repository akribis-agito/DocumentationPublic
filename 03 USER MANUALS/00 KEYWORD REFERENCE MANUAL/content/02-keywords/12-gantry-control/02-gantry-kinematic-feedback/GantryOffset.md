---
keyword: GantryOffset
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 653
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryOffset

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

The GantryOffset is a read-only parameter.

AGantryOffset is calculated once when AGantryOn is switched by the user from 0 to 1.
AGantryOffset = APosRef ­ BPosRef.

The GantryOffset is later used for the calculation of the GantryFdbk readings, so that the initial
offset between the readings of the two encoders is ignored.

The actual calculation is:
AGantryFdbk is equal to (APos + BPos + AGantryOffset) / 2
BGantryFdbk is equal to (APos ­ BPos - AGantryOffset)

?GantryOffset with "?" not equal to "A" has no use and will always returns a value of 0.
