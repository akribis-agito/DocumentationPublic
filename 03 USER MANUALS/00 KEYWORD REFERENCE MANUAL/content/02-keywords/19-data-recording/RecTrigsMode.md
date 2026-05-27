---
keyword: RecTrigsMode
summary: Selects parallel (logical) or serial trigger detection per scope.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

In **parallel** mode, all configured triggers are evaluated every cycle and combined into a single boolean expression using the operators set in [RecTrigsLogic](RecTrigsLogic.md); the recording trigger fires as soon as that combined expression becomes true.

In **serial** mode the triggers must fire in order: trigger 1 first, then trigger 2, then trigger 3. The scope waits at trigger 1 until it activates, then advances to wait for trigger 2, and so on; the overall recording trigger fires only after the last defined trigger has activated. [RecTrigsLogic](RecTrigsLogic.md) has no effect in serial mode.

For a single-trigger setup, configure only trigger 1 and set the unused triggers to an inactive type (see the note on [RecTrigTyp](RecTrigTyp.md)).

## Examples

```text
ARecTrigsMode[1]=1   ; first scope uses parallel (logical) detection
ARecTrigsMode[1]=2   ; first scope uses serial detection
```

## See also

- [RecTrigsLogic](RecTrigsLogic.md) — logic joining triggers in parallel mode
- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
- [RecTrigSrc](RecTrigSrc.md) — trigger source variable
