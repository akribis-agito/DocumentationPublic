---
keyword: MotorTemp
summary: Read-only measured motor temperature (flagged not implemented in current firmware).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 400
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
  - -40
  - 150
  default: 25
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# MotorTemp

Read-only measured motor temperature in °C (flagged not implemented in the keyword table).

## Overview

`MotorTemp` reports the motor temperature in °C, derived from an RTD/PT100 sensor wired to the temperature-sensor input. It is read-only, axis-scoped, and not saved to flash. The protection limit is [MaxMotorTemp](MaxMotorTemp.md); whether the value is read at all is gated by [MotorTempUsed](MotorTempUsed.md).

> **Keyword flagged `NOT_IMPLEMENTED`:** in the firmware parameter table the `MotorTemp` keyword entry carries the `NOT_IMPLEMENTED` attribute, so it is not exposed as a fully released keyword. The underlying `glMotorTemp` value *is* computed and used internally (for over-temperature protection and warnings), but confirm sensor/hardware support with Agito before relying on the reported number. Its default reported value is 25 °C.

## How it works

### Measurement pipeline (sensor → °C)

On products that sample an RTD, the firmware reads the raw ADC word from the FPGA each control cycle and converts it directly to °C with a fixed linear formula (no user scaling, `scaling = 1.0`):

$$
MotorTemp = 133 - \left\lfloor \frac{ADC \times 393}{2^{n}} \right\rfloor
$$

where the shift `n` and source register depend on the product:

| Product / variant | Source register | Shift `n` | Axes read |
|-------------------|-----------------|-----------|-----------|
| AG100 (single-channel PT100) | `FPGA_AG100_PT100` | 10 | A only |
| 3-channel RTD product | `FPGA_RTD_A_REG` / `_B_REG` / `_C_REG` | 16 | A, B, C |

(Firmware: `AG300_CTL01ControlInterrupt.c:12275`, `:12279`–`:12281`, sample slot `SAMPLE_6`.) The `133 − …` form means a larger ADC reading (higher sensor resistance) maps to a lower temperature; the reported value falls in the keyword's −40…150 °C range.

### How the value is used

Once per millisecond the firmware compares `glMotorTemp` against [MaxMotorTemp](MaxMotorTemp.md) and its derived warning thresholds — but **only when [MotorTempUsed](MotorTempUsed.md) ≠ 0**. If the sensor type is "none" (`MotorTempUsed = 0`) the motor-temperature checks are skipped entirely. See [MaxMotorTemp](MaxMotorTemp.md) for the fault/warning thresholds and [StatReg](../../07-status-and-faults/StatReg.md) bits 15–16 for the 4-level warning.

## Examples

```text
AMotorTemp          ; read axis A's motor temperature (°C)
```

## See also

- [MaxMotorTemp](MaxMotorTemp.md) — over-temperature fault limit (and warning thresholds)
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection (gates the reading and protection)
- [MotorTempOffset](MotorTempOffset.md) — reading offset (cable-resistance compensation)
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 15–16 report the motor-temperature warning level
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1040 (motor temperature too high)
