---
keyword: ScheduleMode
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 260
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
  - 0
  - 11
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleMode

Selects the gain-scheduling algorithm — the rule that decides which of the five tuning-gain sets is active at each moment.

## Overview

Gain scheduling lets the controller switch its active position, velocity and feedforward gains between up to five pre-defined sets, automatically, as a function of a chosen condition (motion state, velocity, position, motor temperature, time, an external input, or CNC motion segment). `ScheduleMode` chooses which condition is used. The scheduled gains are:

- [PosGain](../03-position-control/PosGain.md) — position-loop proportional gain
- [VelGain](../04-velocity-control/VelGain.md) — velocity-loop proportional gain
- [VelKi](../04-velocity-control/VelKi.md) — velocity-loop integral gain
- [VelFFW](../05-feedforwards/VelFFW.md) — velocity feedforward gain
- [AccFFW](../05-feedforwards/AccFFW.md) — acceleration feedforward gain
- [PosKi](../03-position-control/PosKi.md) — position-loop integral gain (central-i v5 only)

Each of these is an array of length 5 — one value per gain set. The active set number is reported by [ScheduleSet](ScheduleSet.md), and the gain values actually in use are reported by [ScheduleGains](ScheduleGains.md). With `ScheduleMode = 0` (no scheduling), the controller always uses set 1, i.e. the first element of each gain array.

## How it works

Once per scheduling cycle the controller evaluates the rule selected by `ScheduleMode` and writes the resulting set number into [ScheduleSet](ScheduleSet.md). All scheduled gains then change together to that set; the values are published in [ScheduleGains](ScheduleGains.md) and used by the control loops. Scheduling is evaluated only while the axis is in normal operation.

### Mode value table

| Value | Mode | Set selected by | Configuration keyword(s) |
|---|---|---|---|
| 0 | None | Always set 1 | — |
| 1 | Manual / digital input | [ScheduleSet](ScheduleSet.md) written by communication, or a digital input toggling between set 1 (input low) and set 2 (input high) | [ScheduleSet](ScheduleSet.md) (manual), or a digital input assigned the control-set-change function |
| 2 | Optimal settling by time | Set 1 while in motion; set 2 for `ScheduleTime` after motion ends; set 3 thereafter | [ScheduleTime](ScheduleTime.md) |
| 3 | Optimal settling by in-target | Set 1 while in motion; set 2 while waiting to reach target (in-target timing); set 3 once in position | in-target settings |
| 4 | By velocity range | Set chosen from which velocity band the speed falls into | [ScheduleVel](ScheduleVel.md) |
| 5 | By position range | Set chosen from which position band the position falls into | [SchedulePos](SchedulePos.md) |
| 6 | By quiet standing | Set 2 while in motion and for `ScheduleTime` after; set 1 (quiet) once stationary longer than `ScheduleTime` | [ScheduleTime](ScheduleTime.md) |
| 7 | By PD pulses | Set 2 whenever pulse-and-direction velocity is non-zero; set 1 after pulses have been absent for `ScheduleTime` continuously | [ScheduleTime](ScheduleTime.md) |
| 8 | By temperature range | Set chosen from which motor-temperature band applies | [ScheduleTemp](ScheduleTemp.md) |
| 9 | By velocity range (interpolated) | Gains interpolated continuously between the sets bounding the current speed | [ScheduleVel](ScheduleVel.md) |
| 10 | By position range (interpolated) | Gains interpolated continuously between the sets bounding the current position | [SchedulePos](SchedulePos.md) |
| 11 | CNC motions (channel A) | Set per CNC motion segment: not-in-CNC/blocking, linear, non-linear (corner/arc), and a post-corner settling window | [ScheduleTime](ScheduleTime.md) |
| 12 | CNC motions (channel B) | As mode 11, for the second CNC channel (available only on the higher-axis-count platform) | [ScheduleTime](ScheduleTime.md) |

### Notes on individual modes

- **Manual / digital input (1):** with no input assigned, [ScheduleSet](ScheduleSet.md) is written directly by the user. When a digital input is assigned the control-set-change function for this axis, the input level selects the set: low → set 1, high → set 2.
- **Time-based modes (2, 6, 7, 11/12):** these use a timer measured against [ScheduleTime](ScheduleTime.md) (in milliseconds) to delay the switch back to the steady-state set after the triggering condition clears.
- **Range modes (4, 5, 8):** the band edges are the threshold arrays [ScheduleVel](ScheduleVel.md), [SchedulePos](SchedulePos.md) and [ScheduleTemp](ScheduleTemp.md). Set 1 applies below the first threshold, set 2 below the second, and so on, with set 5 above the fourth threshold. See those keywords for the exact comparison.
- **Interpolated modes (9, 10):** instead of stepping between sets, each scheduled gain is blended linearly between the two sets bounding the measured velocity/position, so gains vary smoothly with the measured quantity. This requires the four thresholds to be strictly increasing; if they are not, scheduling is disabled, set 1 is used, and [ScheduleSet](ScheduleSet.md) reports `-1` to indicate the error.

## Examples

```text
AScheduleMode[1]=4         ; schedule gains by velocity band
AScheduleMode[1]=8         ; schedule gains by motor temperature band
AScheduleMode[1]=0         ; disable scheduling (always use gain set 1)
AScheduleMode[1]           ; read the active scheduling mode
```

## See also

- [ScheduleSet](ScheduleSet.md) — active gain-set number
- [ScheduleGains](ScheduleGains.md) — gain values currently in use
- [SchedulePos](SchedulePos.md) / [ScheduleVel](ScheduleVel.md) / [ScheduleTemp](ScheduleTemp.md) — band thresholds for range modes
- [ScheduleTime](ScheduleTime.md) — timing used by the time-based modes
- [ScheduleGntry](ScheduleGntry.md) — pairing of scheduling with gantry control state
