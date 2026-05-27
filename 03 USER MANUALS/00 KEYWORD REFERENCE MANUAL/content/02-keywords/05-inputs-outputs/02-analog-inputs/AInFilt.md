---
keyword: AInFilt
summary: Digital low-pass filter coefficient for each analog input.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 218
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 50000
  default: 10000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# AInFilt

Digital low-pass filter coefficient for each analog input.

## Overview

`AInFilt` sets the cutoff of a first-order digital low-pass filter applied to an analog input — the first digital stage of the [analog-input signal path](00-overview.md), run on the ADC reading before offset, deadband and gain. The array index is the analog-input number (e.g. `AInFilt[2]` is analog input 2). The value is the cutoff frequency in hundredths of a hertz, so its range 1–50000 corresponds to roughly **0.01 Hz to 500 Hz**, and the default 10000 is about a **100 Hz** cutoff.

## How it works

The filter is a single-pole exponential low-pass. The filtered output of a controller cycle ($y_{i}$) depends on the current input ($u_{i}$) and the previous output ($y_{i-1}$):

$$
y_{i} = a\,u_{i} + (1 - a)\,y_{i - 1}
$$

The coefficient $a$ is **not** `AInFilt/65536`. The coefficient is recomputed whenever `AInFilt` is written:

$$
a = 1 - e^{-2\pi\,T_s\,R\,(AInFilt/100)}
$$

where $T_s$ is the sample time and $R$ is the analog-input update rate (normally 1 — the filter runs every sample). The `AInFilt/100` term is the effective cutoff frequency in hertz: $a = 1 - e^{-2\pi f_c T_s}$ with $f_c = AInFilt/100$. The two coefficients ($a$ and $1-a$) are cached and reused each cycle, so the recurrence above costs only two multiplies.

A **larger** `AInFilt` means a **higher** cutoff and less filtering; a smaller value gives heavier smoothing. The lowest setting `AInFilt = 1` is ≈0.01 Hz (very heavy smoothing).

## Examples

```text
AAInFilt[1]=10000    ; ~100 Hz cutoff on analog input 1 (default)
AAInFilt[1]=50000    ; ~500 Hz cutoff (lightest filtering)
AAInFilt[1]=100      ; ~1 Hz cutoff (heavy smoothing)
```

## See also

- [AInPort](AInPort.md) — resulting readings
- [AInOffset](AInOffset.md), [AInGain](AInGain.md) — later stages of the chain
