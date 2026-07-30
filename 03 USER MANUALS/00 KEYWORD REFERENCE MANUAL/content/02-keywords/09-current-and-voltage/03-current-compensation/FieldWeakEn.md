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

> **Worked example:** commanded to a speed well above its base speed, a test machine capped at 201.9 rad/s with the feature off. With `FieldWeakEn=1` the same drive reached 277.3 rad/s — **37 % higher** — at the same voltage limit. The extra speed was bought with 3 961 mA of d-axis current.

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
