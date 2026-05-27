---
keyword: ProgHeap
summary: Dynamic memory heap used by the user program runtime for variable storage.
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

Dynamic memory heap used by the user program runtime for variable storage.

## Overview

`ProgHeap` is the memory heap used by the user program runtime for variable storage. It is a read/write `int32` array that can be accessed at any time, including over communication, which makes it useful for inspecting or seeding user program variables. It is a non-axis parameter and is not saved to flash, so its contents are cleared on reset (see [ProgResetAll](ProgResetAll.md)).

## How it works

`ProgHeap` is a single shared storage area for the whole controller, not a per-thread structure — unlike the per-thread call stack ([ProgCallStack](ProgCallStack.md)) and numeric stack ([ProgExpStack](ProgExpStack.md)). It backs the persistent (non-stack) variables a user program allocates and is where those variables physically live, so reading or writing an element directly inspects or sets a program variable.

The array is 1-indexed: the first usable element is `ProgHeap[1]`, with 50 usable elements (index 0 is reserved). Each element is a 32-bit signed integer, so the value range is -2147483648 to 2147483647. Because it is not saved to flash, the heap is volatile: a reset clears it. For storage that survives a power cycle, use the general-data arrays instead (see [GenData](../../20-arrays/GenData.md)).

## Examples

```text
AProgHeap[1]        ; read the first heap element
AProgHeap[1]=0      ; write the first heap element
```

## See also

- [GenData](../../20-arrays/GenData.md) — flash-backed general-purpose shared storage
- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
