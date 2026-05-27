---
summary: Jerk (smoothing) for the CNC vector motion profile (future feature, no current effect).
---
# CNCAJerk/CNCBJerk

Jerk (smoothing) for the CNC vector motion profile (future feature, no current effect).

## Overview

`CNCAJerk` (and its `CNCBJerk` counterpart on the second CNC engine) defines the jerk (smoothing) to use when calculating the CNC vector motion profile.

> **Documentation pending:** This is a future feature. The controller accepts the parameter, but it has no effect on the CNC calculations. Currently, the CNC vector motion profiler is calculated without smoothing.

## Examples

```text
CNCAJerk?           ; query the configured jerk value
```

## See also

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active segment acceleration
- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — active segment deceleration
