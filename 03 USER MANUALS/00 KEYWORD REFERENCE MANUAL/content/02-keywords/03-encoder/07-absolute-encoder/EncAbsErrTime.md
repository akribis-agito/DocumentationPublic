---
keyword: EncAbsErrTime
summary: Number of control cycles an absolute-encoder error/warning/CRC condition may persist before the axis faults; -1 disables monitoring.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 423
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
  - -1
  - 10000
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    implemented: partial
---
# EncAbsErrTime

Number of control cycles an absolute-encoder error/warning/CRC condition may persist before the axis faults; -1 disables monitoring.

## Overview

`EncAbsErrTime` sets how long a recoverable absolute-encoder problem is tolerated before the controller treats it as a fault. While a problem is flagged in [EncStatReg](../01-general-settings/EncStatReg.md), the controller keeps the axis running on an extrapolated position for up to this many control cycles; if the condition is still present after that, and the motor is on, the axis is taken off and the matching code is recorded in [ConFlt](../../07-status-and-faults/ConFlt.md).

It is a per-axis parameter, saved to flash. The value is a count of control cycles (the loop runs at the controller's fixed sample rate, so the tolerated time is `EncAbsErrTime` × the control-cycle period). The valid range is `-1` to `10000`, and the default is `-1`. It applies to axes using a serial absolute encoder (see [EncType](../01-general-settings/EncType-AuxEncType.md)).

## How it works

Each control cycle the controller inspects the absolute-encoder status bits ([EncStatReg](../01-general-settings/EncStatReg.md)):

| EncAbsErrTime | Behaviour |
|---|---|
| -1 | Error / warning / CRC monitoring is **disabled**: those conditions are not counted and do not fault the axis. |
| 0 to 10000 | A persisting error / warning / CRC condition is counted; while counting, the position is extrapolated so motion continues, and the axis faults once the count exceeds this value. |

The two recoverable groups are counted separately:

- **CRC errors** (status bit 4). On expiry, [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1069`.
- **Error / warning** (status bit 1 / the warning condition). On expiry, [ConFlt](../../07-status-and-faults/ConFlt.md) reports fault `1068`.

A clean cycle (no abnormal bit) resets the counters, so only a *continuous* condition lasting longer than `EncAbsErrTime` produces a fault — short noise glitches are ridden through by extrapolation.

A genuine **disconnect** (status bit 0) is handled separately and is **not** governed by `EncAbsErrTime`: it takes the axis off immediately ([ConFlt](../../07-status-and-faults/ConFlt.md) fault `1070`).

> **Availability note:** on Central-i v5 this keyword is marked partially implemented.

## Examples

```text
AEncAbsErrTime=-1        ; disable error/warning/CRC monitoring (default)
AEncAbsErrTime=100       ; tolerate up to 100 control cycles of error/warning/CRC before faulting
AEncAbsErrTime           ; read the configured tolerance
```

## See also

- [EncStatReg](../01-general-settings/EncStatReg.md) — the encoder status bits this timeout acts on
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault register; reports codes 1068 / 1069 / 1070
- [EncType](../01-general-settings/EncType-AuxEncType.md) — feedback type; this applies to the serial absolute encoder
