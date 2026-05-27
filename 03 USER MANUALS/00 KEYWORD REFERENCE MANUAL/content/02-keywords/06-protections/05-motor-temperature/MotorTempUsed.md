---
keyword: MotorTempUsed
summary: Selects the motor temperature-sensor type.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 398
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MotorTempUsed

Selects the motor temperature-sensor type.

## Overview

`MotorTempUsed` selects whether a motor temperature sensor is in use. It acts as the master gate for all motor-temperature logic: when it is `0` the firmware skips reading/comparing the temperature entirely; when it is non-zero the [MaxMotorTemp](MaxMotorTemp.md) fault and the [StatReg](../../07-status-and-faults/StatReg.md) warning bands become active. It is axis-scoped and saved to flash.

| Value | Sensor |
|-------|--------|
| 0 | None — motor-temperature reading and protection disabled |
| 1 | PT100 / RTD sensor on the temperature-sensor input |

> **Range note:** in this firmware the keyword range is `0…1` (PT100/RTD only); there is no separate "thermostat" selection. A thermostat is instead wired as a digital input and handled by the I/O / fault logic, not by `MotorTempUsed`.

## How it works

The motor-temperature checks are all guarded by `if (glMotorTempUsed[axis] != 0)`:

- **Fault** — the over-temperature trip against [MaxMotorTemp](MaxMotorTemp.md) runs only when `MotorTempUsed ≠ 0` (`AG300_CTL01ControlInterrupt.c:10303`, `:10329`).
- **Warning** — the [StatReg](../../07-status-and-faults/StatReg.md) bits-15–16 warning bands are evaluated only when `MotorTempUsed ≠ 0`; otherwise the warning field is cleared (`AG300_CTL01ControlInterrupt.c:9584`–`:9585`).

The comparison uses `≠ 0` rather than `== 1`, so the gate is purely on/off.

## Examples

```text
AMotorTempUsed[1]=1    ; enable the PT100/RTD sensor on axis A
AMotorTempUsed=0       ; disable motor-temperature reading and protection
```

## See also

- [MotorTemp](MotorTemp.md) — measured temperature
- [MaxMotorTemp](MaxMotorTemp.md) — over-temperature fault limit
- [MotorTempOffset](MotorTempOffset.md) — reading offset
- [StatReg](../../07-status-and-faults/StatReg.md) — motor-temperature warning bits (15–16)
