---
keyword: MaxPwrTemp
summary: Maximum allowed power-stage temperature (°C); exceeding it triggers protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 90
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 20
  - 80
  default: 65
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPwrTemp

Maximum allowed power-stage temperature (°C); exceeding it triggers protection.

## Overview

`MaxPwrTemp` is the maximum allowed temperature, in °C, for the power stage (IPM). When [PwrTemp](PwrTemp.md) approaches or exceeds this limit the over-temperature protection acts to prevent damage. It is axis-scoped, saved to flash, and may be changed at any time (range 20…80 °C, default 65 °C).

## How it works

### Over-temperature fault

Once per millisecond, while the motor is on and not in simulation:

```text
if (PwrTemp > MaxPwrTemp)   →   disable axis, raise the power over-temperature fault, append to ErrLog
```

The axis is disabled, [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1018 (IPM temperature too high), and the event is logged. The fault clears on re-enable.

### Graduated warning bands (StatReg)

Whenever you write `MaxPwrTemp`, three derived band edges are recomputed at 88 / 92 / 96 % of the limit. These feed the combined power/board-temperature warning field in [StatReg](../../07-status-and-faults/StatReg.md) (bits 11–12) — the reported level is the higher of the `PwrTemp` and [BoardTemp](BoardTemp.md) contributions:

| `PwrTemp` band | StatReg warning level | PCSuite LED |
|----------------|----------------------|-------------|
| < 0.88 × MaxPwrTemp | 0 — none | off |
| 0.88…0.92 × MaxPwrTemp | 1 — low | yellow |
| 0.92…0.96 × MaxPwrTemp | 2 — medium | orange |
| > 0.96 × MaxPwrTemp | 3 — high | red |
| > MaxPwrTemp | fault (`ConFlt = 1018`) | — |


> **Note:** the controller-board over-temperature limit ([BoardTemp](BoardTemp.md)) is a *fixed* 75 °C constant — only the power-stage limit is user-settable through this keyword.

### Edge cases

- **Motor off:** the fault check is gated on motor-on (the doc statement above), so over-temperature does **not** trip with the motor off — a thermal soak only fails the next time you re-enable.
- **Simulation mode:** the trip is skipped in simulation.
- **Mode dependency:** the trip runs regardless of operation mode whenever the motor is on.
- **Range overflow:** writes outside `20…80` are clamped; whenever you write `MaxPwrTemp` the warning band edges are recomputed.
- **Clearing the fault:** ConFlt code 1018 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **Shared warning field:** [StatReg](../../07-status-and-faults/StatReg.md) bits 11–12 report the higher of the [PwrTemp](PwrTemp.md) and [BoardTemp](BoardTemp.md) warning levels.
- **HWProtectBits / ProtectMask:** the IPM over-temperature trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md). The separate hardware [HWProtectBits](../01-general-protection/HWProtectBits.md) IPM-fault bit (ConFlt code 1027) is gated by [ProtectMask](../01-general-protection/ProtectMask.md).

## Examples

```text
AMaxPwrTemp[1]=65    ; trip axis A if the IPM exceeds 65 °C
AMaxPwrTemp          ; read the current limit
```

## See also

- [PwrTemp](PwrTemp.md) — measured power-stage temperature
- [BoardTemp](BoardTemp.md) — controller-board temperature (fixed 75 °C limit)
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 11–12 carry the warning level
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1018 (IPM temperature too high)
