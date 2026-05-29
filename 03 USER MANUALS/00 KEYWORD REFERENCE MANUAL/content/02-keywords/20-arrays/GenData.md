---
keyword: GenData
summary: General-purpose, non-axis 32-bit integer array for shared user/host storage.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 237
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 1001
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
  central-i.v5:
    array_size: 10001
---
# GenData

General-purpose, non-axis 32-bit integer array for shared user/host storage.

## Overview

`GenData` is a general-purpose 32-bit signed integer array that provides shared storage accessible by both the user program and the host. It is not linked to any controller feature, so it is well suited for use as user-program variables, as temporary variables in custom functions, and for debugging. It is non-axis (a single array shared across the controller), readable and writable at any time, and saved to flash so its contents survive a power cycle once the parameters are stored.

`GenData` is the 32-bit integer member of the general-data family: [GenDataF](GenDataF.md) (32-bit floating-point), [GenDataD](GenDataD.md) (64-bit double-precision floating-point) and [GenDataLL](GenDataLL.md) (64-bit signed integer) provide the same kind of shared storage for the other data types. For per-axis storage that the controller also uses internally for certain features, see [UserParam](UserParam.md). Values can be set directly with a normal write, or indirectly through the host-side indirect-write mechanism described below.

![General-purpose array families: the GenData row holds the four non-axis variants (GenData int32, GenDataF float32, GenDataD float64, GenDataLL int64) recommended for user programs, and the UserParam row holds the four per-axis variants (UserParam, UserParamF, UserParamD, UserParamLL) some of whose entries are reserved internally](array-family-types.svg)

Each element holds a 32-bit signed integer, so the value range is -2147483648 to 2147483647 and the default is 0. The array is 1-indexed: the first usable element is `GenData[1]` (index 0 is reserved and inaccessible). The number of usable elements depends on the controller model: typically 1000, with 5000 on larger controllers and up to 10000 on models with double-flash storage.

## Addressing

An element is normally written with a literal index, for example `AGenData[5]=100`. Two additional mechanisms allow the index to be chosen at run time.

### Computed (run-time) index in a user program

Within a user program, addressing an array element with index `[0]` is a request for a *computed* index: the index is taken from the top of the running thread's numeric stack instead of from the instruction. The program pushes the desired index first (for example with a [Math](../17-user-program/02-program-execution/Math.md) result), then writes or reads the element with index `[0]`. The read side of this is documented in [PushParam](../17-user-program/03-stack-operation/PushParam.md).

The controller enforces the following on the popped index:

- If the numeric stack is empty, the instruction is rejected with error 53.
- The popped value must be in the range 1 to the highest usable index; a negative value, 0, or a value above the array size is rejected with error 20.

Outside a user program (a normal host write), index `[0]` is not a computed-index request — it is simply an out-of-range index and is rejected with error 20.

### Indirect write from the host

The host can also write an element without addressing the keyword directly, using the three-register indirect-write mechanism: set [IndirectArray](../../05-legacy-keywords/IndirectArray.md) to select the target array, [IndirectIndex](../../05-legacy-keywords/IndirectIndex.md) to the element index and [IndirectValue](../../05-legacy-keywords/IndirectValue.md) to the value, then trigger [IndirectDo](../../05-legacy-keywords/IndirectDo.md) to perform the write.

This path can target `GenData` only. `IndirectArray` accepts a single value (1 = `GenData`); selecting any other array rejects the write with error 115. The index must be in the range 1 to the highest usable index, otherwise the write is rejected with error 116. `IndirectValue` is a 32-bit signed integer (-2147483648 to 2147483647), so the indirect path can write only 32-bit integer values and cannot target the floating-point or 64-bit members of the family ([GenDataF](GenDataF.md), [GenDataD](GenDataD.md), [GenDataLL](GenDataLL.md)).

## Examples

```text
AGenData[1]=100      ; store 100 in the first element
AGenData[1]         ; read the first element
AGenData[1000]=0     ; highest usable index on a 1000-element model
```

## See also

- [GenDataD](GenDataD.md) — 64-bit double-precision floating-point variant
- [GenDataF](GenDataF.md) — 32-bit single-precision floating-point variant
- [GenDataLL](GenDataLL.md) — long-long (64-bit signed integer) variant
- [UserParam](UserParam.md) — per-axis feature-related general storage
