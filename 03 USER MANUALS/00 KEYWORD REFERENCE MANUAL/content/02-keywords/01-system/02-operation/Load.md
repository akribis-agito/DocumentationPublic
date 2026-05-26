---
keyword: Load
summary: Reloads all parameters from flash into volatile memory, discarding unsaved changes.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 233
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Load

Reloads all parameters from flash into volatile memory, discarding unsaved changes.

## Overview

`Load` retrieves all flash-saveable parameters from non-volatile (flash) memory into the active (volatile) parameter table. The controller performs this once automatically at power-up; issuing `Load` manually repeats it **without** a power cycle.

`Load` overwrites every unsaved change in volatile memory. This makes it the quick way to recover from a bad, unsaved configuration: `Load` reverts the controller to the last known-good parameters stored in flash. Whether a given parameter participates is determined by its `flash` attribute (shown in each keyword's Quick Facts).

## Examples

```text
Load                ; reload all flash-saved parameters, discarding unsaved edits
```

## See also

- [Save](Save.md) — write parameters to flash
- [Reset](Reset.md) — software power cycle (also reloads from flash)
