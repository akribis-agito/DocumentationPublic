---
keyword: BrakeMode
summary: "Selects how the static (holding) brake is engaged and released."
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 380
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# BrakeMode

Selects the engagement policy for the external static (holding) brake.

## Overview

`BrakeMode` chooses how the static brake — a fail-safe electromechanical device (de-energized = engaged/holding, energized = released) — is controlled. The choice ranges from fixed manual states, through motor-state-aware protection, to fully automatic timing tied to the motor-enable sequence or to a discrete input.

`BrakeMode` takes effect only when [BrakeUsed](BrakeUsed.md) = 1. The default is **2** (manual release, without protection). The lock request produced by the selected mode is mirrored in [StatReg](../../07-status-and-faults/StatReg.md) bit 29.

## How it works

The static-brake state machine runs each control cycle and applies the branch selected by `BrakeMode`:

| Value | Mode | Behaviour |
|-------|------|-----------|
| 0 | Manual lock | Always locks the brake (engaged), regardless of motor state. |
| 1 | Manual release, with protection | Releases the brake only while the motor is enabled; if the motor is off, the brake re-engages. |
| 2 | Manual release, without protection *(default)* | Always releases the brake (released), regardless of motor state. |
| 3 | Automatic by motor-on state | Released when the motor is enabled, engaged when disabled; the release and lock are timed by the motor-enable sequence using [BrakeRelTime](BrakeRelTime.md) and [BrakeLockTime](BrakeLockTime.md). |
| 4 | Automatic by discrete input, with protection | Driven from a discrete input configured for the static-brake-lock function: input asserted asks to lock (but the brake is kept released while in motion); input de-asserted asks to release (but the brake is kept locked while the motor is off). |

Notes on specific modes:

- **Modes 0/1/2 (manual):** if [BrakeUsed](BrakeUsed.md) is changed from 1 to 0 in a manual mode, the brake is left in its last commanded state (the axis stops driving the output).
- **Mode 3 (automatic by motor-on):** the release/lock and their delays are applied as part of the motor-enable/disable sequence — see [BrakeRelTime](BrakeRelTime.md) and [BrakeLockTime](BrakeLockTime.md). If the motor is enabled by a path other than the standard motor-on command, the brake is still released, but the release delay is not applied. While the motor is off in this mode the brake is held locked (protection).
- **Mode 4 (discrete input):** handled within the discrete-input function processing. It always keeps motion and motor-off states safe — the brake will not lock while the axis is in motion, and will not release while the motor is off, regardless of the input level.
- **Out-of-range value:** if `BrakeMode` is somehow outside 0–4, the axis falls back to the safe default and keeps the brake **locked**.

`BrakeMode` can be changed while the motor is enabled, but not while the axis is in motion.

## Examples

```text
ABrakeMode=3            ; automatic, timed by the motor-on sequence
ABrakeMode             ; read back the current mode
ABrakeMode=0            ; force the brake locked
ABrakeMode=2            ; force the brake released (default)
```

## See also

- [Static brake](Staticbrake.md) — overview of holding-brake control and timing
- [BrakeUsed](BrakeUsed.md) — enables the static-brake feature
- [BrakeRelTime](BrakeRelTime.md) / [BrakeLockTime](BrakeLockTime.md) — release and lock delays used by mode 3
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — drives the mode-3 release/lock timing
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 29 reports the static-brake lock request
