---
keyword: VBusRatio
summary: 'Read-only: the voltage-scaling ratio DC-bus feedforward is currently applying.'
availability:
  standalone: []
  central-i:
  - v5
can_code: 879
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 10
  default: 1.0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# VBusRatio

Read-only: the voltage-scaling ratio DC-bus feedforward is currently applying.

## Overview

`VBusRatio` reports the factor by which the drive is presently scaling its voltage output to compensate for bus movement. It is the observable that shows whether [AdVBusEn](AdVBusEn.md) is doing anything, and how hard.

```text
VBusRatio = nominal bus at motor-on / filtered measured bus
```

## How it works

- **1.0** — the bus is at the value latched at motor-on; no compensation is being applied.
- **Greater than 1.0** — the bus has sagged and the drive is scaling its output up.
- **Less than 1.0** — the bus is above nominal, typically during braking regeneration, and the drive is scaling down.

> **Note:** the value is clamped to the compensator's authority of **[0.8, 1.2]**. A reading pinned at 1.2 means the bus has sagged further than the feature is permitted to correct — useful diagnostic information, because it says the supply, not the compensation, is the limit.

> **Worked example:** through a hard acceleration on a weak supply the ratio was observed rising from 1.0000 to 1.2000 and holding there while the bus continued to fall. Everything past that point was uncompensated.

### Using it

Record `VBusRatio` alongside [VBus](VBus.md) when diagnosing an axis on a suspect supply. A ratio that spends time at its clamp is direct evidence that the supply is undersized for the move, and no amount of tuning will substitute for a stiffer bus.

### Edge cases

- **Read-only:** writes are rejected.
- **Defaults to 1.0**, not 0, so the value is neutral before the first control cycle rather than reading as full attenuation.
- **Reads 1.0 when disabled:** with [AdVBusEn](AdVBusEn.md) at 0 the ratio is not computed and stays at 1.0.

## Examples

```text
VBusRatio?            ; report the current ratio
```

## See also

- [AdVBusEn](AdVBusEn.md) — enables the feature this reports on
- [VBus](VBus.md) — the measured bus voltage
