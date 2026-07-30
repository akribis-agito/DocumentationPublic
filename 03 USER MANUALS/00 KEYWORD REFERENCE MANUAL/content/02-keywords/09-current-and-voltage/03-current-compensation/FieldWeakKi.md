---
keyword: FieldWeakKi
summary: Integral gain of the field-weakening outer loop.
availability:
  standalone: []
  central-i:
  - v5
can_code: 872
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
  range: [0, 100]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# FieldWeakKi

Integral gain of the field-weakening outer loop.

## Overview

`FieldWeakKi` is the integral term of the field-weakening regulator. It accumulates the voltage error and is what actually drives the d-axis current negative and holds it at its working point.

Like [FieldWeakKp](FieldWeakKp.md), the value is normalised against [CurrBw](CurrBw.md).

## How it works

While the voltage vector is saturated the integrator accumulates, driving the d-axis command more negative until the machine can reach the commanded speed. The accumulator is bounded at zero on one side — field weakening never commands *positive* d-axis current — and at the demagnetising limit derived from [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) on the other.

> **Note:** the integrator needs time to reach its working point. A test or measurement that samples only a short window after enabling field weakening will catch the loop mid-transient and understate what the feature does.

> **Worked example:** on a round machine with a 4 mH phase inductance, enabling field weakening with `FieldWeakKi=2.0` raised the reachable speed from 201.9 to 277.3 rad/s — a 37 % increase — by settling the d-axis current at −3 961 mA. That settling took roughly 15 000 control cycles. On a salient machine of the same mean inductance the same gain reached 315.7 rad/s (57 %) and settled at only −3 446 mA.

### Edge cases

- **Anti-windup:** the d-axis integral continues to integrate while the voltage vector is saturated — which is precisely when the loop must act — with its own explicit bounds rather than the current loop's usual clamping.
- **No effect when disabled:** ignored unless [FieldWeakEn](FieldWeakEn.md) is 1.
- **Range:** writes outside `0…100` are clamped.

## Examples

```text
AFieldWeakKi=2.0
```

## See also

- [FieldWeakKp](FieldWeakKp.md) — the proportional term
- [FieldWkAdapEn](FieldWkAdapEn.md) — adaptive scaling of both gains
