---
keyword: IdenResults
summary: Read-only array holding the calculated input/output relations from sine sweep identification.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 127
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 12
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 23
    data_type: float64
    range:
    - -2251799813685248
    - 2251799813685247
---
# IdenResults

Read-only array holding the calculated input/output relations from sine sweep identification.

## Overview

`IdenResults` stores the calculated relations between the recorded input and output vectors. It applies only to sine sweep identification and is updated after a [CalcIden](CalcIden.md) operation completes. The fundamental (first harmonic) frequency refers to the frequency defined in [InjectFreq](../13-injection/InjectFreq.md). The values feed the auto-tuning and filter-design algorithms via [PlantModel](PlantModel.md).

## How it works

The details of each array entry are as shown (array is 1-indexed). The lower index of each pair (1-11) holds the single result set available on all variants. The higher index of each pair (12-22) exists only on central-i v5, where it holds a second result set (see dual-loop note below).

| Index | Descriptions |
|----|----|
| 1, 12 | Real magnitude ratio of output over input at fundamental sine frequency |
| 2, 13 | Imaginary magnitude ratio of output over input at fundamental sine frequency |
| 3, 14 | Harmonic quality (amplitude ratio of second harmonic to first/fundamental harmonic), in terms of percentage |
| 4, 15 | Noise quality (RMS value of the error between actual output and modelled output, over the amplitude of output fundamental sine wave), in terms of percentage |
| 5, 16 | Amplitude ratio of output over input fundamental sine waves, in terms of dB/100 (the raw value is dB scaled up by 100; PCSuite divides by 100 to display dB) |
| 6, 17 | Phase difference between output and input fundamental sine waves, in terms of deg/100 |
| 7, 18 | Amplitude of output fundamental sine wave |
| 8, 19 | Amplitude of input fundamental sine wave |
| 11, 22 | Amplitude of output fundamental sine wave, scaled up by 1000 |

For standard identification, there is 1 input and 1 output vector, with results populated in array indices 1 to 11. On v4 (standalone v4 and central-i v4) only this single result set in indices 1 to 11 exists.

Dual-loop system plant identification and the second result set in indices 12 to 22 apply to central-i v5 only. In that case there is 1 input and 2 output vectors. The recording order is input first, then the load (main encoder) output, then the motor (auxiliary encoder) output. Accordingly, the relationship between the load (main encoder) output and the input is on indices 1 to 11, and the relationship between the motor (auxiliary encoder) output and the input is on indices 12 to 22.

### Result formulas

The entries are derived from the fundamental sine/cosine coefficients of the input and output produced by the least-squares fit in [CalcIden](CalcIden.md). Let $a_{in}, b_{in}$ be the input fundamental sine and cosine coefficients and $a_{out}, b_{out}$ the corresponding output coefficients; let $a_2, b_2$ be the output second-harmonic coefficients.

The complex frequency response $H = \text{output}/\text{input}$ at the fundamental is

$$\operatorname{Re}(H) = \frac{a_{out}\,a_{in} + b_{out}\,b_{in}}{a_{in}^2 + b_{in}^2}, \qquad \operatorname{Im}(H) = \frac{-a_{out}\,b_{in} + b_{out}\,a_{in}}{a_{in}^2 + b_{in}^2}$$

stored in indices 1 (real) and 2 (imaginary). The fundamental amplitudes are

$$A_{out} = \sqrt{a_{out}^2 + b_{out}^2}\ \ (\text{index } 7), \qquad A_{in} = \sqrt{a_{in}^2 + b_{in}^2}\ \ (\text{index } 8)$$

and index 11 holds $A_{out} \times 1000$. The gain (index 5) and phase (index 6) are

$$[\text{gain}] = 100 \cdot 20\log_{10}|H| \quad (\text{dB}\times 100), \qquad [\text{phase}] = 100 \cdot \frac{180}{\pi}\operatorname{atan2}\!\big(\operatorname{Im}(H), \operatorname{Re}(H)\big) \quad (\text{deg}\times 100)$$

both scaled up by 100 to preserve resolution over the communication link; PCSuite divides by 100 for display. The quality metrics are

$$[\text{harmonic}] = 100 \cdot \frac{\sqrt{a_2^2 + b_2^2}}{A_{out}}\ \%\ \ (\text{index } 3), \qquad [\text{noise}] = 100 \cdot \frac{\sqrt{\tfrac{1}{N}\sum (y_{fit} - y_{out})^2}}{A_{out}}\ \%\ \ (\text{index } 4)$$

where $y_{fit}$ is the modelled output, $y_{out}$ is the recorded output, and $N$ is the record length. The harmonic-quality entry measures how large the output second harmonic is relative to its fundamental, and the noise-quality entry measures the RMS model-fit residual relative to the output fundamental. High values of either indicate a distorted or noisy measurement and a less reliable identified point.

The results are acquired by PCSuite after the [CalcIden](CalcIden.md) operation following each sine excitation. Please contact Agito if more information is needed.

![IdenResults captures one point of the identified frequency response: a magnitude value (IdenResults[5] in dB) and a phase value (IdenResults[6] in deg/100) at the fundamental frequency InjectFreq; PCSuite sweeps InjectFreq and concatenates these points into the full magnitude and phase Bode plot used downstream by tuning and filter design](idenresults-bode-points.svg)

## Examples

```text
AIdenResults        ; read all calculated identification results
AIdenResults[5]     ; read amplitude ratio (dB) of output over input at fundamental
```

## See also

- [CalcIden](CalcIden.md) — calculates and populates these results
- [InjectFreq](../13-injection/InjectFreq.md) — fundamental sine frequency the results refer to
- [PlantModel](PlantModel.md) — identified plant model built for tuning
