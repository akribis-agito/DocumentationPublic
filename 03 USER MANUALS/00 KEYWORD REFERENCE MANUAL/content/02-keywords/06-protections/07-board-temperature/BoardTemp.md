---
keyword: BoardTemp
summary: Read-only controller-board temperature (°C).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 397
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
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BoardTemp

Read-only controller-board temperature (°C).

## Overview

`BoardTemp` reports the temperature of the controller board, measured by an on-board digital sensor, in °C. It is read-only, axis-scoped, not saved to flash, and available at all times. For the power-stage (IPM) temperature, see [PwrTemp](PwrTemp.md).

## How it works

### Measurement

On controller-type products the board sensor is read over I²C: the I²C module is pre-configured at startup to read the temperature device, and the result is copied to `BoardTemp` each background pass. A reading of 255 means "no sensor connected" (e.g. AGC301, where the sensor lives on the amplifier board) and is reported as 0 °C.

### Over-temperature protection (fixed limit)

Unlike [PwrTemp](PwrTemp.md)/[MaxPwrTemp](MaxPwrTemp.md), the board-temperature fault uses a **fixed limit of 75 °C**, not a user keyword. While the motor is on and not in simulation:

```text
if (BoardTemp > 75 °C)   →   disable axis, raise the board over-temperature fault
```

[ConFlt](../../07-status-and-faults/ConFlt.md) then shows fault code 1060 (board temperature too high).

### Warning bands (shared with PwrTemp)

`BoardTemp` contributes to the same **power/board-temperature** warning field in [StatReg](../../07-status-and-faults/StatReg.md) (bits 11–12) as `PwrTemp` — the warning level is the higher of the two. The fixed board-temperature band edges are:

| `BoardTemp` band | StatReg level | PCSuite LED |
|------------------|---------------|-------------|
| < 66 °C | 0 — none | off |
| 66…69 °C | 1 — low | yellow |
| 69…72 °C | 2 — medium | orange |
| > 72 °C | 3 — high | red |
| > 75 °C | fault (`ConFlt` = 1060) | — |

On newer Central-i remote units the board-temperature band edges come from a per-axis limit instead of these fixed values.

## Examples

```text
ABoardTemp          ; controller board temperature (°C)
```

## See also

- [PwrTemp](PwrTemp.md) — power-stage (IPM) temperature
- [MaxPwrTemp](MaxPwrTemp.md) — power-stage over-temperature limit (user-set)
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 11–12 carry the combined power/board-temperature warning
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1060 (board temperature too high)
