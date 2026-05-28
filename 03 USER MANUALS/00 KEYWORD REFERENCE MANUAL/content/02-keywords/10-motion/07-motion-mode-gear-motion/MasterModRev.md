---
keyword: MasterModRev
summary: Modulo divisor that corrects MasterPos accumulation when the master variable wraps.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 519
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MasterModRev

Modulo divisor that corrects MasterPos accumulation when the master variable wraps.

## Overview

`MasterModRev` is the modulo divisor used to ensure correct accumulation of [MasterPos](MasterPos.md) when the variable selected by [GearMaster](GearMaster.md) participates in a modulo operation. The master variable undergoes a modulo operation when:

1. the `ModRev` related to the master variable is non-zero, and
2. it is generally either [Pos](../01-kinematics-status/Pos.md), PDPos, [MasterPos](MasterPos.md), [PosRef](../01-kinematics-status/PosRef.md) or [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md).

You must set `MasterModRev` to match the [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) of the master variable (manual assignment — the firmware does not copy it for you). If the master variable does not involve a modulo operation, `MasterModRev` must be `0`. This parallels `ModRev` on the follower's own [Pos](../01-kinematics-status/Pos.md), but applies to the *master* side of the gear.

## How it works

### Why it is needed

[MasterPos](MasterPos.md) accumulates the *change* of the master each cycle. If the master is a continuous-rotation variable that wraps at its modulo boundary, one wrap produces an apparent change of nearly a full `ModRev` in a single cycle — a huge false change that would jolt the follower. `MasterModRev` tells the accumulator the size of that boundary so it can recognise and unwrap the jump.

### The correction

Each cycle, if `MasterModRev ≠ 0`, the change is compared against half the boundary:

- a change greater than `+MasterModRev/2` is treated as a forward wrap and `MasterModRev` is subtracted;
- a change less than `−MasterModRev/2` is treated as a backward wrap and `MasterModRev` is added.

A change larger than half a revolution is therefore interpreted as a wrap in the opposite direction and unwrapped, so `MasterPos` stays continuous across the master's modulo boundary. This assumes the master moves no more than half its `ModRev` per controller cycle — the same assumption the follower's own modulo handling makes.

## Examples

```text
AMasterModRev=0          ; master variable has no modulo operation (default)
AMasterModRev=3600000    ; match the master's ModRev (e.g. a rotary master)
AMasterModRev            ; read current value
```

## Changes between versions

In **v5 (central-i)** `MasterModRev` is a 64-bit value. The wrap-correction logic is the same. **v5 is central-i only.**

## See also

- [MasterPos](MasterPos.md) — accumulated, scaled master position this divisor protects
- [GearMaster](GearMaster.md) — selects the master variable
- [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) — the master variable's own modulo, which `MasterModRev` must match
