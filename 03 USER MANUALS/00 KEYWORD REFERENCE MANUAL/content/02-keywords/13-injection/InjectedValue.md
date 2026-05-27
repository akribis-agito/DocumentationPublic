---
keyword: InjectedValue
summary: Read-only readout of the present injection value; units follow the injection point.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 118
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectedValue

Read-only readout of the present injection value; units follow the injection point.

## Overview

`InjectedValue` is a read-only readout of the current injection value being applied to the loop. Its unit depends on the active injection location selected by [InjectPoint](InjectPoint.md) (for example, mA for current-command injection). It is useful for monitoring or logging the injected waveform during system identification or step-response testing.

## How it works

The controller recomputes the injected value every controller cycle from the active [InjectType](InjectType.md) waveform and reports the integer result here, so reading `InjectedValue` repeatedly traces the waveform itself (a sine sweeps between ±amplitude, a square alternates between +amplitude and −amplitude, PRBS toggles between the two, a pulse holds amplitude then returns to 0). The amplitude that bounds it comes from the keyword tied to the selected `InjectPoint` (current, velocity, position or force). For current-command injection the reported value is the waveform before the [InjectCurrDC](InjectCurrDC.md) offset is added. When [InjectType](InjectType.md) is 0 (no injection) the value is 0.

This is the same per-cycle injection value that is substituted into or summed onto the targeted command; for the velocity loop this is the term that modifies [VelRef](../10-motion/01-kinematics-status/VelRef.md).

## Examples

```text
AInjectedValue      ; read the present injection value
```

## See also

- [InjectPoint](InjectPoint.md) — determines the unit of this value
- [InjectType](InjectType.md) — selects the waveform being injected
- [InjectCurrDC](InjectCurrDC.md) — DC offset added after this value for current injection
- [VelRef](../10-motion/01-kinematics-status/VelRef.md) — velocity-loop reference that this value modifies for velocity injection
