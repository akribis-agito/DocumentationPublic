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

## Examples

```text
AInjectedValue      ; read the present injection value
```

## See also

- [InjectPoint](InjectPoint.md) — determines the unit of this value
- [InjectType](InjectType.md) — selects the waveform being injected
