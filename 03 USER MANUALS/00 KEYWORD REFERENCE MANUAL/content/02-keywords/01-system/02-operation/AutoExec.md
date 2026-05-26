---
keyword: AutoExec
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 208
attributes:
  access: rw
  scope: non-axis
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
# AutoExec

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

`AutoExec = 1` will cause the user program to start executing automatically on power up or after software restart.

The [Save](Save.md) command must be used before reset to save the value of `AutoExec` to flash memory.
