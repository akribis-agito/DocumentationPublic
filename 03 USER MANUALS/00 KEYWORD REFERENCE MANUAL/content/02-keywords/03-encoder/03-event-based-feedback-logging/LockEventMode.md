---
keyword: LockEventMode
summary: Selects legacy, manual or automatic lock/event offset learning.
availability:
  standalone: []
  central-i:
  - v5
can_code: 831
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -1
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-17'
doc_revision: '2026.10'
---
# LockEventMode

Selects how the controller learns the offset between its position and the remote capture counter. The stored default is `0`.

| Value | Behavior |
| --- | --- |
| `0` | Legacy mode: learn the offset on each `LockEn` or `EventOn` transition from 0 to 1. `LockEventStat` reports 0. |
| `1` | Manual mode: run [LockEventInit](LockEventInit.md) with the source stationary before arming. |
| `2` | Automatic mode: for an applicable capture counter, recompute while both features are off when entering mode 2, changing a tracked dependency, or reconnecting after configuration replay. |

`-1` remains in the numeric range for compatibility but is not a supported operating mode. Use 0, 1 or 2.

In mode 2, writing the same value again does not force a new measurement. `LockEventInit` can explicitly recompute in either mode 1 or mode 2. Keep the source stationary during offset measurement. Configure the source with both `LockEn=0` and `EventOn=0`, then check [LockEventStat](LockEventStat.md) before arming when the source requires an ancillary counter.

In modes 1 and 2, a tracked source/direction/reference change while either feature is armed is refused with error 403. Entering mode 1 or 2 is also refused if a dependency moved the offset after arming. Disarm before changing the configuration. An uncomputed offset prevents arming with error 335; a stale offset prevents arming with error 404. A failed remote read leaves the offset invalid rather than certifying old data.

Mode 1 requires a new explicit initialization after invalidation. Mode 2 attempts automatic recomputation while unarmed and after reconnect; confirm its status rather than assuming an assignment succeeded in obtaining a measurement. The main absolute-encoder source does not require the ancillary-counter offset and can leave the status unchanged.

Use a compatible remote FPGA: see the [ancillary-register requirement](LockEventInit.md#remote-fpga-compatibility). A zero reply from an unmapped register is not an offset measurement.

```text
ALockEn=0
AEventOn=0
ALockEventMode=2
; configure the capture source while it is stationary
ALockEventInit        ; optional explicit refresh in mode 2
ALockEventStat        ; require 1 for an applicable ancillary-counter source
ALockEn=1
```

See also: [LockEventInit](LockEventInit.md), [LockEventStat](LockEventStat.md), [LockEn](LockEn-AuxLockEn.md), [EventOn](../../18-event-generation/EventOn.md).
