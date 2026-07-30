---
keyword: FieldWeakKp
summary: Proportional gain of the field-weakening outer loop.
availability:
  standalone: []
  central-i:
  - v5
can_code: 873
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range: [0, 1]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# FieldWeakKp

Proportional gain of the field-weakening outer loop.

## Overview

Field weakening regulates a negative d-axis current from the *voltage error* — how much voltage headroom remains between the commanded voltage vector and the drive's limit. `FieldWeakKp` is the proportional term of that regulator.

The drive normalises the value you set against the current-loop bandwidth [CurrBw](CurrBw.md), so the gain is comparable across machines with very different electrical time constants.

## How it works

Once the voltage vector saturates, the outer loop computes a d-axis current command from the voltage error using `FieldWeakKp` and [FieldWeakKi](FieldWeakKi.md). The proportional term sets how quickly the loop responds to a change in headroom; the integral term is what walks the d-axis current to its working point and holds it there.

> **Note:** in practice the integral term does most of the work. The proportional term chiefly affects how the loop behaves as the machine first crosses into saturation.

### Tuning

Tune with [FieldWeakEn](FieldWeakEn.md) enabled, accelerating through the base speed, and watch the d-axis current settle. Too much proportional gain makes the d-axis command jittery as the drive crosses in and out of saturation.

> **Important:** the d-axis current this loop commands opposes the magnet. Before tuning, set [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) from the motor's reversible demagnetisation limit **at operating temperature**. Beyond that limit the magnet is permanently weakened and the motor does not recover.

### Edge cases

- **No effect when disabled:** ignored unless [FieldWeakEn](FieldWeakEn.md) is 1.
- **Range:** writes outside `0…1` are clamped.

## Examples

```text
AFieldWeakKp=0.10
```

## See also

- [FieldWeakKi](FieldWeakKi.md) — the integral term
- [FieldWeakEn](FieldWeakEn.md) — master enable
- [CurrBw](CurrBw.md) — the bandwidth these gains are normalised against
