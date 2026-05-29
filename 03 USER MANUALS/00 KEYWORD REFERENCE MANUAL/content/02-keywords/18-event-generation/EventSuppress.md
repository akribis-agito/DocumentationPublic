---
keyword: EventSuppress
summary: "Command that momentarily suppresses event-pulse generation in the remote drive's compare hardware."
availability:
  standalone: []
  central-i:
  - v4
can_code: 188
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventSuppress

Command that momentarily suppresses event-pulse generation in the remote drive's compare hardware.

## Overview

`EventSuppress` is a command that tells the position-compare engine in the remote drive to suppress event-output generation. It is meant for use alongside the rest of the event-generation feature ([EventOn](EventOn.md), [EventType](EventType.md), [EventPulseWid](EventPulseWid.md)): where those keywords arm and shape the output pulses fired as the axis crosses configured compare positions, `EventSuppress` is the command that asserts the hardware's suppress control so a pulse is not emitted.

It is a Central-i feature: the command is forwarded to the compare hardware in the remote drive. On products without that remote compare hardware the command has no effect. It carries no value and stores no persistent state — it is issued, takes effect on the remote drive, and reports completion.

This keyword is present on **central-i v4**. It is not part of the v5 keyword set.

## How it works

When `EventSuppress` is issued, the controller sends the suppress control to the remote drive's compare hardware as a momentary action — it asserts the suppress control and then releases it. The command always reports success once the remote messages have been queued; there is no readable on/off state associated with it (reading the keyword is not a status query — it is a command).

Use `EventSuppress` together with the event-generation configuration: arm generation with [EventOn](EventOn.md) and shape the pulse with [EventPulseWid](EventPulseWid.md), then issue `EventSuppress` when you need the compare hardware to skip emitting an output.

## Examples

```text
AEventSuppress       ; suppress event-pulse generation in the remote drive
```

## See also

- [EventOn](EventOn.md) — arms event generation
- [EventType](EventType.md) — selects the compare scheme (single / by-gap / by-table)
- [EventPulseWid](EventPulseWid.md) — shape of the event output pulse
- [EventSelect](EventSelect.md) — routing of the event output
