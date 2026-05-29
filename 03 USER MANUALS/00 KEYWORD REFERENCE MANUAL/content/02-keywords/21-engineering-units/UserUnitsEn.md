---
keyword: UserUnitsEn
summary: Master enable for the global engineering-units feature on an axis.
availability:
  standalone: []
  central-i:
  - v5
can_code: 826
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserUnitsEn

Master enable for the global engineering-units feature on an axis.

## Overview

`UserUnitsEn` turns the global engineering-units feature on or off for an axis. When enabled, the keywords belonging to the position, velocity, acceleration, and force unit groups are intended to be presented and accepted in the engineering units configured by the per-quantity factor and unit-label keywords, rather than in the controller's internal units. When disabled (the default), the axis uses its ordinary user-units behaviour.

This feature is available from central-i v5 only.

## How it works

`UserUnitsEn` is a per-axis on/off switch:

| Value | Meaning |
|---|---|
| 0 | Disabled (default). The global engineering-units feature is off for this axis. |
| 1 | Enabled. The global engineering-units configuration applies to this axis. |

The setting is stored in flash, so it persists across power cycles.

### Mutual exclusivity with the embedded UsrUnits scaling

The global engineering-units feature and the embedded per-axis [UsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) / `AuxUsrUnits` scaling are **mutually exclusive on the same axis**. Both express keyword values in something other than raw internal units, so only one may be active at a time.

The controller enforces this on writes. When you assign a value to a keyword that belongs to one of the global unit groups, the assignment is rejected with error code `338` if both of the following are true for that axis:

- `UserUnitsEn` is set to 1, and
- the corresponding embedded scaling (`UsrUnits` for main-feedback keywords, or the auxiliary / pulse-direction variants for their respective keywords) is set to a non-default value.

Error `338` reports: "Global User Units feature is mutually exclusive with embedded controller user units. Please disable one of the scaling factors." To resolve the conflict, leave the embedded scaling at its default or set `UserUnitsEn` back to 0.

If the embedded scaling is at its default value, enabling `UserUnitsEn` does not raise this conflict.

## Examples

```text
AUserUnitsEn[1]=1      ; enable the global engineering-units feature on the axis
AUserUnitsEn[1]=0      ; disable it (default)
AUserUnitsEn[1]        ; read the current enable state
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [PosUnitGrp](PosUnitGrp.md) — keywords affected for position
- [PosUnitFct](PosUnitFct.md) — position scale factor
- [UsrUnits/AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — the embedded scaling this feature is mutually exclusive with
