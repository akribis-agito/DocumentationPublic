---
keyword: ComtStatus
summary: Read-only array reporting the actual commutation (phasing) status of the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 143
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ComtStatus

Read-only array reporting the actual commutation (phasing) status of the axis.

## Overview

`ComtStatus` is a read-only array that reports the actual commutation status of the axis. It is used to monitor the commutation process configured by [ComtMode](ComtMode.md) and to diagnose failures: a positive value of 100 indicates a successfully finished commutation, intermediate values indicate progress, and negative values are error codes. Being read-only and not flash-saved, it can be read at any time, including while the motor is on or in motion. The resulting electrical angle is reported by [ComtAng](ComtAng.md).

## How it works

The array holds the following elements (1-indexed):

| Index | Description |
|---|---|
| `[1]` | Phasing status. Default 0. See the value table below. |
| `[2]` | Number of successful consecutive steps. Default 0. Reported only when `ComtMode[1]=1` ("jump to zero" commutation mode). |
| `[3]` | Reserved / not specified in the source. |

`ComtStatus[1]` (phasing status) values:

| Value | Commutation status |
|---|---|
| 0 | Required and not executed yet. |
| 1 | Commutation in progress. |
| 100 | Successfully finished. |
| 200 | Commutation is not required (e.g. DC, voice coil or stepper motors). |
| 300 | Rough commutation is done, waiting for index pulse for fine commutation adjustment. |
| 400 | Rough commutation is done. Waiting for Hall sequence change for fine commutation adjustment. |
| 500 | Learn process changed parameters (recommended to save to flash). |
| 600 | Burn-in mode is activated. |
| -1 | Unexpected motor off. Motor off occurred during commutation. |
| -2 | Illegal commutation method selected. |
| -3 | "Jump to zero" commutation failed. Please check motor, encoder and commutation parameters (such as voltage and accuracy). |
| -4 | Encoder error is detected. Commutation is required. |
| -5 | Parameter is modified. Commutation is required. |
| -6 | Amplifier power cycle is required. |
| -7 | Illegal halls sequence detected. |
| -8 | Central-I failure during commutation process. |
| -9, -10, -11, -12 | Illegal halls sequence is detected during learn process. |

## Examples

```text
ComtStatus[1]?      ; query the phasing status
ComtStatus[2]?      ; successful consecutive steps ("jump to zero" mode)
```

## See also

- [ComtMode](ComtMode.md) — commutation settings driving this status
- [ComtAng](ComtAng.md) — instantaneous commutation angle
- [HallsValue](HallsValue.md) — current raw Hall sensor state (related to illegal-Hall-sequence errors)
