# PosFiltOn

**Definition:**

PosFiltOn is used to turn on/off the position filters. If PosFiltOn\[Index\] = 1, the filter is enabled. If PosFiltOn\[Index\] = 0, the filter is disabled (bypassed). The indices indicate the location of the position filter.

| Index | Descriptions |
|---|---|
| 1 | Post-profiler filter It is used to filter the profiler’s output and will change the final PosRef value. |
| 2 | Position error filter It is used to filter the position error input, and generally applicable to dual-loop system. |
