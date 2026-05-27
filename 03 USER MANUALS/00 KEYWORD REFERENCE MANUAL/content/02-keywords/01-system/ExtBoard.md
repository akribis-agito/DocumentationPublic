---
keyword: ExtBoard
summary: Selects the hardware configuration of the attached external expansion board.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Selects the hardware configuration of the attached external expansion board.

## Overview

`ExtBoard` selects the hardware configuration for an external expansion board attached to the controller. Setting it to the appropriate board type lets the firmware correctly initialise and use the board's I/O resources. It is saved to flash and takes effect after a [Reset](02-operation/Reset.md). It cannot be changed while the motor is on or in motion.

## Examples

```text
AExtBoard           ; query the configured expansion-board type
```

## See also

- [AInPort](../05-inputs-outputs/02-analog-inputs/AInPort.md) — analog-input port mapping
- [DInPort](../05-inputs-outputs/04-digital-inputs/DInPort-DInPortHigh.md) — digital-input port mapping
