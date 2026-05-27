---
keyword: RecTrigsMode
summary: Selects parallel (logical) or serial trigger detection per scope.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 564
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigsMode

Selects parallel (logical) or serial trigger detection per scope.

## Overview

`RecTrigsMode` defines the trigger detection mode, with each scope supporting up to 3 triggers. In parallel mode, triggers are combined logically via [RecTrigsLogic](RecTrigsLogic.md); in serial mode, triggers must occur in sequence. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## How it works

Its value definitions are as shown. Please refer to [Data recording](00-overview.md) for the flowchart.

| Value | Detection mode               |
|-------|------------------------------|
| 1     | Parallel (logical) detection |
| 2     | Serial detection             |

## Examples

```text
ARecTrigsMode[1]=1   ; first scope uses parallel (logical) detection
ARecTrigsMode[1]=2   ; first scope uses serial detection
```

## See also

- [RecTrigsLogic](RecTrigsLogic.md) — logic joining triggers in parallel mode
- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
- [RecTrigSrc](RecTrigSrc.md) — trigger source variable
