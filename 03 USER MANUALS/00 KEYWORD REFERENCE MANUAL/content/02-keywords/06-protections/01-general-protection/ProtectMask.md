---
keyword: ProtectMask
summary: Bitfield enabling which hardware protection conditions trigger a fault.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 97
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProtectMask

Bitfield that masks (disables) selected hardware protection conditions.

## Overview

`ProtectMask` selects which hardware protection conditions are *suppressed*. It uses the same bit positions as [HWProtectBits](HWProtectBits.md), but it is a **mask of exclusions**:

- `ProtectMask` bit = **1** &rarr; that protection is **disabled** (masked out — it will not disable the axis).
- `ProtectMask` bit = **0** &rarr; that protection is **enabled** (the default — the condition disables the axis).

So the default `ProtectMask = 0` leaves every (maskable) protection active. Setting a bit turns one protection off. It is axis-scoped, saved to flash, and may be changed at any time (in motion or motor-on).

> **Caution:** masking a hardware protection removes a safety limit. Disable a protection only when you understand why it is firing and what it guards against.

## How it works

`ProtectMask` is not used directly in the control loop; instead, whenever it (or [PowerSupply](../02-current-and-voltage/PowerSupply.md)) changes, the drive re-computes the hardware fault-enable settings from it. The enable applied to the hardware is, in effect:

```text
hardware_enable = (all maskable protections & ~ProtectMask) | non-maskable protections
```

That is: start from "all protections on", clear the bits you set in `ProtectMask`, then force the non-maskable protections back on. This is why a `1` in `ProtectMask` *removes* a protection and why certain critical protections (the non-maskable set) cannot be disabled no matter what you write.

On a standalone drive the result is applied locally; on **Central-i (v5)** the equivalent enable word is sent to the remote amplifier. The power-phase protections are additionally gated by [PowerSupply](../02-current-and-voltage/PowerSupply.md) so that unused AC phases are not protected against.

When an enabled protection condition appears in [HWProtectBits](HWProtectBits.md), the axis is disabled and the corresponding [ConFlt](../../07-status-and-faults/ConFlt.md) ConFlt code is raised.

### Edge cases

- **Motor off:** writes take effect immediately (the keyword is `ok_in_motion: true`, `ok_motor_on: true`). The hardware re-derives the enable word whenever `ProtectMask` (or [PowerSupply](../02-current-and-voltage/PowerSupply.md)) changes.
- **Mode dependency:** the mask is applied unconditionally to all maskable hardware-protection bits.
- **Non-maskable protections:** STO1/STO2, IPM-fault, dead-time, ground-short, watchdog and other safety-critical conditions are forced back on regardless of `ProtectMask`. Setting the corresponding bit has no effect — these protections cannot be disabled.
- **Software protections out of scope:** `ProtectMask` does **not** mask software-level trips (following-error / overspeed / over-temperature / I²t / motor-stuck / dual-stuck / stall / force-error / position-limit). Those run independently and cannot be disabled with this mask.
- **Range overflow:** the keyword has no explicit numeric `range` in the parameter table — write any 32-bit value; bits that map to non-existent protections are silently ignored.
- **Snapshot on fault:** the value of [HWProtectBits](HWProtectBits.md) at the moment of a fault is captured in [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md)`[11]`.

## Examples

```text
AProtectMask         ; read the current protection mask
AProtectMask=0       ; default: every maskable protection enabled
```

To disable only the auxiliary-encoder-error protection (standalone bit 3) while leaving everything else enabled, set the corresponding bit: `AProtectMask=0x0008`.

## See also

- [HWProtectBits](HWProtectBits.md) — reports the live state of these protections (same bit positions)
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault raised by an enabled protection
- [PowerSupply](../02-current-and-voltage/PowerSupply.md) — additionally gates the power-phase protections
