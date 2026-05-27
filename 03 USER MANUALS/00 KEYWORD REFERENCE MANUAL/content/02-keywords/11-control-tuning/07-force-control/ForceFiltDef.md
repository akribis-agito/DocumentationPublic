---
keyword: ForceFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 740
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
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
# ForceFiltDef

Defines the type and parameters of each force-loop filter.

## Overview

`ForceFiltDef` holds the definition of the two force output filters that [ForceFiltOn](ForceFiltOn.md) enables. Each filter is described by up to 5 consecutive array elements (a type code plus up to four parameters):

| Filter (N) | Description    | Array elements |
|------------|----------------|----------------|
| 1          | Force filter 1 | `ForceFiltDef[1]` … `ForceFiltDef[5]`   |
| 2          | Force filter 2 | `ForceFiltDef[6]` … `ForceFiltDef[10]`  |

For each filter, the first element is the **type of filter** and the next four are **parameters 1 to 4** whose meaning depends on the type.

These filters are used **only** in standard force control ([ForcePIVOn](ForcePIVOn.md) = 0); in force-over-PIV control (`ForcePIVOn = 1`) they have no effect.

## How it works

Within each 5-element block the layout is:

| Offset | Meaning |
|--------|---------|
| 1st | Type of filter (`0` = none, `1` = first-order low-pass, `2` = second-order low-pass, `3` = second-order low-pass with one zero, `4`/`5` = first/second-order lead-lag, `6`/`7` = first/second-order lead-lag by phase, `8` = notch, `9` = complex lead-lag) |
| 2nd–5th | Parameters 1 to 4 (frequencies in Hz/100, damping ratios in %, phase in degrees, notch depth in dB — depending on type) |

Each filter is realised as a second-order (biquad) section. Force filter 1 and force filter 2 are applied in series to the force PID-plus-feedforward output to form the current reference, at the location enabled by [ForceFiltOn](ForceFiltOn.md). After writing `ForceFiltDef` (and the matching [ForceFiltOn](ForceFiltOn.md)), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the coefficients are recomputed.

The full parameter-by-type definitions, transfer functions and units are in the appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md).

## Examples

```text
; Force filter 1 as a second-order low-pass at 500 Hz, damping 0.71
AForceFiltDef[1]=2      ; type: second-order low-pass
AForceFiltDef[2]=50000  ; cutoff 500 Hz (Hz/100)
AForceFiltDef[3]=71     ; damping ratio 0.71 (%)
AForceFiltOn[1]=1       ; enable force filter 1
ACalcFilters            ; recompute filter coefficients
```

## Changes between versions

In **v4** `ForceFiltDef` can only be changed with the motor off and out of motion. In **v5 (central-i)** it may also be changed while the motor is on and in motion.

## See also

- [ForceFiltOn](ForceFiltOn.md) — enables each force filter defined here
- [ForcePIVOn](ForcePIVOn.md) — these filters apply only when this is 0
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- Appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md)
