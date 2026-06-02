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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# PTPKeepMoving

Lets a new `Begin` blend into the existing move instead of stopping first.

## Overview

`PTPKeepMoving` controls what happens when a new [Begin](../04-motion-command/Begin.md) command is issued before the previous point-to-point move has completed. When set to `1`, the axis blends smoothly into the new target ([AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)) without first stopping, which is useful for on-the-fly retargeting. When `0`, a new `Begin` is only accepted after the current move finishes. It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## How it works

In a normal point-to-point move the profiler declares the motion finished once it reaches the target and its speed is low enough — it enters the profile-smoothing tail ([MotionStat](../05-motion-status/MotionStat.md) bit 6) and eventually clears the in-motion bits of `MotionStat`. With `PTPKeepMoving = 1` the controller **skips that end-of-motion test entirely**, so the axis stays in the in-motion state and the profiler keeps tracking [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) indefinitely.

Because the motion never reports "done", a fresh `Begin` (with a new `AbsTrgt`/`RelTrgt`) retargets the already-running profiler, and the profiler ramps toward the new target from the current speed instead of starting from rest — producing the blend. With `PTPKeepMoving = 0` the move completes normally, so a `Begin` issued during it is governed by the usual in-motion rules.

The same point-to-point profiler is shared by single PTP ([MotionMode](MotionMode.md) `= 1`) and repetitive PTP (`MotionMode = 2`), so `PTPKeepMoving` is consulted in both. For repetitive PTP it should be left at `0`: setting it to `1` suppresses the end-of-segment completion, so a segment never reports done, [RptCounter](../05-motion-status/RptCounter.md) never increments, and the repetition cannot advance. The joystick-position modes (`MotionMode = 12` and `13`) are independently endless and are not influenced by `PTPKeepMoving`. It has no effect on jog, gear, ECAM or the other modes.

![PTPKeepMoving blend vs restart](ptpkeepmoving-blend.svg)

## Examples

```text
APTPKeepMoving=1     ; blend into a new target without stopping
APTPKeepMoving=0     ; require the move to complete first
APTPKeepMoving      ; query state
```

### Worked example: on-the-fly retarget

```text
AMotionMode=1        ; PTP
APTPKeepMoving=1     ; allow blend
AAbsTrgt=100000      ; first target
ABegin               ; start the move
; ... while the axis is still moving toward 100000:
AAbsTrgt=140000      ; profiler retargets to the new value, no stop, no re-Begin
```

Without `PTPKeepMoving = 1` the second `AAbsTrgt` would simply be parked for the next move — the running move would still target the original 100000. With it set, the profiler reads the updated `AbsTrgt` each cycle and ramps the axis to the new destination, blending the trajectory.

For incremental retargets, writing [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) while the axis is in motion **and** `PTPKeepMoving = 1` automatically adds the written `RelTrgt` to the current `AbsTrgt` (so the blend shifts by that increment). The update is applied atomically, so it stays correct even if a `ModRev` wrap occurs at the same moment — this is the intended way to do incremental on-the-fly retargets while `ModRev` is active. Outside of in-motion blending, writing `AbsTrgt` clears `RelTrgt` to `0`.

### Edge cases

- **Motor off:** the parameter is held; it is read on the next `Begin`.
- **Out-of-range write:** the parameter system rejects values outside `0`–`1`.
- **Simulation mode (`MotorType` = 5):** behaviour is identical (the profiler runs in simulation).
- **ModRev wrap:** blends work through a wrap because the wrap shifts both `AbsTrgt` and the reference state by `ModRev` together; the blend ramps toward the post-wrap target.
- **Active fault:** the axis is disabled and the in-motion bits are cleared regardless of `PTPKeepMoving`.
- **Repetitive PTP (`MotionMode = 2`):** leave `PTPKeepMoving = 0`. Because the repetitive mode shares the PTP profiler and its end-of-segment test, setting `PTPKeepMoving = 1` suppresses segment completion and stops the repetition advancing — [RptCounter](../05-motion-status/RptCounter.md) never increments. Repetition is otherwise governed by [RptCounter](../05-motion-status/RptCounter.md)/[RptCycles](RptCycles.md) and [StopRep](../04-motion-command/StopRep.md).
- **Stop/Abort:** `Stop` and `Abort` end the motion regardless of `PTPKeepMoving` (the stop-request bit takes priority).

## See also

- [Begin](../04-motion-command/Begin.md) — starts (or retargets) the move
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — absolute target position
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — relative target position
- [MotionMode](MotionMode.md) — applies to point-to-point (mode 1) and repetitive PTP (mode 2)
- [MotionStat](../05-motion-status/MotionStat.md) — the in-motion bits that `PTPKeepMoving` keeps set
