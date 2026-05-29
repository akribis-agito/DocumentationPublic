---
keyword: RecGap
summary: Down-sampling factor per scope that sets the recording frequency.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 242
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
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecGap

Down-sampling factor per scope that sets the recording frequency.

## Overview

`RecGap` is an array that defines the down-sampling factor applied to the controller cycle frequency, thereby setting the data recording frequency of each scope. A larger value records less often, which extends the time span captured for a given [RecLength](RecLength.md). Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## How it works

The data recording frequency is:

$$
\text{Data recording frequency of scope } x\ [\text{Hz}] = \frac{\text{Controller cycle rate}\ [\text{Hz}]}{\text{RecGap}[x]}
$$

Internally the scope keeps a down-counter that is reloaded with `RecGap` and decremented once per controller cycle; a sample of every recorded channel is taken only on the cycle when the counter reaches zero, after which it reloads. So `RecGap[x]=1` records on every cycle, `RecGap[x]=10` records on every tenth cycle, and so on. `RecGap` is read once when [RecStart](RecStart.md) runs and is fixed for the duration of that recording.

Together with [RecLength](RecLength.md), `RecGap` also determines the total recording period.

## Examples

```text
ARecGap[1]=1         ; first scope records at full controller cycle rate
ARecGap[2]=10        ; second scope records at 1/10 of the cycle rate
ARecGap[1]          ; query the first scope down-sampling factor
```

## See also

- [RecLength](RecLength.md) — number of data points per parameter (sets the period)
- [RecStart](RecStart.md) — start recording once setup is complete
- [LoggerGap](LoggerGap.md) — continuous-logger equivalent down-sampling
