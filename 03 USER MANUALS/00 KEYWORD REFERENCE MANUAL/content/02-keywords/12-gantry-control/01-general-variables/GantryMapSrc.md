---
summary: Selects the position source used to index the gantry map correction table.
keyword: GantryMapSrc
availability:
  standalone: []
  central-i:
  - v5
can_code: 753
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapSrc

Selects the position source that indexes the gantry decoupling map.

## Overview

`GantryMapSrc` is a pointer that selects which position drives the lookup into the gantry decoupling map ([GantryMap](GantryMap.md)). The value written is the numeric code of the source variable — typically the gantry position along the beam — using the same numbering scheme as other source-pointer keywords; the default `0` selects no source. It is axis-scoped, saved to flash, and can be set with the motor on but not while in motion.

As the gantry moves, the controller reads the live value of the selected source and uses it to interpolate the decoupling ratio from the map; that ratio is reported by [GantryMapVal](GantryMapVal.md) and applied as described in [GantryMapType](GantryMapType.md). The first map entry corresponds to source position [GantryMapInit](GantryMapInit.md), with later entries spaced one map gap apart.

## How it works

`GantryMapSrc` is resolved to its target variable when written, so change it only with the motor off and the system idle. Each control cycle, when the map is enabled ([GantryMapType](GantryMapType.md) = 1), the controller takes the current value of that variable, subtracts [GantryMapInit](GantryMapInit.md), divides by the map gap to get a fractional table index, and linearly interpolates between the two surrounding [GantryMap](GantryMap.md) entries. Positions below the first entry or above the last clamp to the end entries.

## Examples

```text
AGantryMapSrc=<code>  ; index the map by a chosen gantry position source (use the CAN code of that source)
AGantryMapSrc        ; read the configured source code
```

## See also

- [GantryMap](GantryMap.md) — table indexed by this source
- [GantryMapType](GantryMapType.md) — enables use of the map
- [GantryMapVal](GantryMapVal.md) — live interpolated ratio at the indexed position
- [GantryMapInit](GantryMapInit.md) — source position corresponding to the first table entry
