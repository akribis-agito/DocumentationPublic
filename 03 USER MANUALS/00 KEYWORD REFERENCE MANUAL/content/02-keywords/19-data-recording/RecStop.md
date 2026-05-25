# RecStop

**Definition:**

RecStop commands the selected scope to stop recording. It can be called at any stage of the recording. If the recording is ongoing when RecStop is called, RecDataA/RecDataB metadata will be updated to report the actual length of the recording made.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

For example, RecStop\[1\] command will stop the recording of first scope.
