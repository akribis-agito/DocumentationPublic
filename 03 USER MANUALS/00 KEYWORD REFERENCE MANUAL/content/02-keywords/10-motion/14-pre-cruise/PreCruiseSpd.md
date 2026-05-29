---
keyword: PreCruiseSpd
summary: Speed held during the pre-cruise stage of a sine point-to-point move (user units).
availability:
  standalone: []
  central-i:
  - v5
can_code: 843
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PreCruiseSpd

Speed held during the pre-cruise stage of a sine point-to-point move (user units).

This keyword is available from **v5 (central-i only)**.

## Overview

`PreCruiseSpd` is the speed the axis runs at during the **pre-cruise stage** — the faster opening run of a sine point-to-point move ([MotionMode](../02-motion-configuration/MotionMode.md) `= 20` and `= 21`). After the axis covers the pre-cruise stroke (up to the target set by [PreCruAbsTrgt](PreCruAbsTrgt.md) or [PreCruRelTrgt](PreCruRelTrgt.md)) it slows to the ordinary cruise speed [Speed](../03-kinematics-configuration/Speed.md) for the rest of the move. See the [pre-cruise overview](00-overview.md) for the staging concept.

The value is always zero or positive; the direction of travel comes from the targets, not from the sign of this keyword.

## How it works

A pre-cruise stage is inserted only when `PreCruiseSpd` is **greater than** the cruise speed [Speed](../03-kinematics-configuration/Speed.md) **and** a pre-cruise stroke is defined. The reasoning:

- If `PreCruiseSpd` &gt; `Speed`, the move runs the opening stroke fast and then steps **down** to the cruise speed to finish — accelerate to pre-cruise speed, hold it, slow to cruise speed, hold cruise speed, decelerate to the target.
- If `PreCruiseSpd` is **less than or equal to** `Speed` (including the default `0`), there is no faster stage to run first, so the pre-cruise speed is effectively capped and the move reduces to an ordinary sine point-to-point profile at the cruise speed.

The acceleration, deceleration and jerk shaping of every stage use the same [Accel](../03-kinematics-configuration/Accel.md), [Decel](../03-kinematics-configuration/Decel.md) and jerk settings as a normal sine point-to-point move. At `Begin` the controller checks that the pre-cruise stroke is long enough to accelerate from rest to the cruise speed; if not, the move is rejected (pre-cruise stroke insufficient, [instruction error code](../../../04-error-codes/instruction-error-codes.md) 384).

## Examples

```text
AMotionMode=20         ; sine point-to-point
ASpeed=300000          ; cruise speed
APreCruiseSpd=800000   ; faster pre-cruise speed (> Speed, so a pre-cruise stage runs)
APreCruRelTrgt=200000  ; pre-cruise stroke
ARelTrgt=500000        ; total move distance
ABegin                 ; start the move
APreCruiseSpd          ; read back the pre-cruise speed
```

To disable the pre-cruise stage on a configured axis, set the pre-cruise speed at or below the cruise speed:

```text
APreCruiseSpd=0        ; no pre-cruise; plain sine point-to-point at Speed
```

## See also

- [Speed](../03-kinematics-configuration/Speed.md) — the cruise speed used after the pre-cruise stage
- [PreCruAbsTrgt](PreCruAbsTrgt.md) / [PreCruRelTrgt](PreCruRelTrgt.md) — where the pre-cruise stage ends
- [Pre-cruise overview](00-overview.md) — how the stages compose
- [MotionMode](../02-motion-configuration/MotionMode.md) — modes 20 and 21 select sine point-to-point motion
- [Begin](../04-motion-command/Begin.md) — validates and starts the move
