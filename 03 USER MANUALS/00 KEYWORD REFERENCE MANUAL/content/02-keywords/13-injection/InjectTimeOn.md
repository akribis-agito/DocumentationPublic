---
keyword: InjectTimeOn
summary: Pulse duration for pulse injection, in milliseconds.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 125
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 65536
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectTimeOn

Pulse duration for pulse injection, in milliseconds.

## Overview

`InjectTimeOn` defines the on-time (duration) of a pulse injection, in milliseconds. It applies only when [InjectType](InjectType.md) selects the pulse waveform (`InjectType = 5`), which is reserved for current-command injection (`InjectPoint = 0`). The pulse amplitude comes from [InjectCurrAmp](InjectCurrAmp.md).

## How it works

The pulse is a single, non-repeating rectangular pulse. When pulse injection starts, the output is held at the configured amplitude; the controller counts elapsed controller cycles, and once the elapsed time reaches `InjectTimeOn` the output drops to zero and remains there (the pulse does not repeat). The value is entered in milliseconds and the controller converts it internally to a whole number of controller cycles, so the realised duration is rounded to the nearest cycle. A value of 0 produces no pulse. The injected level while the pulse is high can be read back through [InjectedValue](InjectedValue.md).

## Examples

```text
AInjectTimeOn=10     ; 10 ms pulse
AInjectTimeOn       ; query the current pulse duration
```

## See also

- [InjectType](InjectType.md) — selects the pulse waveform (InjectType = 5)
- [InjectCurrAmp](InjectCurrAmp.md) — amplitude of the current pulse
- [InjectPoint](InjectPoint.md) — selects the injection location (must be 0 for the pulse)
- [InjectedValue](InjectedValue.md) — reads back the pulse level while it is high
