---
keyword: IdRef
summary: Read-only direct-axis current reference, used in dq0-domain control; currently always 0.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# IdRef

Read-only direct-axis current reference, used in dq0-domain control; currently always 0.

## Overview

`IdRef` is the reference current of the direct (d) axis, in milliamperes, used in dq0-domain (vector) current control. It is the reference regulated against the feedback [Id](Id.md), producing the error [IdErr](IdErr.md). The d axis is the flux/field axis; holding `IdRef` at 0 keeps all commanded current torque-producing (on the q axis).

## How it works

In the three-phase current loop the firmware sets the direct-axis reference to zero unconditionally:

$$
\text{IdRef}\ \lbrack mA\rbrack = 0
$$

so the d-axis PI controller drives [Id](Id.md) toward zero. A non-zero `IdRef` (for field weakening) is not produced by the current firmware. For brush and stepper motors the d axis is unused and `IdRef` is 0. Contact Agito if an application involving a non-zero `IdRef` (for example flux weakening) is needed.

## Examples

```text
AIdRef              ; read direct-axis current reference (mA)
```

## See also

- [Id](Id.md) — direct-axis feedback current regulated against IdRef
- [IdErr](IdErr.md) — direct-axis current error (IdRef − Id)
- [IqRef](IqRef.md) — quadrature-axis (torque) current reference
