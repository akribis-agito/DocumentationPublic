---
keyword: ForceRefFOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 579
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# ForceRefFOn

Enables the force-command reference filter.

## Overview

`ForceRefFOn` is the switch for the first-order low-pass filter applied to the force command:

| Value | Behaviour |
|-------|-----------|
| 0     | Filter bypassed — the force reference equals the raw command |
| 1     | Filter enabled — the cut-off frequency is set by [ForceRefFilt](ForceRefFilt.md) |

The default is `0` (filter disabled). The keyword is stored in flash.

## How it works

When `ForceRefFOn = 1`, the filter coefficient is computed from [ForceRefFilt](ForceRefFilt.md) and the raw force command is low-pass filtered each cycle to produce the force reference [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md). When `ForceRefFOn = 0`, the filter coefficient is set so the filter passes the command through unchanged, and `ForceRef` follows the raw command directly.

Writing `ForceRefFOn` recomputes the coefficient immediately. The setting applies in both force-control structures selected by [ForcePIVOn](ForcePIVOn.md).

## Examples

```text
AForceRefFOn[1]=1       ; enable the force-command reference filter
AForceRefFOn[1]=0       ; bypass the filter
AForceRefFOn[1]         ; read the filter switch
```

## See also

- [ForceRefFilt](ForceRefFilt.md) — cut-off frequency used when this filter is enabled
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — filtered force reference
- [Force control](00-overview.md) — force-loop structure overview
