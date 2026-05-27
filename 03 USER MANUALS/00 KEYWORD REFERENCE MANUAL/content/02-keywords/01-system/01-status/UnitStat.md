---
keyword: UnitStat
summary: Read-only bitfield reporting the unit's hardware and firmware health.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 75
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# UnitStat

Read-only bitfield reporting the unit's hardware and firmware health.

## Overview

`UnitStat` is a read-only status word that reports the health of the unit's hardware and firmware. Each bit flags a specific fault or image-mismatch condition; a value of `0` means none of them are set. Because it is non-axis, `UnitStat` describes the controller/drive unit as a whole rather than any individual axis, and it is not saved to flash — it always reflects the live state.

Read `UnitStat` after a firmware or FPGA update, or when diagnosing why a unit will not operate, to confirm the images are consistent and no hardware fault is present.

## How it works

`UnitStat` is a single 32-bit word built up during start-up. As the controller initialises it checks each hardware/image condition in turn and **OR**s the corresponding bit into the word when the condition is true; conditions that are re-checked later (such as the dynamic-brake firmware/FPGA match) clear their own bit when they pass. A clean unit therefore reads `0`. Each flag is product-specific — a bit is only set on the products where that check applies — so an unset bit means either "not faulted" or "not applicable to this model".

The firmware also uses the word internally: for example, a faulty-FPGA bit prevents the unit from coming online. Host software reads the word after programming to confirm the firmware and FPGA images are a matched, valid set.

## Status bits

| Bit | Status |
|-----|--------|
| 0 | FPGA is faulty |
| 1 | AGD155 firmware and FPGA do not match |
| 2 | AGD301 firmware and FPGA do not match |
| 3 | No golden image is present |
| 4 | Dynamic-brake firmware and FPGA do not match |

## Responding to warnings

- **No golden image (bit 3)** can be ignored on units that are not expected to carry a golden image.
- For an **FPGA fault or any firmware/FPGA mismatch** (bits 0–2, 4), obtain the latest matching firmware and FPGA from Agito and reprogram them — see [DownloadFW](../02-operation/DownloadFW.md) and [DownloadFPGA](../02-operation/DownloadFPGA.md).

## Examples

```text
AUnitStat           ; read the current unit status word
```

## See also

- [FWInfo](FWInfo.md) — firmware version and build information
- [Identity](Identity.md) — controller identification and implemented features
- [DownloadFW](../02-operation/DownloadFW.md) / [DownloadFPGA](../02-operation/DownloadFPGA.md) — reprogram firmware / FPGA images
