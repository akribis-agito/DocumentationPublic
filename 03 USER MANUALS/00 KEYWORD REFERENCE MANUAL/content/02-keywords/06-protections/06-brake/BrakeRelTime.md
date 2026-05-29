---
keyword: BrakeRelTime
summary: "Delay after releasing the static brake before motion is allowed (BrakeMode 3)."
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 382
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
  scaling: 1.0
  implemented: final
overrides: {}
---
# BrakeRelTime

Sets the static-brake **release** delay — how long the axis waits after releasing the brake before allowing motion.

## Overview

A holding brake takes a finite time to physically open after it is energized. `BrakeRelTime` is the time the axis waits, after commanding the brake to release, before it permits motion. This protects the start of a move: the profiler is not allowed to run until the brake has had time to open, so the motor does not have to fight a partly-engaged brake.

`BrakeRelTime` is active **only** when [BrakeMode](BrakeMode.md) = 3 (automatic by motor-on state). In the other modes the value is stored but has no effect.

The value is a time in **milliseconds**, settable from about **10 ms to 800 ms**, defaulting to **100 ms**. (Internally the time is held in control samples; the controller converts your millisecond value to samples.)

## How it works

In [BrakeMode](BrakeMode.md) = 3, the standard motor-on sequence:

1. enables the motor;
2. commands the static brake to release (energize) and clears the lock request in [StatReg](../../07-status-and-faults/StatReg.md) bit 29;
3. arms a timer for `BrakeRelTime` and waits for it to elapse;
4. only then returns, allowing motion to be commanded.

Because the wait happens inside the enable sequence, motion you queue immediately after enabling the axis will not begin until the brake-release window has passed.

`BrakeRelTime` protects the **enable → motion** transition; the complementary [BrakeLockTime](BrakeLockTime.md) protects the **stop → disable** transition. Do not set `BrakeRelTime` to 0 in mode 3 — the timing logic relies on a non-zero delay; keep it at least a few milliseconds (the minimum is around 10 ms).

## Examples

```text
ABrakeUsed=1
ABrakeMode=3            ; automatic by motor-on state
ABrakeRelTime=200       ; wait 200 ms after release before allowing motion
ABrakeRelTime          ; read back the configured release delay
```

If a move stutters or the axis lurches at the very start of motion, increase `BrakeRelTime` so the brake is fully open before the profiler starts.

## See also

- [Static brake](Staticbrake.md) — overview, including the mode-3 timing diagram
- [BrakeLockTime](BrakeLockTime.md) — the complementary lock (engage) delay
- [BrakeMode](BrakeMode.md) — must be 3 for this delay to apply
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — the enable sequence that applies the delay
