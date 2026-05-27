---
keyword: MaxMotorTemp
summary: Maximum allowable motor temperature (PT100 sensor); exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 399
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
  - 10
  - 150
  default: 80
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxMotorTemp

Maximum allowable motor temperature (PT100 sensor); exceeding it faults.

## Overview

`MaxMotorTemp` is the maximum allowable motor temperature, in °C. If the measured [MotorTemp](MotorTemp.md) exceeds this limit, the controller disables the axis with a fault to protect the motor. It is axis-scoped, saved to flash, and may be changed at any time (range 10…150 °C, default 80 °C).

> **Condition:** the limit applies only when a temperature sensor is selected — i.e. [MotorTempUsed](MotorTempUsed.md) ≠ 0. With `MotorTempUsed = 0` (no sensor) both the fault check and the warning bands are skipped.

## How it works

### Over-temperature fault

Once per millisecond, while the motor is on and not in simulation, the firmware checks:

```text
if (MotorTempUsed != 0  &&  MotorTemp > MaxMotorTemp)
    → disable axis, ConFlt = 1040 (CON_FLT_HIGH_MOTOR_TEMP), append to ErrLog
```

(Firmware: `AG300_CTL01ControlInterrupt.c:10303`–`:10306` and `:10329`–`:10332`; the same check also runs in the comm/funcs path at `AG300_CTL01Funcs.c:19815`–`:19817`.) The action is a latching fault via `MotorOffAndAddToErrorLog(...)`: the axis is disabled, [ConFlt](../../07-status-and-faults/ConFlt.md) is set to `1040`, a snapshot is captured, and the fault is logged. The fault clears when the axis is re-enabled.

### Graduated warning bands (StatReg)

Before tripping, the firmware sets the motor-temperature **warning** field in [StatReg](../../07-status-and-faults/StatReg.md) (bits 15–16) at three sub-thresholds derived from `MaxMotorTemp`. Whenever you write `MaxMotorTemp` the firmware recomputes the band edges (`SpMaxMotorTemp`, `SpecialFuncs.c:5173`):

| `MotorTemp` band | StatReg warning level | PCSuite LED |
|------------------|----------------------|-------------|
| < 0.88 × MaxMotorTemp | 0 — none | off |
| 0.88…0.92 × MaxMotorTemp | 1 — low | yellow |
| 0.92…0.96 × MaxMotorTemp | 2 — medium | orange |
| > 0.96 × MaxMotorTemp | 3 — high | red |
| > MaxMotorTemp | — fault (`ConFlt = 1040`) | — |

(Bands evaluated at `AG300_CTL01ControlInterrupt.c:9585`–`:9603`.) So the warning ramps up well before the fault, giving early indication on the status panel.

## Examples

```text
AMaxMotorTemp[1]=80    ; trip axis A if motor temperature exceeds 80 °C
AMaxMotorTemp          ; read the current limit
```

## See also

- [MotorTemp](MotorTemp.md) — measured motor temperature
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection (gates this limit)
- [MotorTempOffset](MotorTempOffset.md) — reading offset (cable compensation)
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 15–16 carry the 4-level warning
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1040 raised on over-temperature
