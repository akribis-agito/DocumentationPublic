---
keyword: DualStuckVel
summary: Maximum tolerated velocity difference between the two dual-loop feedbacks.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 157
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
  - 0
  - 1300000000
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualStuckVel

Maximum tolerated velocity difference between the two dual-loop feedbacks.

## Overview

`DualStuckVel` is the maximum absolute velocity difference tolerated between the two feedbacks in a dual-loop configuration, in count/s (counts referring to the main / position-loop feedback). If the difference exceeds this for [DualStuckTime](DualStuckTime.md) consecutive cycles, the axis is disabled — catching a slipped or broken coupling between the two encoders.

## How it works

$$
\text{Absolute velocity difference} = \left| Vel[2] - \frac{AuxVel \cdot DualLoopFact}{65536} \right|
$$

## Examples

```text
ADualStuckVel=40000  ; max tolerated feedback velocity mismatch (count/s)
```

## See also

- [DualStuckTime](DualStuckTime.md) — how long the mismatch may persist
