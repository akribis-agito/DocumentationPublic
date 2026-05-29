---
keyword: AnomDtctSt
summary: "Read-only status array reporting the detector state, filtered signal value, active band, and active motion."
availability:
  standalone: []
  central-i:
  - v5
can_code: 780
attributes:
  access: ro
  scope: axis
  flash: true
  type: array
  array_size: 6
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
# AnomDtctSt

Read-only status array reporting the detector state, filtered signal value, active band, and active motion.

## Overview

`AnomDtctSt` reports what the anomaly detector is doing right now. It is the main diagnostic for the feature: it tells you whether the detector is idle, waiting, actively checking, or has tripped, and it exposes the filtered signal value and the band currently being compared against. Use it to tune the [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) limit tables and to confirm the detector is tracking the motion you expect.

This array is read-only. It is updated by the controller; you cannot write it.

This keyword is available from v5 (central-i).

## How it works

The array is 1-indexed (index 0 is reserved). The usable elements are:

| Index | Element |
| --- | --- |
| 1 | **State** of the detector (see the state table below). |
| 2 | **Filtered signal value** — the monitored signal after the low-pass filter, the value actually compared against the band. |
| 3 | **Active lower limit** — the [AnomDtctLL](AnomDtctLL.md) value currently in force at this point of the motion. |
| 4 | **Active upper limit** — the [AnomDtctUL](AnomDtctUL.md) value currently in force at this point of the motion. |
| 5 | **Active motion** — which monitored motion (0–3) the detector is currently tracking. |

State values reported in element 1:

| Value | Meaning |
| --- | --- |
| 0 | Idle. Detection is off ([AnomDtctOn](AnomDtctOn.md) = 0). |
| 1 | Waiting for motion. Detection is armed but no motion has started yet. |
| 2 | Active. The detector is tracking the motion and comparing the filtered signal against the band. |
| 3 | Anomaly detected. The filtered signal left the band; the axis has been stopped or tripped with fault code 1067 on [ConFlt](../../07-status-and-faults/ConFlt.md). |

A further reserved state value (4) is defined for a suspended condition but is not entered by the detector in the firmware consulted for this reference.

When element 1 reports 3, inspect elements 2, 3, and 4 to see by how much and on which side the signal exceeded the band, and element 5 to confirm which motion was being checked.

## Examples

```text
AAnomDtctSt[1]     ; read the detector state
AAnomDtctSt[2]     ; read the filtered monitored value
AAnomDtctSt[3]     ; active lower limit
AAnomDtctSt[4]     ; active upper limit
AAnomDtctSt[5]     ; active monitored motion
```

## See also

- [AnomDtctOn](AnomDtctOn.md) — arm or disable the detector
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — the band the active limits come from
- [AnomDtctCnfg](AnomDtctCnfg.md) — monitored source and stop behavior
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1067 raised on a trip
