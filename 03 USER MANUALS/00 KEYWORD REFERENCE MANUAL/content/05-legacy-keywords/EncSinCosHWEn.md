---
keyword: EncSinCosHWEn
summary: Selects which encoder source feeds the hardware lock/event capture mechanism for the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 496
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# EncSinCosHWEn

*Legacy keywords*

**Definition:**

EncSinCosHWEn selects which encoder source feeds the hardware lock/event capture mechanism for the axis. Range 0..7, default 0. Verified sources: 0 = main encoder (incremental), 1 = main encoder, 2 = virtual encoder, 3 = auxiliary encoder.

The selection only takes effect when the axis encoder is configured as a Sin/Cos type. For any other encoder type the controller internally forces the selection to 0, regardless of the value written.
