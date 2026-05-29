---
keyword: BrakeLockTime
summary: Delay after engaging the static brake before the motor is disabled (BrakeMode 3).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 381
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: scaling
  range:
  - 655
  - 13107
  default: 1638
  scaling: 65.536
  implemented: final
overrides: {}
---
# BrakeLockTime

Sets the static-brake **lock** delay — how long the axis keeps the motor energized after engaging the brake, before disabling the motor.

## Overview

A holding brake takes a finite time to physically engage after it is de-energized. `BrakeLockTime` is the time the axis holds the motor energized (still able to hold position/torque) after commanding the brake to lock, before it actually disables the motor. This protects the disable transition: the load is held by the motor until the brake has had time to grip, so it does not drop in the gap between "brake commanded" and "brake engaged".

`BrakeLockTime` is active **only** when [BrakeMode](BrakeMode.md) = 3 (automatic by motor-on state). In the other modes the value is stored but has no effect.

The value is a time in **milliseconds**, settable from about **10 ms to 800 ms**, defaulting to **100 ms**. (Internally the time is held in control samples; the controller converts your millisecond value to samples.)

## How it works

In [BrakeMode](BrakeMode.md) = 3, when the motor is disabled (and the axis is currently enabled), the sequence:

1. commands the static brake to lock (de-energize) and arms a timer for `BrakeLockTime` while the motor stays energized;
2. keeps the motor energized until the timer elapses — the motor continues to hold the load during this window;
3. when the timer elapses, sets the lock request in [StatReg](../../07-status-and-faults/StatReg.md) bit 29 and disables the motor.

The bit-29 set and the motor disable happen together when the lock timer elapses, not at the moment the lock is commanded.

`BrakeLockTime` protects the **stop → disable** transition; the complementary [BrakeRelTime](BrakeRelTime.md) protects the **enable → motion** transition. Do not set `BrakeLockTime` to 0 in mode 3 — the timing logic relies on a non-zero delay; keep it at least a few milliseconds (the minimum is around 10 ms).

## Examples

```text
ABrakeUsed=1
ABrakeMode=3            ; automatic by motor-on state
ABrakeLockTime=350      ; hold the motor 350 ms after engaging the brake, then disable
ABrakeLockTime         ; read back the configured lock delay
```

If the load drops or sags when the axis is disabled, increase `BrakeLockTime` so the brake fully engages before the motor torque is removed.

## See also

- [Static brake](Staticbrake.md) — overview, including the mode-3 timing diagram
- [BrakeRelTime](BrakeRelTime.md) — the complementary release delay
- [BrakeMode](BrakeMode.md) — must be 3 for this delay to apply
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — the disable sequence that applies the delay
