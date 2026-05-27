---
keyword: VelFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 121
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
---
# VelFiltDef

Defines the type and parameters of each velocity-loop filter.

## Overview

`VelFiltDef` holds the definition of the velocity-loop filters that [VelFiltOn](VelFiltOn.md) enables. Each filter is described by up to 5 consecutive array elements (a type code plus up to four parameters), so filter N occupies elements `VelFiltDef[N*5-4]` through `VelFiltDef[N*5]`:

| Filter (N) | Description | Array elements |
|---|---|---|
| 1 | Velocity filter 1 | `VelFiltDef[1]` … `VelFiltDef[5]` |
| 2 | Velocity filter 2 | `VelFiltDef[6]` … `VelFiltDef[10]` |
| 3 | Velocity filter 3 | `VelFiltDef[11]` … `VelFiltDef[15]` |
| 4 | Velocity filter 4 | `VelFiltDef[16]` … `VelFiltDef[20]` |

For each filter, the first element is the **type of filter** and the next four are **parameters 1 to 4** whose meaning depends on the type.

## How it works

Within each 5-element block the layout is:

| Offset | Meaning |
|---|---|
| 1st | Type of filter (`0` = none, `1` = first-order low-pass, `2` = second-order low-pass, `3` = second-order low-pass with one zero, `4`/`5` = first/second-order lead-lag, `6`/`7` = first/second-order lead-lag by phase, `8` = notch, `9` = complex lead-lag) |
| 2nd–5th | Parameters 1 to 4 (frequencies in Hz/100, damping ratios in %, phase in degrees, notch depth in dB — depending on type) |

Each enabled filter is realised as a second-order (biquad) section applied in series to the velocity-PI output (the [VelGain](VelGain.md) + [VelKi](VelKi.md) result) on its way to the current command [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md). After writing `VelFiltDef` (and the matching [VelFiltOn](VelFiltOn.md)), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the coefficients are recomputed.

The full parameter-by-type definitions, transfer functions and units are in the appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md).

## Examples

```text
; Velocity filter 1 as a notch at 450 Hz, 6 dB depth, 40 Hz width
AVelFiltDef[1]=8        ; type: notch
AVelFiltDef[2]=45000    ; notch frequency 450 Hz (Hz/100)
AVelFiltDef[3]=6        ; notch depth 6 dB
AVelFiltDef[4]=4000     ; notch width 40 Hz (Hz/100)
AVelFiltOn[1]=1         ; enable velocity filter 1
ACalcFilters            ; recompute filter coefficients
```

## Changes between versions

In **v4** `VelFiltDef` can only be changed with the motor off and out of motion. In **v5 (central-i)** it may also be changed while the motor is on and in motion.

## See also

- [VelFiltOn](VelFiltOn.md) — enables each velocity filter defined here
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- [VelGain](VelGain.md) / [VelKi](VelKi.md) — produce the PI output these filters shape
- [CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md) — current command after the velocity filters
- [PosFiltDef](../03-position-control/PosFiltDef.md) — position-loop filter definitions
- Appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md)
