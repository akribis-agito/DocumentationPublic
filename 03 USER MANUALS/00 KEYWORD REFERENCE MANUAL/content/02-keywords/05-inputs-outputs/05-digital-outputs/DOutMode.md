---
keyword: DOutMode
summary: Maps a controller status onto each digital output (software function assignment).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 210
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 17
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 65557
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutMode

Maps a controller status onto each digital output (software function assignment).

## Overview

`DOutMode` assigns a software function to a digital output so the output reflects a selected controller status. It applies only when [DOutSelect](DOutSelect.md) for that output is `0` (software control). The array **index** is the output number (1-based: `DOutMode[1]` is output 1).

## How it works

`DOutMode` packs two fields into one 32-bit value:

- the **lower 16 bits** select the *function* — the status the output should follow;
- the **upper 16 bits** select the *source axis* whose status is read (A = 0, B = 1, …; `0` also means "this axis / not axis-related", kept for backward compatibility). A source-axis number that exceeds the number of axes is rejected with a warning and the entry is ignored.

Writing `DOutMode` does not act on it directly each cycle. Instead a compact **functionality table** is rebuilt: every output whose lower-16-bit function is non-zero is recorded with a target `DOutPort` bit (a set-mask and its complement clear-mask), the function code, and the source axis. The new table is swapped in atomically so a half-built table is never used. There is a hard limit of **18 active output functions** at once; beyond that the extra entries are dropped and a warning is logged.

This table is then walked and each function applied, spread across three consecutive control cycles (about six functions per cycle) to bound the per-cycle cost. For each entry the selected status is evaluated and the output's [DOutPort](DOutPort.md) bit is either **set** (status true) or **cleared** (status false). Because the function drives `DOutPort`, [DOutLog](DOutLog.md) polarity and [DOutType](DOutType.md) sink/source routing still apply on top, exactly as for a manual output. This also means a `DOutMode`-driven output overwrites any value you write to that `DOutPort` bit by hand.

The function code maps to a controller status as follows:

| Value | Function | Status source (set when…) |
|-------|----------|---------------------------|
| 0 | General output – no function | output follows [DOutPort](DOutPort.md) |
| 1 | Reserved (dedicated hardware function placeholder) | — |
| 2 | Motor-on status | motor is enabled |
| 3 | In-motion status | [MotionStat](../../10-motion/05-motion-status/MotionStat.md) ≠ 0 |
| 4 | In-acceleration status¹ | `MotionStat` in-acceleration bit set |
| 5 | In-deceleration status¹ | `MotionStat` in-deceleration bit set |
| 6 | In-constant-speed status¹ | in motion and neither accel nor decel bit set |
| 7 | End of motion | not implemented |
| 8 | In-target status | [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md) = target-reached |
| 9 | Fault/alarm status | [ConFlt](../../07-status-and-faults/ConFlt.md) ≠ 0 |
| 10 | Warnings in last motion | not implemented |
| 11 | Current saturation in last motion | not implemented |
| 12 | Limit active | [LimitsStat](../../06-protections/03-motion/position-limit-protection/LimitsStat.md) ≠ 0 |
| 13 | Out-of-travel-range | shaped position reference > [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) or < [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md) |
| 14 | Regeneration active | [RegenUsed](../../09-current-and-voltage/05-regeneration/RegenUsed.md) ≠ 0 **and** [StatReg](../../07-status-and-faults/StatReg.md) bit 1 set (clears when `RegenUsed = 0`) |
| 15 | Dynamic-brake active | `StatReg` dynamic-brake bit set |
| 16 | Static-brake lock | `StatReg` static-brake-lock-request bit set |
| 17 | Reserved | (internal watchdog use on some products) |
| 18 | Reverse limit switch (RLS) active | `LimitsStat` RLS bit set |
| 19 | Forward limit switch (FLS) active | `LimitsStat` FLS bit set |
| 20 | Homing done | [HomingStat](../../16-homing/HomingStat.md) = finished-successfully |
| 21 | Force-in-target status | [ForceInTStat](../../08-axis-operation/04-force-operation-mode/ForceInTStat.md) = target-reached |

¹ Valid only for motion modes that use the built-in profiler (e.g. indirect Pulse/Direction does; direct Pulse/Direction does not).

## Examples

```text
ADOutMode[1]=2       ; output 1 follows this axis' motor-on status
ADOutMode[2]=65538   ; upper 16 bits = 1 (axis B), lower 16 bits = 2 (motor-on):
                     ;   output 2 reflects axis B's motor-on status
ADOutMode[3]=14      ; output 3 follows "regeneration active"
ADOutMode[1]=0       ; hand output 1 back to manual DOutPort control
```

## See also

- [DOutSelect](DOutSelect.md) — must be 0 for DOutMode to apply (hardware function otherwise)
- [DOutPort](DOutPort.md) — the bit the function drives (function 0 = manual)
- [DOutLog](DOutLog.md) — polarity applied on top of the driven bit
- [StatReg](../../07-status-and-faults/StatReg.md) — source of the regen / brake status bits
- [RegenOn](../../09-current-and-voltage/05-regeneration/RegenOn.md) — drives the "regeneration active" function (value 14)
