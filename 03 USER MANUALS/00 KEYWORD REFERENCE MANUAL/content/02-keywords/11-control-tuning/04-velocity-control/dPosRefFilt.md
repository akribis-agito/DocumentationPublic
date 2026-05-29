---
keyword: dPosRefFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 106
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
  - 20000
  - 1000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides: {}
---
# dPosRefFilt

Cutoff frequency of the first-order low-pass filter applied to the reference velocity (the derivative of the position reference).

## Overview

`dPosRefFilt` sets the cutoff frequency of a first-order low-pass filter that smooths the reference velocity [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) — the derivative of the position reference — before it is used as the velocity feed-forward. The filtered reference velocity is then scaled by [VelTrackFact](VelTrackFact.md) and added to the position-controller output to form the velocity-loop reference [VelRef](../../10-motion/01-kinematics-status/VelRef.md).

The unit is Hz/100. For example, a cutoff of 4500 Hz is entered as `dPosRefFilt = 450000`.

## How it works

The position reference is differenced cycle-to-cycle to obtain the raw reference velocity; that signal is passed through a single-pole low-pass filter whose corner is `dPosRefFilt`. The filter coefficient is derived from the cutoff and the control sample time, so a lower `dPosRefFilt` smooths the feed-forward more (at the cost of more lag), while a higher value tracks the raw reference velocity more closely. The filtered result is the [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) that [VelTrackFact](VelTrackFact.md) scales:

$$
\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

- **Range / default:** `20000` to `1000000` (i.e. 200 Hz to 10000 Hz), default `1000000`.
- **Units:** Hz/100.

**Note:** the low-pass filter is bypassed (no filtering) when the cutoff exceeds 8192 Hz; at the default of `1000000` the reference velocity passes through unfiltered.

## Examples

```text
AdPosRefFilt=450000 ; low-pass the reference velocity at 4500 Hz
AdPosRefFilt        ; read the reference-velocity filter cutoff
```

### Worked example: choosing a cut-off

Suppose the motion profile generates reference-velocity steps with significant content up to a few kHz, and the position loop is operating with a bandwidth around 200 Hz. A cut-off of `dPosRefFilt = 100000` (1000 Hz) leaves the velocity feed-forward following all profile content the position loop can react to while filtering quantisation jitter above 1 kHz. Increasing the cut-off above the bypass threshold (`dPosRefFilt > 819200`, i.e. 8192 Hz) — for example the default `1000000` — leaves the reference velocity unfiltered.

## See also

- [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) — reference velocity that this filter smooths
- [VelTrackFact](VelTrackFact.md) — scales the filtered reference velocity into the feed-forward
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference the feed-forward joins
- [PosGain](../03-position-control/PosGain.md) — position gain whose output the feed-forward is added to
