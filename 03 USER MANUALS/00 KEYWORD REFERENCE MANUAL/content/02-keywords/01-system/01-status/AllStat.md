---
keyword: AllStat
summary: Ethernet-binary multi-axis status query used by the AAMotion API (being deprecated).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 420
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AllStat

Ethernet-binary multi-axis status query used by the AAMotion API (being deprecated).

## Overview

`AllStat` is supported only over **Ethernet Binary** communication. The AAMotion API uses it to query various statuses for multiple axes in a single message, reducing round-trips when polling a multi-axis system.

> **Deprecation:** `AllStat` is scheduled to be deprecated / revamped. Avoid relying on it for new integrations.

## See also

- [UnitStat](UnitStat.md) — unit hardware/firmware health
