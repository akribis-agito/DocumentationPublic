---
keyword: FFFiltOn
summary: Enables or bypasses the feedforward filter.
availability:
  standalone: []
  central-i:
  - v5
can_code: 728
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# FFFiltOn

Enables or bypasses the feedforward filter.

## Overview

`FFFiltOn` enables or bypasses the feedforward filter that acts on the combined feedforward output (the sum of the [AccFFW](AccFFW.md) and [VelFFW](VelFFW.md) terms and, on AGM800 and AGM800-EC, the friction feedforward current) before it is added to the velocity-loop output to form the current reference.

| `FFFiltOn[1]` | Behaviour |
|---|---|
| 0 | Filter bypassed (default) — the combined feedforward output passes through unchanged. |
| 1 | Filter enabled — the combined feedforward output is passed through the filter defined by [FFFiltDef](FFFiltDef.md). |

## How it works

When enabled, the filter is a second-order (biquad) section whose coefficients are computed from the parameters in [FFFiltDef](FFFiltDef.md). It is placed on the combined feedforward signal:

$$
\text{AccFFW term} + \text{VelFFW term} + \text{friction term} \;\longrightarrow\; \boxed{\text{feedforward filter}} \;\longrightarrow\; \text{add to velocity-loop output}
$$

The feedforward filter is a single second-order (biquad) section placed on the combined feedforward branch — it is not a cascade of sections like the velocity-output filter. Its internal history (the stored previous and previous-previous samples) advances each control cycle independently of the rest of the loop.

On AGM800 and AGM800-EC the friction feedforward current ([Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md)) is added to the same sum before the filter, so the filter smooths friction too. With `FFFiltOn` = 1 the friction step at a reversal is smoothed and delayed. At CNC segment transitions the firmware zeroes all feedforward for two control cycles, friction included; this happens on the sum, before the filter. In velocity mode, and in force mode with [ForcePIVOn](../07-force-control/ForcePIVOn.md) = 1, [AccFFW](AccFFW.md) and [VelFFW](VelFFW.md) are not used, so the filter carries friction only. [CurrFFWValues](CurrFFWValues.md)`[1]` reads the filter output; `CurrFFWValues[6]` reads the friction current before the filter.

When bypassed, the combined feedforward output is used directly. After changing `FFFiltOn` or [FFFiltDef](FFFiltDef.md), run [CalcFilters](../01-general-keywords/CalcFilters.md) so the controller recomputes the internal filter coefficients.

## Examples

```text
AFFFiltOn[1]=1       ; enable the feedforward filter
AFFFiltOn[1]=0       ; bypass the feedforward filter
ACalcFilters         ; recompute filter coefficients
```

## See also

- [FFFiltDef](FFFiltDef.md) — feedforward filter definition parameters
- [CalcFilters](../01-general-keywords/CalcFilters.md) — recomputes filter coefficients after changes
- [AccFFW](AccFFW.md) / [VelFFW](VelFFW.md) — feedforward terms the filter acts on
- [Friction feedforward](../../../03-special-features/friction-compensation/00-overview.md) — friction current that also passes through this filter
- [CurrFFWValues](CurrFFWValues.md) — read back the feedforward currents before and after the filter
