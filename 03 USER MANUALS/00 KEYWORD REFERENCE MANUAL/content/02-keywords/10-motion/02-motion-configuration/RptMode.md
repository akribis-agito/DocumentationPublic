---
keyword: RptMode
summary: Selects whether repetitive point-to-point motion is bidirectional or unidirectional.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 712
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 730
---
# RptMode

Selects whether repetitive point-to-point motion is bidirectional or unidirectional.

## Overview

`RptMode` defines whether repetitive motion is bidirectional (to-and-fro) or unidirectional (stepping ever further away), which is useful for repeated step-motion applications. It is used only when [MotionMode](MotionMode.md) = 2 (repetitive point-to-point motion), and it also determines what one repetition means for the [RptCycles](RptCycles.md) count. It cannot be changed while the axis is in motion.

## How it works

| RptMode | Descriptions |
|---|---|
| 0 | **Bidirectional motion** Axis will move to AbsTrgt (or relative location defined by RelTrgt) and then back to initial location. 1 repetition number equals to 1 motion to AbsTrgt (or relative location defined by RelTrgt), or 1 motion back to initial position This means RptCycles = 2 equals to one set of to-and-fro motion. |
| 1 | **Unidirectional motion** Axis will always move at the position delta of (AbsTrgt – initial position) or RelTrgt, where axis will move further and further away. 1 repetition number equals 1 delta motion. |

### How the return target is computed

When the move begins, the firmware records the starting reference and sets up the *next* target, `glAbsTrgtRepetitive`, according to `RptMode` (`AG300_CTL01Funcs.c:1122`–`1129`, and re-applied each dwell at `AG300_CTL01Profiler.c:930`–`937`):

| RptMode | Next target each repetition |
|---|---|
| 0 (bidirectional) | `AbsTrgtRepetitive = PosRef_at_begin` — the move goes out to `AbsTrgt`, then the next move targets the original start, alternating out/back forever. |
| 1 (unidirectional) | `AbsTrgtRepetitive = AbsTrgt + (AbsTrgt − PosRef_at_begin)` — each repetition advances by the same delta, so the axis keeps stepping the same distance in one direction. |

If [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) ≠ 0 the absolute target is first derived as `AbsTrgt = PosRef + RelTrgt` (`AG300_CTL01Funcs.c:1117`). At `Begin` both `AbsTrgt` and the computed `AbsTrgtRepetitive` are range-checked against the software position limits [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md), so for unidirectional mode the *first* repetition's target must already lie inside the limits (`AG300_CTL01Funcs.c:1132`).

## Examples

```text
ARptMode=0           ; bidirectional (to-and-fro)
ARptMode=1           ; unidirectional (stepping away)
ARptMode            ; query current value
```

## See also

- [MotionMode](MotionMode.md) — must be 2 for `RptMode` to apply
- [RptCycles](RptCycles.md) — number of repetitions (one leg vs one step depends on `RptMode`)
- [RptWait](RptWait.md) — dwell time between repetitions
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) / [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — define the per-repetition target
- [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) / [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) — targets are range-checked at `Begin`
