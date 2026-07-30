---
keyword: DTCompLvl
summary: Current band around zero within which dead-time compensation is interpolated rather than switched.
availability:
  standalone: []
  central-i:
  - v5
can_code: 870
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: [0, 1000]
  default: 1
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# DTCompLvl

Current band around zero within which dead-time compensation is interpolated rather than switched.

## Overview

Dead-time compensation adds a voltage whose **sign** follows the commanded phase current. Near a zero crossing that sign is ill-defined, and switching it abruptly would make the compensation flip back and forth on noise. `DTCompLvl` sets the half-width, in mA, of a band around zero current in which the sign is ramped linearly instead of switched.

## How it works

For each phase, with commanded current `i`:

- `i > DTCompLvl` → full positive compensation
- `i < −DTCompLvl` → full negative compensation
- otherwise → compensation scaled by `i / DTCompLvl`

> **Note:** `DTCompLvl` must remain greater than zero. The interpolation slope is `1/DTCompLvl`, so a value of zero would be a division by zero; the drive guards against this by disabling the slope, which makes the compensation switch abruptly.

### Choosing a value

Set it a little above the noise floor of your current measurement. Too small and the compensation chatters near zero crossings; too large and a meaningful band of low-current operation receives only partial compensation — which matters, because low current is exactly where dead time hurts most.

### Edge cases

- **No effect when disabled:** with [DTCompGain](DTCompGain.md) at 0 this keyword has no effect at all.
- **Range:** writes outside `0…1000` mA are clamped.

## Examples

```text
ADTCompLvl=50        ; interpolate within +/-50 mA of zero current
```

## See also

- [DTCompGain](DTCompGain.md) — the compensation gain itself
