---
keyword: RegenOff
summary: DC bus-voltage threshold (mV) below which the regeneration resistor is deactivated.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 96
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
  range:
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides: {}
---
# RegenOff

DC bus-voltage threshold (mV) below which the regeneration resistor is deactivated.

## Overview

`RegenOff` sets the DC bus-voltage threshold (mV) at or below which the regeneration (braking-resistor) circuit is switched off. After the bus has risen past [RegenOn](RegenOn.md) and the brake-chopper transistor is conducting, the resistor keeps dissipating energy until the bus voltage [VBus](../01-system-variables/VBus.md) falls back to `RegenOff`, at which point the chopper is switched off. `RegenOff` is therefore the lower edge of the switching hysteresis.

## How it works

`RegenOff` is the partner of [RegenOn](RegenOn.md); both are evaluated in the same regeneration step (per-axis on central-i, controller-wide on a standalone controller) whenever [RegenUsed](RegenUsed.md) ≠ 0:

| Condition | Action |
|-----------|--------|
| `VBus ≥ RegenOn`  | Chopper ON, [StatReg](../../07-status-and-faults/StatReg.md) bit 1 set |
| `VBus ≤ RegenOff` | Chopper OFF, `StatReg` bit 1 cleared |
| `RegenOff < VBus < RegenOn` | No change — chopper holds state |

The comparison is `VBus ≤ RegenOff` (inclusive), so the resistor switches off the moment the bus reaches the threshold. The gap between `RegenOff` and `RegenOn` is the dead-band that prevents the chopper from chattering: make it wide enough to cover the bus-voltage ripple produced by the resistor switching. Set **`RegenOff` < `RegenOn`** — equal values remove the hysteresis, and `RegenOff` > `RegenOn` is not a valid configuration. See [RegenOn](RegenOn.md) for the hysteresis diagram.

## Examples

```text
ARegenOff=75000      ; deactivate regen once the bus falls back to 75 V (mV)
ARegenOff            ; read the present deactivation threshold
```

## See also

- [RegenOn](RegenOn.md) — activation threshold (upper edge of the hysteresis; holds the diagram)
- [RegenCurr](RegenCurr.md) — measured regen-resistor current while the chopper is on
- [RegenUsed](RegenUsed.md) — enables the regen circuit; thresholds are ignored when 0
- [VBus](../01-system-variables/VBus.md) — bus voltage compared against this threshold
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 1 reports regeneration active
