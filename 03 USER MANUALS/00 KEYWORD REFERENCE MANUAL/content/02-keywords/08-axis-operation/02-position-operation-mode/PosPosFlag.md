---
keyword: PosPosFlag
summary: Trigger direction for the position-feedback check to enter position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 328
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosPosFlag

Trigger direction for the position-feedback check to enter position mode.

## Overview

`PosPosFlag` arms and selects the direction of the position-feedback condition check that automatically switches the axis into position operation mode. It works only while the axis is in current or force operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1 or 4) and only after commutation is complete, together with the threshold [PosPosTh](PosPosTh.md). When the condition is met the controller switches to position mode and clears `PosPosFlag` to 0, so it must be re-armed for the next switch.

## How it works

Each control cycle, while the axis is commutated and in current or force mode, the firmware evaluates (`AG300_CTL01ControlLoops.c:958` for current mode, `:1125` for force mode):

| PosPosFlag | Condition checked | Result |
|---|---|---|
| 0 | (none) | Axis stays in the existing current or force mode. |
| 1 | [Pos](../../10-motion/01-kinematics-status/Pos.md) &lt; [PosPosTh](PosPosTh.md) | Switch to position mode. |
| 2 | [Pos](../../10-motion/01-kinematics-status/Pos.md) &gt; [PosPosTh](PosPosTh.md) | Switch to position mode. |

When the condition fires, the firmware in the same cycle:

1. sets `OperationMode = 3` (position);
2. clears `PosPosFlag = 0` (one-shot — re-arm for the next switch);
3. latches [ModeSwitchPos](ModeSwitchPos.md)[2] = `Pos`;
4. if [BeginOnToPos](BeginOnToPos.md) is set, clears it and launches the entry move ([RetractTarget](RetractTarget.md)/[RetractSpeed](RetractSpeed.md)).

No special preparation is needed at the switch because, in current and force mode, the position reference is continuously held aligned with the feedback, so the transition is bumpless (see [GoToPosMode](GoToPosMode.md)). This feedback-threshold check is the **only** condition-based entry into position mode; position mode is also entered automatically when a scheduled current/force command table reaches its end (see [Current operation mode](../03-current-operation-mode/00-overview.md) / [Force operation mode](../04-force-operation-mode/00-overview.md)).

## Examples

```text
APosPosTh=100000     ; position threshold (user units)
APosPosFlag=2        ; switch to position mode when Pos > PosPosTh
```

## See also

- [PosPosTh](PosPosTh.md) — position threshold compared against Pos
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — the feedback compared against the threshold
- [BeginOnToPos](BeginOnToPos.md) — optional entry move on the resulting switch
- [Current operation mode](../03-current-operation-mode/00-overview.md) — switching from current mode
- [Force operation mode](../04-force-operation-mode/00-overview.md) — switching from force mode
