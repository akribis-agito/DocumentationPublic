---
keyword: ConFlt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 31
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ConFlt

**Definition:**

ConFlt stores the error code that caused the disabling of the axis. The error codes reportable by ConFlt are value 0 and values from 1001 and above. See [Controller error codes](../../04-error-codes/controller-error-codes.md) for more information.

On every update of positive ConFlt value, the value is also appended to ErrLog. ConFlt is cleared to 0 upon motor enable (MotorOn=1).

User can write value 0 to ConFlt to clear the error status. However, user cannot write positive value to simulate fault. Negative values are writable and reserved for internal use.
