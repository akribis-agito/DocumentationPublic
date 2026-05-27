---
keyword: BiDirConfig
summary: Bitfield configuring each bi-directional I/O pin as an input or an output.
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

Bitfield configuring each bi-directional I/O pin as an input or an output.

## Overview

`BiDirConfig` sets the direction of the controller's bi-directional I/O pins — which pins act as inputs and which as outputs. Each bit of the value corresponds to one bi-directional channel. It is saved to flash and can be changed at any time. Configure pin direction here before using the digital-input or digital-output keywords for those channels.

## Examples

```text
ABiDirConfig        ; read the current direction configuration
```

## See also

- [DInPort-DInPortHigh](../04-digital-inputs/DInPort-DInPortHigh.md) — digital-input port states
- [DOutPort](../05-digital-outputs/DOutPort.md) — digital-output port states
