---
keyword: FIFOPosCurrOf
summary: Current (torque) feedforward offset added to every FIFO position segment.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 664
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# FIFOPosCurrOf

Current (torque) feedforward offset added to every FIFO position segment.

## Overview

`FIFOPosCurrOf` is a constant current (torque) feedforward bias added to the current reference while the axis runs in position-tracking mode. It lets a host inject an extra torque term — for example to counter a known constant load or gravity — on top of the streamed position trajectory, without altering the queued targets. It is the current member of the three position-tracking offsets, alongside the position offset [FIFOPosPosOf](FIFOPosPosOf.md) and the velocity offset [FIFOPosVelOf](FIFOPosVelOf.md). It is not saved to flash and can be changed at any time, including during motion.

## How it works

On every sample, while the axis is in motion and in position-tracking mode, the value of `FIFOPosCurrOf` is added to the current reference:

```text
current reference = current from control + FIFOPosCurrOf
```

The bias is applied in position and velocity operation modes (in pure current/force operation the current reference is set directly and this bias does not apply). It is active only in position-tracking mode and only while the axis is in motion; outside those conditions it has no effect. It biases the torque feedforward and does not change the position targets.

## Changes between versions

On the v5 central-controller build, `FIFOPosCurrOf` is a floating-point value, allowing fractional current bias. On v4 (and on standalone drives) it is a whole-number value with a range of -64000 to 64000.

## Examples

```text
AFIFOPosCurrOf=2000  ; add a uniform current feedforward bias
AFIFOPosCurrOf=0     ; remove the bias
```

## See also

- [FIFOPosPosOf](FIFOPosPosOf.md) — position offset
- [FIFOPosVelOf](FIFOPosVelOf.md) — velocity feedforward offset
- [FIFOPosTrgt](FIFOPosTrgt.md) — working target position
