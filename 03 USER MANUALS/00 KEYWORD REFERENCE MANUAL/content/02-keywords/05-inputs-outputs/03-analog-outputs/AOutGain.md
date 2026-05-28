---
keyword: AOutGain
summary: Floating-point scale applied to the monitored parameter on an analog output (v5).
availability:
  standalone: []
  central-i:
  - v5
can_code: 221
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutGain

Floating-point scale applied to the monitored parameter on an analog output (v5).

## Overview

`AOutGain` scales the monitored parameter (see [AOutMode](AOutMode.md)) by a floating-point factor, to fit it into the output's dynamic range. The array index is the analog-output number (1-based: `AOutGain[1]` applies to analog output 1). This is the scaling stage of the [analog-output signal path](00-overview.md) and applies **only in monitoring mode** — in direct command mode the output follows [AOutPort](AOutPort.md) and `AOutGain` is not used.

`AOutGain` is the **v5 (Central-i)** replacement for the v4 power-of-two scaler [AOutShifts](AOutShifts.md): instead of restricting the scale to a power of two, v5 allows any real multiplier. The default is `1` (unity).

## How it works

Each control cycle, for an output in monitoring mode, the monitored parameter is multiplied by `AOutGain`, then the offset is added and the result converted to a DAC code:

$$
\text{DAC code} = \big(\text{parameter} \times \text{AOutGain} + \text{AOutOffset}\big) \times \text{(mV-to-DAC factor)}
$$

Because the emulated parameter is treated as millivolts, choose `AOutGain` so the parameter's working range maps usefully onto the ±11905 mV output span. A negative gain inverts the output.

## Changes between versions

`AOutGain` exists only on **Central-i v5**. On v4 (standalone and Central-i) the equivalent scaling is the power-of-two [AOutShifts](AOutShifts.md); v5 replaces that integer shift with this floating-point gain.

## Examples

```text
AAOutGain[1]=4       ; scale the monitored value by 4
AAOutGain[1]=0.5     ; scale the monitored value by one half
AAOutGain[1]          ; read back the gain
```

## See also

- [AOutMode](AOutMode.md) — selects the monitored parameter (gain applies only in monitoring mode)
- [AOutShifts](AOutShifts.md) — the v4 power-of-two scaling this replaces in v5
- [AOutOffset](AOutOffset.md) — output offset (added after this scaling, before the DAC conversion)
- [AOutPort](AOutPort.md) — direct-mode value (not affected by this gain)
- [analog-output overview](00-overview.md) — full signal path
