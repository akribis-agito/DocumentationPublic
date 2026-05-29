---
keyword: RegenUsed
summary: Selects whether an external or internal regeneration resistor is used.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 378
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
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# RegenUsed

Selects whether an external or internal regeneration resistor is used.

## Overview

`RegenUsed` configures whether the regeneration (braking-resistor) circuit is used, matching the controller to the connected hardware. It is a 0/1 setting (default 1). Because it is a hardware-configuration setting, it cannot be changed while the axis is in motion or the motor is on, and it is saved to flash. The thresholds [RegenOn](RegenOn.md) / [RegenOff](RegenOff.md) only take effect when `RegenUsed` is non-zero.

## How it works

`RegenUsed` is an enable gate for the whole regeneration mechanism. In the regeneration step (per-axis on central-i, controller-wide on a standalone controller) the controller evaluates the [RegenOn](RegenOn.md) / [RegenOff](RegenOff.md) thresholds **only if `RegenUsed` ≠ 0**:

| `RegenUsed` | Behaviour |
|-------------|-----------|
| 0 | Regeneration disabled. The brake-chopper command and [StatReg](../../07-status-and-faults/StatReg.md) bit 1 are forced clear, the threshold comparisons are skipped, and the "regeneration active" digital output always reads inactive. |
| 1 (default) | Regeneration enabled. The chopper switches according to the `RegenOn` / `RegenOff` hysteresis around [VBus](../01-system-variables/VBus.md). |

Writing `RegenUsed = 0` takes effect immediately: the chopper command and the regeneration status bit (on every axis on a standalone controller) are cleared at the moment the value is written, so an already-active resistor is switched off without waiting for the next regen step.

> **Note:** disabling regeneration removes the bus-voltage dissipation path. With no regen resistor, hard decelerations can drive [VBus](../01-system-variables/VBus.md) into the over-voltage protection ([MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../../06-protections/02-current-and-voltage/MaxVBusAbs.md)) and trip the axis.

## Examples

```text
ARegenUsed=1         ; enable the regen circuit (default)
ARegenUsed=0         ; disable regeneration (chopper forced off)
ARegenUsed           ; read the present setting
```

## See also

- [RegenOn](RegenOn.md), [RegenOff](RegenOff.md) — regen activation/deactivation thresholds (active only when this is non-zero)
- [RegenCurr](RegenCurr.md) — measured regen-resistor current
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 1 reports regeneration active
