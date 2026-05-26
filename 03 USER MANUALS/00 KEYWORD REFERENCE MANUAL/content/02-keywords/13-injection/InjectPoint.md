---
keyword: InjectPoint
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 113
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
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectPoint

**Definition:**

InjectPoint defines the location of waveform injection, as shown.

| Value | Injection locations | Locations in block diagram |
|----|----|----|
| 0 | Current command | see [Control tuning – Current control](../../02-keywords/11-control-tuning/06-current-control/00-overview.md) |
| 1 | Velocity command | see [Control tuning – Velocity control](../../02-keywords/11-control-tuning/04-velocity-control/00-overview.md) |
| 2 | Position command | see [Control tuning – Position control](../../02-keywords/11-control-tuning/03-position-control/00-overview.md) |
| 3 | Force command | see [Control tuning – Force control](../../02-keywords/06-protections/04-force-control/00-overview.md) |
