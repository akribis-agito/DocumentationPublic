---
keyword: AutoGDownSm
summary: Sets the downsampling exponent applied to the motion data collected during auto-gain identification.
availability:
- controller
- ci-master
products:
- agc300-et
- agc301-et
- agc301-et-bioxtreme
- agd155-af-2a06
- agd155-af-2a10
- agd200-et-2d01
- agd200-et-2d02
- agd200-et-2d05
- agd200-et-2d05-71
- agd301-et-2d01
- agd301-et-2d02
- agd301-et-2d05
- agd301-et-2d09
can_code: 359
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 6
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGDownSm

**Definition:**

AutoGDownSm sets the downsampling exponent applied to the motion data collected during auto-gain identification. The actual downsampling factor is 2 raised to this value, so the effective sample time is multiplied by that factor (for example, a value of 4 downsamples by a factor of 16). Increasing it reduces computation load at the cost of frequency resolution. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGPosFilt](AutoGPosFilt.md), [AutoGMinLen](AutoGMinLen.md)
