---
keyword: ForceSamples
summary: Timings of the last completed ForceCmdVal application, in controller cycles.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 736
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceSamples

Timings of the last completed ForceCmdVal application, in controller cycles.

## Overview

`ForceSamples` reports the timings of the last completed [ForceCmdVal](ForceCmdVal.md) application. It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2. The unit is the number of controller cycles (typically 1 cycle equals $T_{s} = \frac{1}{16384}Hz = 61.03515\mu s$). The settling timings derive from [ForceInTTol](ForceInTTol.md) and [ForceInTTime](ForceInTTime.md).

## How it works

Each array element represents a different time, as shown.

| Index | Descriptions |
|----|----|
| 1 | The time for ForceRef to reach the target value (ForceCmdVal), starting from its initial value. It is analogous to move time. |
| 2 | The time since the start of new target force application until the time when ForceErr **begins to** settle into the ForceInTTol for at least ForceInTTime. It is analogous to move and settle time. |
| 3 | The time since the start of new target force application until the time when ForceErr **settles** into the ForceInTTol for at least ForceInTTime. It is analogous to move, settle and in-target time. |
| 4 | The time since ForceRef equals to target value (ForceCmdVal) until the axis **begins to** settle into the ForceInTTol for at least ForceInTTime. It is analogous to settle time. |

In summary,

$$
ForceSamples\lbrack 2\rbrack = \ ForceSamples\lbrack 1\rbrack + \ ForceSamples\lbrack 4\rbrack
$$

$$
ForceSamples\lbrack 3\rbrack = \ ForceSamples\lbrack 2\rbrack + \frac{ForceInTTol}{T_{s}}\ 
$$

## Examples

```text
ForceSamples[1]?    ; move time, in controller cycles
ForceSamples[3]?    ; move + settle + in-target time
```

## See also

- [ForceInTStat](ForceInTStat.md) — in-target status
- [ForceInTTol](ForceInTTol.md) — settling window
- [ForceInTTime](ForceInTTime.md) — required dwell time within the window
