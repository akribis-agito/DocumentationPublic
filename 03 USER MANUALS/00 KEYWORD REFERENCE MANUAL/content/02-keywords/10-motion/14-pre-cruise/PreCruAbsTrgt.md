---
keyword: PreCruAbsTrgt
summary: "Absolute position of the pre-cruise target for a sine point-to-point move (user units)."
availability:
  standalone: []
  central-i:
  - v5
can_code: 841
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
# PreCruAbsTrgt

Absolute position of the pre-cruise target for a sine point-to-point move (user units).

This keyword is available from **v5 (central-i only)**.

## Overview

`PreCruAbsTrgt` sets the absolute position, in user units, of the **pre-cruise target** — the point up to which the axis runs at the faster [PreCruiseSpd](PreCruiseSpd.md) before settling to the normal cruise speed for the rest of the move. It applies to the sine point-to-point modes ([MotionMode](../02-motion-configuration/MotionMode.md) `= 20` and `= 21`); see the [pre-cruise overview](00-overview.md) for the staging concept.

It is the absolute counterpart of [PreCruRelTrgt](PreCruRelTrgt.md), which gives the same point as a distance from where the move starts. The final destination of the move is still set by [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md).

## How it works

When [Begin](../04-motion-command/Begin.md) is issued in a sine point-to-point mode the controller resolves the pre-cruise target the same way it resolves the main target:

- If [PreCruRelTrgt](PreCruRelTrgt.md) is **non-zero**, the pre-cruise target is taken as a relative distance from the start of the move and `PreCruAbsTrgt` is ignored for that move.
- If `PreCruRelTrgt` is `0`, the pre-cruise target is `PreCruAbsTrgt`. Under modulo mode ([ModRev](../../03-encoder/04-modulo-mode/ModRev.md), [ModShort](../../03-encoder/04-modulo-mode/ModShort.md)) the absolute target is adjusted into the active reference frame just like a main absolute target.

The distance from the start of the move to this target is the **pre-cruise stroke**. A pre-cruise stage is only run when the pre-cruise speed is higher than the cruise speed and a pre-cruise stroke is defined; otherwise the move is an ordinary sine point-to-point profile. The controller validates the geometry at `Begin` and rejects the move if a condition is not met:

| Condition | Effect if it fails |
|---|---|
| Pre-cruise target lies in the same direction as the final target | rejected — total and pre-cruise stroke must be in the same direction (error 381) |
| Final target is beyond the pre-cruise target | rejected — total stroke must be longer than the pre-cruise stroke (error 383) |
| Pre-cruise stroke long enough to reach pre-cruise speed and slow back to cruise speed | rejected — pre-cruise stroke insufficient (error 384) |

## Examples

A fast opening run to position 200000, then a calmer cruise into the final target at 500000:

```text
AMotionMode=20         ; sine point-to-point
ASpeed=300000          ; cruise speed (used after pre-cruise)
APreCruiseSpd=800000   ; faster pre-cruise speed
APreCruRelTrgt=0       ; use the absolute pre-cruise target below
APreCruAbsTrgt=200000  ; run fast up to here
AAbsTrgt=500000        ; final destination
ABegin                 ; start the move
APreCruAbsTrgt[1]      ; read back the pre-cruise target
```

## See also

- [PreCruRelTrgt](PreCruRelTrgt.md) — same target expressed as a distance from the move start
- [PreCruiseSpd](PreCruiseSpd.md) — speed held over the pre-cruise stroke
- [Pre-cruise overview](00-overview.md) — how the stages compose
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — the final target of the move
- [MotionMode](../02-motion-configuration/MotionMode.md) — modes 20 and 21 select sine point-to-point motion
- [Begin](../04-motion-command/Begin.md) — validates and starts the move
