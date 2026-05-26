---
keyword: FastIdInit
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 540
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FastIdInit

**Condition:**

FastIdInit is only applicable for PRBS injection (InjectType = 6 or 7).

**Definition:**

FastIdInit resets the PRBS sequence index to the first pre-defined binary value. Please refer to InjectType for more information on PRBS waveform.

**Note:**

FastIdInit does not reset the PRBS downsampling factor ( FastIdDownSam ).
