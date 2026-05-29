---
keyword: PreCruRelTrgt
summary: Pre-cruise target as a distance from the start of a sine point-to-point move (user units).
availability:
  standalone: []
  central-i:
  - v5
can_code: 842
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PreCruRelTrgt

Pre-cruise target as a distance from the start of a sine point-to-point move (user units).

This keyword is available from **v5 (central-i only)**.

## Overview

`PreCruRelTrgt` sets the **pre-cruise stroke** directly — the signed distance, in user units, from where the move starts to the **pre-cruise target**, the point up to which the axis runs at the faster [PreCruiseSpd](PreCruiseSpd.md) before settling to the normal cruise speed for the rest of the move. It applies to the sine point-to-point modes ([MotionMode](../02-motion-configuration/MotionMode.md) `= 20` and `= 21`); see the [pre-cruise overview](00-overview.md) for the staging concept.

It is the relative counterpart of [PreCruAbsTrgt](PreCruAbsTrgt.md), which gives the same point as an absolute position. The final destination of the move is still set by [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md).

## How it works

When [Begin](../04-motion-command/Begin.md) is issued in a sine point-to-point mode the controller resolves the pre-cruise target:

- If `PreCruRelTrgt` is **non-zero**, the pre-cruise target is `start position + PreCruRelTrgt`, and [PreCruAbsTrgt](PreCruAbsTrgt.md) is ignored for that move.
- If `PreCruRelTrgt` is `0`, the absolute [PreCruAbsTrgt](PreCruAbsTrgt.md) is used instead.

Because a non-zero relative value always takes priority, set `PreCruRelTrgt` to `0` whenever you want to drive the pre-cruise target absolutely.

A pre-cruise stage is only run when the pre-cruise speed is higher than the cruise speed and a pre-cruise stroke is defined; otherwise the move is an ordinary sine point-to-point profile. The controller validates the geometry at `Begin` and rejects the move if a condition is not met:

| Condition | Effect if it fails |
|---|---|
| Pre-cruise stroke points toward the final target | rejected — total and pre-cruise stroke must be in the same direction (error 381) |
| Final target is beyond the pre-cruise target | rejected — total stroke must be longer than the pre-cruise stroke (error 383) |
| Pre-cruise stroke long enough to reach pre-cruise speed and slow back to cruise speed | rejected — pre-cruise stroke insufficient (error 384) |

## Examples

A move of 500000 user units in which the first 200000 are run at the faster pre-cruise speed:

```text
AMotionMode=20         ; sine point-to-point
ASpeed=300000          ; cruise speed (used after pre-cruise)
APreCruiseSpd=800000   ; faster pre-cruise speed
APreCruRelTrgt=200000  ; run fast for the first 200000 units
ARelTrgt=500000        ; total move distance
ABegin                 ; start the move
APreCruRelTrgt[1]      ; read back the pre-cruise distance
```

To switch a configured axis back to an absolute pre-cruise target, clear this keyword:

```text
APreCruRelTrgt=0       ; fall back to PreCruAbsTrgt
```

## See also

- [PreCruAbsTrgt](PreCruAbsTrgt.md) — same target expressed as an absolute position
- [PreCruiseSpd](PreCruiseSpd.md) — speed held over the pre-cruise stroke
- [Pre-cruise overview](00-overview.md) — how the stages compose
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — the final target of the move
- [MotionMode](../02-motion-configuration/MotionMode.md) — modes 20 and 21 select sine point-to-point motion
- [Begin](../04-motion-command/Begin.md) — validates and starts the move
