---
keyword: DCDC
summary: Read-only array of internal logic-rail voltage measurements.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 42
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 8
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
# DCDC

Read-only array of internal logic-rail voltage measurements.

## Overview

`DCDC` reports the drive's internal logic-supply voltage measurements as an array, one entry per rail. It is a read-only diagnostic complementing the single 5 V reading in [VLogic](VLogic.md). Not every entry is populated on every product; contact Agito for the readings applicable to a specific product.

## How it works

Each array index maps to a logic rail as follows.

| Index | Description                                       |
|-------|---------------------------------------------------|
| 1     | 3.3 V logic                                       |
| 2     | 15 V logic                                        |
| 3     | -15 V logic                                       |
| 4     | 1.2 V logic                                       |
| 5     | 1.8 V logic                                       |
| 6     | Internal 10.5 V or backup logic (whichever higher) |
| 7     | 4.7 V logic                                       |

## Examples

```text
DCDC[1]?            ; read the 3.3 V logic rail
DCDC[2]?            ; read the 15 V logic rail
```

## See also

- [VLogic](VLogic.md) — 5 V logic-supply voltage reading
- [VBus](VBus.md) — amplifier DC bus voltage reading
