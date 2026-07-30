---
keyword: FieldWeakEn
summary: Enables field weakening, allowing operation above the base speed.
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

# FieldWeakEn

Enables field weakening, allowing operation above the base speed.

## Overview

Every motor has a *base speed*: the speed at which its own back-EMF consumes the whole DC bus, leaving no voltage to drive current. Above it the machine stops accelerating regardless of what is commanded.

Field weakening commands a **negative d-axis current**, which opposes the magnet flux and lowers the back-EMF, so the same bus reaches a higher speed. `FieldWeakEn` is the master switch.

## How it works

With `FieldWeakEn=0` the entire outer loop is skipped and the current-loop output is bit-identical to a drive without the feature. With `FieldWeakEn=1` the loop operates in one of three regions:

| Region | Condition | Behaviour |
|---|---|---|
| 0 | Voltage headroom remains | Inactive, d-axis current 0 |
| 1 | Headroom exhausted | d-axis current regulated from the voltage error |
| 2 | d-axis current at its limit | Held at the limit, q-axis limit tapered down |

> **Note:** below the base speed the feature costs nothing. The drive is not voltage limited there, so the outer loop commands zero d-axis current and behaves exactly as if disabled.

> **Worked example:** with `FieldWeakEn = 0` the outer loop is skipped entirely and `Id` is held at 0, so the current-loop output is identical to a drive built without the feature.
>
> Set `FieldWeakEn = 1` and nothing changes yet: below the base speed the voltage vector is not saturated, the loop stays in region 0, and it still commands `Id = 0`. Once the vector saturates, `Id` is driven negative until either the voltage error is nulled (region 1) or `Id` reaches the limit derived from [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) — at which point `Id` is held there and the q-axis limit is tapered instead (region 2).

> **Important:** how much extra speed this buys is a property of **your motor**, not of the firmware. It follows from the flux linkage, the d/q inductance ratio, and how much demagnetising current the magnet tolerates at temperature — a salient interior-magnet machine gains substantially more than a round surface-magnet one. For measured figures across machine geometries, see the *Current-Loop Compensation* application note. Do not size a machine from a number in this manual.

### Preconditions

> **Important:** field weakening cannot arm unless the motor is characterised. The drive derives the magnet flux linkage from [MotForceConst](../../02-motor-and-amplifier/MotForceConst.md) and [MagneticPitch](../../02-motor-and-amplifier/MagneticPitch.md) for a linear motor, or from [MotTorqConst](../../02-motor-and-amplifier/MotTorqConst.md) and [PolePrs](../../02-motor-and-amplifier/PolePrs.md) for a rotary one. Left at defaults, the flux linkage is meaningless and the loop stays inactive whatever this keyword is set to.

### Safety

> **Important:** the d-axis current opposes the magnet. Past the knee of the magnet's B–H curve the flux loss is **permanent** — the motor returns weaker than it started, and no amount of subsequent care recovers it. The knee also falls with temperature, so a setting that is safe on a cold bench can damage a hot machine.
>
> Set [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) from the motor's reversible limit at operating temperature before enabling this feature, and consult the motor manufacturer if that figure is not on the data sheet.

### Edge cases

- **Torque falls:** d-axis current occupies part of the current budget, so the available q-axis current — and therefore torque — is reduced. This is the trade the feature makes, not a fault.
- **Machines that cannot be weakened:** a motor whose characteristic current far exceeds its current rating has little field-weakening headroom. Low-inductance ironless motors fall into this category.

## Examples

```text
AFieldWeakEn=1        ; enable, after characterising the motor and setting CurrLimRev
```

## See also

- [FieldWeakKp](FieldWeakKp.md), [FieldWeakKi](FieldWeakKi.md) — the loop gains
- [FieldWkAdapEn](FieldWkAdapEn.md) — adaptive gain scaling
- [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) — bounds the demagnetising current
