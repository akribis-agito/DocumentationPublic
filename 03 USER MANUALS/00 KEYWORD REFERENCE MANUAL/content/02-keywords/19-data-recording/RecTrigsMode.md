---
keyword: RecTrigsMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 564
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigsMode

**Definition:**

RecTrigsMode defines the trigger detection mode, with each scope supporting up to 3 triggers.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

Its value definitions are as shown. Please refer to [Data recording](../../02-keywords/19-data-recording/00-overview.md) for the flowchart.

| Value | Detection mode               |
|-------|------------------------------|
| 1     | Parallel (logical) detection |
| 2     | Serial detection             |
