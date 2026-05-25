# EncFilt/AuxEncFilt

**Condition:**

EncSubType is only used when EncType=1 (digital incremental encoder). For filter of SIN/COS encoders, please refer to [SinCosSetup](../../../02-keywords/03-encoder/01-general-settings/SinCosSetup-AuxSinCosSet.md).

**Definition:**

EncFilt specifies the digital filter to apply on the encoder input channels A, B and Z. The filter is implemented at the hardware/FPGA. Its definition varies according to products.

For **AG300 controller**, the filter is characterized as follows:

1.  The A, B and Z inputs are sampled by the filter mechanism. An input level is qualified only after 6 consecutive samples with identical value. This means that the "1" logic of the signal needs to be sampled at least 6 times and same for the "0" logic, to a total of (2\*6) =12 samples.

2.  The filter frequency (sampling frequency) is determined by the EncFilt parameter.

    1.  If EncFilt is 0,

> 
> $$
> Filter\ frequency = DSP\ clock\ frequency = \ 300\ \lbrack MHz\rbrack
> ```

2.  If EncFilt is not 0,

> 
> ``` math
> Filter\ frequency = \ \ 300/(2*EncFilt)\ \lbrack MHz\rbrack
> ```

3.  The maximum theoretical input frequency (when no noise is present) is as follows.

    1.  If EncFilt is 0,

> 
> ``` math
> Max\ input\ frequency = \ \ 300/12\ \lbrack MHz\rbrack
> ```

2.  If EncFilt is not 0,

> 
> ``` math
> Max\ input\ frequency = \ \ 300/(2*12*EncFilt)\ \lbrack MHz\rbrack
> ```

4.  The maximum theoretical supported speed (when no noise is present) is as follows.

    1.  If EncFilt is 0,

> 
> ``` math
> Max\ theoretical\ supported\ speed = \ \ (4*3E8)/12\ \lbrack count/s\rbrack = 1.0E8\ \lbrack count/s\rbrack
> ```

2.  If EncFilt is not 0,

> 
> ``` math
> Max\ theoretical\ supported\ speed = \ \frac{4*3E8}{2*12*EncFilt}\left\lbrack \frac{count}{s} \right\rbrack = \ \ 5E7/EncFilt\ \lbrack count/s\rbrack
> ```

5.  From the filter point of view and disregarding hardware limitations, the highest filter frequency is 300 MHz, and the highest input frequency is 25MHz when EncFilt = 0, assuming no noises.

For **Central-i remote units**, the filter is characterized as follows:

1.  The input is sampled by the filter mechanism. An input level is qualified only after 4 consecutive samples with identical value. This means that the "1" logic of the signal needs to be sampled at least 6 times and same for the "0" logic, to a total of (2\*4) = 8 samples.

2.  The filter frequency (sampling frequency) is determined by the EncFilt parameter.

> 
> ``` math
> Filter\ frequency = \ \ 100/2\hat{}(EncFilt + 1)\ \ \lbrack MHz\rbrack
> ```

3.  The maximum theoretical input frequency (when no noise is present) is as follows.

$$ math
Max\ input\ frequency = \ \ 100/(8*2\hat{}(EncFilt + 1)\ )\ \lbrack MHz\rbrack
```

4.  The maximum theoretical supported speed (when no noise is present) is as follows.

$$
Max\ theoretical\ supported\ speed = \ \ (4*1E8)/(8*2\hat{}(EncFilt + 1)\ )\ \lbrack count/s\rbrack
$$

5.  Table below summarises respective frequencies and supported speed.

| EncFilt value | Filter frequency \[MHz\] | Max input frequency \[MHz\] | Max theoretical supported speed \[\*1E6 count/s\] |
|----|----|----|----|
| 0 | 50 | 6.25 | 25 |
| 1 | 25 | 3.125 | 12.5 |
| 2 | 12.5 | 1.5625 | 6.25 |
| 3 | 6.25 | 0.78125 | 3.125 |
| 4 | 3.125 | 0.390625 | 1.5625 |
| 5 | 1.5625 | 0.1953125 | 0.78125 |
| 6 | 0.78125 | 0.09765625 | 0.390625 |
| 7 | 0.390625 | 0.048828125 | 0.1953125 |

6.  From the filter point of view and disregarding hardware limitations, the highest filter frequency is 50 MHz, and the highest input frequency is 6.25MHz when EncFilt = 0, assuming no noises.

**Note:**

1. The "Max Input Frequency" (or maximal axis speed) set by EncFilt is the theoretical upper limit of the input frequency (axis speed), which assume ideal square wave signal (infinite slew rate) and ideal electronics (no delays and slew rate at the receiver chips in the controller). The actual “Max Input Frequency” will be smaller, depending on the quality of the signals.
2. Noise on the signal may impede the filter from counting 6 consecutive samples of a given logic level. Hence it is recommended not to set EncFilt too high.
3. It is recommended to set EncFilt such that the maximum theoretical supported speed will be two times higher than the actual maximum speed expected in the system.
4. The initial value of EncFilt can be set according to above equations/considerations. However, the final value must be set in careful consideration of the quality of the encoder signals themselves (e.g. noise).
5. Please consult Agito if faster input is required.
