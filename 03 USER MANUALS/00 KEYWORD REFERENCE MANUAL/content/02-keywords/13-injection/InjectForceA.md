---
keyword: InjectForceA
summary: Amplitude of force-command injection, in internal force units.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 590
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectForceA

Amplitude of force-command injection, in internal force units.

## Overview

`InjectForceA` is the amplitude of the injected waveform when injecting at the force command, expressed in the internal force unit. It applies only when [InjectPoint](InjectPoint.md) selects the force command (`InjectPoint = 3`). The waveform shape is chosen by [InjectType](InjectType.md).

## How it works

This value sets the peak magnitude the waveform reaches at the force command: a sine swings between +`InjectForceA` and −`InjectForceA`, a square and PRBS toggle between those two levels. At the force command the supported waveforms are **sine, square, PRBS and chirp** (the pulse is current-command only). In **direct** mode the waveform is added to the force reference captured when injection began, so the command follows that fixed baseline plus the waveform; in **additive** mode it is summed onto the live force command. The present level can be read back with [InjectedValue](InjectedValue.md).

## Examples

```text
AInjectForceA=10000      ; force injection amplitude (internal force units)
AInjectForceA           ; query the current force injection amplitude
```

## See also

- [InjectPoint](InjectPoint.md) — must be 3 for force-command injection
- [InjectType](InjectType.md) — selects the waveform shape and direct/additive mode
- [InjectedValue](InjectedValue.md) — reads back the present injection value
