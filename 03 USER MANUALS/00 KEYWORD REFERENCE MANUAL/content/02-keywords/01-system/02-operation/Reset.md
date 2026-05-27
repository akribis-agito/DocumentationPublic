---
keyword: Reset
summary: Performs a software power cycle; flash parameters are reloaded on restart.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 234
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
# Reset

Performs a software power cycle; flash parameters are reloaded on restart.

## Overview

`Reset` performs a software power-cycle of the controller. On restart, the parameters stored in flash are loaded, overriding any unsaved changes in volatile memory. Use it to apply settings that only take effect at startup (for example after a [Save](Save.md)), or to return the controller to its saved state. `Reset` cannot be issued while the motor is on or in motion.

## Examples

```text
AReset               ; software power cycle (motor must be off)
```

## See also

- [Save](Save.md) — persist parameters before resetting
- [Load](Load.md) — reload from flash without a power cycle
- [AutoExec](AutoExec.md) — auto-start the user program after reset
