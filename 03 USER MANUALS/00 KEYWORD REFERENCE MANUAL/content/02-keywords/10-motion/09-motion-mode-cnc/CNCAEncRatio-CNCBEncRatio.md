---
summary: Reserved per-axis CNC resolution-ratio keyword (not exposed in current firmware).
---
# CNCAEncRatio/CNCBEncRatio

Reserved per-axis CNC resolution-ratio keyword. Not exposed by current firmware.

## Overview

`CNCAEncRatio` / `CNCBEncRatio` were intended to describe the ratio between the resolution of one CNC member axis and the others, so that a CNC path stays geometrically accurate when member axes do not share the same counts-per-unit.

> **Not in current firmware.** Neither `CNCAEncRatio` nor `CNCBEncRatio` is exposed as a keyword by the present firmware (LTS v3.X.X or develop). Use the rational pair [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) for the equivalent per-axis CNC encoder scaling.

The vector-motion analogue [VecEncRatio](../10-motion-mode-vector/VecEncRatio.md) does exist for the Vector engine; the CNC engine uses the factor pair above instead.

## See also

- [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — numerator/denominator form actually applied to the CNC path
- [VecEncRatio](../10-motion-mode-vector/VecEncRatio.md) — the vector-engine analogue
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
