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
