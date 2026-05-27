---
keyword: ComtMode
summary: Array of commutation settings that configure how the motor electrical angle is established.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 72
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 25
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 33
---
# ComtMode

Array of commutation settings that configure how the motor electrical angle is established.

## Overview

`ComtMode` is an array that stores the commutation settings for the axis. These settings select and configure the method used to find and maintain the motor electrical angle for a DC brushless motor, which is required so that the controller can correctly drive the phase currents during motion. The resulting angle is reported by [ComtAng](ComtAng.md), and the progress and outcome of the commutation process are reported by [ComtStatus](ComtStatus.md).

The commutation process is automatically performed following power-on or reset when `ComtMode[5]=1282`. Depending on the selected method, the angle may be derived from Hall sensors (see [HallsAngle](HallsAngle.md), [HallsValue](HallsValue.md), [HallOnlyFilt](HallOnlyFilt.md)) or from the encoder readings. Being an array, axis-scope, and flash-saved, `ComtMode` cannot be changed while the motor is on or in motion.

> **Documentation pending:** The full meaning of each `ComtMode` array index and its valid values is not specified in the source material and is not documented here to avoid fabricating details. Refer to the product manual for the per-index definitions.

## How it works

When a search-based commutation method is used:

1. The position loop is closed temporarily and an additional user-defined, non-zero constant current command is applied. An additional control loop on the commutation offset is formed.
2. The motor moves only slightly until the correct commutation offset is found, after which the motor returns to its starting position.

![image73.emf](../../assets/image73.emf)

## Examples

```text
AComtMode[5]=1282    ; perform commutation automatically after power-on/reset
AComtMode[1]        ; query a single array element
```

## See also

- [ComtAng](ComtAng.md) — instantaneous commutation angle produced by the configured method
- [ComtStatus](ComtStatus.md) — reports the commutation process status
- [HallsAngle](HallsAngle.md) — electrical angle mapped to each Hall state
- [HallsValue](HallsValue.md) — current raw Hall sensor state
- [HallOnlyFilt](HallOnlyFilt.md) — filter for Hall-only commutation angle
