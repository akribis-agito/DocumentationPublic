---
keyword: LoggerGap
summary: Sets the continuous logger sampling interval in servo cycles.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`LoggerGap` sets the sampling interval of the continuous data logger in servo cycles, controlling how frequently the parameters in [LoggerParams](LoggerParams.md) are captured relative to the control loop rate. A larger value samples less often, extending the time span captured in the buffer. It is a non-axis parameter saved to flash and can be changed at any time. This is the continuous-logger counterpart of [RecGap](RecGap.md) for the recording scope.

## Examples

```text
LoggerGap=10        ; sample every 10 servo cycles
LoggerGap?          ; query the current sampling interval
```

## See also

- [LoggerOn](LoggerOn.md) — start/stop the logger
- [LoggerParams](LoggerParams.md) — parameters the logger records
- [LoggerFullMod](LoggerFullMod.md) — buffer-full behavior
- [RecGap](RecGap.md) — equivalent down-sampling for the recording scope
