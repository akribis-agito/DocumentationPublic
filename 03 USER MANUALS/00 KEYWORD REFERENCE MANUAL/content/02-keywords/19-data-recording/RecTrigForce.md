---
keyword: RecTrigForce
summary: Command that overrides trigger detection and forces recording to proceed.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`RecTrigForce` overrules trigger detection and forces the recording to continue as if the trigger condition were met. It is useful when the configured trigger ([RecTrigTyp](RecTrigTyp.md), [RecTrigSrc](RecTrigSrc.md)) does not fire. Each array index selects a scope.

`RecTrigForce` can be issued at any time after [RecStart](RecStart.md). If the scope is still filling pre-trigger data ([RecStat](RecStat.md) 1), the force is latched and takes effect on the first recorded sample once the pre-trigger portion is filled and the scope begins waiting for the trigger ([RecStat](RecStat.md) 2); it does not shorten the pre-trigger fill. If the scope is already waiting for the trigger ([RecStat](RecStat.md) 2), it fires on the next recorded sample. The forced-trigger flag is cleared by the next [RecStart](RecStart.md).

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
