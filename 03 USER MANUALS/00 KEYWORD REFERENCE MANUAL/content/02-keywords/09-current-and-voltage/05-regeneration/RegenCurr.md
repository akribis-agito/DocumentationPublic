---
keyword: RegenCurr
summary: Read-only current flowing through the regeneration resistor.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 349
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# RegenCurr

Read-only current flowing through the regeneration resistor.

## Overview

`RegenCurr` is a read-only status value that reports the current flowing through the regeneration (braking) resistor. It lets you monitor how much energy the regen circuit is dissipating during braking, when the bus voltage has risen above [RegenOn](RegenOn.md) and the brake-chopper transistor is conducting. It reads near zero when the chopper is off. It is not saved to flash.

## How it works

On products that have regen-current sensing, the regen current is read once per group of control cycles and the raw ADC count is converted to a current with a fixed scale-and-offset. The conversion is an affine map of the form `RegenCurr = offset − gain × reading` — i.e. the sensor sits around a mid-scale zero point, so the raw count is scaled by a fixed gain and subtracted from a constant offset to give a signed result. Products without regen-current sensing do not update this value.

The value is meaningful only while regeneration is active (when [StatReg](../../07-status-and-faults/StatReg.md) bit 1 is set); at other times the resistor is disconnected and the reading reflects only the sensor's zero point.

## Examples

```text
ARegenCurr          ; read the present regen-resistor current
```

## Changes between versions

On central-i v5 `RegenCurr` is reported as a **floating-point** value (`float32`, no fixed integer range) rather than the scaled integer used on v4. The underlying measurement is the same; only the data type returned over communication changes, so a v5 read may include a fractional part.

## See also

- [RegenOn](RegenOn.md), [RegenOff](RegenOff.md) — regen activation/deactivation thresholds
- [RegenUsed](RegenUsed.md) — enables the regen circuit
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 1 indicates regeneration is active
