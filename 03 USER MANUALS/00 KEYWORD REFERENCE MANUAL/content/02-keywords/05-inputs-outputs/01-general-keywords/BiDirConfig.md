---
keyword: BiDirConfig
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 495
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BiDirConfig

**Definition:**

BiDirConfig configures the direction of bi-directional I/O pins on the controller, specifying which pins are used as inputs and which as outputs. Each bit in the value corresponds to one bi-directional channel. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[DInPort-DInPortHigh](../04-digital-inputs/DInPort-DInPortHigh.md), [DOutPort](../05-digital-outputs/DOutPort.md)
