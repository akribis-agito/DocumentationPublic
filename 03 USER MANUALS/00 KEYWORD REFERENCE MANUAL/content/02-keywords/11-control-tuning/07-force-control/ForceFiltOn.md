---
keyword: ForceFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 741
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
---
# ForceFiltOn

Enables each of the two force-loop output filters.

## Overview

`ForceFiltOn` enables or bypasses the two force output filters. Each element controls one filter: `ForceFiltOn[Index] = 1` enables the filter, `ForceFiltOn[Index] = 0` bypasses it. The defaults are `0` (both bypassed).

| Index | Description    |
|-------|----------------|
| 1     | Force filter 1 |
| 2     | Force filter 2 |

These filters are used **only** in standard force control ([ForcePIVOn](ForcePIVOn.md) = 0); in force-over-PIV control (`ForcePIVOn = 1`) they have no effect.

## How it works

In standard force control the force PID output, summed with the feedforward terms ([ForceFFW](ForceFFW.md) and the velocity compensation [ForceVelFFW](-spanclass=-mark--ForceVelFFW--span-.md)), is passed in series through force filter 1 then force filter 2; the output of the second filter is the current reference. Where a filter is bypassed, the signal passes through unchanged.

Each filter is realised as a second-order (biquad) section whose type and parameters are defined by [ForceFiltDef](ForceFiltDef.md). After changing `ForceFiltOn` (or `ForceFiltDef`), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the coefficients are recomputed.

## Examples

```text
AForceFiltOn[1]=1       ; enable force filter 1
AForceFiltOn[2]=0       ; bypass force filter 2
ACalcFilters            ; recompute filter coefficients
```

## Changes between versions

In **v4** `ForceFiltOn` can only be changed with the motor off and out of motion. In **v5 (central-i)** it may also be changed while the motor is on and in motion.

## See also

- [ForceFiltDef](ForceFiltDef.md) — defines the type and parameters of each force filter
- [ForcePIVOn](ForcePIVOn.md) — these filters apply only when this is 0
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- [Force control](00-overview.md) — force-loop structure overview
