---
keyword: LoggerGap
summary: Sets the continuous logger sampling interval in servo cycles.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 531
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
---
# LoggerGap

Sets the continuous logger sampling interval in servo cycles.

## Overview

`LoggerGap` sets the sampling interval of the continuous data logger, controlling how frequently the parameters in [LoggerParams](LoggerParams.md) are captured. A larger value samples less often, extending the time span the buffer covers. It is a non-axis parameter saved to flash. Unlike the recording scope, the logger reads the interval live, so `LoggerGap` can be changed on the fly while logging and the new rate takes effect immediately. This is the continuous-logger counterpart of [RecGap](RecGap.md) for the recording scope.

## How it works

The logger evaluates whether a sample is due on a fixed internal tick of roughly 1 ms (one tick per 16 servo cycles). `LoggerGap` is the number of those ticks between successive logged samples, so the sample period is approximately:

$$
\text{Sample period}\ [\text{ms}] \approx \text{LoggerGap}
$$

The minimum value of `1` logs on every tick (about 1 kHz). The default of `10` corresponds to roughly one sample every 10 ms (about 100 Hz). Because the buffer holds a fixed number of samples, a larger `LoggerGap` trades time resolution for a longer total capture window before the buffer-full behavior set by [LoggerFullMod](LoggerFullMod.md) takes over.

## Examples

```text
ALoggerGap=10        ; sample about every 10 ms (default, ~100 Hz)
ALoggerGap=1         ; sample on every tick (~1 ms, ~1 kHz)
ALoggerGap          ; query the current sampling interval
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerParams](LoggerParams.md) — parameters the logger records
- [LoggerFullMod](LoggerFullMod.md) — buffer-full behavior
- [RecGap](RecGap.md) — equivalent down-sampling for the recording scope
