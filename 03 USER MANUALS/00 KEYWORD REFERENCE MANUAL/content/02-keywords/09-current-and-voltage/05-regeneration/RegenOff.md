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
  scope: non-axis
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
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

The regeneration thresholds are not tested on every control cycle. The controller services its periodic checks in a 16-step round-robin (one step per control interrupt), and the `RegenOn`/`RegenOff` comparison runs in one of those steps — so `VBus` is compared against the thresholds once every 16 control interrupts. The chopper can therefore switch with a delay of up to 16 control-interrupt periods after `VBus` crosses a threshold. Size the dead-band (`RegenOn` − `RegenOff`) so the bus voltage cannot swing back across the opposite threshold within that interval, which keeps the chopper from chattering.

On a standalone controller `RegenOn` and `RegenOff` share their default, minimum, and maximum with [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md). In the factory default both thresholds equal the `MaxVBus` default, so there is no hysteresis gap and the activation point coincides with the over-voltage limit. You must lower `RegenOff` (and usually `RegenOn`) yourself to create a usable dead-band below `MaxVBus` before relying on the regen circuit.

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
