---
keyword: FIFOPosVelOf
summary: Velocity feedforward offset added to every FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 663
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPosVelOf

Velocity feedforward offset added to every FIFO position segment.

## Overview

`FIFOPosVelOf` is a constant velocity feedforward bias added to the velocity reference while the axis runs in position-tracking mode. It supplements the velocity feedforward that the controller derives from the streamed position trajectory, letting a host inject an extra velocity term without altering the queued targets. It is the velocity member of the three position-tracking offsets, alongside the position offset [FIFOPosPosOf](FIFOPosPosOf.md) and the current offset [FIFOPosCurrOf](FIFOPosCurrOf.md). It is not saved to flash and can be changed at any time, including during motion.

## How it works

On every sample, while the axis is in motion and in position-tracking mode, the value of `FIFOPosVelOf` is added to the velocity reference:

```text
velocity reference = velocity from trajectory + FIFOPosVelOf
```

The offset is applied only in position-tracking mode and only while the axis is in motion; outside those conditions it has no effect. It biases the feedforward path and does not change the position targets, so it does not by itself move the axis to a new position — it primarily improves tracking or applies a deliberate velocity bias. The value is interpreted in the controller's velocity units.

## Examples

```text
AFIFOPosVelOf=10000  ; add a uniform velocity feedforward bias
AFIFOPosVelOf=0      ; remove the bias
```

## See also

- [FIFOPosPosOf](FIFOPosPosOf.md) — position offset
- [FIFOPosCurrOf](FIFOPosCurrOf.md) — current feedforward offset
- [FIFOPosTrgt](FIFOPosTrgt.md) — working target position
