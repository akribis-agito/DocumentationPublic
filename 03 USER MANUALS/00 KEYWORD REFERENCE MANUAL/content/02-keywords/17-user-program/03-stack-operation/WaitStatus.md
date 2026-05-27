---
keyword: WaitStatus
summary: Holds a user program thread until a selected status reaches a required value.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 194
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 34
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# WaitStatus

Holds a user program thread until a selected status reaches a required value.

## Overview

`WaitStatus` is a low-level user-program keyword, used only in user program compilation; it cannot be commanded normally over communication channels. `WaitStatus` holds the user program thread until the selected status reaches the required value. It is the status-driven counterpart of [WaitTime](WaitTime.md), which instead waits for a fixed time. The status to wait on is chosen by the array index, and the required value is the assigned value.

## How it works

The array index selects which status bit or counter the thread waits on:

| StatusType | Description |
|----|----|
| 1 | CounterDown1 |
| 2 | CounterDown2 |
| 3 | CounterDown3 |
| 4 | CounterDown4 |
| 5 | CounterUp1 |
| 6 | CounterUp2 |
| 7 | MotionStat: In Motion Bit |
| 8 | MotionStat: In Repetitive Wait Bit |
| 9 | MotionStat: In Repetitive Stop Bit |
| 10 | MotionStat: In Stop Request Bit |
| 11 | MotionStat: In Acceleration Bit |
| 12 | MotionStat: In Deceleration Bit |
| 13 | MotionStat: In Wait End Smooth Bit |
| 14 | MotionStat: In ECAM Stop Bit |
| 15 | MotionStat: In Wait End Smooth Bit |
| 16 | StatReg: Commutation Bit |
| 17 | StatReg: In Target Bit |
| 18 | RecStat: Trigger Detected Bit |
| 19 | RecStat: Recording Completed Bit |
| 20 | DInPort: Bit 0 (Digital Input 1) |
| 21 | DInPort: Bit 1 (Digital Input 2) |
| 22 | DInPort: Bit 2 (Digital Input 3) |
| 23 | DInPort: Bit 3 (Digital Input 4) |
| 24 | DInPort: Bit 4 (Digital Input 5) |
| 25 | DInPort: Bit 5 (Digital Input 6) |
| 26 | DInPort: Bit 6 (Digital Input 7) |
| 27 | DInPort: Bit 7 (Digital Input 8) |
| 28 | DInPort: Bit 8 (Digital Input 9) |
| 29 | DInPort: Bit 9 (Digital Input 10) |
| 30 | DInPort: Bit 10 (Digital Input 11) |
| 31 | DInPort: Bit 11 (Digital Input 12) |
| 32 | DInPort: Bit 12 (Digital Input 13) |
| 33 | DInPort: Bit 13 (Digital Input 14) |
| 34 | Designated input with DInMode set as “2 – Motor On + Begin” |
| 35 | Designated input with DInMode set as “14 – Control Set Change” |
| 36 | Designated input with DInMode set as “19 – Clear Abs Enc” |
| 37 | Designated input with DInMode set as “5 – Clear PD Input Pulse” |
| 38 | Designated input with DInMode set as “9 – Reverse Limit” |
| 39 | Designated input with DInMode set as “10 – Forward Limit” |
| 40 | Designated input with DInMode set as “11 – Torque Limit On” |
| 41 | Designated input with DInMode set as “7 – Reset/Clear Alarm” |
| 42 | Designated input with DInMode set as “8 – Abort Motion” |
| 43 | Designated input with DInMode set as “16 – Mode Switch Vel/Pos” |
| 44 | Designated input with DInMode set as “17 – Mode Switch Vel/Curr” |
| 45 | Designated input with DInMode set as “18 – Mode Switch Pos/Curr” |
| 46 | Designated input with DInMode set as “15 – Add Velocity Filter” |

## Examples

```text
AWaitStatus[17],1   ; hold until the axis reaches and settles in target (StatReg In Target bit = 1)
```

## See also

- [WaitTime](WaitTime.md) — hold a task for a fixed time instead of a status
