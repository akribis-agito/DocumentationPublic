---
keyword: RetractTarget
summary: Absolute target of the point-to-point move on entry to position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 609
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# RetractTarget

Absolute target of the point-to-point move on entry to position mode.

## Overview

`RetractTarget` is the **absolute** target position, in user units, of the point-to-point move that runs on entry to position operation mode (subject to [BeginOnToPos](BeginOnToPos.md) being armed). It is overridden by a non-zero [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md): in that case the target is taken relative to the position reference at the moment of entry instead. The move runs at [RetractSpeed](RetractSpeed.md). It is a flash-stored setting, so it persists across power cycles.

## How it works

When the entry move is launched, `QuickBeginOnSwitchToPos()` selects the PTP target (`AG300_CTL01ControlLoops.c:2364`):

```text
if RelTrgt != 0:  gllAbsTrgt = gllFinalPosRef + RelTrgt   ; relative to the entry reference
else:             gllAbsTrgt = RetractTarget              ; absolute target
```

So `RetractTarget` is used **only when [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) is 0**; otherwise it is ignored and the relative target wins. The resulting `gllAbsTrgt` is the standard point-to-point target, so the move respects the software position limits ([FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)) like any other motion. The default is 0.

## Changes between versions

In **v5 (central-i)** the motion pipeline is 64-bit, so `RetractTarget` is a 64-bit value with the larger range shown in the frontmatter; the target-selection logic is unchanged. **v5 is central-i only**, so on standalone `RetractTarget` remains the v4 32-bit value.

## Examples

```text
ARetractTarget=50000 ; absolute entry-move target (user units)
ARetractSpeed=20000  ; entry-move speed
ABeginOnToPos=1      ; arm the move
AGoToPosMode         ; switch and start the move
```

## See also

- [BeginOnToPos](BeginOnToPos.md) — arms the entry move
- [RetractSpeed](RetractSpeed.md) — speed of the entry move
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) — relative-target override (takes precedence when non-zero)
- [GoToPosMode](GoToPosMode.md) — one of the commands that triggers the move
