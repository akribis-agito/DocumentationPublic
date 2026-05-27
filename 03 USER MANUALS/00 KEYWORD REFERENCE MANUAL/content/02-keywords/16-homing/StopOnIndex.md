---
keyword: StopOnIndex
summary: Enables automatic stop of axis motion on the next encoder index pulse.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 167
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
# StopOnIndex

Enables automatic stop of axis motion on the next encoder index pulse.

## Overview

`StopOnIndex` enables the index stop function. When set to a non-zero value, the next encoder index causes the axis to halt, which is useful for homing procedures that reference the encoder index position — see the "Jog to index" step in [HomingDef](HomingDef.md). It works analogously to [StopOnHome](StopOnHome.md), which stops on the home digital input instead. It is an axis-scoped parameter, not saved to flash, and can be changed at any time.

## How it works

`StopOnIndex` is evaluated by the motion profiler only while the axis is jogging. On each cycle, if `StopOnIndex` is non-zero and the encoder index is currently detected ([IndexStat](../03-encoder/02-index-detection/IndexStat-AuxIndexStat.md) active), the profiler:

1. raises the in-stop-request bit so the move decelerates to a stop,
2. sets the motion end reason to "index" (reported by [MotionReason](../10-motion/05-motion-status/MotionReason.md) as `MOTION_REASON_END_INDEX`), and
3. clears `StopOnIndex` back to `0`.

Because the firmware auto-clears it, `StopOnIndex` is a one-shot arm: read it back as `0` to confirm the stop was triggered, then wait for [MotionStat](../10-motion/05-motion-status/MotionStat.md) to show the axis is no longer in motion. The homing engine sets this flag internally for the "Jog to index" step; the related "Move to index position" step instead does a point-to-point move to the recorded [IndexPos](../03-encoder/02-index-detection/IndexPos-AuxIndexPos.md) and therefore does not use `StopOnIndex`.

## Examples

```text
AStopOnIndex=1       ; arm a stop on the next encoder index
AStopOnIndex        ; 0 = disabled / already triggered, 1 = armed
```

## See also

- [StopOnHome](StopOnHome.md) — equivalent stop on the home digital input
- [IndexStat](../03-encoder/02-index-detection/IndexStat-AuxIndexStat.md) — the index detection this flag reacts to
- [IndexPos](../03-encoder/02-index-detection/IndexPos-AuxIndexPos.md) — recorded index position used by the "move to index position" step
- [MotionReason](../10-motion/05-motion-status/MotionReason.md) — reports the "index" end-of-motion reason
- [HomingDef](HomingDef.md) — homing steps that reference the index
