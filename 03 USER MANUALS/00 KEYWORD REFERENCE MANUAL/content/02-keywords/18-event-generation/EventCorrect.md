---
keyword: EventCorrect
summary: Command that recalculates corrected event-table positions from the current axis position and mapping.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 419
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventCorrect

Command that recalculates corrected event-table positions from the current axis position and mapping.

## Overview

`EventCorrect` is a command that converts the event-table positions in [EventTable](EventTable.md) into corrected positions and writes them to [EventTableCor](EventTableCor.md), using the axis's active encoder error map. Table-driven event generation can then use the corrected table ([EventTableCor](EventTableCor.md)) so that pulses fire at the *true* mechanical positions rather than at the raw encoder readings.

It is a command, not a stored value, so it takes no argument; issuing it triggers the recomputation. It cannot be executed while the axis is in motion, and it is not saved to flash.

## How it works

For each entry in the table the controller treats the listed position as a desired true position and looks up where the encoder must read for the mapped (corrected) feedback to equal it, interpolating through the active error map. The result is stored in the matching entry of [EventTableCor](EventTableCor.md). For multi-dimensional maps, the correction also uses the present positions of the other mapped axes, which is why those axes must be enabled and standing still while the command runs.

The command checks several prerequisites and is rejected (returns an error) if any fail:

| Prerequisite | Why |
|--------------|-----|
| Encoder error mapping must be active on this axis | The correction is derived from the map; with no map there is nothing to correct. |
| This axis's main encoder must be the first encoder of its error map | The table positions are corrected against this axis's own feedback. |
| For 2D/3D maps, the other mapped axes must use their main encoders | The interpolation reads those axes' feedback. |
| For 2D/3D maps, the other mapped axes must be motor-on and not moving | Their positions must be stable while the table is recomputed. |

Run `EventCorrect` again whenever the error map or the source [EventTable](EventTable.md) changes, then select the corrected table for table-mode generation.

## Examples

```text
AEventCorrect        ; recompute the corrected event-table positions
```

## See also

- [EventTable](EventTable.md) — source positions being corrected
- [EventTableCor](EventTableCor.md) — holds the corrected positions
- [EventType](EventType.md) — table modes that can use the corrected table
