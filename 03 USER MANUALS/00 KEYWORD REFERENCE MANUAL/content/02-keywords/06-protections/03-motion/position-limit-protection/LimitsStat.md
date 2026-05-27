---
keyword: LimitsStat
summary: Read-only bitfield reporting reverse/forward limit-switch activation.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 49
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LimitsStat

Read-only bitfield reporting reverse/forward limit-switch activation.

## Overview

`LimitsStat` reports the current state of the two hardware limit-switch inputs as a bitfield. A set bit (`1`) means that limit is currently active (the switch is engaged). These are physical inputs, distinct from the firmware software travel limits `FwdPLim`/`RevPLim`.

## How it works

The control interrupt updates `LimitsStat` whenever a limit-switch input changes state, OR-ing in the appropriate bit when the switch becomes active and masking it out when it clears (firmware `CommonC/AG300_CTL01ControlInterrupt.c:10645`, `:10659`, and `:11159`/`:11173`). The bit masks are defined in `CommonIncludes/AG300_CTL01ParamsCommon.h:457`:

| `#define` | Value | Action |
|-----------|-------|--------|
| `RLS_SET` | `0x0001` | OR-ed in when the reverse limit switch becomes active |
| `FLS_SET` | `0x0002` | OR-ed in when the forward limit switch becomes active |
| `RLS_CLEAR` | `0xFFFE` | AND mask that clears the RLS bit |
| `FLS_CLEAR` | `0xFFFD` | AND mask that clears the FLS bit |

### Bit layout

![LimitsStat bit layout](LimitsStat-bits.svg)

| Bit # | Name | Meaning when set |
|-------|------|------------------|
| 0 | RLS | Reverse limit switch active |
| 1 | FLS | Forward limit switch active |
| 2–31 | — | Unused (always 0) |

| `LimitsStat` value | Meaning |
|--------------------|---------|
| 0 | No limit switch active |
| 1 | RLS active |
| 2 | FLS active |
| 3 | Both RLS and FLS active |

### Effect on motion

The profiler reads these bits to brake the axis on contact (firmware `CommonC/AG300_CTL01Profiler.c`):

- Moving forward into an active `FLS_SET` requests a stop with `MotionReason = MOTION_REASON_END_FLS` (code `5`) (`AG300_CTL01Profiler.c:574`).
- Moving backward into an active `RLS_SET` requests a stop with `MotionReason = MOTION_REASON_END_RLS` (code `4`) (`AG300_CTL01Profiler.c:647`).
- These stops use the emergency deceleration `EmrgDec` (`AG300_CTL01Profiler.c:783`).
- A `Begin` is rejected (`DO_NOT_ALLOW_MOTION_INTO_RLS_OR_FLS`) if the axis is already inside a limit switch and the commanded direction is further into it.

Homing also inspects `LimitsStat` (e.g. `AG300_CTL01Homing.c:233`) to detect and react to switch contact during a homing sequence.

## Examples

```text
ALimitsStat         ; 0 = none, 1 = RLS, 2 = FLS, 3 = both
```

## See also

- [FwdPLim](FwdPLim.md) / [RevPLim](RevPLim.md) — software travel limits (firmware-computed, distinct from these physical switches)
- [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) — carries the stop request set when a switch is hit
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — records reason codes 4 (RLS) and 5 (FLS) when motion ends on a limit switch
