---
keyword: PTPKeepMoving
summary: Lets a new Begin blend into the existing move instead of stopping first.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 625
attributes:
  access: rw
  scope: axis
  flash: false
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
# PTPKeepMoving

Lets a new `Begin` blend into the existing move instead of stopping first.

## Overview

`PTPKeepMoving` controls what happens when a new [Begin](../04-motion-command/Begin.md) command is issued before the previous point-to-point move has completed. When set to `1`, the axis blends smoothly into the new target ([AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)) without first stopping, which is useful for on-the-fly retargeting. When `0`, a new `Begin` is only accepted after the current move finishes. It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## How it works

In a normal point-to-point move the profiler declares the motion finished once it reaches the target and its speed is low enough — it enters the profile-smoothing tail ([MotionStat](../05-motion-status/MotionStat.md) bit 6) and eventually clears the in-motion bits of `MotionStat`. With `PTPKeepMoving = 1` the controller **skips that end-of-motion test entirely**, so the axis stays in the in-motion state and the profiler keeps tracking [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) indefinitely (the same behaviour also keeps the endless joystick-position modes running).

Because the motion never reports "done", a fresh `Begin` (with a new `AbsTrgt`/`RelTrgt`) retargets the already-running profiler, and the profiler ramps toward the new target from the current speed instead of starting from rest — producing the blend. With `PTPKeepMoving = 0` the move completes normally, so a `Begin` issued during it is governed by the usual in-motion rules.

This affects only point-to-point modes ([MotionMode](MotionMode.md) `= 1`); it has no effect on jog, gear, ECAM or the other modes.

## Examples

```text
APTPKeepMoving=1     ; blend into a new target without stopping
APTPKeepMoving=0     ; require the move to complete first
APTPKeepMoving      ; query state
```

## See also

- [Begin](../04-motion-command/Begin.md) — starts (or retargets) the move
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — absolute target position
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — relative target position
- [MotionMode](MotionMode.md) — applies only to point-to-point (mode 1)
- [MotionStat](../05-motion-status/MotionStat.md) — the in-motion bits that `PTPKeepMoving` keeps set
