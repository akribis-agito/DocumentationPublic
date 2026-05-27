---
keyword: MaxVBus
summary: Maximum allowed bus voltage; sustained excess disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 92
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
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVBus

Maximum allowed bus voltage; sustained excess disables the axis.

## Overview

`MaxVBus` is the maximum allowed bus voltage, in mV. If the actual bus voltage exceeds this limit for longer than [MaxVBusTime](MaxVBusTime.md), the axis is disabled and a fault is raised. For an instantaneous (no-delay) over-voltage ceiling, see [MaxVBusAbs](MaxVBusAbs.md).

## How it works

The bus voltage (`VBus`) is checked periodically (every 16th control cycle). On each check:

- If `VBus ≥ MaxVBus`, an over-voltage timer is accumulated (and [StatReg](../../07-status-and-faults/StatReg.md) bit 3 is set); otherwise the timer is reset to 0.
- When the timer reaches [MaxVBusTime](MaxVBusTime.md) while still over the limit, the axis is disabled and [ConFlt](../../07-status-and-faults/ConFlt.md) is set to `1008` (`CON_FLT_BUS_OVER_VOLTAGE`, "Bus Voltage too high").

This time-windowed trip tolerates brief over-voltage transients (e.g. regeneration spikes). For warning purposes the firmware also reports a multi-level VBus warning in `StatReg` (bits 7–8) as `VBus` approaches the limit, at 0.88 / 0.92 / 0.96 × `MaxVBus` (low / medium / high).

## Examples

```text
AMaxVBus=80000       ; 80 V maximum bus voltage (mV)
```

## See also

- [MinVBus](MinVBus.md) — minimum bus voltage
- [MaxVBusTime](MaxVBusTime.md) — out-of-range time before tripping
- [MaxVBusAbs](MaxVBusAbs.md) — instantaneous over-voltage trip
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1008 raised on trip
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 3 (over-MaxVBus) and bits 7–8 (VBus warning)
