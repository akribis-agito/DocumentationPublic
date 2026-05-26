---
keyword: DownloadFW
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 230
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
# DownloadFW

**Definition:**

DownloadFW will cause the controller to go into firmware download mode. To prevent unexpected behaviour, user must use this keyword only through Agito PCSuite’s firmware download tab.

Please contact Agito if user wishes to program their own user interface.
