---
keyword: DInFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 213
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
  - 15
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# DInFilt

DInFilt determines the number of consecutive samples where each raw digital input must have the same state/value, before its change is asserted. Otherwise, the digital input retains its state. In short, it defines software debouncing filter. For example, if DInFilt is 3, 3 consecutive readings of “1” is needed before “1” is asserted.

After n-cycle debouncing, the effective digital input sampling rate will be reduced by a factor of n. However, this filter improves the noise immunity of the digital input.

DInFilt is a single parameter that applies to all of the digital inputs of the axis. For example, CDInFilt applies to all digital inputs of axis/module C.
