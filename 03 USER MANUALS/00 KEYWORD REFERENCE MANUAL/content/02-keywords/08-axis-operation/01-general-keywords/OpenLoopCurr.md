---
keyword: OpenLoopCurr
summary: Current reference applied to the current loop in current open-loop mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 145
attributes:
  access: rw
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
# OpenLoopCurr

Current reference applied to the current loop in current open-loop mode.

## Overview

`OpenLoopCurr` is the current reference, in milliamperes, applied onto the current loop while the axis is in the current open-loop condition. It is only used when [OpenLoopOn](OpenLoopOn.md) = 1.

This value bypasses all current references contributed by position, velocity or force control, except for cogging compensation ([UPMVelTable](../../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)) and DC offset ([CurrRefOffset](../../../02-keywords/09-current-and-voltage/03-current-compensation/CurrRefOffset.md)). It is applied on a per-individual-motor basis, which means the decoupling matrix is not used (for example, excitation is not applied across a gantry axis).

## How it works

While [OpenLoopOn](OpenLoopOn.md) = 1 and the motor is on, the control loop uses this value as the current reference each cycle, then adds anti-cogging. The closed current loop then regulates the motor phase currents to this reference, so the motor produces a (roughly) constant force/torque set directly by the value — useful for commissioning, friction and force checks, and verifying current direction.

The magnitude is in milliamperes. The allowed range tracks the drive's full-scale current command (±full-scale current command), shown as ±64000 mA in the frontmatter for the largest full scale; smaller drives clamp to their own full scale.

The value is **forced to 0** whenever `OpenLoopOn ≠ 1` or the motor is disabled, so there is no residual current command when you leave the mode.

## Examples

```text
AOpenLoopOn=1        ; enter current open loop
AOpenLoopCurr=1000   ; apply a 1000 mA current reference
```

### Edge cases

- **Wrong mode** ([OpenLoopOn](OpenLoopOn.md) ≠ 1) — the value is **forced to `0` every cycle**; the current loop does not use it.
- **Motor off** — the value is forced to `0` every motor-off cycle, so re-enabling the motor never finds a residual command.
- **In motion at write** — rejected (`NOMOTN`). The keyword may be changed while the motor is on (since the open-loop mode itself requires the motor to engage afterwards), but not while a motion profile is running.
- **Out of range** — values outside the drive's ±full-scale current command are rejected by the parameter table.
- **Gantry** — the value is applied per-motor without the decoupling matrix; in a gantry the same value drives both members directly, with no common/differential split.
- **UPM/cogging compensation** — added on top of `OpenLoopCurr` even in open-loop, so the commanded current per-cycle may not match `OpenLoopCurr` exactly when [UPMVelTable](../../09-current-and-voltage/03-current-compensation/UPMVelTable.md) is non-zero.
- **DC offset** — [CurrRefOffset](../../09-current-and-voltage/03-current-compensation/CurrRefOffset.md) is still applied; subtract it from `OpenLoopCurr` if you want the raw value to drive the loop.
- **Save** — not flash-saveable; restarts at `0` after reset.
- **Platform** — v5 stores as `float32` (fractional mA); v4 stores as `int32`.

## Changes between versions

In **v5 (central-i)** `OpenLoopCurr` is stored as a 32-bit float rather than the v4 integer, so a fractional milliampere reference can be commanded; the range and behaviour are otherwise unchanged. **v5 is central-i only** — on the standalone product `OpenLoopCurr` remains the v4 integer value.

## See also

- [OpenLoopOn](OpenLoopOn.md) — selects the open-loop point (1 = current open loop)
- [OpenLoopVolt](OpenLoopVolt.md) — voltage amplitude for voltage open loop
- [MotorOn](MotorOn.md) — must be on for the reference to drive; disabling forces it to 0
