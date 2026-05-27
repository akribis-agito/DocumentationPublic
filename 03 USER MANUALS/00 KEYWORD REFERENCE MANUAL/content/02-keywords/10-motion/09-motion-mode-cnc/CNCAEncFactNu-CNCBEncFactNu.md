---
summary: Numerator of the CNC queue A (or B) encoder scaling ratio.
---
# CNCAEncFactNu/CNCBEncFactNu

Numerator of the CNC queue A (or B) encoder scaling ratio.

## Overview

`CNCAEncFactNu` (and its `CNCBEncFactNu` counterpart) is the numerator of the encoder scaling ratio applied to CNC motion queue A (or B) position values. The effective scale is `CNCAEncFactNu / CNCAEncFactDn`, converting CNC position units to internal encoder counts. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

## Examples

```text
CNCAEncFactNu=1     ; numerator of the CNC position scale factor
```

## See also

- [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — denominator of the scale factor
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
