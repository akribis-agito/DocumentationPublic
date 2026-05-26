---
keyword: Save
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 232
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Save

**Definition:**

Save command is used to save the parameters to a non-volatile (flash) memory. After the Save command is entered, previous parameter content area in the non-volatile memory is erased. Then, all the flash-saveable parameters are copied from the volatile memory to the flash.

Saving to flash is not allowed while motor is enabled.

Please refer to the attribute table to identify whether each parameter can be saved to/loaded from flash.
