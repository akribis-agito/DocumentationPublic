---
keyword: UnitStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 75
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
# UnitStat

**Definition:**

UnitStat reports the status of the unit. The bits of UnitStat reflect the following statues

| Bit \# | Status                                  |
|--------|-----------------------------------------|
| 0      | FPGA is faulty.                         |
| 1      | AGD155 FW and FPGA do not match.        |
| 2      | AGD301 FW and FPGA do not match.        |
| 3      | No golden image is present.             |
| 4      | Dynamic brake FW and FPGA do not match. |

Suggestions if warnings appear:
- Ignore if there is no golden image.
- Approach Agito for latest FW and FPGA.
