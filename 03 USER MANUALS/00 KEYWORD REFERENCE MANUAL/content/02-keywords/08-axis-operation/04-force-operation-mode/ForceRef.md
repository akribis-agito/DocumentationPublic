---
keyword: ForceRef
summary: Filtered force reference used in the force control loop.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 581
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
    data_type: float32
---
# ForceRef

Filtered force reference used in the force control loop.

## Overview

`ForceRef` is the **filtered** force reference used in the force control loop. It follows the source defined by [ForceCmdSrc](ForceCmdSrc.md) (analog input or the [ForceCmdVal](ForceCmdVal.md) table). The force loop drives the feedback [Force](Force.md) toward this reference, and the difference is reported as [ForceErr](ForceErr.md).

## How it works

The force-command generator first builds a *raw* force reference each cycle from the selected source — the analog input, or the [ForceCmdVal](ForceCmdVal.md) table value (after applying the [ForceCmdSlope](ForceCmdSlope.md) ramp). That raw reference is then passed through a first-order reference filter to produce `ForceRef`, which is the value the loop and [ForceErr](ForceErr.md) use.

This filtering is why the in-target / sequence timing in force mode is keyed to the **unfiltered** (pre-filter) reference: the holding timer and the move/settle measurements start the moment the raw reference reaches the target [ForceCmdVal](ForceCmdVal.md), not when the filtered `ForceRef` catches up. When force mode is not active, `ForceRef` is held equal to the [Force](Force.md) feedback so the switch into force mode is bumpless.

Please refer to [Control tuning – Force control](../../11-control-tuning/07-force-control/00-overview.md) for more information on the filter.

## Examples

```text
AForceRef           ; read the filtered force reference
```

### Edge cases

- **Wrong mode** ([OperationMode](../01-general-keywords/OperationMode.md) ≠ 4) — `ForceRef` is held equal to [Force](Force.md) so the next force-mode entry is bumpless.
- **Motor off** — `ForceRef` tracks `Force`; the loop is not running.
- **Sequence timing vs filter** — in-target / sequence timing is keyed to the **unfiltered** reference; do not compare `ForceRef` directly to [ForceCmdVal](ForceCmdVal.md) for sequence-step decisions.
- **Read-only** — writes are rejected.

## See also

- [ForceCmdSrc](ForceCmdSrc.md) — selects the reference source
- [ForceCmdSlope](ForceCmdSlope.md) — ramp rate of the raw reference toward each table value
- [Force](Force.md) — force feedback the loop tracks
- [ForceErr](ForceErr.md) — ForceRef minus Force
