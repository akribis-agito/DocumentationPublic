---
keyword: Save
summary: Writes all flash-saveable parameters from volatile memory to flash.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 232
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
# Save

Writes all flash-saveable parameters from volatile memory to flash.

## Overview

`Save` persists parameters to non-volatile (flash) memory. It first erases the previous parameter area in flash, then copies every flash-saveable parameter from volatile memory into it — so the stored set always reflects the controller's current configuration. Settings that are not saved are lost on the next power cycle or [Load](Load.md).

Saving is **not allowed while the motor is enabled**. Whether a given parameter is included depends on its `flash` attribute (shown in each keyword's Quick Facts).

## Examples

```text
ASave                ; persist current parameters to flash (motor must be off)
```

## See also

- [Load](Load.md) — reload parameters from flash
- [Reset](Reset.md) — software power cycle
- [ParamCS](../01-status/ParamCS.md) — checksum to verify stored configuration
