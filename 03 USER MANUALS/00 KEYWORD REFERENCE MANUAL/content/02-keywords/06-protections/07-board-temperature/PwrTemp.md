---
keyword: PwrTemp
summary: Read-only power-stage temperature (°C).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 38
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
  default: 25
  scaling: 1.0
  implemented: final
overrides: {}
---
# PwrTemp

Read-only power-stage temperature (°C).

## Overview

`PwrTemp` reports the temperature, in °C, of the IPM (intelligent power module) inside the power stage. It is read-only, axis-scoped, and not saved to flash. The protection limit is [MaxPwrTemp](MaxPwrTemp.md); the power-stage cooling fan is also driven from this value.

## How it works

### Measurement pipeline (sensor → °C)

The IPM temperature is sensed as an analog voltage and converted to °C through a lookup against a calibration curve (the IPM thermistor is non-linear, so a fixed formula is not used). Two product paths exist:

| Product | Method | Firmware |
|---------|--------|----------|
| AG100-class amplifier | Each cycle the raw IPM voltage is scaled to mV (`glPwrTempMiliVolt`) and a **table search** walks `glThermistorVoltage[]` (indexed `−40…+119 °C`, one entry per degree) up or down from the previous estimate until the voltage bracket is found. | `AG300_CTL01ControlInterrupt.c:12199`; search at `AG300_CTL01Controller.c:2563`–`:2588` |
| Central-i (master) | For each axis, the synced ADC reading is **linearly interpolated** between the two nearest points of a per-axis 10-point calibration table (`CITemperatureTables[]`). | `AG300_CTL01Controller.c:2595`–`:2617` |

The reading is clamped to the valid range (the AG100 search stops at −39 / +119 °C, keeping one guard point at each end).

### Invalid-reading handling

If the STO2 or IPM-fault hardware-protection bits are set, the IPM voltage cannot be measured. The firmware then forces `PwrTemp = −40 °C` as a sentinel ("can't measure") and re-arms a fresh search for when the protection clears (`AG300_CTL01Controller.c:2551`–`:2554`). During the first few milliseconds after STO2 is plugged in, `PwrTemp` can read spuriously high due to IPM behaviour — the fan logic accounts for this.

### Fan control

`PwrTemp` drives the power-stage cooling fan with hysteresis:

| Product | Fan ON at | Fan OFF at | Firmware |
|---------|-----------|-----------|----------|
| AG100 | ≥ 50 °C (or during the first 5 ms after power-up) | ≤ 45 °C | `AG300_CTL01ControlInterrupt.c:12374`–`:12377` |
| Central-i | ≥ 50 °C | ≤ 45 °C | `AG300_CTL01ControlInterrupt.c:13409`/`:13423` |

### Protection

While the motor is on, `PwrTemp > MaxPwrTemp` disables the axis with [ConFlt](../../07-status-and-faults/ConFlt.md) = 1018 (IPM temperature too high). Graduated warnings appear in [StatReg](../../07-status-and-faults/StatReg.md) bits 11–12 — see [MaxPwrTemp](MaxPwrTemp.md).

## Examples

```text
APwrTemp            ; power-stage (IPM) temperature (°C)
```

## See also

- [MaxPwrTemp](MaxPwrTemp.md) — power-stage over-temperature limit and warning bands
- [BoardTemp](BoardTemp.md) — controller-board temperature
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 11–12 carry the power/board-temperature warning
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1018 (IPM temperature too high)
