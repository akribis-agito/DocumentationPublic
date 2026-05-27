---
keyword: ParamAbout
summary: Function returning a parameter's metadata (CAN code, name, attributes, range, default).
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 499
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ParamAbout

Function returning a parameter's metadata (CAN code, name, attributes, range, default).

## Overview

`ParamAbout` returns descriptive metadata about a single parameter — its CAN code, mnemonic name, attribute flags, valid range, and default value. It lets host software and diagnostic tools enumerate or inspect parameter metadata at runtime instead of hard-coding it.

The parameter to inspect is selected by its CAN code (the valid range, 0–1023, matches the controller's CAN-code space). Unlike [About](About.md), which dumps every parameter, `ParamAbout` targets one.

## Examples

```text
AParamAbout=100      ; select the parameter with CAN code 100 (PosGain)
AParamAbout         ; read back its descriptor
```

## See also

- [About](About.md) — full parameter dump (Agito PCSuite internal use)
- [ParamCS](ParamCS.md) — checksum over the parameter set
- [Identity](Identity.md) — controller identification and features
