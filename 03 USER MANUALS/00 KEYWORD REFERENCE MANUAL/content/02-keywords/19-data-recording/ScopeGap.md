---
keyword: ScopeGap
summary: Sets the Central-i scope sampling interval.
availability:
  standalone: []
  central-i:
  - v5
can_code: 743
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 1000000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeGap

Sets the Central-i scope sampling interval.

## Overview

`ScopeGap` sets the sampling interval of the Central-i scope, controlling how frequently the signals in [ScopeParams](ScopeParams.md) are captured. A larger value samples less often, extending the time span the fixed buffer covers. It is a non-axis parameter saved to flash. The scope reads the interval live, so `ScopeGap` can be changed while the scope is running and the new rate takes effect immediately. This is the Central-i-scope counterpart of [LoggerGap](LoggerGap.md) and [RecGap](RecGap.md).

## How it works

The scope evaluates whether a sample is due on a fixed internal tick of roughly 1 ms (one tick per 16 servo cycles). `ScopeGap` is the number of those ticks between successive captured samples, so the sample period is approximately:

$$
\text{Sample period}\ [\text{ms}] \approx \text{ScopeGap}
$$

A value of `1` captures on every tick (about 1 kHz). Because the buffer holds a fixed number of samples, a larger `ScopeGap` trades time resolution for a longer total capture window before the buffer fills and the scope pauses (see [ScopeStatus](ScopeStatus.md)). Refer to the keyword attributes for the allowed range and default.

## Examples

```text
AScopeGap=1          ; capture on every tick (~1 ms, ~1 kHz)
AScopeGap=10         ; capture about every 10 ms (~100 Hz)
AScopeGap           ; query the current sampling interval
```

## See also

- [ScopeOn](ScopeOn.md) — start/stop the scope
- [ScopeParams](ScopeParams.md) — signals the scope captures
- [ScopeStatus](ScopeStatus.md) — scope run state and buffer fill
- [LoggerGap](LoggerGap.md) — equivalent interval for the continuous logger
