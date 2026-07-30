---
keyword: FieldWkAdapEn
summary: Scales the field-weakening gains by the stator-flux ratio as speed rises.
availability:
  standalone: []
  central-i:
  - v5
can_code: 874
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
  range: [0, 1]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# FieldWkAdapEn

Scales the field-weakening gains by the stator-flux ratio as speed rises.

## Overview

The field-weakening loop's ideal gain is not constant across the speed range — the relationship between voltage error and the d-axis current needed to correct it changes as the machine is weakened. `FieldWkAdapEn` makes the drive scale both loop gains by the ratio of the present stator flux to its unweakened value.

## How it works

With `FieldWkAdapEn=1` the drive computes the stator flux from the d- and q-axis currents and the actual inductances, and scales [FieldWeakKp](FieldWeakKp.md) and [FieldWeakKi](FieldWeakKi.md) by the square of its ratio to the unweakened flux. The ratio is bounded at 1, so the adaptive term only ever reduces the gains.

In region 2 a separate linear taper is applied to the q-axis limit instead.

> **Note:** this is the feature's designed operating mode. With adaptive scaling off, gains tuned at one point in the field-weakening range may be too aggressive or too slow elsewhere in it.

### Edge cases

- **No effect when disabled:** ignored unless [FieldWeakEn](FieldWeakEn.md) is 1.
- **Depends on inductance:** the flux computation uses the drive's derived d- and q-axis inductances, so [Lm](../04-motor-measurement/Lm.md) must be set correctly for the scaling to be meaningful.

## Examples

```text
AFieldWkAdapEn=1
```

## See also

- [FieldWeakEn](FieldWeakEn.md), [FieldWeakKp](FieldWeakKp.md), [FieldWeakKi](FieldWeakKi.md)
