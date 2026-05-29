# Engineering Units

This category groups the keywords of the global engineering-units subsystem. They let a host application present and accept a set of related keyword values in a chosen engineering unit (for example mm, deg/s, or N) instead of the controller's internal units, without changing how the control loop itself runs.

The feature is available from central-i v5 only.

![Internal units pass through a scale factor (UnitFct) to an engineering unit labelled by UnitUnt; the group (UnitGrp) lists the keywords the conversion applies to, and UserUnitsEn is the master enable](units-model.svg)

## The Group / Factor / Unit model

Each physical quantity has its own triplet of keywords. For a quantity *Q* (Position, Velocity, Acceleration, or Force):

- **`Q`UnitGrp** — a read-only array that lists which keywords belong to that quantity's unit group. These are the keywords whose values are reinterpreted together when the engineering unit is changed. The list is fixed by the firmware; you read it to see exactly which keywords a unit change affects.
- **`Q`UnitFct** — a floating-point scale factor between the controller's internal units for that quantity and the selected engineering unit. One factor applies to the whole group.
- **`Q`UnitUnt** — the display label (name) of the engineering unit for that quantity, stored as a short text string (up to 10 characters). It is a free-text label such as `mm` or `deg/s`; it documents the unit but does not by itself perform any conversion.

`UserUnitsEn` is the master enable for the whole subsystem on an axis. The four triplets are:

| Quantity | Group | Factor | Unit label |
|---|---|---|---|
| Position | [PosUnitGrp](PosUnitGrp.md) | [PosUnitFct](PosUnitFct.md) | [PosUnitUnt](PosUnitUnt.md) |
| Velocity | [VelUnitGrp](VelUnitGrp.md) | [VelUnitFct](VelUnitFct.md) | [VelUnitUnt](VelUnitUnt.md) |
| Acceleration | [AccUnitGrp](AccUnitGrp.md) | [AccUnitFct](AccUnitFct.md) | [AccUnitUnt](AccUnitUnt.md) |
| Force | [FrcUnitGrp](FrcUnitGrp.md) | [FrcUnitFct](FrcUnitFct.md) | [FrcUnitUnt](FrcUnitUnt.md) |

## Relationship to the embedded UsrUnits scaling

This global engineering-units feature is separate from the existing per-axis [UsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) (and `AuxUsrUnits`) scaling. The two methods are **mutually exclusive on a given axis**: if `UserUnitsEn` is active for an axis while the embedded `UsrUnits` scaling is also set to a non-default value on that axis, an assignment to a keyword that belongs to one of the global unit groups is rejected with error code `338` ("Global User Units feature is mutually exclusive with embedded controller user units"). Disable one of the two scaling methods to clear the conflict. See [UserUnitsEn](UserUnitsEn.md) for details.

## Keywords

| Keyword | Summary |
|---|---|
| [UserUnitsEn](UserUnitsEn.md) | Master enable for the global engineering-units feature on an axis. |
| [PosUnitGrp](PosUnitGrp.md) | Lists the keywords in the position unit group. |
| [PosUnitFct](PosUnitFct.md) | Scale factor between internal position units and the selected engineering unit. |
| [PosUnitUnt](PosUnitUnt.md) | Display label for the position engineering unit. |
| [VelUnitGrp](VelUnitGrp.md) | Lists the keywords in the velocity unit group. |
| [VelUnitFct](VelUnitFct.md) | Scale factor between internal velocity units and the selected engineering unit. |
| [VelUnitUnt](VelUnitUnt.md) | Display label for the velocity engineering unit. |
| [AccUnitGrp](AccUnitGrp.md) | Lists the keywords in the acceleration unit group. |
| [AccUnitFct](AccUnitFct.md) | Scale factor between internal acceleration units and the selected engineering unit. |
| [AccUnitUnt](AccUnitUnt.md) | Display label for the acceleration engineering unit. |
| [FrcUnitGrp](FrcUnitGrp.md) | Lists the keywords in the force unit group. |
| [FrcUnitFct](FrcUnitFct.md) | Scale factor between internal force units and the selected engineering unit. |
| [FrcUnitUnt](FrcUnitUnt.md) | Display label for the force engineering unit. |
