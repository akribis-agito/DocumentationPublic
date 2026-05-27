---
keyword: ScheduleGntry
availability:
  standalone: []
  central-i:
  - v5
can_code: 658
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# ScheduleGntry

Pairs gain scheduling with the axis's gantry-control state, selecting whether scheduling acts on the standard tuning gains or the gantry tuning gains.

## Overview

When an axis can run under gantry (beam) control, it has two complete sets of tuning gains: the standard gains used when gantry control is off, and the gantry gains used when gantry control is on. `ScheduleGntry` tells the scheduler which of those two situations the configured scheduling is meant for. It is an axis-scoped flag:

| Value | Scheduling acts when |
|---|---|
| 0 | Gantry control is **off** (default) |
| 1 | Gantry control is **on** |

## How it works

Each scheduling cycle, the controller checks whether the axis's current gantry-control state matches `ScheduleGntry`:

- If `ScheduleGntry = 0` and gantry control is off, **or** `ScheduleGntry = 1` and gantry control is on, the scheduling rule selected by [ScheduleMode](ScheduleMode.md) is evaluated normally and drives [ScheduleSet](ScheduleSet.md).
- If the state does not match (for example `ScheduleGntry = 1` but gantry control is currently off), scheduling is not applied and the default gain set 1 is used.

When the match condition is met with gantry control **on**, the scheduled gains in [ScheduleGains](ScheduleGains.md) are loaded from the gantry tuning arrays rather than the standard ones; for the range-based modes, the gantry feedback position or gantry velocity is used as the scheduling quantity. When the match condition is met with gantry control **off**, the standard tuning arrays and the standard axis position/velocity are used.

## Examples

```text
AScheduleGntry=1             ; apply this axis's scheduling while gantry control is on
AScheduleGntry=0             ; apply scheduling while gantry control is off (default)
```

## See also

- [ScheduleMode](ScheduleMode.md) — the scheduling rule that is gated by this pairing
- [ScheduleGains](ScheduleGains.md) — gains in use (standard or gantry arrays)
- [ScheduleSet](ScheduleSet.md) — active set, forced to 1 when the gantry state does not match
