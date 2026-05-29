---
keyword: RetractSpeed
summary: Maximum velocity of the point-to-point move on entry to position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 608
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -1300000000
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# RetractSpeed

Maximum velocity of the point-to-point move on entry to position mode.

## Overview

`RetractSpeed` is the maximum velocity, in user units/s, of the point-to-point move that runs on entry to position operation mode. The move runs only when [BeginOnToPos](BeginOnToPos.md) is armed, toward the target defined by [RetractTarget](RetractTarget.md) (or [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)). It is a flash-stored setting, so it persists across power cycles.

## How it works

When the entry move is launched, `RetractSpeed` is copied directly into the active PTP move speed. The move then runs as an ordinary point-to-point profile — `RetractSpeed` sets only the cruise (maximum) velocity; acceleration, deceleration and jerk are taken from the axis' normal motion-profile settings.

The keyword is signed and may be negative; the value is the commanded speed for the profiler, which moves toward the target regardless of sign. The default is 1000. The range is symmetric about zero; see the frontmatter for the exact limits.

## Changes between versions

In **v5 (central-i)** the motion pipeline is 64-bit, so `RetractSpeed` is held as a 64-bit value; the speed-copy behaviour is unchanged. **v5 is central-i only**, so on standalone `RetractSpeed` remains the v4 32-bit value.

## Examples

```text
ARetractSpeed=20000  ; entry-move speed (user units/s)
ARetractTarget=50000 ; entry-move target
ABeginOnToPos=1      ; arm the move
AGoToPosMode         ; switch and start the move
```

### Edge cases

- **Not used unless armed** — only consulted when [BeginOnToPos](BeginOnToPos.md) is set and an entry-mode switch occurs.
- **Sign-agnostic for direction** — the profiler infers direction from the target; sign of `RetractSpeed` is the commanded cruise rate.
- **Out of range** — values outside the platform range are rejected.
- **Save** — flash-saveable.
- **Platform** — v5 widens to 64-bit; v4 is 32-bit.

## See also

- [BeginOnToPos](BeginOnToPos.md) — arms the entry move
- [RetractTarget](RetractTarget.md) — target of the entry move
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) — relative-target override for the entry move
- [GoToPosMode](GoToPosMode.md) — one of the commands that triggers the move
