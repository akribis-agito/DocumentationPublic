---
summary: CNC vector deceleration used for an emergency stop.
---
# CNCAEmrgDec/CNCBEmrgDec

CNC path deceleration used for an emergency stop.

## Overview

`CNCAEmrgDec` (and its `CNCBEmrgDec` counterpart on the second CNC group) is the deceleration of the CNC path-velocity profile used when an **emergency stop** of the group is triggered, in user units per second squared. It is normally set larger than the per-segment deceleration so the path can be brought to rest quickly. It is a non-axis parameter and can be set at any time.

An emergency stop is triggered when any member axis of the group reaches a travel limit: a hardware reverse/forward limit switch, or a software position limit (`RevPLim`/`FwdPLim`).

## How it works

When a member axis hits a limit while the group is moving, the controller requests a stop along the path for the whole group and switches the path-velocity profile from the normal deceleration [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) to `CNCAEmrgDec` for the remainder of the braking. Because the single path velocity is shared, every member axis brakes together along the path, preserving the geometry while stopping.

The effective emergency rate is scaled by the square of the on-the-fly time-scaling factor [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md), the same way the normal deceleration is scaled: effective rate = `CNCAEmrgDec × (CNCAPercents/100)²`.

The stop is also visible on the member axes:

- [MotionStat](../05-motion-status/MotionStat.md) shows the ending state (bit 12 for group A, bit 15 for group B) during the stop.
- [MotionReason](../05-motion-status/MotionReason.md) records the cause: for group A, `23` (a member hit a hardware limit switch) or `24` (a member hit a software position limit); for group B, `26` or `27` respectively.

### CNCB note

`CNCBEmrgDec` is the identical emergency-stop deceleration for the independent second CNC group.

## Examples

```text
ACNCAEmrgDec=2000000 ; emergency-stop path deceleration on group A
ACNCBEmrgDec=2000000 ; emergency-stop path deceleration on group B
```

## See also

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — normal active-segment deceleration
- [StopCNCA](StopCNCA.md) / [StopCNCB](StopCNCB.md) — request a controlled stop of the group
- [MotionReason](../05-motion-status/MotionReason.md) — codes 23/24 (group A), 26/27 (group B) for limit-triggered stops
- [MotionStat](../05-motion-status/MotionStat.md) — group ending bits 12 (A) / 15 (B)
