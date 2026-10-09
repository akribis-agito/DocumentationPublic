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
last_updated: '2026-10-10'
doc_revision: '2026.06'
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

### Embedded-scaling conflict

Error `338` applies only when the accessed keyword uses embedded `UsrUnits`, `AuxUsrUnits` or `PDUsrUnits` scaling, belongs to the corresponding global unit group, and both `UserUnitsEn = 1` and a non-default embedded ratio are set on that axis. On AGM800-EC, `AuxVel` and `PDVel` use fixed time-domain scaling and do not raise this conflict. Position keywords that retain embedded scaling remain subject to the check. See [AGM800-EC timing and units](../01-system/03-timing/AGM800-EC-units.md) for the full conversion list.

To clear a conflict, restore the matching embedded ratio to its default or set `UserUnitsEn` to 0.

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
- [UsrUnits/AuxUsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — embedded per-axis scaling
