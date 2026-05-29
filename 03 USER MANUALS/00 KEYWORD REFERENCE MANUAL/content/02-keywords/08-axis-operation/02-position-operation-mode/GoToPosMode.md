---
keyword: GoToPosMode
summary: Command to gracefully enter position operation mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 336
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GoToPosMode

Command to gracefully enter position operation mode.

## Overview

`GoToPosMode` instructs the controller to enter position operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 3) in a graceful, bumpless manner. The position feedback ([Pos](../../10-motion/01-kinematics-status/Pos.md)) at the moment the command is processed is recorded in [ModeSwitchPos](ModeSwitchPos.md) index 2.

`GoToPosMode` can only switch the axis **from current mode (1) or force mode (4)**, because only those modes continuously prepare the variables needed for a clean transition. It is rejected from velocity mode (2) and does nothing if the axis is already in position mode (3). Through the [BeginOnToPos](BeginOnToPos.md) flag the command can also launch a point-to-point move on entry, to a target set by [RetractTarget](RetractTarget.md) (or [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)) at speed [RetractSpeed](RetractSpeed.md). For the other ways to reach position mode (direct [OperationMode](../01-general-keywords/OperationMode.md) assignment, the internal condition check via [PosPosFlag](PosPosFlag.md)/[PosPosTh](PosPosTh.md), or a [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) digital input), see [OperationMode](../01-general-keywords/OperationMode.md).

## How it works

`GoToPosMode` is a function keyword. When commanded, the controller branches on the current [OperationMode](../01-general-keywords/OperationMode.md):

| Source `OperationMode` | Action |
|---|---|
| 1 (current) or 4 (force) | Set `OperationMode = 3` (position); record [ModeSwitchPos](ModeSwitchPos.md)[2] = `Pos`; if [BeginOnToPos](BeginOnToPos.md) = 1, clear it and start the entry move. |
| 2 (velocity) | Rejected with an error (cannot switch to position mode from velocity mode). |
| 3 (position) | No effect (already in position mode). |

### Bumpless transfer

The transition is bumpless because the position reference is kept aligned with the feedback the whole time the axis is in the source mode, so there is no step in position error at the instant of the switch:

- **From current mode** — while in current-only control the position/velocity loops are open and the reference is held tracking the feedback, so on the switch `PosRef ≈ Pos` and position error is ~0.
- **From force mode** — the force loop continuously regenerates the position reference relative to the position captured on force-mode entry (the [ModeSwitchPos](ModeSwitchPos.md)[1] anchor). Because the reference is already where the feedback is, position control resumes without a jump.

The operation mode simply changes, assuming everything was prepared in current (or force) operation mode each cycle. See [PosRef](../../10-motion/01-kinematics-status/PosRef.md) for the reference pipeline.

### Optional entry move

If [BeginOnToPos](BeginOnToPos.md) is armed, `GoToPosMode` starts the same entry move used by the internal switching algorithm and by [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md). See [BeginOnToPos](BeginOnToPos.md) for the move details.

> **Note:** `GoToPosMode` cannot be used while the axis is in velocity operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2).

## Examples

```text
AGoToPosMode         ; gracefully switch to position operation mode
AModeSwitchPos[2]   ; read the position recorded on entry to position mode
```

### Edge cases

- **From velocity mode** — rejected (error 157, "Can't GoToPosMode from Velocity Operation Mode. Only from Current Operation Mode"). The recommended path is to disable the motor, set [OperationMode](../01-general-keywords/OperationMode.md) = 3, then re-enable.
- **Already in position mode** — no-op; returns OK.
- **Motor off** — accepted; the mode flag changes but no power is applied until `MotorOn = 1`.
- **In motion (current or force)** — the source mode's command sequence stops being applied at the switch; the entry move (if [BeginOnToPos](BeginOnToPos.md) = 1) starts immediately, otherwise the axis holds at `Pos`.
- **CNC / vector member** — not blocked at this entry point; consider stopping the group first to avoid the rest of the group entering an unexpected state.
- **`BeginOnToPos` self-clearing** — when an entry move launches, `BeginOnToPos` is reset to `0`; arm it again for the next entry.
- **Mode-switch position anchor** — [ModeSwitchPos](ModeSwitchPos.md)`[2]` is overwritten on every successful entry; previous values are lost.
- **DInMode parallel** — [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) codes 18 and 22 perform the same transition on edge but only from current/force respectively (and refuse vector/CNC members).

## See also

- [BeginOnToPos](BeginOnToPos.md) — optionally run a move on entry
- [ModeSwitchPos](ModeSwitchPos.md) — positions recorded at mode transitions
- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [PosPosFlag](PosPosFlag.md) / [PosPosTh](PosPosTh.md) — automatic feedback-threshold entry from current/force mode
- [RetractSpeed](RetractSpeed.md) / [RetractTarget](RetractTarget.md) — kinematics of the optional entry move
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback recorded at the transition
