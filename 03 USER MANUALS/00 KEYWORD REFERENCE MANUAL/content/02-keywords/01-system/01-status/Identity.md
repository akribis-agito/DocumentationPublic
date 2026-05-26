---
keyword: Identity
summary: Read-only array describing the controller — product type, serial number, versions, limits and capability flags — used by host software for identification and feature detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 1
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 63
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Identity

Read-only array describing the controller: identification, versions, limits and capability flags.

## Overview

`Identity` is a read-only, 1-indexed array that describes the controller. Host software — notably Agito PCSuite — reads it to identify the unit, detect which features the firmware implements, and adapt its behaviour accordingly. It is non-axis and reflects the live device.

## Index reference

| Index | Field | Notes |
|-------|-------|-------|
| [1] | Product type | Numeric product-model code — see table below |
| [2] | Serial number | Production serial number; copied from `ProductSN[2]` at power-up |
| [3] | Hardware version | Hardware revision; copied from `ProductSN[1]` at power-up |
| [4] | Firmware version | |
| [5] | FPGA version | |
| [6] | Manufacture date | |
| [7] | Tester code | |
| [8] | Customer code | |
| [9] | Continuous current limit | |
| [10] | Peak current limit | |
| [11] | Minimum bus voltage | |
| [12] | Maximum bus voltage | |
| [13] | Current-loop frequency | |
| [14] | Maximum recording length | |
| [15] | Maximum recording vectors | |
| [16] | Number of axes | |
| [17] | Boot version | |
| [18] | User-program maximum threads | |
| [19] | User-program numeric stack depth | |
| [20] | Maximum internal PWM value | |
| [21] | Number of parameters | |
| [22] | Type of communication | |
| [23] | Central-i master: number of servo axes | |
| [24] | Analog-inputs update rate | |
| [25] | Feature flags, word 1 | Capability bitfield (see below) |
| [26]–[61] | Reserved | |
| [62] | Feature flags, word 2 | Capability bitfield (see below) |

### Product-type codes (index 1)

| Value | Model |
|-------|-------|
| 5 | AGD200 |
| 9 | AGD155 |
| 10 | AGM800 |
| 11 | AGD301 |
| 12 | AGD155EC |
| 13 | AGD101EC |
| 14 | AGD156EC |

### Feature-flag words (indices 25 and 62)

`Identity[25]` and `Identity[62]` are bitfields in which each bit advertises support for a specific firmware capability — for example learn-commutation, vector motion mode, true-jerk CNC, or dynamic (indirect) array indexing. Host software tests these bits to decide which features are available, rather than inferring capability from the firmware version number.

## Examples

```text
Identity[1]?        ; product-type code
Identity[2]?        ; production serial number
Identity[16]?       ; number of axes
```

## See also

- [ProductSN](ProductSN.md) — source of the serial number (`Identity[2]`) and hardware version (`Identity[3]`)
- [FWInfo](FWInfo.md) — firmware version and build information
- [About](About.md) — full parameter dump (Agito PCSuite internal use)
