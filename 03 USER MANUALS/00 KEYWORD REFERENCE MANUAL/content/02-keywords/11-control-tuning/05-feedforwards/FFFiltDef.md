---
keyword: FFFiltDef
summary: Defines the feedforward filter parameters.
availability:
  standalone: []
  central-i:
  - v5
can_code: 729
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# FFFiltDef

Defines the feedforward filter parameters.

## Overview

`FFFiltDef` defines the parameters of the feedforward filter. The filter acts on the combined feedforward output (the sum of the [AccFFW](AccFFW.md) and [VelFFW](VelFFW.md) terms and, on AGM800 and AGM800-EC, the friction feedforward current) when it is enabled by [FFFiltOn](FFFiltOn.md), before that output is added to the velocity-loop output to form the current reference.

The feedforward filter is the single customisable filter in this group, index N = 1. Each customisable filter is described by up to 5 parameters: a filter-type selector plus up to four type-specific parameters. The five elements for the feedforward filter are `FFFiltDef[1]` through `FFFiltDef[5]`.

| Index | Description |
|---|---|
| `FFFiltDef[1]` | Type of filter |
| `FFFiltDef[2]` | Parameter 1 |
| `FFFiltDef[3]` | Parameter 2 |
| `FFFiltDef[4]` | Parameter 3 |
| `FFFiltDef[5]` | Parameter 4 |

## How it works

The filter type and its parameters (cutoff/notch/pole/zero frequencies, damping ratios, etc.) are listed in the customisable filter reference. The controller computes the second-order (biquad) coefficients from these parameters and applies the filter to the combined feedforward output when [FFFiltOn](FFFiltOn.md)`[1] = 1`. This is a single biquad section on the combined feedforward branch, not a cascade of sections. After writing `FFFiltDef` (and the matching [FFFiltOn](FFFiltOn.md)), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the coefficients are recomputed.

On AGM800 and AGM800-EC the friction feedforward current ([Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md)) is added to the same sum before the filter, so the filter smooths friction too. With [FFFiltOn](FFFiltOn.md) = 1 the friction step at a reversal is smoothed and delayed. At CNC segment transitions the firmware zeroes all feedforward for two control cycles, friction included; this happens on the sum, before the filter. In velocity mode, and in force mode with [ForcePIVOn](../07-force-control/ForcePIVOn.md) = 1, [AccFFW](AccFFW.md) and [VelFFW](VelFFW.md) are not used, so the filter carries friction only. [CurrFFWValues](CurrFFWValues.md)`[1]` reads the filter output; `CurrFFWValues[6]` reads the friction current before the filter.

The full parameter-by-type definitions, transfer functions and units are in the appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md) (index N = 1 for the feedforward filter).

## Examples

```text
AFFFiltDef[1]=2      ; filter type: second-order low-pass
AFFFiltDef[2]=85000  ; parameter 1: cutoff frequency (850 Hz, in Hz/100)
AFFFiltDef[3]=71     ; parameter 2: damping ratio (0.71, in %)
AFFFiltOn[1]=1       ; enable the feedforward filter
ACalcFilters         ; recompute filter coefficients
```

## See also

- [FFFiltOn](FFFiltOn.md) — enable/bypass the feedforward filter
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- [AccFFW](AccFFW.md) / [VelFFW](VelFFW.md) — feedforward terms the filter acts on
- [Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md) — friction current that also passes through this filter
- [CurrFFWValues](CurrFFWValues.md) — read back the feedforward currents before and after the filter
- Appendix: [Customisable filter (FiltDef)](../../../06-appendix/customisable-filter-filtdef.md) — full filter-type and parameter reference
