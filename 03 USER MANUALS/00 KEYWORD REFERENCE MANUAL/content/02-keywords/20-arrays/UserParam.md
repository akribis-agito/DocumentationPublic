---
keyword: UserParam
summary: Per-axis, feature-related 32-bit integer array for shared user/host storage.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 624
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 251
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
# UserParam

Per-axis, feature-related 32-bit integer array for shared user/host storage.

## Overview

`UserParam` is an axis-related general-purpose 32-bit signed integer array that provides per-axis storage accessible by both the user program and the host. It can be read and written at any time, including while in motion and with the motor on, and is saved to flash so its contents survive a power cycle once the parameters are stored.

Unlike the [GenData](GenData.md) family, the user-parameter arrays are feature-related: some entries are used internally to store temporary variables (for example, in the homing sequence and for CNC motion variables). The controller guarantees that any given entry is not used by more than one feature at a time, but because some entries are reserved by features, it is not recommended to use `UserParam` for the user program, custom functions, or debugging — use [GenData](GenData.md) for that. `UserParam` is the 32-bit integer member of the family; see [UserParamF](UserParamF.md) (32-bit floating-point), [UserParamD](UserParamD.md) (64-bit double-precision floating-point) and [UserParamLL](UserParamLL.md) (64-bit signed integer) for the other data types.

Each element holds a 32-bit signed integer, so the value range is -2147483648 to 2147483647 and the default is 0. The array is 1-indexed: the first usable element is `UserParam[1]` (index 0 is reserved and inaccessible). The number of usable elements is model-dependent — 250 on most models, 50 on smaller ones.

## Examples

```text
AUserParam[1]=5      ; store a value in the first element
AUserParam[1]       ; read the first element
AUserParam[250]=0    ; highest usable index on a 250-element model
```

## See also

- [UserParamD](UserParamD.md) — 64-bit double-precision integer variant
- [UserParamF](UserParamF.md) — floating-point variant
- [UserParamLL](UserParamLL.md) — long-long (64-bit signed integer) variant
- [GenData](GenData.md) — non-axis general-purpose storage (recommended for user programs)
