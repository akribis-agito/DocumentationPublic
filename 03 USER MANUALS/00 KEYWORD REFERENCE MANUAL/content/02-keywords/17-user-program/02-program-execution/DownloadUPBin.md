---
keyword: DownloadUPBin
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 207
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
# DownloadUPBin

**Definition:**

DownloadUPBin is a command that transfers a compiled user program binary image into the controller's program memory. It cannot be executed while the axis is in motion or with the motor on. It is a non-axis command and is not saved to flash.

**See also:**

[ProgErase](ProgErase.md), [ProgReset](ProgReset.md), [ProgStatAll](ProgStatAll.md)
