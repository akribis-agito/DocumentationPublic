---
keyword: EventAlwaysOn
summary: Forces the event output permanently active, ignoring position and table conditions.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 619
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventAlwaysOn

Runs by-gap event generation continuously, without stopping at EventEndPos.

## Overview

`EventAlwaysOn` selects continuous ("endless") operation for by-gap event generation ([EventType](EventType.md) = 1). It does **not** force the output level high; it changes when the engine *stops*. With normal (windowed) operation, by-gap pulses stop once the position passes [EventEndPos](EventEndPos.md). With `EventAlwaysOn = 1`, the generator keeps producing a pulse every [EventGap](EventGap.md) without ever reaching an end position, so it runs for as long as [EventOn](EventOn.md) remains set.

This applies only to by-gap mode. The single-event, table, hardware-table, and trigger-now schemes are unaffected by `EventAlwaysOn`.

## How it works

| Value | By-gap behavior |
|-------|-----------------|
| 0 | Windowed: pulses run from [EventBegPos](EventBegPos.md) and stop once [EventEndPos](EventEndPos.md) is passed; [EventOn](EventOn.md) returns to `0`. |
| 1 | Continuous: pulses repeat every [EventGap](EventGap.md) with no end position; generation continues until [EventOn](EventOn.md) is cleared. |

When `EventAlwaysOn = 1`, the controller arms the by-gap engine in continuous mode at the [EventOn](EventOn.md) `0 → 1` edge, so the end-position check that would normally halt generation is bypassed. Change `EventAlwaysOn` before arming for it to take effect on the next run. The actual output state can be read back through [EventLoopback](EventLoopback.md).

`EventAlwaysOn` is an axis-related parameter saved to flash and can be changed at any time.

## Examples

```text
AEventType=1         ; by-gap mode
AEventBegPos=1000
AEventGap=500
AEventAlwaysOn=1     ; run continuously, ignoring EventEndPos
AEventOn=1           ; arm (set while below EventBegPos)
AEventAlwaysOn=0     ; return to windowed by-gap operation
AEventAlwaysOn      ; query the current setting
```

## See also

- [EventType](EventType.md) — by-gap mode (value 1) is the one affected
- [EventGap](EventGap.md) — spacing between successive continuous pulses
- [EventEndPos](EventEndPos.md) — window end that is bypassed when EventAlwaysOn = 1
- [EventOn](EventOn.md) — arms generation; clear it to stop continuous output
- [EventLoopback](EventLoopback.md) — reads back the actual output state
