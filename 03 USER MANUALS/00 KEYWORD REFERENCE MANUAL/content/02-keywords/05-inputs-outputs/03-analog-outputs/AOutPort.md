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

`AOutPort` sets the value, in millivolts, driven on an analog output when that output is in **direct command mode**. The array index is the analog-output number (1-based: `AOutPort[1]` is analog output 1, `AOutPort[2]` is analog output 2). Index 0 is unused — the array is sized one larger so the indices line up with the channel number (`AOUTPORT_SIZE` is 3 on 2-output products and 5 on 4-output products). `AOutPort[Index]` only takes effect when `AOutMode[Index] == 0`; in monitoring mode the output follows the emulated parameter instead. See the [analog-output overview](00-overview.md) for both modes.

The range ±11905 mV comes directly from the DAC: the firmware scales by `AOUT_VALUE_TO_MV = -2.752457` LSB/mV, so the full-scale −32768 LSB corresponds to 11905 mV.

## How it works

Each analog-output index maps to one physical DAC channel: index 1 → DAC channel A, index 2 → DAC channel B, index 3 → C, index 4 → D (`FPGA_ANALOG_OUT1_REG`…`FPGA_ANALOG_OUT4_REG`).

In direct command mode the control interrupt computes the DAC code each cycle as

$$
\text{DAC code} = (\text{AOutPort} + \text{AOutOffset}) \times \text{AOUT\_VALUE\_TO\_MV}
$$

then clamps it to the DAC range before writing it to the channel register (`AG300_CTL01ControlInterrupt.c:7027`–`7048`). Note that [AOutOffset](AOutOffset.md) is added in the same millivolt units **before** the LSB conversion. The per-output decision between direct and monitoring mode is taken from a flag, `gsUseAOutPort[]`, set when [AOutMode](AOutMode.md) is written (`SpAOutMode`, `SpecialFuncs.c:4877`–`4883`): direct mode is forced (flag = 1) when `AOutMode = 0`, or when the amplifier is an analog-current-command / built-in-linear type (the DAC is then driving the amplifier's current command).

`AOutPort` is written to flash, is array-typed, and may be changed in motion and with the motor on.

## Examples

```text
AAOutMode[1]=0       ; direct command mode
AAOutPort[1]=5000    ; drive analog output 1 to 5000 mV
AAOutPort[1]          ; read back the commanded value
```

## See also

- [AOutMode](AOutMode.md) — selects direct vs monitoring mode (this value is honored only when `AOutMode = 0`)
- [AOutOffset](AOutOffset.md) — output calibration offset, added before the DAC conversion
- [analog-output overview](00-overview.md) — full signal path
