---
keyword: PosPosTh
summary: Position-feedback threshold used with PosPosFlag to enter position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 329
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
# PosPosTh

Position-feedback threshold used with PosPosFlag to enter position mode.

## Overview

`PosPosTh` is the position-feedback threshold, in user units, compared against [Pos](../../10-motion/01-kinematics-status/Pos.md) by the condition check that switches the axis into position operation mode. It is used together with [PosPosFlag](PosPosFlag.md), which arms the check and selects the comparison direction, and only while the axis is in current or force operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1 or 4). `PosPosTh` itself is a persistent setting (it is not cleared when the switch fires; only [PosPosFlag](PosPosFlag.md) is).

## How it works

Each control cycle, while commutated and in current/force mode, the firmware compares [Pos](../../10-motion/01-kinematics-status/Pos.md) against `PosPosTh` in the direction chosen by [PosPosFlag](PosPosFlag.md) (`AG300_CTL01ControlLoops.c:958`, `:1125`):

| PosPosFlag | Condition | Result |
|------------|-----------|--------|
| 0          | (none) | Axis stays in the existing current or force mode. |
| 1          | [Pos](../../10-motion/01-kinematics-status/Pos.md) &lt; `PosPosTh` | Switch to position mode. |
| 2          | [Pos](../../10-motion/01-kinematics-status/Pos.md) &gt; `PosPosTh` | Switch to position mode. |

When the condition is met the controller switches to position mode, clears [PosPosFlag](PosPosFlag.md), records [ModeSwitchPos](ModeSwitchPos.md)[2], and runs the optional [BeginOnToPos](BeginOnToPos.md) entry move. See [PosPosFlag](PosPosFlag.md) for the full switching sequence.

## Changes between versions

In **v5 (central-i)** the position pipeline is 64-bit, so `PosPosTh` is a 64-bit value with the larger range shown in the frontmatter; the comparison logic is unchanged. **v5 is central-i only**, so on standalone `PosPosTh` remains the v4 32-bit value.

## Examples

```text
APosPosTh=100000     ; position threshold (user units)
APosPosFlag=1        ; switch when Pos < PosPosTh
```

## See also

- [PosPosFlag](PosPosFlag.md) — arms the check and selects the comparison direction
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — the feedback compared against this threshold
- [Current operation mode](../03-current-operation-mode/00-overview.md) — switching from current mode
- [Force operation mode](../04-force-operation-mode/00-overview.md) — switching from force mode
