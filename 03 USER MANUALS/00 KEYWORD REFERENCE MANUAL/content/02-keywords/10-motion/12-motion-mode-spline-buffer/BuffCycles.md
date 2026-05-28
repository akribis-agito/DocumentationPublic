---
keyword: BuffCycles
summary: Number of times the spline buffer trajectory is repeated.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 548
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
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffCycles

Number of times the spline buffer trajectory is repeated.

## Overview

`BuffCycles` sets how many times the spline-buffer trajectory is replayed when executed. The valid range is 1 to 2147483647, with a default of 1 (a single pass). The value is read from the **primary axis** of the spline-buffer group. A running move can be ended early with [StopBuff](../04-motion-command/StopBuff.md). `BuffCycles` is saved to flash and can be changed at any time.

## How it works

### Cycle counting during playback

The expanded trajectory produced by [BuffCalc](BuffCalc.md) is one cycle. During motion the controller keeps a per-group cycle counter and an index into the cycle, both reported through [BuffStatus](BuffStatus.md):

- Each control cycle the playback index advances by one. When it passes the last interpolated point of the cycle, the index wraps back to the first point and the cycle counter is incremented.
- The move ends when the cycle counter exceeds `BuffCycles` — i.e. after `BuffCycles` complete passes. At that point the controller clears the in-motion state for every member axis and the move finishes normally.

Because the waypoint positions are applied **relative to the start of each cycle**, repeated cycles chain end-to-end: if the trajectory's last waypoint differs from its first, each repeat continues from where the previous one ended (a net advance per cycle), rather than snapping back. For example, if `BuffPos` ranges from `0` to `5000` over one cycle and `BuffCycles = 4`, the axis advances by `5000` user units per cycle, ending `20000` user units beyond the position captured at `Begin`.

### Ending early

[StopBuff](../04-motion-command/StopBuff.md) does not interrupt mid-cycle; it requests the move to finish at the **next cycle boundary**, taking the same end-of-cycle path used when `BuffCycles` is exhausted. This keeps the trajectory continuous. The reason is reported as [MotionReason](../05-motion-status/MotionReason.md) = 35.

## Examples

```text
ABuffCycles=1        ; run the trajectory once (default)
ABuffCycles=10       ; repeat the trajectory ten times, chained end-to-end
```

## See also

- [BuffCalc](BuffCalc.md) — expands one cycle of the trajectory
- [BuffStatus](BuffStatus.md) — reports the live cycle counter and in-cycle index
- [BuffPos](BuffPos.md) — waypoint positions (applied relative to each cycle start)
- [StopBuff](../04-motion-command/StopBuff.md) — ends playback at the next cycle boundary
