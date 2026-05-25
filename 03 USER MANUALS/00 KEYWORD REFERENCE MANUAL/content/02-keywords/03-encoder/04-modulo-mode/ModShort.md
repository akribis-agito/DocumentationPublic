# ModShort

**Definition:**

ModShort defines the path of motion taken in absolute point-to-point (PTP) motion when modulo mode is enabled (ModRev ≠ 0). It is used for general motion (when MotionMode = 1 or 2) or during homing (when HomingDef\[1, 11, …, 141\] = 12).

| Value | Descriptions |
|---|---|
| 0 | Axis will move to the target position similar to linear axis (additional revolution(s) if absolute position delta is more than ModRev). |
| 1 | Axis will move to the target only in negative direction. If the target is higher than current position, axis will take the shortest negative only path to the target. Otherwise, axis will move to the target position similar to linear axis (additional revolution(s) if absolute position delta is more than ModRev). |
| 2 | Axis will move to the target only in positive direction. If the target is lower than current position, axis will take the shortest positive only path to the target. Otherwise, axis will move to the target position similar to linear axis (additional revolution(s) if absolute position delta is more than ModRev). |
| 3 | Axis will move to the target in the shortest path. Axis will not move additional revolution(s) even if absolute position delta is more than ModRev. |

**Example:**

Assuming we command a point-to-point motion,

**Note:**

Conditions Path of motion Position delta is positive (absolute value more than 0.5*ModRev). ModShort = 0 (normal) ModShort = 2 (positive only) ModShort = 1 (negative only) ModShort = 3 (shortest path) Position delta is positive (absolute value less than 0.5*ModRev). ModShort = 0 (normal) ModShort = 2 (positive only) ModShort = 3 (shortest path) ModShort = 1 (negative only) Position delta is negative (absolute value more than 0.5*ModRev). ModShort = 0 (normal) ModShort = 1 (negative only) ModShort = 2 (positive only) ModShort = 3 (shortest path) Position delta is negative (absolute value less than 0.5*ModRev). ModShort = 0 (normal) ModShort = 1 (negative only) ModShort = 3 (shortest path) ModShort = 2 (positive only)
