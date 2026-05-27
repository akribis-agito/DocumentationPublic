---
keyword: IdRef
summary: Read-only direct-axis current reference, used in dq0-domain control; currently always 0.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 29
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# IdRef

Read-only direct-axis current reference, used in dq0-domain control; currently always 0.

## Overview

`IdRef` is the reference current of the direct (d) axis, in milliamperes, used in dq0-domain current control. It is the reference regulated against the feedback [Id](Id.md), producing the error [IdErr](IdErr.md). Currently `IdRef` is always 0; contact Agito if an application involving `IdRef` (for example flux weakening) is needed.

## Examples

```text
AIdRef              ; read direct-axis current reference (mA)
```

## See also

- [Id](Id.md) — direct-axis feedback current
- [IdErr](IdErr.md) — direct-axis current error
- [IqRef](IqRef.md) — quadrature-axis current reference
