---
keyword: IdRef
summary: Read-only direct-axis current reference, used in dq0-domain control; currently always 0.
availability:
- controller
- ci-master
can_code: 29
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -16000
  - 16000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000
    - 64000
  agc300-et:
    range:
    - -4000
    - 4000
  agc301-et:
    range:
    - -4000
    - 4000
  agc301-et-bioxtreme:
    range:
    - -4000
    - 4000
  agd200-et-2d01:
    range:
    - -4000
    - 4000
  agd200-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d01:
    range:
    - -4000
    - 4000
  agd301-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d09:
    range:
    - -25500
    - 25500
  agd155-af-2a06:
    range:
    - -25500
    - 25500
  agd155-af-2a10:
    range:
    - -28500
    - 28500
  agd155-ec:
    range:
    - -25500
    - 25500
  agd155-ec-var34:
    range:
    - -28500
    - 28500
  agd155-ec-var34-3:
    range:
    - -42500
    - 42500
  agd156-ec:
    range:
    - -12726
    - 12726
  agd101-ec-34a:
    range:
    - -28280
    - 28280
  agd101-ec-17a:
    range:
    - -14140
    - 14140
last_updated: '2026-05-29'
doc_revision: '2026.06'
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
