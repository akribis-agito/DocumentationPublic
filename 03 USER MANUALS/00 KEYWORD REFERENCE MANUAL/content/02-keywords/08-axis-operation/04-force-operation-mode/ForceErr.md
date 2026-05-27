---
keyword: ForceErr
summary: Difference between force reference and force feedback.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 583
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
overrides: {}
---
# ForceErr

Difference between force reference and force feedback.

## Overview

`ForceErr` is the difference between the force reference ([ForceRef](ForceRef.md)) and the force feedback ([Force](Force.md)). It is the error signal driven by the force control loop.

## How it works

$$
ForceErr\ \lbrack unit\rbrack\  = \ ForceRef\ \lbrack unit\rbrack\  - \ Force\ \lbrack unit\rbrack
$$

## Examples

```text
ForceErr?           ; read the current force error
```

## See also

- [ForceRef](ForceRef.md) — force reference (minuend)
- [Force](Force.md) — force feedback (subtrahend)
- [ForceInTTol](ForceInTTol.md) — settling window applied to this error
