---
keyword: PosFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 123
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
# PosFiltDef

Defines the type and parameters of each position-loop filter.

## Overview

`PosFiltDef` holds the definition of the two position-loop filters that [PosFiltOn](PosFiltOn.md) enables. Each filter is described by up to 5 consecutive array elements (a type code plus up to four parameters), so the two filters together occupy the 6-element array:

| Filter (N) | Description | Array elements |
|---|---|---|
| 1 | Post-profiler filter | `PosFiltDef[1]` … `PosFiltDef[5]` |
| 2 | Position-error filter | `PosFiltDef[6]` … `PosFiltDef[10]` |

For each filter, the first element is the **type of filter** and the next four are **parameters 1 to 4** whose meaning depends on the type.

## How it works

Within each 5-element block the layout is:

| Offset | Meaning |
|---|---|
| 1st | Type of filter (`0` = none, `1` = first-order low-pass, `2` = second-order low-pass, `3` = second-order low-pass with one zero, `4`/`5` = first/second-order lead-lag, `6`/`7` = first/second-order lead-lag by phase, `8` = notch, `9` = complex lead-lag) |
| 2nd–5th | Parameters 1 to 4 (frequencies in Hz/100, damping ratios in %, phase in degrees, notch depth in dB — depending on type) |

The selected filter is realised as a second-order (biquad) section in the position loop at the location set by [PosFiltOn](PosFiltOn.md): index 1 shapes the profiler output (the final [PosRef](../../10-motion/01-kinematics-status/PosRef.md)), index 2 shapes the position error [PosErr](../../10-motion/01-kinematics-status/PosErr.md) before [PosGain](PosGain.md). After writing `PosFiltDef` (and the matching [PosFiltOn](PosFiltOn.md)), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the coefficients are recomputed.

The full parameter-by-type definitions, transfer functions and units are in the appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md).

## Examples

```text
; Position-error filter (index 2) as a second-order low-pass at 850 Hz, damping 0.71
APosFiltDef[6]=2        ; type: second-order low-pass
APosFiltDef[7]=85000    ; cutoff 850 Hz (Hz/100)
APosFiltDef[8]=71       ; damping ratio 0.71 (%)
APosFiltOn[2]=1         ; enable the position-error filter
ACalcFilters            ; recompute filter coefficients
```

## Changes between versions

In **v4** `PosFiltDef` can only be changed with the motor off and out of motion. In **v5 (central-i)** it may also be changed while the motor is on and in motion.

## See also

- [PosFiltOn](PosFiltOn.md) — enables each position filter defined here
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — signal filtered at index 2
- [PosRef](../../10-motion/01-kinematics-status/PosRef.md) — reference shaped at index 1
- [VelFiltDef](../04-velocity-control/VelFiltDef.md) — velocity-loop filter definitions
- Appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md)
