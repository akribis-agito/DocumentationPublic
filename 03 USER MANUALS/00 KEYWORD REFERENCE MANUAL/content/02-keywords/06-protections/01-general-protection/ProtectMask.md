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

`ProtectMask` is not used directly in the control loop; instead, whenever it (or [PowerSupply](../02-current-and-voltage/PowerSupply.md)) changes, the firmware re-computes the FPGA / amplifier fault-enable register from it. The value written to the hardware is, in effect:

```text
hardware_enable = (ALL_PROTECTIONS & ~ProtectMask) | NON_MASKABLE
```

That is: start from "all protections suggested on", clear the bits you set in `ProtectMask`, then force the non-maskable protections back on. This is why a `1` in `ProtectMask` *removes* a protection and why certain critical protections (the non-maskable set) cannot be disabled no matter what you write.

On a standalone drive the result is written to the FPGA protections-mask register; on **Central-i (v5)** the equivalent enable word is sent to the remote amplifier (`AmpFaultEnable`). The power-phase protections are additionally gated by [PowerSupply](../02-current-and-voltage/PowerSupply.md) so that unused AC phases are not protected against.

When an enabled protection condition appears in [HWProtectBits](HWProtectBits.md), the axis is disabled and the corresponding [ConFlt](../../07-status-and-faults/ConFlt.md) fault code is raised.

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
