---
summary: Denominator of the CNC queue A (or B) encoder scaling ratio.
---
# CNCAEncFactDn/CNCBEncFactDn

Denominator of the CNC queue A (or B) encoder scaling ratio.

## Overview

`CNCAEncFactDn` (and its `CNCBEncFactDn` counterpart) is the denominator of the encoder scaling ratio applied to CNC motion queue A (or B) position values. Together with [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) it defines the rational scale factor (`CNCAEncFactNu / CNCAEncFactDn`) that converts CNC position units to internal encoder counts. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
ACNCAEncFactDn=1     ; denominator of the CNC position scale factor
```

## See also

- [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) — numerator of the scale factor
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
