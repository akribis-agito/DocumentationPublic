---
keyword: ProductSN
summary: Two-element array holding the unit's hardware version and production serial number; written only under elevated permission and persisted to flash.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# ProductSN

Two-element array holding the unit's hardware version and production serial number.

## Overview

`ProductSN` stores the controller's hardware version and production serial number and persists them to flash, so they survive power cycles and uniquely identify a physical unit for production and field service.

The array is 1-indexed:

| Index | Contents |
|-------|----------|
| [1] | Hardware version number |
| [2] | Production serial number — a concatenation of year (2 digits), week (2 digits) and unit count (4 digits) |

On power-up, after the controller loads its keywords, it copies `ProductSN[1]` and `ProductSN[2]` into the [Identity](Identity.md) array — into `Identity[3]` (hardware version) and `Identity[2]` (serial number) respectively — where host software reads them to display the unit's serial number.

## Writing the serial number (elevated permission)

`ProductSN` is intended to be programmed once, during production. Writing any element requires the controller to be in an **elevated (burn-in) permission** state; otherwise the controller rejects the write with:

> Communication error **328** — "Setting Product Serial Number is not allowed without Elevated Permissions."

As a safeguard, the elevated-permission state is cleared automatically immediately after a `ProductSN` element is written, so each write must be individually authorized. In normal use, integrators and end users only ever **read** `ProductSN`.

## Examples

```text
ProductSN[1]?       ; read the hardware version
ProductSN[2]?       ; read the production serial number
```

## See also

- [Identity](Identity.md) — exposes the serial number (`Identity[2]`) and hardware version (`Identity[3]`) to host software
- [UnitStat](UnitStat.md) — unit hardware/firmware health
