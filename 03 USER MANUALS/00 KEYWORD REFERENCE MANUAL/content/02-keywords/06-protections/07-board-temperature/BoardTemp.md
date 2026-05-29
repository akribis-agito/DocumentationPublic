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
  scope: non-axis
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# BoardTemp

Read-only controller-board temperature (°C).

## Overview

`BoardTemp` reports the temperature of the controller board, measured by an on-board digital sensor, in °C. It is read-only, not saved to flash, and available at all times — non-axis on standalone (one value across axes), per-axis on Central-i. For the power-stage (IPM) temperature, see [PwrTemp](PwrTemp.md).

## How it works

### Measurement

On controller-type products the board sensor is read over I²C: the I²C module is pre-configured at startup to read the temperature device, and the result is copied to `BoardTemp` each background pass. A reading of 255 means "no sensor connected" (e.g. AGC301, where the sensor lives on the amplifier board) and is reported as 0 °C. On the Central-i master the board-temperature read is not currently active, so `BoardTemp` stays at its default there.

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

On newer Central-i remote units the board-temperature WARNING band edges are derived (at 88 / 92 / 96 %) from a per-axis limit reported by the remote unit, instead of the fixed 66 / 69 / 72 °C values; the board over-temperature FAULT limit stays the fixed 75 °C on both standalone and Central-i.

### Edge cases

- **Motor off:** like [MaxPwrTemp](MaxPwrTemp.md), the over-temperature trip is gated on motor-on, so a board overheat with the axis disabled does not trip — the fault only fires the next time you re-enable.
- **Simulation mode:** the trip is skipped in simulation.
- **No sensor (AGC301, etc.):** I²C returns 255 → `BoardTemp` is reported as 0 °C and the fixed-75 °C trip never fires.
- **Fixed limit:** the board limit is **not** configurable on standalone v4 — it is the fixed 75 °C constant. Only [MaxPwrTemp](MaxPwrTemp.md) is user-settable.
- **Shared warning field:** [StatReg](../../07-status-and-faults/StatReg.md) bits 11–12 carry the higher of [PwrTemp](PwrTemp.md) and `BoardTemp` warning levels.
- **Clearing the fault:** ConFlt code 1060 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **Which axis tripped:** the matching [ErrLog](../../07-status-and-faults/ErrLog.md) entry is tagged with the axis that tripped — the source tag in the upper 8 bits carries the 1-based axis number (axis A = 1) alongside fault code 1060 in the lower bits — so on a multi-axis unit you can tell which axis faulted.
- **HWProtectBits / ProtectMask:** the board over-temperature trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md).

## Examples

```text
ABoardTemp          ; controller board temperature (°C)
```

## See also

- [PwrTemp](PwrTemp.md) — power-stage (IPM) temperature
- [MaxPwrTemp](MaxPwrTemp.md) — power-stage over-temperature limit (user-set)
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 11–12 carry the combined power/board-temperature warning
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1060 (board temperature too high)
