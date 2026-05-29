---
keyword: GoToForceMode
summary: Command to gracefully enter force operation mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 575
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
# GoToForceMode

Command to gracefully enter force operation mode.

## Overview

`GoToForceMode` instructs the controller to enter force operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 4) in a graceful manner. Unlike a direct `OperationMode = 4` assignment, the command runs a controlled hand-off so the actuator does not jump when the loop switches over. For other ways to enter force mode (direct assignment, automatic condition, or digital input), see [Force operation mode](00-overview.md).

> **Note:** `GoToForceMode` does nothing if the axis is already in force mode, and it is **rejected** while the axis is in current operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1) or while it is a member of a CNC (multi-axis) motion group.

## How it works

When accepted, the command performs the following hand-off:

1. **Ends any active motion** (reported as [MotionReason](../../10-motion/05-motion-status/MotionReason.md) = 17, motion ended due to GoToForceMode command) and stores the move profiler time, so the axis is no longer in motion when the force loop takes over.
2. **Resets the command-sequence state** — [ForceCmdIndex](ForceCmdIndex.md) is set to `1` (first table entry) and [ForceCmdCntr](ForceCmdCntr.md) is cleared to `0`.
3. **Seeds the force-loop integrator** from the present current reference so the commanded current is continuous across the switch and the motor does not jump.
4. **Switches [OperationMode](../01-general-keywords/OperationMode.md) to force control** and records the switch position.

Because the command resets [ForceCmdIndex](ForceCmdIndex.md) and [ForceCmdCntr](ForceCmdCntr.md), the force-command sequence always restarts from the first [ForceCmdVal](ForceCmdVal.md) entry. (A direct `OperationMode = 4` assignment does **not** reset them, so it can resume from a preset entry.)

## Examples

```text
AGoToForceMode       ; gracefully switch to force operation mode
```

### Edge cases

- **From current mode** — rejected with `CANT_GO_TO_FORCE_FROM_CURR`. Pass through position mode first (e.g. via [GoToPosMode](../02-position-operation-mode/GoToPosMode.md)) before calling `GoToForceMode`.
- **Already in force mode** — no-op; returns OK.
- **CNC member** (`CNCA_MEMBER` or `CNCB_MEMBER`) — rejected with `CANT_GO_TO_CURRENT_OR_FORCE_WHEN_CNC`.
- **Vector member** — not blocked here (only the [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) code 22 dispatch refuses vector members).
- **From velocity mode** — accepted; force loop seeding works the same way (`CurrRef` is in a defined state).
- **From position mode** — accepted (the common case); the in-motion check is honoured.
- **Motor off** — accepted; the mode flag changes but no power is applied until `MotorOn = 1`.
- **PIV mode** ([ForcePIVOn](ForcePIVOn.md) = 1) — the force integrator is seeded to `0` rather than from `CurrRef`; the PIV structure does its own integral handling.
- **Tables intact** — `ForceCmdVal` / `ForceCmdSlope` / `ForceCmdHTime` are not cleared; the dispatcher always restarts from `ForceCmdIndex = 1`.
- **Direct assignment vs `GoToForceMode`** — writing [OperationMode](../01-general-keywords/OperationMode.md) = `4` does **not** reset `ForceCmdIndex` / `ForceCmdCntr`; it can resume an in-progress sequence. `GoToForceMode` always restarts from entry 1.
- **Atomic** — the firmware disables interrupts around the integrator seed and mode flip so the change is visible to all loops in a single control cycle.

## See also

- [OperationMode](../01-general-keywords/OperationMode.md) — the active control mode
- [ForceCmdSrc](ForceCmdSrc.md) — source of the force reference once in mode
- [ForceCmdIndex](ForceCmdIndex.md) / [ForceCmdCntr](ForceCmdCntr.md) — sequence state this command resets
- [Force operation mode](00-overview.md) — overview of force-mode behavior
