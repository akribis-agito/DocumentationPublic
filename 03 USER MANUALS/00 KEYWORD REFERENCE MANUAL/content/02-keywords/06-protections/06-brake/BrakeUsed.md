---
keyword: BrakeUsed
summary: Enables or disables control of an external static (holding) brake.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 379
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
  range:
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# BrakeUsed

Declares whether an external static (holding) brake is present and should be driven by the axis.

## Overview

`BrakeUsed` is the master switch for the static-brake feature. A static brake is an external, fail-safe electromechanical device (de-energized = engaged/holding, energized = released) that holds a load when the axis is off. Set `BrakeUsed = 1` when such a brake is wired to the axis; set `BrakeUsed = 0` when no brake is fitted.

When `BrakeUsed = 0`, the axis never drives release voltage to the (absent) device, so all of the static-brake handling — including the [BrakeMode](BrakeMode.md) policy and the [BrakeRelTime](BrakeRelTime.md)/[BrakeLockTime](BrakeLockTime.md) timing — has no electrical effect.

This keyword applies to the static brake only. The electrical [dynamic brake](Dynamicbrake.md) is controlled separately by [DynBrakeOn](DynBrakeOn.md).

| Value | Meaning |
|-------|---------|
| 0 | No static brake (the axis drives no release voltage) |
| 1 | Static brake present and controlled by the axis *(default)* |

## How it works

Each control cycle the axis runs the static-brake state machine selected by [BrakeMode](BrakeMode.md). All of its branches act only when `BrakeUsed ≠ 0`; with `BrakeUsed = 0` the brake output is left unchanged in the manual modes (see below).

- **Disabling a present brake (`1 → 0`) in a manual mode** ([BrakeMode](BrakeMode.md) 0/1/2): the axis simply stops driving the brake output and leaves it in its last commanded state. The brake hardware then holds whatever state it was in until power is removed.
- **Disabling a present brake (`1 → 0`) in automatic-by-motor mode** ([BrakeMode](BrakeMode.md) 3): the axis cannot wait for the next motor-on/off sequence, so it locks the brake immediately and sets the lock request in [StatReg](../../07-status-and-faults/StatReg.md) bit 29.
- While `BrakeUsed = 1`, the lock request is mirrored in [StatReg](../../07-status-and-faults/StatReg.md) bit 29, and a motion command issued while the brake is locked is rejected (the axis reports a "can't start motion while the static brake is locked" error).

`BrakeUsed` cannot be changed while the motor is enabled; disable the axis first.

## Examples

```text
ABrakeUsed=1            ; declare a static brake on the axis
ABrakeUsed             ; read back the setting
ABrakeUsed=0            ; no static brake fitted
```

Typical vertical-axis setup, enabling the brake and selecting automatic timing:

```text
ABrakeUsed=1
ABrakeMode=3            ; automatic by motor-on state
```

## See also

- [Static brake](Staticbrake.md) — overview of holding-brake control and timing
- [BrakeMode](BrakeMode.md) — how the brake is engaged/released
- [BrakeRelTime](BrakeRelTime.md) / [BrakeLockTime](BrakeLockTime.md) — release and lock delays (mode 3)
- [DynBrakeOn](DynBrakeOn.md) — the separate electrical dynamic brake
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 29 reports the static-brake lock request
