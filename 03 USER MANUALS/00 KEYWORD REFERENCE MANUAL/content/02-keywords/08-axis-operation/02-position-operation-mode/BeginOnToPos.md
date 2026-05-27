---
keyword: BeginOnToPos
summary: One-time flag to run a point-to-point move on entering position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 587
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BeginOnToPos

One-time flag to run a point-to-point move on entering position mode.

## Overview

`BeginOnToPos` is a one-time (auto-clearing) flag which, if set to 1, instructs the controller to launch a point-to-point motion at the moment the axis enters position operation mode. The target position is defined by [RetractTarget](RetractTarget.md) (or [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)) and the maximum velocity by [RetractSpeed](RetractSpeed.md). As soon as the move is armed and triggered, the flag is reset to 0, so it must be set again for the next entry.

The flag is honoured only on the transitions that prepare a clean entry into position mode: the [GoToPosMode](GoToPosMode.md) command, the internal feedback-threshold switch ([PosPosFlag](PosPosFlag.md)/[PosPosTh](PosPosTh.md) and the scheduled-table end), and a [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) position/current or position/force input. It has **no effect** when [OperationMode](../01-general-keywords/OperationMode.md) is changed by direct assignment.

## How it works

Every path that switches the axis into position mode checks `glBeginOnToPos`; if it is non-zero the firmware clears it and calls the shared routine `QuickBeginOnSwitchToPos()` (`AG300_CTL01ControlLoops.c:2364`). The call sites are:

| Entry path | Firmware site |
|---|---|
| `GoToPosMode` command | `AG300_CTL01Funcs.c:17908` |
| Internal switch from current mode | `AG300_CTL01ControlLoops.c:1109` |
| Internal switch from force mode | `AG300_CTL01ControlLoops.c:1424` |
| `DInMode` position/current input (rising edge) | `AG300_CTL01ControlInterrupt.c:9066` |
| `DInMode` position/force input (rising edge) | `AG300_CTL01ControlInterrupt.c:9158` |

### The entry move

`QuickBeginOnSwitchToPos()` sets up and starts a standard point-to-point move:

1. **Target** — if [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) ≠ 0, the absolute target is `gllFinalPosRef + RelTrgt` (relative to the reference at entry); otherwise it is the absolute [RetractTarget](RetractTarget.md). The result is written to the PTP target `gllAbsTrgt`.
2. **Speed** — the move speed `gllSpeed` is set to [RetractSpeed](RetractSpeed.md).
3. **Start** — if a conditional-start input is armed (`glBeginDInOn` ≠ 0) the motion is flagged `IN_MOTION | IN_WAIT_FOR_INPUT` and actually begins on the input's rising edge; otherwise it starts immediately. Acceleration/deceleration and jerk come from the axis' normal PTP profile settings; the friction-compensation flag is set and the motion-samples counter is reset.

Because this is an ordinary PTP move, it obeys the software position limits ([FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)) like any other motion.

## Examples

```text
ARetractTarget=50000 ; absolute target for the entry move
ARetractSpeed=20000  ; speed for the entry move
ABeginOnToPos=1      ; arm the entry move (auto-clears after it starts)
AGoToPosMode         ; switch to position mode and start the move
```

Relative entry move (target relative to the reference at entry):

```text
ARelTrgt=10000       ; +10000 user units from the entry reference
ARetractSpeed=20000  ; speed for the entry move
ABeginOnToPos=1      ; arm the entry move
AGoToPosMode         ; switch and start the relative move
```

## See also

- [GoToPosMode](GoToPosMode.md) — command that triggers the armed move
- [RetractTarget](RetractTarget.md) — absolute target of the entry move
- [RetractSpeed](RetractSpeed.md) — speed of the entry move
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) — relative-target override
- [PosPosFlag](PosPosFlag.md) / [PosPosTh](PosPosTh.md) — internal threshold entry that also honours the flag
- [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) — digital-input mode switching that also honours the flag
