---
summary: Forward/reverse limits that re-interpret an out-of-range absolute encoder position at power-on (customized firmware only).
---
# EncAbsFL/EncAbsRL

Forward/reverse limits that re-interpret an out-of-range absolute encoder position at power-on (customized firmware only).

## Overview

`EncAbsFL` and `EncAbsRL` offset the absolute encoder position at power-on so that a reading near the top of the unsigned range is interpreted as a small negative position instead. `EncAbsFL` defines the forward limit and `EncAbsRL` defines the reverse limit of the allowed travel. They are applied after the absolute offset ([EncAbsOff](EncAbsOff-AuxEncAbsOff.md)). This is intended for a rotary motor with an absolute encoder whose stroke is restricted by a hard stop.

> **Note:** These keywords are a customization (originally for a Korea project) and are only implemented in customized firmware versions. Confirm availability before use.

## How it works

Absolute encoder positions are read as unsigned integers, so a position just below zero appears as a large value near the top of the range. `EncAbsFL` and `EncAbsRL` tell the controller which readings should be treated as negative positions:

Consider a rotary motor whose hard stop only allows motion between +90 deg and -90 deg. If at power-on the axis is at -45 deg, the absolute encoder reports 315 deg (because values are unsigned). A command to move to 0 deg would then drive 315 deg in reverse (instead of 45 deg forward) and hit the hard stop.

Setting `EncAbsFL` to 90 deg and `EncAbsRL` to -90 deg informs the controller that 315 deg is out of the allowed range and should be interpreted as -45 deg instead.

## Examples

```text
AEncAbsFL=90         ; forward limit (customized firmware)
EncAbsRL=-90        ; reverse limit (customized firmware)
```

## See also

- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — absolute offset, applied before these limits
- [EncType](EncType-AuxEncType.md) — encoder type; these apply for absolute encoders
