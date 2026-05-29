---
keyword: DynBrakeOn
summary: Enables electrical dynamic braking when the motor is off.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 405
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DynBrakeOn

Enables or disables electrical dynamic braking, which rapidly slows the motor when it is disabled.

## Overview

Dynamic braking is a purely electrical brake: it shorts the motor phases (through the low-side devices) and dissipates the back-EMF current, quickly slowing a motor that has just been disabled. Unlike the [static brake](Staticbrake.md), it needs no external hardware and is used to bleed off motion energy when the motor goes off.

`DynBrakeOn` is the enable switch. The default is **0** (disabled), so dynamic braking is opt-in.

| Value | Meaning |
|-------|---------|
| 0 | Dynamic braking disabled *(default)* |
| 1 | Dynamic braking enabled |

## How it works

When `DynBrakeOn ≠ 0`, the axis engages the dynamic brake each control cycle only while **all** of these hold:

1. `DynBrakeOn ≠ 0`;
2. the motor is **off** ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 0); and
3. no active fault prohibits dynamic braking (certain [ConFlt](../../07-status-and-faults/ConFlt.md) conditions, such as a ground short or power-stage fault, forbid it).

While engaged, the axis sets [StatReg](../../07-status-and-faults/StatReg.md) bit 28 (dynamic brake active) and modulates the shorting duty cycle to keep the braking current within the [PeakCL](../02-current-and-voltage/PeakCL.md)/[ContCL](../02-current-and-voltage/ContCL.md) limits; [DynBrkRef](DynBrkRef.md) sets the strongest-braking ceiling. If the motor is re-enabled, a forbidding fault appears, or the bus voltage gets too high, the brake releases and bit 28 clears.

Notes:

- Dynamic braking never fights an active current loop — it engages only when the motor is off.
- Engagement does not depend on [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md); it depends only on `DynBrakeOn`, the motor-off state, and the per-fault permission.
- With `DynBrakeOn = 0`, the brake never engages and [StatReg](../../07-status-and-faults/StatReg.md) bit 28 never sets.
- On the PWM amplifier, dynamic braking is supported on axes A and B (and C on the 3-axis product).

`DynBrakeOn` may be changed at any time, including with the motor on and while in motion (it simply has no effect until the motor is off).

## Examples

```text
ADynBrakeOn=1           ; enable dynamic braking on the axis
ADynBrakeOn            ; read back the setting
ADynBrakeOn=0           ; disable (default)
```

To configure both the enable and the braking strength:

```text
ADynBrakeOn=1
ADynBrkRef=1000         ; brake at full strength (100%) when engaged
```

## See also

- [Dynamic brake](Dynamicbrake.md) — overview of the dynamic-braking mechanism
- [DynBrkRef](DynBrkRef.md) — the maximum braking strength
- [Static brake](Staticbrake.md) — the separate mechanical holding brake
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 28 reports dynamic brake active
- [PeakCL](../02-current-and-voltage/PeakCL.md) / [ContCL](../02-current-and-voltage/ContCL.md) — current limits that bound the braking
