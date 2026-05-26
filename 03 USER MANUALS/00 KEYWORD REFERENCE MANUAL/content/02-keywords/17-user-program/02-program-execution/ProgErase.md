---
keyword: ProgErase
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 299
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgErase

**Definition:**

ProgErase is a command that erases the stored user program from controller memory. It cannot be executed while the axis is in motion or with the motor on. It is a non-axis command and is not saved to flash.

**See also:**

[DownloadUPBin](DownloadUPBin.md), [ProgReset](ProgReset.md)
