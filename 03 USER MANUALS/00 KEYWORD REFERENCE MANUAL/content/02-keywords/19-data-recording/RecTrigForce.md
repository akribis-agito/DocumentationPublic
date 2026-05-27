---
keyword: RecTrigForce
summary: Command that overrides trigger detection and forces recording to proceed.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 252
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigForce

Command that overrides trigger detection and forces recording to proceed.

## Overview

`RecTrigForce` overrules trigger detection and forces the recording to continue as if the trigger condition were met. The forced trigger occurs regardless of whether `RecTrigForce` is called while pre-trigger data is being filled or while the scope is waiting for the trigger (after pre-trigger data is filled). It is useful when the configured trigger ([RecTrigTyp](RecTrigTyp.md), [RecTrigSrc](RecTrigSrc.md)) does not fire. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## Examples

```text
ARecTrigForce[1]     ; force-trigger the first scope
ARecTrigForce[2]     ; force-trigger the second scope
```

## See also

- [RecStart](RecStart.md) — start recording
- [RecStat](RecStat.md) — recording status
- [RecTrigTyp](RecTrigTyp.md) — trigger activation type
