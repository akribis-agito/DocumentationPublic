---
keyword: DontDownload
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 670
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DontDownload

**Definition:**

DontDownload is a read-only flag that, when non-zero, prevents the host from downloading a new firmware image to the controller. It is used as a safety interlock to block accidental firmware updates during critical operation.

**See also:**

[DownloadFW](../02-operation/DownloadFW.md), [DownloadFPGA](../02-operation/DownloadFPGA.md)
