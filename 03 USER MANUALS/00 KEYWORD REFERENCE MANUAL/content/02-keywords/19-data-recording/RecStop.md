---
keyword: RecStop
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 250
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecStop

**Definition:**

RecStop commands the selected scope to stop recording. It can be called at any stage of the recording. If the recording is ongoing when RecStop is called, RecDataA/RecDataB metadata will be updated to report the actual length of the recording made.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

For example, RecStop\[1\] command will stop the recording of first scope.
