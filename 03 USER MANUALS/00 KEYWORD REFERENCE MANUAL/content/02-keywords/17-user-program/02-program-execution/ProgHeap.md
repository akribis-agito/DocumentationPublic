---
keyword: ProgHeap
summary: Dynamic memory heap used by the user program runtime for variable storage.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`ProgHeap` is the dynamic memory heap used by the user program runtime for variable storage. It is a read/write array of 51 `int32` elements that can be accessed at any time, including over communication, which makes it useful for inspecting or seeding user program variables. It is a non-axis parameter and is not saved to flash, so its contents are cleared on reset (see [ProgResetAll](ProgResetAll.md)).

## Examples

```text
AProgHeap[1]        ; read the first heap element
AProgHeap[1]=0       ; write the first heap element
```

## See also

- [ProgResetAll](ProgResetAll.md) — stop all threads and reset pointers and stacks
- [ProgStatAll](ProgStatAll.md) — combined status of all tasks
