# RecStat

**Definition:**

RecStat reports the recording status of each scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

The definition of value returned from RecStat is as shown.

| Value | Status |
|----|----|
| 0 | Invalid recorded data (default condition upon power up) |
| 1 | Scope is filling pre-trigger data, as defined by RecTrigPos |
| 2 | Pre-trigger data are filled. Scope is buffering and waiting for the trigger. |
| 3 | Trigger is detected and recording is progressing. |
| 4 | Recording is completed without interruption. |
| 5 | Recording is stopped. |
| 6 | Recording is stopped before trigger is detected. |

For example, if RecStat\[1\] returns the value of 4, it indicates that recording of first scope is successful, where user can begin to stream the recorded data.
