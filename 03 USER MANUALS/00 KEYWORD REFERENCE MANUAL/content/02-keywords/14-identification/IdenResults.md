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

The details of each array entry are as shown (array is 1-indexed).

| Index | Descriptions |
|----|----|
| 1, 12 | Real magnitude ratio of output over input at fundamental sine frequency |
| 2, 13 | Imaginary magnitude ratio of output over input at fundamental sine frequency |
| 3, 14 | Harmonic quality (amplitude ratio of second harmonic to first/fundamental harmonic), in terms of percentage |
| 4, 15 | Noise quality (RMS value of the error between actual output and modelled output, over the amplitude of output fundamental sine wave), in terms of percentage |
| 5, 16 | Amplitude ratio of output over input fundamental sine waves, in terms of dB |
| 6, 17 | Phase difference between output and input fundamental sine waves, in terms of deg/100 |
| 7, 18 | Amplitude of output fundamental sine wave |
| 8, 19 | Amplitude of input fundamental sine wave |
| 11, 22 | Amplitude of output fundamental sine wave, scaled up by 1000 |

For standard identification, there will only be 1 input and 1 output vector, with results populated in array indices 1 to 11.

For dual-loop system plant identification, there will be 1 input and 2 output vectors. The relationship between the first output and the input, and the second output and the input, will be on indices 1 to 11 and 12 to 22, respectively.

The results are acquired by PCSuite after the [CalcIden](CalcIden.md) operation following each sine excitation. Please contact Agito if more information is needed.

## Examples

```text
AIdenResults        ; read all calculated identification results
AIdenResults[5]     ; read amplitude ratio (dB) of output over input at fundamental
```

## See also

- [CalcIden](CalcIden.md) — calculates and populates these results
- [InjectFreq](../13-injection/InjectFreq.md) — fundamental sine frequency the results refer to
- [PlantModel](PlantModel.md) — identified plant model built for tuning
