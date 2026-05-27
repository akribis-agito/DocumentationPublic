---
keyword: DInFilt
summary: Software debounce filter for all digital inputs on an axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 213
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# DInFilt

Software debounce filter for all digital inputs on an axis.

## Overview

`DInFilt` sets a software debounce filter: a raw digital input must hold the same value for `DInFilt` consecutive samples before the change is asserted; otherwise the input keeps its previous state. For example, `DInFilt = 3` requires three consecutive readings of "1" before a "1" is asserted. It is the first stage of the [digital-input signal path](00-overview.md).

`DInFilt` is a single value that applies to **all** digital inputs of the axis/module (e.g. `CDInFilt` applies to all inputs of axis/module C). Debouncing improves noise immunity at the cost of reducing the effective sampling rate by the filter factor.

## Examples

```text
ADInFilt=3           ; require 3 consecutive matching samples
```

## See also

- [DInPort-DInPortHigh](DInPort-DInPortHigh.md) — resulting input states
- [DInLog-DInLogHigh](DInLog-DInLogHigh.md) — logic inversion
