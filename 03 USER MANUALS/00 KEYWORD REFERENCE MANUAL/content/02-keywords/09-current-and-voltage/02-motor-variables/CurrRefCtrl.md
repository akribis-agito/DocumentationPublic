---
summary: Read-only loop-side current reference, taken before the decoupling matrix, injection and compensation.
keyword: CurrRefCtrl
availability:
- controller
- ci-master
can_code: 717
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
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
last_updated: '2026-05-27'
doc_revision: '2026.06'
---
# CurrRefCtrl

Read-only loop-side current reference, taken before the decoupling matrix, injection and compensation.

## Overview

`CurrRefCtrl` is the loop's current reference (as distinct from the motor's current reference [CurrRef](CurrRef.md)). It is the value just before the decoupling matrix, current injection and current-related compensation. Its meaning depends on the operation mode:

- **Position, velocity and force operation mode:** `CurrRefCtrl` is the sum of the current reference from the feedback loop, the feedforwards and the loop compensation.
- **Current operation mode:** `CurrRefCtrl` is the current reference from the source defined by [CurrCmdSrc](../../08-axis-operation/03-current-operation-mode/CurrCmdSrc.md) (analog input, [CurrCmdVal](../../08-axis-operation/03-current-operation-mode/CurrCmdVal.md) array, etc.).

See [Control tuning – Velocity control](../../11-control-tuning/04-velocity-control/00-overview.md), [Control tuning – Feedforwards](../../11-control-tuning/05-feedforwards/00-overview.md) and [Control tuning – Force control](../../11-control-tuning/07-force-control/00-overview.md) for where `CurrRefCtrl` sits in the signal path.

## How it works

`CurrRefCtrl` reports the current reference on the loop side, before the decoupling matrix, current injection and current-related compensation are applied. The compensated and injected result, after current limiting and the [CurrDir](CurrDir.md) sign correction, becomes the final motor current command [CurrRef](CurrRef.md). On the motor side that command becomes the q-axis reference [IqRef](IqRef.md) for three-phase motors or the phase-A reference [IaRef](IaRef.md) for brush motors. `CurrRefCtrl` is reported only on central-i (v5).

## Examples

```text
ACurrRefCtrl        ; read the loop-side current reference
```

## See also

- [CurrRef](CurrRef.md) — final motor current command after decoupling/compensation
- [CurrCmdSrc](../../08-axis-operation/03-current-operation-mode/CurrCmdSrc.md) — current-command source in current operation mode
- [IqRef](IqRef.md), [IaRef](IaRef.md) — references derived from CurrRefCtrl after direction correction
