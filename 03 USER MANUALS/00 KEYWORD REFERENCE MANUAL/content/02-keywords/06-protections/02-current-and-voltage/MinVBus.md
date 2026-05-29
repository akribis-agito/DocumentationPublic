---
keyword: MinVBus
summary: Minimum allowed bus voltage; dropping to or below it immediately disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 89
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
  - 11000
  - 90000
  default: 11000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MinVBus

Minimum allowed bus voltage; dropping to or below it immediately disables the axis.

## Overview

`MinVBus` is the minimum allowed bus voltage, in mV. If the actual bus voltage drops to or below this limit, the axis is disabled and a fault is raised. This guards against brown-out / supply-loss conditions.

## How it works

On each periodic bus-voltage check the drive compares `VBus` with `MinVBus`:

- If `VBus ≤ MinVBus`, the axis is disabled and [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1009 (bus voltage too low).
- As `VBus` approaches the limit from above, a multi-level under-voltage warning is reported in [StatReg](../../07-status-and-faults/StatReg.md) (bits 7–8) at 1.12 / 1.08 / 1.04 × `MinVBus` (low / medium / high); at or below `MinVBus`, bit 4 (under-MinVBus) is set.

> **Note:** unlike the over-voltage trip, the under-voltage trip is **immediate** — it does *not* use the [MaxVBusTime](MaxVBusTime.md) delay.

> **Worked example:** with `MinVBus = 18000` (18 V), if `VBus` momentarily drops to 17 V on the next bus check the axis is disabled and `ConFlt = 1009`. Even a single sub-`MinVBus` sample trips; there is no debounce or time window. For a category-level view of where this fits relative to the over-voltage band and `MaxVBusAbs` ceiling, see the [bus-voltage protection bands](00-overview.md).

### Edge cases

- **Motor off:** the under-voltage check still runs (drive-level protection); a brown-out trips even when no axis is enabled.
- **Mode dependency:** the trip runs regardless of operation mode.
- **No delay:** `MaxVBusTime` is for the over-voltage path only; under-voltage is always immediate.
- **Range overflow:** writes outside `11000…90000` (mV) are clamped to the keyword `range`.
- **Clearing the fault:** ConFlt code 1009 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1, once the supply has recovered) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the under-voltage trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md).

## Examples

```text
AMinVBus=18000       ; 18 V minimum bus voltage (mV)
```

## See also

- [MaxVBus](MaxVBus.md) — maximum bus voltage
- [MaxVBusTime](MaxVBusTime.md) — delay (over-voltage path only; does not apply here)
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1009 raised on trip
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 4 (under-MinVBus) and bits 7–8 (VBus warning)
