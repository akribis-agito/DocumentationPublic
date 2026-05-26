---
keyword: PowerSupply
summary: Declares the drive's power-supply type so protections behave correctly.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 401
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 3
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# PowerSupply

Declares the drive's power-supply type so protections behave correctly.

## Overview

`PowerSupply` tells the amplifier what type of power supply feeds it, so that bus-voltage and related protections operate correctly. Select the value matching your hardware (typically via the PCSuite configuration page). It cannot be changed while the motor is on or in motion.

| Value | Supply type |
|-------|-------------|
| 1 | Single-phase AC |
| 2 | DC |
| 3 | Three-phase AC |

## Examples

```text
PowerSupply=2       ; DC supply
```

## See also

- [MaxVBus](MaxVBus.md) / [MinVBus](MinVBus.md) — bus-voltage limits
