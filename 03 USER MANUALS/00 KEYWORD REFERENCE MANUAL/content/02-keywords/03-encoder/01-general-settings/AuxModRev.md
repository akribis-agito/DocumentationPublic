---
keyword: AuxModRev
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 71
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
---
# AuxModRev

**Definition:**

AuxModRev is the modulo revolution divisor for the auxiliary encoder, analogous to [ModRev](ModRev.md) for the main encoder. When set to a non-zero value, the auxiliary encoder position (AuxPos) is wrapped to the range [0, AuxModRev − 1]. This parameter is axis-related, saved to flash, and is currently marked as not implemented in the firmware.

%%
Needs verification
AuxModRev is flagged NOT_IMPLEMENTED in the current firmware table; confirm availability before use.
%%
**See also:**

[ModRev](ModRev.md), [AuxPos](../../09-current-and-voltage/01-system-variables/AuxPos.md)
