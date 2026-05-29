---
keyword: ProgHeap
summary: Controller-wide, volatile read/write int32 array providing shared storage for the user program and communication.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 1021
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 51
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
# ProgHeap

Controller-wide, volatile read/write `int32` array providing shared storage for the user program and communication.

## Overview

`ProgHeap` is a controller-wide read/write `int32` array that provides shared storage accessible both to the user program and over communication. It can be accessed at any time, including over communication, which makes it useful for exchanging values with a running user program. It is a non-axis parameter and is not saved to flash, so it is volatile: its contents do not survive a power cycle (the default value is `0`).

## How it works

`ProgHeap` is a single shared storage area for the whole controller, not a per-thread structure — unlike the per-thread call stack ([ProgCallStack](ProgCallStack.md)) and numeric stack ([ProgExpStack](ProgExpStack.md)). The same elements are visible to the user program and over communication, so it can be used to pass values between them.

The array is 1-indexed: the first usable element is `ProgHeap[1]`, with 50 usable elements (index 0 is reserved so that communication indexes start at 1). Each element is a 32-bit signed integer, so the value range is -2147483648 to 2147483647. Because it is not saved to flash, it is volatile and starts from `0` after each power-up. For storage that survives a power cycle, use the general-data arrays instead (see [GenData](../../20-arrays/GenData.md)).

## Examples

```text
AProgHeap[1]        ; read the first element
AProgHeap[1]=0      ; write the first element
```

## See also

- [GenData](../../20-arrays/GenData.md) — flash-backed general-purpose shared storage
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgStatAll](ProgStatAll.md) — combined status of all threads
