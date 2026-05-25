# RecTrigTyp

**Definition:**

RecTrigTyp defines how the trigger is activated (trigger type). Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

Each RecTrigTyp refers to different trigger activation logic. The trigger source value originates from variable pointed by RecTrigSrc, subject to masking.

| Value | Trigger activation logic |
|----|----|
| 0 | Immediate trigger (no trigger source needed) |
| 1 | Activated when the source value is more than RecTrigVal |
| 2 | Activated when the source value equals RecTrigVal |
| 3 | Activated when the source value is not equal to RecTrigVal |
| 4 | Activated when the source value is less than RecTrigVal |
| 5 | Activated upon the rising edge of source value beyond RecTrigVal. |
| 6 | Activated upon the falling edge of source value below RecTrigVal. |
| 7 | Immediate trigger (no trigger source needed) |
| 8 | Activated when the source value is different from its value at the start of recording |
| 9 | Activated when the source value is within the range of (RecTrigVal, RecTrigValMax) |
| 10 | Activated when the source value is not within the range of (RecTrigVal, RecTrigValMax) |
| 11 | Activated upon the entry of source value into the range of (RecTrigVal, RecTrigValMax) |
| 12 | Activated upon the exit of source value into the range of (RecTrigVal, RecTrigValMax) |

**Note:**

RecTrigTyp[2] = 0, RecTrigTyp[3] = 0, RecTrigsLogic[1] = 1, RecTrigsLogic[2] = 1 and RecTrigMode[1] = 1 are normally commanded to achieve single trigger setting for the first scope. Similar commands can be made for the second scope.
