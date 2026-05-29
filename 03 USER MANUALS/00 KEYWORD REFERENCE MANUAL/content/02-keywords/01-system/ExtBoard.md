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

`ExtBoard` tells the firmware which external expansion board is fitted to the controller, so it can configure the board's resources correctly. It is a non-axis parameter saved to flash; because it declares the fitted hardware, set it and then [Reset](02-operation/Reset.md) to ensure all board resources are fully reconfigured. It cannot be changed while the motor is on or in motion. On a controller with no expansion-board option the only valid value is `0` (no board); on hardware that supports an expansion board, a non-zero value selects the fitted board type.

## How it works

| Value | Meaning |
|-------|---------|
| 0 | No expansion board (default) |
| (non-zero) | A specific expansion-board type supported by the controller hardware — for example a higher-resolution analog-input (ADC) daughter board |

When `ExtBoard` selects a supported board, the firmware sets the corresponding board-enable bit in its hardware-settings register and adjusts the affected resources. For the higher-resolution ADC board, the full-scale range of the analog inputs ([AInPort](../05-inputs-outputs/02-analog-inputs/AInPort.md) 1-4) is changed from approximately +/-12175 mV to +/-12500 mV so the readings are scaled correctly. With `ExtBoard = 0` the enable bit is cleared and the default analog range is used.

The set of valid values is hardware-dependent: most controller variants accept only `0`, while variants that physically support the board also accept its selector value. Because the setting declares the fitted hardware, change it and reset to ensure all board resources are fully reconfigured before relying on them.

## Examples

```text
AExtBoard           ; query the configured expansion-board type
AExtBoard=0         ; no expansion board (default)
```

## See also

- [Reset](02-operation/Reset.md) — apply a changed `ExtBoard` setting
- [AInPort](../05-inputs-outputs/02-analog-inputs/AInPort.md) — analog-input port mapping
- [DInPort](../05-inputs-outputs/04-digital-inputs/DInPort-DInPortHigh.md) — digital-input port mapping
