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
