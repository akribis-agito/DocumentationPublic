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

**Special case (selected automatically):** when the follower is geared 1:1 (on v5/central-i, [MasterFact](MasterFact.md) and [MasterFactDen](MasterFactDen.md) reduce to unity; on v4, [MasterFact](MasterFact.md) `= 65536`), with no filter ([MasterFilt](MasterFilt.md) `= 64`), in direct gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5`), and `GearMaster` points to another axis's [PosRef](../01-kinematics-status/PosRef.md), the controller follows that axis's full-resolution (sub-count) position reference directly rather than re-reading it at count resolution. This makes a 1:1 unfiltered `PosRef`-follower exact, with no per-count quantization. Any other master variable, a non-unity ratio, or any filtering reverts to the standard count-resolution accumulation through [MasterPos](MasterPos.md).

## How it works

### Resolution of the master variable

When `GearMaster` is written, the complex CAN code identifies the master variable (its keyword, axis and array index) and the controller resolves a pointer to it. The controller then reads that variable every cycle without re-resolving the code. It also captures the variable's current value as the "previous" value, so the first cycle produces a zero change.

The master pointer is (re-)resolved and the master's current value is (re-)captured as the "previous" value whenever [GearMaster](GearMaster.md), [MasterFact](MasterFact.md), [MasterFilt](MasterFilt.md) or [MotionMode](../02-motion-configuration/MotionMode.md) is written (and, on v5/central-i, [MasterFactDen](MasterFactDen.md)) — not only when `GearMaster` itself is set. Because the previous value is refreshed at each of these writes, changing the ratio or filter while configuring the axis does not inject a spurious one-cycle jump into [MasterPos](MasterPos.md).

A `GearMaster` write is validated before it is accepted, and a rejected write leaves the previous master selection in force. The write is rejected with a distinct instruction error if:

- the CAN code is out of range,
- the axis letter is out of range,
- the array index is wrong for the target keyword (an index is supplied for a non-array keyword, or omitted for an array keyword — array keywords require an index of 1 or higher), or
- the target is not a parameter (for example, it names a function rather than a settable keyword).

![Gear-motion signal path from GearMaster to PosRef](gear-signal-path.svg)

### A separate "direct slave" motion mode also exists

`GearMaster`, `MasterFact`/`MasterFactDen`, `MasterFilt` and `MasterPos` all belong to gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5` and `= 6`). The controller also implements a separate, narrower motion mode — direct slave ([MotionMode](../02-motion-configuration/MotionMode.md) `= 10`, see [MotionMode10](MotionMode10.md)) — that builds a follower reference from another axis's reference directly, without going through `GearMaster`, `MasterPos` or `MasterFilt`. It is not the same mechanism as gear motion and does not use this keyword.

### Relationship to the other gearing keywords

- The scaled, accumulated master change is reported by [MasterPos](MasterPos.md).
- If the selected master variable itself wraps (its `ModRev` is non-zero — e.g. a rotary [Pos](../01-kinematics-status/Pos.md) or another axis's [PosRef](../01-kinematics-status/PosRef.md)), you must set [MasterModRev](MasterModRev.md) to that wrap so the accumulation stays continuous.

### Trajectory math (v5/central-i)

On v5 (central-i) the per-cycle accumulation into [MasterPos](MasterPos.md) is exact and drift-free. Each cycle the master change Δ (the difference between the current master value and the captured previous value) is divided by [MasterFactDen](MasterFactDen.md) into an integer quotient and a remainder. The integer part advances the fixed-point accumulator by quotient × [MasterFact](MasterFact.md); the remainder is added to a carried fractional accumulator that is kept below [MasterFactDen](MasterFactDen.md), with any whole multiples that emerge folded back into the integer accumulator. Because the surviving fraction is always carried forward rather than rounded away, there is no cumulative rounding drift, and [MasterPos](MasterPos.md) equals the integer accumulation plus the carried fraction × [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md). The ratio is reduced to lowest terms with a positive denominator before this is applied (see [MasterFactDen](MasterFactDen.md)).

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
