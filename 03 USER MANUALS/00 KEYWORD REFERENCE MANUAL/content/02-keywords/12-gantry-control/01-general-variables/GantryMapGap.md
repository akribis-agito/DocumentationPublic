---
keyword: GantryMapGap
summary: Spacing in source-position units between consecutive entries of the gantry decoupling map.
availability:
  standalone: []
  central-i:
  - v5
can_code: 751
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
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryMapGap

Spacing in source-position units between consecutive entries of the gantry decoupling map.

## Overview

`GantryMapGap` sets the **step size** of the position-dependent gantry decoupling map: the distance, in the units of the source selected by [GantryMapSrc](GantryMapSrc.md), between one [GantryMap](GantryMap.md) entry and the next. Together with [GantryMapInit](GantryMapInit.md) (the position of the first entry) it fixes where every table entry sits along the beam:

```text
position of entry n  =  GantryMapInit + GantryMapGap × (n − 1)
```

So entry 1 is at [GantryMapInit](GantryMapInit.md), entry 2 one gap further on, and so on. The gap multiplied by the number of populated entries is the total travel the map covers.

It is an axis-scoped value on the gantry master axis, saved to flash, settable with the motor on but not while in motion. The minimum value is `1` (a gap of zero is not allowed because the controller forms the per-unit interpolation slope from `1 ÷ gap`). Default `1`. Available on central-i (v5).

## How it works

When the position-dependent map is active ([GantryMapType](GantryMapType.md) = 1), each control cycle the controller takes the live source position from [GantryMapSrc](GantryMapSrc.md), subtracts [GantryMapInit](GantryMapInit.md), and divides by `GantryMapGap` to get a fractional table index. It then linearly interpolates between the two surrounding [GantryMap](GantryMap.md) entries and reports the result as [GantryMapVal](GantryMapVal.md). Writing `GantryMapGap` recomputes the reciprocal used for that interpolation, so a new gap takes effect on the next lookup.

Choose the gap together with the number of map entries so the map spans the gantry's working travel: a smaller gap gives finer position resolution but covers less range for a given number of entries; a larger gap covers more travel more coarsely. Positions before the first entry or beyond the last clamp to the end entries.

## Examples

```text
AGantryMapGap=1000   ; map entries are spaced 1000 source-position units apart
AGantryMapGap        ; read the configured spacing
```

### Edge cases

- **In motion at write** — rejected (`NOMOTN`); may be changed with the motor on.
- **Gap of zero** — not allowed; the minimum is `1`.
- **Map type off** ([GantryMapType](GantryMapType.md) = 0) — stored but **not consulted**; the gantry uses the fixed symmetric 50/50 split.
- **Gap too large / too small for the travel** — if the working range exceeds `GantryMapInit + GantryMapGap × (entries − 1)`, positions past the last entry clamp to the last entry; reduce the gap or add entries to cover the full range.
- **Set on wrong axis** — read on the gantry master axis only; writes elsewhere are stored but ignored.
- **Save** — flash-saveable; reloaded at boot.
- **Platform** — v5 central-i only.

## See also

- [GantryMap](GantryMap.md) — table of decoupling ratios whose entries this spaces
- [GantryMapInit](GantryMapInit.md) — source position of the first entry
- [GantryMapSrc](GantryMapSrc.md) — source whose units this gap is expressed in
- [GantryMapType](GantryMapType.md) — enables use of the map
- [GantryMapVal](GantryMapVal.md) — live interpolated ratio at the indexed position
