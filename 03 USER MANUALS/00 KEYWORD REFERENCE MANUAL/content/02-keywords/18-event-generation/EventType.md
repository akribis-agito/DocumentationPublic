---
keyword: EventType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 180
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
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventType

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Events are pulses on a designated output that are generated when the actual feedback position
equals a required compare position. EventType determines different compare options:
EventType = 0: A pulse will be generated when the feedback position equals the position in
EventBegPos
EventType = 1: Event by gap. A first pulse is generated when the position equals EventBegPos.
Another pulse is generated every time the distance defined by EventGap is passed. When the
position exceeds EventEndPos pulses stop being generated.
EventType = 2: Events by table. A table of positions where events should be generated is entered
into GenData[] array. EventTableBeg is the index of the event table start. EventTableEnd is the
index of the event table end. The position in the table must be ordered from low to high.
