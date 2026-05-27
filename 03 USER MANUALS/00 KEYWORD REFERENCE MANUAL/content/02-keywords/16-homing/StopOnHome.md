---
keyword: StopOnHome
summary: Enables automatic stop of axis motion when the home digital input is asserted.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 169
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
# StopOnHome

Enables automatic stop of axis motion when the home digital input changes state.

## Overview

`StopOnHome` enables the home-switch stop function. When set to a non-zero value, the axis automatically requests a stop when the home digital input *changes state* during a jog move. It is typically used in homing procedures that reference the home switch — see the "Jog until a change in the Home discrete input" step in [HomingDef](HomingDef.md) — and works analogously to [StopOnIndex](StopOnIndex.md), which stops on the encoder index pulse instead. It is an axis-scoped parameter, not saved to flash, and can be changed at any time.

## How it works

`StopOnHome` is evaluated by the motion profiler only while the axis is jogging. On each cycle, if `StopOnHome` is non-zero and the home input has just changed state (the internal one-cycle "home change" pulse derived from [HomeStat](HomeStat.md)), the profiler:

1. raises the in-stop-request bit so the move decelerates to a stop,
2. sets the motion end reason to "home change" (reported by [MotionReason](../10-motion/05-motion-status/MotionReason.md) = 16), and
3. clears `StopOnHome` back to `0`.

Because the firmware auto-clears it, `StopOnHome` is a one-shot arm: read it back as `0` to confirm the stop was triggered, then wait for [MotionStat](../10-motion/05-motion-status/MotionStat.md) to show the axis is no longer in motion. The homing engine sets and relies on this flag internally for step 11; outside homing you can arm it yourself for a custom jog-to-home move.

> Note: the trigger is a *change* of the home input level, not a particular level. The "Jog until a change in the Home discrete input" homing step uses [HomeStat](HomeStat.md) to pick the initial jog direction so that the move always crosses the home flag edge.

## Examples

```text
AStopOnHome=1        ; arm a stop on the next change of the home input
AStopOnHome         ; 0 = disabled / already triggered, 1 = armed
```

## See also

- [StopOnIndex](StopOnIndex.md) — equivalent stop on the encoder index pulse
- [HomeStat](HomeStat.md) — the home-input state this flag reacts to
- [MotionReason](../10-motion/05-motion-status/MotionReason.md) — reports the "home change" end-of-motion reason
- [HomingDef](HomingDef.md) — homing step 11 jogs until the home input changes
