---
summary: Per-axis resolution ratio for CNC calculations (future feature, no current effect).
---
# CNCAEncRatio/CNCBEncRatio

Per-axis resolution ratio for CNC calculations (future feature, no current effect).

## Overview

`CNCAEncRatio` (and its `CNCBEncRatio` counterpart on the second CNC engine) defines the ratio between the resolution of one axis and the other member axes, to allow accurate CNC calculations when the member axes have non-identical physical resolutions. This parameter is axis related and should be set separately for each member axis.

> **Documentation pending:** This is a future feature. The controller accepts the parameter, but it has no effect on the CNC calculations. Currently, the CNC motion calculations assume identical resolution for all member axes.

## Examples

```text
CNCAEncRatio?       ; query the configured resolution ratio
```

## See also

- [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) — encoder scale factor numerator
- [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — encoder scale factor denominator
