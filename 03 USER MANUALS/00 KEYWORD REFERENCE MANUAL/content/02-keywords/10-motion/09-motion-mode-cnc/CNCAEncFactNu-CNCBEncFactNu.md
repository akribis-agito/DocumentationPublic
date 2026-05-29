---
summary: Numerator of the CNC queue A (or B) encoder scaling ratio.
---
# CNCAEncFactNu/CNCBEncFactNu

Numerator of the CNC queue A (or B) encoder scaling ratio.

## Overview

`CNCAEncFactNu` (and its `CNCBEncFactNu` counterpart on the second CNC engine) is the numerator of the per-axis path-to-encoder scaling ratio applied to a CNC path. The effective scale for the axis is `CNCAEncFactNu / CNCAEncFactDn`, which maps CNC path units to the axis encoder counts so that member axes with different encoder resolutions can take part in the same coordinated path while the resultant geometry stays accurate. It is an axis-related parameter saved to flash, paired with the denominator [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md), and cannot be changed while the axis is in motion. This is the numerator/denominator form that the CNC engine actually applies; the single-value [CNCAEncRatio/CNCBEncRatio](CNCAEncRatio-CNCBEncRatio.md) expresses the same idea but currently has no effect.

## How it works

Set the pair so that `CNCAEncFactNu / CNCAEncFactDn` equals the resolution ratio needed for the axis. When numerator and denominator are equal (the default `1` / `1`), the ratio is 1 and no scaling is applied. Both keywords accept whole numbers in the range `1`-`2000`, so a wide range of rational ratios can be expressed — for example `3` / `2` for a 1.5:1 resolution difference.

The ratio is applied as the path runs: the engine uses it to convert each axis's position reference into the queued path units, and applies it the other way to convert the queued segment coordinates back into per-axis position commands. Configure the pair on each member axis before starting the move, since it cannot be changed in motion.

## Examples

```text
ACNCAEncFactNu=1        ; numerator = 1 on axis A (default)
ACNCAEncFactNu=3        ; with CNCAEncFactDn = 2 gives a 3/2 (1.5:1) scaling ratio
ACNCAEncFactNu          ; read the current numerator on axis A
```

## See also

- [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — denominator of the scaling ratio
- [CNCAEncRatio/CNCBEncRatio](CNCAEncRatio-CNCBEncRatio.md) — single-value form (no current effect)
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
