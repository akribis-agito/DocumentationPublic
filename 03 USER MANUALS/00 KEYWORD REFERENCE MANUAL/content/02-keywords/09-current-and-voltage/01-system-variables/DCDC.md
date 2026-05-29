---
keyword: DCDC
summary: Read-only array of internal logic-rail voltage measurements.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 42
attributes:
  access: ro
  scope: non-axis
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# DCDC

Read-only array of internal logic-rail voltage measurements.

## Overview

`DCDC` reports the drive's internal logic-supply voltage measurements as an array, one entry per rail, in millivolts. It is a read-only diagnostic complementing the single 5 V reading in [VLogic](VLogic.md). Not every entry is populated on every product; contact Agito for the readings applicable to a specific product.

## How it works

The array has 8 elements (index 0 is unused so that communication indexes start at 1). Each index maps to a logic rail as follows.

| Index | Description                                        |
|-------|----------------------------------------------------|
| 1     | 3.3 V logic                                        |
| 2     | 15 V logic                                         |
| 3     | -15 V logic                                        |
| 4     | 1.2 V logic                                        |
| 5     | 1.8 V logic                                        |
| 6     | Backup or logic supply                             |
| 7     | 4.7 V logic                                        |

The rails are sampled across two control sub-cycles (the 3.3 V / ±15 V group in one step, the 1.2 V / 1.8 V group in the next), each raw reading being scaled to millivolts with a fixed per-rail multiplier. Which rails are actually sampled is product-dependent:

- On products that do not sense a given rail, the nominal value is substituted (for example 3300 mV for the 3.3 V rail, ±15000 mV for the ±15 V rails, 1200 / 1800 mV for the 1.2 V / 1.8 V rails) so the reading is still plausible rather than zero.
- The −15 V reading is corrected for the 3.3 V loading on some products, so it is a computed rather than a directly read value.
- On a **central-i** remote axis, index 6 (backup / logic) and index 1 (3.3 V) are filled from the amplifier-sync message, each scaled by a per-axis calibration factor and offset; the 5 V reading from that same message is stored in [VLogic](VLogic.md) instead.

Because of this, a constant nominal reading on a rail does not necessarily mean the rail is healthy — it may simply not be sensed on that product.

## Examples

```text
ADCDC[1]            ; read the 3.3 V logic rail
ADCDC[2]            ; read the 15 V logic rail
ADCDC[6]            ; read the backup / logic rail
```

## See also

- [VLogic](VLogic.md) — 5 V logic-supply voltage reading
- [VBus](VBus.md) — amplifier DC bus voltage reading
