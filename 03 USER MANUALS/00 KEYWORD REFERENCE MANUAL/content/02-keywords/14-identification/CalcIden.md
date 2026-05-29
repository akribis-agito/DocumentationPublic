---
keyword: CalcIden
summary: Command that calculates the input/output sinusoidal relation for sine sweep identification.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 128
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
# CalcIden

Command that calculates the input/output sinusoidal relation for sine sweep identification.

## Overview

`CalcIden` instructs the controller to calculate the sinusoidal relation between the internally recorded input and output data at the injection frequency [InjectFreq](../13-injection/InjectFreq.md). It applies only to sine sweep identification. Once the calculation completes, the controller returns an `OK` message and the results are stored in [IdenResults](IdenResults.md), from which the identified plant model in [PlantModel](PlantModel.md) is built.

## How it works

The input and output data must each contain at least 30 and at most 250 data points. `CalcIden` evaluates the recorded vectors at the fundamental frequency set in [InjectFreq](../13-injection/InjectFreq.md) and populates [IdenResults](IdenResults.md) with the magnitude and phase relations.

### Mechanism

`CalcIden` fits each recorded vector with a least-squares regression onto a fixed six-term model evaluated at the injection frequency. For each recorded sample $x = 0, 1, \dots, N-1$ (where $N$ is the record length), a row of the model matrix $M$ is built from six basis terms:

$$M_x = \big[\, \sin(\omega t),\ \cos(\omega t),\ \sin(2\omega t),\ \cos(2\omega t),\ 1,\ t \,\big]$$

where $t = x \cdot T_s \cdot \text{RecGap}$ is the time of the sample, $T_s$ is the controller cycle time (default $T_s = 1/16384 \approx 61\ \mu s$), $\text{RecGap}$ is the number of cycles between recorded samples, and the fundamental angular frequency is

$$\omega = 2\pi \cdot \frac{[\text{InjectFreq}]}{100}$$

(InjectFreq is expressed in units of Hz/100). The first two terms capture the fundamental sine and cosine, the next two capture the second harmonic, the constant term absorbs any DC offset, and the linear term $t$ absorbs any drift over the record.

The least-squares solution uses the pseudo-inverse $\left(M^{\mathsf T} M\right)^{-1} M^{\mathsf T}$, which is computed once and applied to both the input and output vectors to obtain the six fitted coefficients of each. The recorded input is used as captured; the recorded output has its first sample subtracted so the fit is taken relative to the starting point. The fundamental sine and cosine coefficients ($a$ and $b$) of the input and output are then combined into the frequency-response, amplitude, and quality entries reported in [IdenResults](IdenResults.md).

### Error conditions

- If the record length is outside the range 30 to 250 samples, the instruction returns error 103.
- If the number of recorded parameters is wrong, the instruction returns error 104. A standard identification record must contain exactly two parameters (one input, one output). On central-i v5, a dual-loop identification record may contain two or three parameters (one input and one or two outputs); see the dual-loop note in [IdenResults](IdenResults.md).

## Examples

```text
ACalcIden            ; calculate the sine-sweep relation; results land in IdenResults
```

## See also

- [IdenResults](IdenResults.md) — stores the calculated input/output relations
- [InjectFreq](../13-injection/InjectFreq.md) — fundamental sine frequency used for the calculation
- [PlantModel](PlantModel.md) — identified plant model derived from the results
