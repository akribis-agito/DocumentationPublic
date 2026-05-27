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

**Definition:**

ScheduleGntry configures gain scheduling parameters specific to gantry (beam) control axes. It is an axis-related parameter.

%%
Needs verification
ScheduleGntry was not found in the AG300_CTL01Params.c firmware parameter table. Confirm availability and the specific scheduling variable it controls before use.
%%

**See also:**

[ScheduleGains](ScheduleGains.md), [ScheduleMode](ScheduleMode.md)
