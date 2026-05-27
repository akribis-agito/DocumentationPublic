---
summary: Per-axis resolution ratio for CNC calculations (future feature, no current effect).
---
# CNCAEncRatio/CNCBEncRatio

Per-axis resolution ratio for CNC calculations (future feature, no current effect).

## Overview

`CNCAEncRatio` (and its `CNCBEncRatio` counterpart on the second CNC engine) is intended to describe the ratio between the resolution of one member axis and the others, so that a CNC path stays geometrically accurate when the member axes do not share the same counts-per-unit. It is the single-value form of the same compensation provided by the numerator/denominator pair [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md). It is an axis-related parameter and should be set separately for each member axis.

> **Future feature — no effect today.** The controller accepts and stores this parameter, but it does not currently influence the CNC path calculations. As things stand the CNC engine assumes identical resolution for all member axes unless you compensate through the factor pair below.

## How it works

For per-axis encoder-resolution compensation on a CNC path today, use the rational pair [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md), which expresses the resolution ratio as a numerator over a denominator and is the form the CNC engine actually applies. `CNCAEncRatio` is retained for compatibility and for a future implementation; configure the factor pair instead, and verify behavior against your firmware before relying on `CNCAEncRatio` alone.

## Examples

```text
ACNCAEncRatio[1]      ; read the configured resolution ratio (no effect on motion today)
```

## See also

- [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — numerator/denominator form actually applied to the CNC path
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
