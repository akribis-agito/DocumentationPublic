---
keyword: FFFiltOn
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
---
# FFFiltOn

Enables or bypasses the feedforward filter.

## Overview

`FFFiltOn` enables or bypasses the feedforward filter that acts on the combined feedforward output (the sum of the [AccFFW](AccFFW.md) and [VelFFW](VelFFW.md) terms) before it is added to the velocity-loop output to form the current reference.

| `FFFiltOn[1]` | Behaviour |
|---|---|
| 0 | Filter bypassed (default) — the combined feedforward output passes through unchanged. |
| 1 | Filter enabled — the combined feedforward output is passed through the filter defined by [FFFiltDef](FFFiltDef.md). |

## How it works

When enabled, the filter is a second-order (biquad) section whose coefficients are computed from the parameters in [FFFiltDef](FFFiltDef.md). It is placed on the combined feedforward signal:

$$
AccFFW \text{ term} + VelFFW \text{ term} \;\longrightarrow\; \boxed{\text{feedforward filter}} \;\longrightarrow\; \text{add to velocity-loop output}
$$

When bypassed, the combined feedforward output is used directly.

## Examples

```text
AFFFiltOn[1]=1       ; enable the feedforward filter
AFFFiltOn[1]=0       ; bypass the feedforward filter
```

## See also

- [FFFiltDef](FFFiltDef.md) — feedforward filter definition parameters
- [AccFFW](AccFFW.md) / [VelFFW](VelFFW.md) — feedforward terms the filter acts on
