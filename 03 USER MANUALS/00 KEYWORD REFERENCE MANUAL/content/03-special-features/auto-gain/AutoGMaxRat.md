---
keyword: AutoGMaxRat
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 365
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
  - 100
  - 20000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGMaxRat

**Definition:**

AutoGMaxRat sets the upper bound of the acceptable load-to-motor inertia ratio (in percent) used by the auto-gain algorithm to validate identification results. On each calculation cycle the estimated ratio must satisfy AutoGMinRat <= ratio <= AutoGMaxRat before the gains are updated; an estimate above AutoGMaxRat is rejected for that cycle and no gain update occurs. In the modes that accept a user-supplied inertia ratio, that supplied ratio is checked against the same bounds. Range 100 to 20000; default 1000. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGMinRat](AutoGMinRat.md), [AutoGJm](AutoGJm.md), [AutoGQualTh](AutoGQualTh.md)
