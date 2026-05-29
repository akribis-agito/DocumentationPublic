---
keyword: MaxVBusAbs
summary: Absolute bus-voltage ceiling; exceeding it disables the axis instantly.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 94
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
# MaxVBusAbs

Absolute bus-voltage ceiling; exceeding it disables the axis instantly.

## Overview

`MaxVBusAbs` is the maximum allowable absolute bus voltage, in mV. If the bus voltage exceeds `MaxVBusAbs`, the axis is **instantaneously** disabled — there is no time window. This is the no-delay counterpart to [MaxVBus](MaxVBus.md), which tolerates excess for up to [MaxVBusTime](MaxVBusTime.md).

## How it works

On each periodic bus-voltage check the drive compares `VBus` directly with `MaxVBusAbs`:

- If `VBus ≥ MaxVBusAbs`, the axis is disabled immediately and [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1023 (bus voltage too high — absolute limit exceeded).
- If `VBus ≥ MaxVBusAbs`, [StatReg](../../07-status-and-faults/StatReg.md) bit 6 (over-MaxVBusAbs) is set as a status indication.

Because no timer is involved, set `MaxVBusAbs` above [MaxVBus](MaxVBus.md) so that the time-windowed limit acts first on normal transients, with `MaxVBusAbs` as the hard backstop.

> **Worked example:** with `MaxVBus = 80000` (80 V), `MaxVBusTime = 200` (ms) and `MaxVBusAbs = 90000` (90 V), a regeneration spike to 82 V is tolerated for up to 200 ms (`ConFlt = 1008` only after that). A spike to 91 V trips immediately on the next bus check with `ConFlt = 1023`, regardless of `MaxVBusTime`.

### Edge cases

- **Motor off:** the absolute-ceiling check still runs (drive-level protection).
- **Mode dependency:** the trip runs regardless of operation mode.
- **No delay:** `MaxVBusTime` does not apply here — `MaxVBusAbs` is unconditional and acts on the next bus check.
- **Range overflow:** writes outside `12000…95000` (mV) are clamped. Set above [MaxVBus](MaxVBus.md) so the timed band acts first.
- **Clearing the fault:** ConFlt code 1023 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the absolute over-voltage trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md).

## Examples

```text
AMaxVBusAbs=90000    ; instantaneous over-voltage ceiling (mV)
```

## See also

- [MaxVBus](MaxVBus.md) — time-delayed over-voltage limit
- [MaxVBusTime](MaxVBusTime.md) — delay used by MaxVBus (not by MinVBus or MaxVBusAbs)
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1023 raised on trip
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 6 flags over-MaxVBusAbs
