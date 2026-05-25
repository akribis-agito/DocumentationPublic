# ForceSamples

**Condition:**

This keyword is only applicable when [ForceCmdSrc](../../../02-keywords/08-axis-operation/04-force-operation-mode/ForceCmdSrc.md) = 1 or 2.

**Definition:**

ForceSamples reports the timings of the last completed ForceCmdVal application. The unit is in number of controller cycles (typically 1 cycle equals to $T_{s} = \frac{1}{16384}Hz = 61.03515\mu s$).

Each array element represents different times, as shown.

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
