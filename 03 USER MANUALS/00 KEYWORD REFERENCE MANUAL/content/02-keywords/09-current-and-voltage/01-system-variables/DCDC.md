---
keyword: DCDC
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 42
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 8
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DCDC

**Definition:**

DCDC reports the system internal logic voltage measurement values, as follows.

| Index | Descriptions                                      |
|-------|---------------------------------------------------|
| 1     | 3.3V logic                                        |
| 2     | 15V logic                                         |
| 3     | -15V logic                                        |
| 4     | 1.2V logic                                        |
| 5     | 1.8V logic                                        |
| 6     | Internal 10.5V or backup logic (whichever higher) |
| 7     | 4.7V logic                                        |

Please contact Agito for more information on applicable readings for different products.
