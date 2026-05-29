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

The control loop runs at ~16 kHz, and the over-temperature check is evaluated once per ~1 ms (the warning bands are updated on a separate ~1 ms sub-phase of the same cycle). Once per millisecond, while the motor is on and not in simulation, the controller checks:

```text
if (MotorTempUsed != 0  &&  MotorTemp > MaxMotorTemp)
    → disable axis, raise the motor over-temperature fault, append to ErrLog
```

The action is a latching fault: the axis is disabled, [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1040 (motor temperature too high), a snapshot is captured, and the fault is logged. The fault clears when the axis is re-enabled.

### Graduated warning bands (StatReg)

Before tripping, the controller sets the motor-temperature **warning** field in [StatReg](../../07-status-and-faults/StatReg.md) (bits 15–16) at three sub-thresholds derived from `MaxMotorTemp`. Whenever you write `MaxMotorTemp` the band edges are recomputed:

| `MotorTemp` band | StatReg warning level | PCSuite LED |
|------------------|----------------------|-------------|
| < 0.88 × MaxMotorTemp | 0 — none | off |
| 0.88…0.92 × MaxMotorTemp | 1 — low | yellow |
| 0.92…0.96 × MaxMotorTemp | 2 — medium | orange |
| > 0.96 × MaxMotorTemp | 3 — high | red |
| > MaxMotorTemp | — fault (`ConFlt = 1040`) | — |

So the warning ramps up well before the fault, giving early indication on the status panel.

### Edge cases

- **Motor off:** the fault check is gated on motor-on (the doc statement above), so over-temperature does **not** trip with the motor off — the sensor would still be live but a thermal soak only fails the next time you re-enable. The warning bands (StatReg bits 15–16) continue to update even with the motor off, so you can watch the temperature climb on the status panel; only the trip itself is suppressed until the next re-enable.
- **Sensor not selected:** with [MotorTempUsed](MotorTempUsed.md) = `0` both the fault check and the warning bands are skipped entirely, and the warning field is cleared.
- **Simulation mode:** the trip is skipped in simulation (no real sensor).
- **Range overflow:** writes outside `10…150` are **rejected** (out-of-range error) and the stored value is left unchanged — the limit is not clamped. Whenever a valid write of `MaxMotorTemp` is accepted, the warning band edges are recomputed.
- **Clearing the fault:** ConFlt code 1040 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **Which axis tripped:** the matching [ErrLog](../../07-status-and-faults/ErrLog.md) entry is tagged with the axis that tripped — the source tag in the upper 8 bits carries the 1-based axis number (axis A = 1) alongside fault code 1040 in the lower bits — so on a multi-axis unit you can tell which axis faulted.
- **HWProtectBits / ProtectMask:** the motor over-temperature trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md).

## Examples

```text
AMaxMotorTemp[1]=80    ; trip axis A if motor temperature exceeds 80 °C
AMaxMotorTemp          ; read the current limit
```

### Walk-through: verify the warning bands ramp before the trip

Confirm the sensor is enabled, set the trip ceiling, then watch the warning bands climb on a thermal soak (long duty cycle):

```text
AMotorTempUsed[1]=1    ; enable the PT100/RTD sensor
AMaxMotorTemp[1]=80    ; over-temperature trip at 80 deg C
AMotorTemp             ; sample the live temperature
AStatReg               ; bits 15-16 carry the 4-level warning
```

During a sustained high-duty move:

| Reading | Expected StatReg bits 15-16 | PCSuite LED |
|---|---|---|
| `MotorTemp < 70` | 0 (none) | off |
| `70 <= MotorTemp < 74` | 1 (low) | yellow |
| `74 <= MotorTemp < 77` | 2 (medium) | orange |
| `77 <= MotorTemp <= 80` | 3 (high) | red |
| `MotorTemp > 80` | trip: `AConFlt = 1040`, axis disabled | — |

If `AMotorTemp` reads the default `25` even under load, [MotorTempUsed](MotorTempUsed.md) is probably still `0` (sensor disabled) — the warning and trip checks are then both skipped.

## See also

- [MotorTemp](MotorTemp.md) — measured motor temperature
- [MotorTempUsed](MotorTempUsed.md) — sensor-type selection (gates this limit)
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 15–16 carry the 4-level warning
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1040 raised on over-temperature
