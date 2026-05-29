---
keyword: GearMaster
summary: Complex CAN code selecting the master variable for gear motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 489
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GearMaster

Complex CAN code selecting the master variable for gear motion.

## Overview

`GearMaster` selects which variable the axis follows in gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5` direct or `= 6` indirect). It is not a fixed enumeration but a [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) — the encoded reference of *any* keyword, including its axis letter and array index — so the master can be another axis's position, an encoder, a counter, an analog input, and so on. Each controller cycle the controller reads that variable, scales its change by [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md), and accumulates the result into [MasterPos](MasterPos.md), which drives the follower's reference [PosRef](../01-kinematics-status/PosRef.md).

## How it works

### Resolution of the master variable

`GearMaster` is resolved once, when the value is set: the complex CAN code identifies the master variable (its keyword, axis and array index). The controller then reads that variable every cycle without re-resolving the code. It also captures the variable's current value as the "previous" value, so the first cycle produces a zero change.

![Gear-motion signal path from GearMaster to PosRef](gear-signal-path.svg)

### A separate "direct slave" motion mode also exists

`GearMaster`, `MasterFact`/`MasterFactDen`, `MasterFilt` and `MasterPos` all belong to gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5` and `= 6`). The controller also implements a separate, narrower motion mode — direct slave ([MotionMode](../02-motion-configuration/MotionMode.md) `= 10`, see [MotionMode10](MotionMode10.md)) — that builds a follower reference from another axis's reference directly, without going through `GearMaster`, `MasterPos` or `MasterFilt`. It is not the same mechanism as gear motion and does not use this keyword.

### Relationship to the other gearing keywords

- The scaled, accumulated master change is reported by [MasterPos](MasterPos.md).
- If the selected master variable itself wraps (its `ModRev` is non-zero — e.g. a rotary [Pos](../01-kinematics-status/Pos.md) or another axis's [PosRef](../01-kinematics-status/PosRef.md)), you must set [MasterModRev](MasterModRev.md) to that wrap so the accumulation stays continuous.

`GearMaster` can be changed while the motor is on but **not** while the axis is in motion: change the master selection only while the axis is not in gear motion.

## Examples

```text
AGearMaster=...      ; set to the complex CAN code of the desired master variable
AGearMaster          ; read the current master complex CAN code
```

The value is a complex CAN code; build it with the [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) rules for the keyword, axis and index you want to follow.

### Walk-through: run electronic gearing on a master encoder

Configure axis A as a 1:1 follower of a master variable using direct gear motion. The example below uses unity numerator and pass-through filter, but any ratio and any filter coefficient is valid; non-unity ratios use `MasterFact` alone on v4, or `MasterFact / MasterFactDen` on v5 (central-i). Both axes are assumed motor-on but not in motion; encode the master selection per the [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) rules.

```text
; --- 1) Select the master variable on the follower (axis A) ---
AGearMaster[1]=...   ; complex CAN code identifying the master variable

; --- 2) Set the gear ratio numerator (and denominator on v5) ---
AMasterFact[1]=65536    ; 65536 = unity numerator (1:1)
AMasterFactDen[1]=65536 ; v5 (central-i) only -- exact rational denominator, default 65536
AMasterFilt[1]=64       ; 64 = pass-through (no smoothing); lower for more smoothing

; --- 3) (Optional) Tell the controller the master wraps, if it does ---
AMasterModRev[1]=0      ; set to the master's wrap value if the master variable wraps

; --- 4) Arm direct gear motion ---
AMotionMode[1]=5        ; 5 = direct gear, 6 = indirect gear
ABegin                  ; latches MasterPos at start; follower now tracks the master delta

; --- 5) Observe the follower while the master moves ---
AMasterPos[1]           ; scaled, accumulated master position since Begin
APosRef[1]              ; follower reference -- should mirror filtered MasterPos
```

The follower exits gear motion on `Stop`, `Abort`, or when the motor is disabled. To change the master selection, leave gear motion first; `GearMaster` is rejected while the axis is in motion.

## See also

- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) — gear ratio numerator / denominator
- [MasterFilt](MasterFilt.md) — low-pass filter on the geared reference (direct mode)
- [MasterModRev](MasterModRev.md) — modulo divisor for the master variable
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects gear motion (`= 5` or `6`)
- [MotionMode10](MotionMode10.md) — separate direct-slave motion mode (`MotionMode = 10`) that does not use `GearMaster`
- [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) — how the master is encoded
