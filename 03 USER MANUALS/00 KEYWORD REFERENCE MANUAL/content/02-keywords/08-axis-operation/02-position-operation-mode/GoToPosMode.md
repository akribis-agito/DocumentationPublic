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

`GoToPosMode` is a function keyword. When commanded, the controller branches on the current [OperationMode](../01-general-keywords/OperationMode.md) (`GoToPosMode()`, `AG300_CTL01Funcs.c:17888`):

| Source `OperationMode` | Action |
|---|---|
| 1 (current) or 4 (force) | Set `OperationMode = 3` (position); record [ModeSwitchPos](ModeSwitchPos.md)[2] = `Pos`; if [BeginOnToPos](BeginOnToPos.md) = 1, clear it and start the entry move. |
| 2 (velocity) | Rejected with error (`CANT_GO_TO_POS_FROM_VEL`). |
| 3 (position) | No effect (already in position mode). |

### Bumpless transfer

The transition is bumpless because the position reference is kept aligned with the feedback the whole time the axis is in the source mode, so there is no step in position error at the instant of the switch:

- **From current mode** — while in current-only control the position/velocity loops are open and the reference is held tracking the feedback, so on the switch `PosRef ≈ Pos` and position error is ~0.
- **From force mode** — the force loop continuously regenerates the position reference relative to the position captured on force-mode entry: `gllFinalPosRef = (force-PID output × SAMPLE_TIME) + gllModeSwitchPos[axis][1]` (`AG300_CTL01ControlLoops.c:2339`). Because the reference is already where the feedback is, position control resumes without a jump.

The firmware comment makes this explicit: *"just change to operation mode, assuming everything was prepared at the Current (or Force) Operation Mode, each sample."* See [PosRef](../../10-motion/01-kinematics-status/PosRef.md) for the reference pipeline.

### Optional entry move

If [BeginOnToPos](BeginOnToPos.md) is armed, `GoToPosMode` calls the shared routine `QuickBeginOnSwitchToPos()` (`AG300_CTL01ControlLoops.c:2364`) — the same routine used by the internal switching algorithm and by [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md). See [BeginOnToPos](BeginOnToPos.md) for the move details.

> **Note:** `GoToPosMode` cannot be used while the axis is in velocity operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 2).

## Examples

```text
AGoToPosMode         ; gracefully switch to position operation mode
AModeSwitchPos[2]   ; read the position recorded on entry to position mode
```

## See also

- [BeginOnToPos](BeginOnToPos.md) — optionally run a move on entry
- [ModeSwitchPos](ModeSwitchPos.md) — positions recorded at mode transitions
- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [PosPosFlag](PosPosFlag.md) / [PosPosTh](PosPosTh.md) — automatic feedback-threshold entry from current/force mode
- [RetractSpeed](RetractSpeed.md) / [RetractTarget](RetractTarget.md) — kinematics of the optional entry move
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback recorded at the transition
