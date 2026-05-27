---
keyword: VecdPosRef
summary: Read-only derivative of the vector position reference (vector velocity), always positive.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 644
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
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
# VecdPosRef

Read-only derivative of the vector position reference (vector velocity), always positive.

## Overview

`VecdPosRef` is a status parameter that reports the derivative of the vector motion position reference, i.e. the time derivative of [VecPosRef](VecPosRef.md). It represents the instantaneous speed along the vector path and follows the profile shaped by [VecAccel](VecAccel.md), [VecDecel](VecDecel.md) and [VecSpeed](VecSpeed.md). `VecdPosRef` is always positive.

## How it works

`VecdPosRef` is computed each control cycle as the change in the (filtered, high-precision) path position [VecPosRef](VecPosRef.md) over that cycle, expressed in user units per second. It is therefore the live path velocity of the move:

- during acceleration it rises at [VecAccel](VecAccel.md) toward the cruise ceiling [VecSpeed](VecSpeed.md);
- it holds at the cruise value while the move is at speed;
- it falls at [VecDecel](VecDecel.md) (or [VecEmrgDec](VecEmrgDec.md) on a stop or fault) as the path end nears.

It is the resultant speed along the path, not the speed of any one member axis; each member axis moves at `VecdPosRef` scaled by its share of the path (its direction cosine on a linear move, or the tangential component on an arc). The controller forces it to exactly 0 at the end of the move so the reported value settles cleanly to zero. A [VecPause](VecPause.md) ramps it down to 0 and back up on resume.

## Examples

```text
AVecdPosRef         ; read the current speed along the vector path
```

## See also

- [VecPosRef](VecPosRef.md) — the position reference whose derivative this reports
- [VecSpeed](VecSpeed.md) — commanded maximum resultant speed
