---
keyword: AOutPort
summary: Commanded analog-output value (mV) in direct command mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 219
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -11905
  - 11905
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutPort

Commanded analog-output value (mV) in direct command mode.

## Overview

`AOutPort` sets the value, in millivolts, driven on an analog output when that output is in **direct command mode**. The array index is the analog-output number (e.g. `AOutPort[2]` is analog output 2). `AOutPort[Index]` only takes effect when `AOutMode[Index] == 0`; in monitoring mode the output follows the emulated parameter instead. See the [analog-output overview](00-overview.md) for both modes.

## Examples

```text
AOutMode[1]=0       ; direct command mode
AOutPort[1]=5000    ; drive analog output 1 to 5000 mV
```

## See also

- [AOutMode](AOutMode.md) — direct vs monitoring mode
- [AOutOffset](AOutOffset.md) — output calibration offset
