---
keyword: ProductSN
summary: Two-element array holding the unit's hardware version and production serial number; written only under elevated permission and persisted to flash.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 468
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
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
overrides:
  central-i.v5:
    can_code: 348
---
# ProductSN

Two-element array holding the unit's hardware version and production serial number.

## Overview

`ProductSN` stores the controller's hardware version and production serial number and persists them to flash, so they survive power cycles and uniquely identify a physical unit for production and field service. The array is declared with three slots; element `[0]` is unused so that communication indices start at 1, leaving two usable elements:

| Index | Contents |
|-------|----------|
| [1] | Hardware version number |
| [2] | Production serial number — a concatenation of year (2 digits), week (2 digits) and unit count (4 digits) |

![ProductSN[2] format — year, week, unit-count fields](productsn-format.svg)

## How it works

`ProductSN` is held in flash. On power-up, after the controller loads its keywords from flash, it copies `ProductSN[1]` and `ProductSN[2]` into the [Identity](Identity.md) array — into `Identity[3]` (hardware version) and `Identity[2]` (serial number) respectively — where host software reads them to display the unit's serial number. The same copy is repeated whenever `ProductSN` is written, so `Identity` always tracks the stored value.

## Writing the serial number (elevated permission)

`ProductSN` is intended to be programmed once, during production. The write is guarded: the controller only accepts a write to `ProductSN` while it is in an **elevated (burn-in) permission** state. Without that permission the write is rejected with:

> Communication error **328** — "Setting Product Serial Number is not allowed without Elevated Permissions."

As a safeguard, the firmware clears the elevated-permission state immediately upon accepting a `ProductSN` write, so the permission only ever authorises a **single** write — programming both elements requires re-authorising before each one. In normal use, integrators and end users only ever **read** `ProductSN`.

## Examples

```text
AProductSN[1]       ; read the hardware version
AProductSN[2]       ; read the production serial number
```

## See also

- [Identity](Identity.md) — exposes the serial number (`Identity[2]`) and hardware version (`Identity[3]`) to host software
- [UnitStat](UnitStat.md) — unit hardware/firmware health
