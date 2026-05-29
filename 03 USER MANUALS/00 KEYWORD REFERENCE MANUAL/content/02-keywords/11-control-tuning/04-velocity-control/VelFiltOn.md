---
keyword: VelFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 122
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
# VelFiltOn

Enables or bypasses the velocity-loop filters that act on the velocity-PI output.

## Overview

`VelFiltOn` enables the velocity-loop filters defined by [VelFiltDef](VelFiltDef.md). The filters are applied in series to the velocity-PI output (the [VelGain](VelGain.md) + [VelKi](VelKi.md) result) before it becomes the motor current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md). Each enabled filter shapes that signal — for example a notch to suppress a mechanical resonance.

| Index | Filter |
|-------|--------|
| 1 | Velocity filter 1 |
| 2 | Velocity filter 2 |

`VelFiltOn[Index] = 1` enables the corresponding filter; `VelFiltOn[Index] = 0` bypasses it (the signal passes through unchanged). Range `0` to `1`, default `0` (all bypassed).

## How it works

The velocity-PI output is passed through the enabled filters in order, each realised as a second-order (biquad) section from its [VelFiltDef](VelFiltDef.md) parameters. A disabled stage passes its input straight through to the next stage. The output of the final stage (plus the acceleration/velocity feed-forwards in position mode) forms [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md).

After changing `VelFiltOn` or [VelFiltDef](VelFiltDef.md), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the controller recomputes the internal filter coefficients.

## Examples

```text
AVelFiltOn[1]=1     ; enable velocity filter 1
AVelFiltOn[2]=0     ; bypass velocity filter 2
AVelFiltOn[1]       ; read the velocity filter 1 enable state
```

## Changes between versions

In **v4** `VelFiltOn` can only be changed with the motor off and out of motion. In **v5 (central-i)** it may also be changed while the motor is on and in motion.

## See also

- [VelFiltDef](VelFiltDef.md) — defines each velocity filter's type and parameters
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- [VelGain](VelGain.md) / [VelKi](VelKi.md) — produce the PI output these filters shape
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — current command after the velocity filters
- [PosFiltOn](../03-position-control/PosFiltOn.md) — position-loop filter enables
- Appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md)
