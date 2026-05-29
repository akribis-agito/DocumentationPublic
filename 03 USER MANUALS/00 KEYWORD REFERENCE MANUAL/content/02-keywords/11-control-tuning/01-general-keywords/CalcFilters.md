---
keyword: CalcFilters
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 360
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
---
# CalcFilters

Command that recalculates the internal coefficients of the customisable loop filters from their definition keywords.

## Overview

The customisable filters in the position, velocity, feedforward and force paths are configured through definition keywords. Changing a definition keyword does **not** change the filter the controller runs — it only records that the filter *definition* has changed and is now out of step with the coefficients in use. `CalcFilters` is the command that reads all the pending definitions, validates them, computes the new coefficients, and switches the running filters over to them in one step.

`CalcFilters` operates on the axis it is addressed to and acts on every filter of that axis that is marked as changed. Filters whose definition has not changed since the last calculation are left untouched.

The keywords whose change requires a `CalcFilters` to take effect are:

1. `PosFiltDef` / `PosFiltOn` — position filters
2. `VelFiltDef` / `VelFiltOn` — velocity filters
3. `FFFiltDef` / `FFFiltOn` — feedforward filter
4. `ForceFiltDef` / `ForceFiltOn` — force filters

## How it works

### What marks a filter as needing recalculation

Each time one of the definition keywords above is written, the new value is compared against the value that was in effect at the last successful calculation. If it differs, the corresponding filter is flagged as "pending recalculation" in [FilterStatus](FilterStatus.md) (bit `n+0` of that filter's field is set). Writing a value identical to the one already in use does not flag the filter. While any filter is flagged, [StatReg](../../07-status-and-faults/StatReg.md) bit 26 ("filters modified") is set.

### What CalcFilters does, per filter

For every filter flagged as pending, the controller:

1. **Validates the definition.** The filter type must be a known type; each parameter must be within its allowed range. The result is written to that filter's field in [FilterStatus](FilterStatus.md): bit `n+1` is set if the filter type is unknown, and bits `n+2`–`n+5` are set per out-of-range parameter.
2. **On success**, computes the new coefficients, switches the running filter to them, clears that filter's history buffer (so the new filter starts clean), clears the pending-recalculation flag, and records the accepted definition as the new reference for future change-detection.
3. **On failure** (unknown type or out-of-range parameter), the controller rejects that filter's changes. The whole definition reverts to the last accepted state: the filter on/off flag, the filter type, and all four defining parameters are restored to the values from the last successful calculation. The filter therefore keeps running with its previous, valid coefficients. An error is logged and returned. (This validate-and-revert behaviour is present on central-i v5 only.)

After processing all of an axis's filters, the controller returns a single reply: an error if any filter failed validation, otherwise success.

### Status bits cleared

When `CalcFilters` completes with no failure, both [StatReg](../../07-status-and-faults/StatReg.md) bit 26 ("filters modified") and bit 27 ("calc-filters failed") are cleared. If any filter failed validation, the "calc-filters failed" bit (27) is set instead.

On firmware where the enable sequence checks these bits, the axis cannot be enabled while bit 26 or bit 27 is set — see [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md). On firmware that allows on-the-fly recalculation (where `CalcFilters` is permitted in motion and with the motor on), these two bits no longer block enabling.

### Order of messages matters

Because `CalcFilters` validates whatever is present at the moment it runs, all the parameters of a filter must be set **before** `CalcFilters` in the same message. If `CalcFilters` runs before the full definition is in place, the partially defined filter is validated as-is. If that partial definition is invalid, it is rejected (the on/off flag, type, and all four parameters revert to the last accepted definition), and the previously running filter is kept. Parameters written after `CalcFilters` are not seen by that calculation, so they take effect only when a later `CalcFilters` validates them.

The example below configures velocity filter 1 as a notch at 450 Hz, 6 dB depth, 40 Hz width.

| Parameters | Initial values | Good order, after CalcFilters | Bad order, after CalcFilters |
|---|---|---|---|
| `VelFiltOn[1]` | 1 | 1 | 1 |
| `VelFiltDef[1]` | 1 | 8 | 8 |
| `VelFiltDef[2]` | 20000 | 45000 | 45000 |
| `VelFiltDef[3]` | 0 | 6 | 0 |
| `VelFiltDef[4]` | 0 | 4000 | 0 |
| `VelFiltDef[5]` | 0 | 0 | 0 |
| Result | Velocity filter 1 = low-pass at 200 Hz, on | Notch at 450 Hz, 6 dB, 40 Hz width, on. **Accepted.** | Notch definition incomplete (depth 0, width 0) — **rejected as an invalid notch.** The definition reverts to the last accepted state (the filter stays a low-pass). `VelFiltDef[3]` and `[4]` are then written, but having arrived after `CalcFilters` they were not part of this validation and are not applied until the next `CalcFilters`. |

- Good order: `VelFiltDef[1]=8; VelFiltDef[2]=45000; VelFiltDef[3]=6; VelFiltDef[4]=4000; CalcFilters`
- Bad order: `VelFiltDef[1]=8; VelFiltDef[2]=45000; CalcFilters; VelFiltDef[3]=6; VelFiltDef[4]=4000`

## Examples

```text
AVelFiltDef[1]=8; AVelFiltDef[2]=45000; AVelFiltDef[3]=6; AVelFiltDef[4]=4000; ACalcFilters   ; define then calculate
ACalcFilters                                                                                  ; recalculate the axis filters now
```

## See also

- [FilterStatus](FilterStatus.md) — per-filter calculation/validation result
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 26 (filters modified) / bit 27 (calc-filters failed)
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — enable sequence may check the filter status bits
