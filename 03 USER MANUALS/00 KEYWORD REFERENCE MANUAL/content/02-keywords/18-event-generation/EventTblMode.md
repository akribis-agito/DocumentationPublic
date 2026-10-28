---
keyword: EventTblMode
summary: Chooses common or per-row settings for a preloaded hardware event table.
availability:
  standalone: []
  central-i:
  - v5
can_code: 975
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
last_updated: '2026-10-28'
doc_revision: '2026.10'
---
# EventTblMode

For AGM800 firmware implementing the original-engine preload (`EventType=3`), select how pulse width and output settings are resolved before [EventLoad](EventLoad.md).

| Value | Settings |
|-------|----------|
| 0 (default) | Resolve settings from the first selected row, `EventTableBeg`, and use them for the whole run. |
| 1 | Resolve settings for each selected row using the existing software-table width inheritance; transfer a new settings word only when its resolved value changes. |

See [EventTableWid](EventTableWid.md) for begin-row global/toggle behavior and width inheritance, and [EventTableSel](EventTableSel.md) for output selection. The selected range can begin at any valid index; it need not begin at 1. Both modes use the same positions, `EventTableSrc`, table offset and existing correction/coordinate conversion.

Set this parameter before loading. It is not saved to flash and cannot change while preparing or running. Stop with `EventOn=0` before changing it, then load again. Every run preloads its selected range, with at most 2048 rows; there is no retained-window mode.

For this hardware preload path, the first selected row determines run-wide toggle: literal width 0, or width -1 with `EventPulseWid=0`, toggles every event in either mode. Later widths do not switch a pulse run into toggle mode.

```text
AEventOn=0
AEventType=3
AEventTblMode=0
; Configure/upload the selected position, width and output rows.
AEventLoad
AEventStatus        ; wait for Ready (bit 1), with no Fault (bit 4)
AEventOn=1
```

This parameter does not change the behavior of other event types.
