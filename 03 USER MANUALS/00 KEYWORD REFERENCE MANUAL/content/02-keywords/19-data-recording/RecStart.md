---
keyword: RecStart
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 248
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
# RecStart

**Definition:**

RecStart commands the selected scope to start recording, according to the configured setup and trigger keywords. Once recording is started, changing of the setup or trigger keywords will not affect the recording process.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

For example, RecStart\[2\] command will start the recording of second scope.
