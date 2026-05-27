---
keyword: FilterStatus
availability:
  standalone: []
  central-i:
  - v5
can_code: 828
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 5
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
# FilterStatus

**Definition:**

FilterStatus is an array that describes the filter calculation status. Every 6 bits of the array element describes 1 filter.

| FilterStatus[Index] | Description |
|---|---|
| FilterStatus[1] | Position filter (Bit 0 - 5: Position reference filter) (Bit 6 - 11: Position error filter) |
| FilterStatus[2] | Velocity filter (Bit 0 - 5: Velocity PI output filter 1) (Bit 6 - 11: Velocity PI output filter 2) (Bit 12 - 17: Velocity PI output filter 3) (Bit 18 - 23: Velocity PI output filter 4) |
| FilterStatus[3] | Feedforward filter (Bit 0 – 5: Feedforward filter) |
| FilterStatus[4] | Force filter (Bit 0 - 5: Force filter 1) (Bit 6 - 11: Force filter 2) |

The 6 bits for each filter are described as shown (LSB to MSB, where n = (Filter number – 1) \* 6).

| Bit # | Description |
|---|---|
| n + 0 | 0 (Cleared) – Filter coefficients are updated <br>1 (Set) – FiltDef has changed, pending coefficients update |
| n + 1 | 0 (Cleared) – No issue with the filter type <br>1 (Set) – Unknown filter type |
| n + 2 | 0 (Cleared) – Parameter is in range <br>1 (Set) – Parameter is out of range |
| n + 3 | 0 (Cleared) – Parameter is in range <br>1 (Set) – Parameter is out of range |
| n + 4 | 0 (Cleared) – Parameter is in range <br>1 (Set) – Parameter is out of range |
| n + 5 | 0 (Cleared) – Parameter is in range <br>1 (Set) – Parameter is out of range |

Bit n + 1 to n + 5 will only refresh when CalcFilters is commanded.
