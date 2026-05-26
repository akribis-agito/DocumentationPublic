---
keyword: ParamCS
summary: Read-only checksum over the controller's parameter set, for verifying configuration.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 428
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 4
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
# ParamCS

Read-only checksum over the controller's parameter set, for verifying configuration.

## Overview

`ParamCS` is a read-only, 1-indexed array holding a checksum computed over the controller's parameter set. A host can read it to verify that the parameters stored on the device match an expected configuration — for example to confirm a fleet of units is identically configured — without downloading and comparing the full parameter list. Comparing `ParamCS` before and after a [Save](../02-operation/Save.md) also confirms whether stored configuration changed.

## Examples

```text
ParamCS[1]?         ; read the first word of the parameter checksum
```

## See also

- [ParamAbout](ParamAbout.md) — metadata for a single parameter
- [Save](../02-operation/Save.md) — persist parameters to flash
