---
keyword: CalcIden
summary: Command that calculates the input/output sinusoidal relation for sine sweep identification.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

## Examples

```text
CalcIden            ; calculate the sine-sweep relation; results land in IdenResults
```

## See also

- [IdenResults](IdenResults.md) — stores the calculated input/output relations
- [InjectFreq](../13-injection/InjectFreq.md) — fundamental sine frequency used for the calculation
- [PlantModel](PlantModel.md) — identified plant model derived from the results
