---
keyword: AOutPort
summary: Commanded analog-output value (mV) in direct command mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 219
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
  - -11905
  - 11905
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# AOutPort

Commanded analog-output value (mV) in direct command mode.

## Overview

`AOutPort` sets the value, in millivolts, driven on an analog output when that output is in **direct command mode**. The array index is the analog-output number (1-based: `AOutPort[1]` is analog output 1, `AOutPort[2]` is analog output 2). The usable index range matches the number of physical outputs (1 to 2 on 2-output products, 1 to 4 on 4-output products). `AOutPort[Index]` only takes effect when `AOutMode[Index] == 0`; in monitoring mode the output follows the emulated parameter instead. See the [analog-output overview](00-overview.md) for both modes.

The range ±11905 mV comes directly from the DAC: the mV-to-DAC scale factor is −2.752457 LSB/mV, so the full-scale −32768 LSB corresponds to 11905 mV.

## How it works

Each analog-output index maps to one physical DAC channel: index 1 → DAC channel A, index 2 → DAC channel B, index 3 → C, index 4 → D.

In direct command mode the DAC code is computed each cycle as

$$
\text{DAC code} = (\text{AOutPort} + \text{AOutOffset}) \cdot \text{(mV-to-DAC factor)}
$$

then clamped to the DAC range before being written to the channel. Note that [AOutOffset](AOutOffset.md) is added in the same millivolt units **before** the LSB conversion. The per-output decision between direct and monitoring mode is set when [AOutMode](AOutMode.md) is written: direct mode is forced when `AOutMode = 0`, or when the amplifier is an analog-current-command / built-in-linear type (the DAC is then driving the amplifier's current command).

`AOutPort` is written to flash, is array-typed, and may be changed in motion and with the motor on.

## Examples

```text
AAOutMode[1]=0       ; direct command mode
AAOutPort[1]=5000    ; drive analog output 1 to 5000 mV
AAOutPort[1]          ; read back the commanded value
```

### Edge cases

- **Index 0** — invalid; valid indices are `AOutPort[1]`–`AOutPort[4]`. `AOutPort[0]` does not exist.
- **Wrong mode** — `AOutPort` is only read by the DAC when [AOutMode](AOutMode.md)`[i] = 0`. Writing it while `AOutMode[i] ≠ 0` stores the value but the output continues to follow the monitored parameter; the stored value takes effect the moment `AOutMode[i]` is set back to `0`.
- **Out of range** — writes outside ±11905 mV are rejected by the parameter table; the DAC code is also clamped each cycle.
- **2-output products** — only `AOutPort[1]` and `AOutPort[2]` drive physical channels; `AOutPort[3]` / `AOutPort[4]` accept writes but do not reach any DAC.
- **Amplifier override** — when the amplifier is an analog-current-command or built-in-linear type, the DAC is owned by the amplifier current command; `AOutPort` writes are stored but do not reach the pin.
- **Motor on/off** — independent of `MotorOn`; the DAC follows `AOutPort` whether the servo is enabled or not.
- **Save** — flash-saveable; the last commanded value is restored at boot.
- **Platform** — central-i v5 stores the value as `float32`; behaviour and units are unchanged.

## See also

- [AOutMode](AOutMode.md) — selects direct vs monitoring mode (this value is honored only when `AOutMode = 0`)
- [AOutOffset](AOutOffset.md) — output calibration offset, added before the DAC conversion
- [analog-output overview](00-overview.md) — full signal path
