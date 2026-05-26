---
keyword: FastIdDownSam
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 541
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
  - 3
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# FastIdDownSam

**Condition:**

FastIdDownSam is only applicable for PRBS injection (InjectType = 6 or 7).

**Definition:**

FastIdDownSam defines the downsampling factor for generation rate of PRBS, as shown.

$$
Rate\ of\ generation\ of\ new\ binary\ value\ \lbrack Hz\rbrack = \ \frac{Controller\ cycle\ rate\lbrack Hz\rbrack}{2^{FastIdDownSam}}
$$

Please refer to InjectType for more information on the PRBS waveform.

<span class="mark">**DN:** This value is not reset by PCSuite.</span>
