---
keyword: ExtBoard
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 612
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ExtBoard

**Definition:**

ExtBoard selects the hardware configuration for the external expansion board attached to the controller. Setting this parameter to the appropriate board type enables the firmware to correctly initialize and use the expansion board's I/O resources. It is saved to flash and takes effect after reset.

**See also:**

[AInPort](../09-current-and-voltage/01-system-variables/AInPort.md), [DInPort](../09-current-and-voltage/01-system-variables/DInPort.md)
