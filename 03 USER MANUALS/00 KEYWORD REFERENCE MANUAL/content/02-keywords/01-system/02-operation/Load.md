---
keyword: Load
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 233
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
# Load

**Definition:**

Load command is used to retrieve all the parameters from the non-volatile (flash) memory and is performed once internally upon power up. Running Load command will not cause power cycle.

Please refer to the attribute table to identify whether each parameter can be saved to/loaded from flash.

**Note:**

Load will overwrite all unsaved changes in volatile memory. As a use case, in case of bad and unsaved parameter settings, user can use Load to revert to good parameter settings saved in flash.
