---
keyword: ProgEventStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 525
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 6
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
# ProgEventStat

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Reports the state of this event. "0" for waiting for trigger, "1" for pending for service (triggered)

and "2" for in service. Note that this mean that while a given event is being serviced, it can't not

be triggered again, till servicing is completed (returning from the event function using the Return

keyword).

This parameter is R/W, so user can clear a pending event ­ only the value of 0 can be written to

this parameter).
