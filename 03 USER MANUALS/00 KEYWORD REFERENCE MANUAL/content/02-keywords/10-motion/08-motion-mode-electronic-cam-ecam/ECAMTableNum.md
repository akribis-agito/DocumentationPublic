---
keyword: ECAMTableNum
summary: Selects the active ECAM cam pattern / look-up table (1-10).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 311
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
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ECAMTableNum

Selects the active ECAM cam pattern / look-up table (1-10).

## Overview

`ECAMTableNum` selects which of the up-to-10 cam patterns (look-up tables) is active. Each cam pattern has its own set of parameters that fully define it — [ECAMStart](ECAMStart.md), [ECAMEnd](ECAMEnd.md), [ECAMStartCyc](ECAMStartCyc.md), [ECAMEndCyc](ECAMEndCyc.md), [ECAMGap](ECAMGap.md), [ECAMCycles](ECAMCycles.md), [ECAMMaster](ECAMMaster.md) and [ECAMMasterIni](ECAMMasterIni.md) — held as element-per-pattern arrays. The pattern can be changed only when the axis is not in motion.

## How it works

The controller keeps the eight defining parameters for all 10 patterns at all times, but only one is in effect during a move. When ECAM motion starts ([Begin](../04-motion-command/Begin.md)), the controller copies the parameters of the pattern named by `ECAMTableNum` into the active working set and validates them. A [Begin](../04-motion-command/Begin.md) is rejected with a specific [instruction error code](../../../04-error-codes/instruction-error-codes.md) if, for the selected pattern:

- any of `ECAMStart`, `ECAMStartCyc`, `ECAMEndCyc` or `ECAMEnd` is `0` — a zero index marks the pattern as unused (error code 73);
- the indices do not satisfy `ECAMStart ≤ ECAMStartCyc < ECAMEndCyc ≤ ECAMEnd` (error code 74);
- `ECAMGap` is `0` (error code 75), or `ECAMCycles` is `0` (error code 76);
- the `ECAMMaster` source has a complex CAN code that is out of range (error code 77), names an invalid axis (error code 78), uses a wrong array index (error code 79), or points at a function instead of a parameter (error code 80);
- the master range needed to play the pattern exceeds ±2,000,000,000 master units (error code 81);
- two consecutive cam-table entries differ by too much (error code 82);
- `ECAMMasterIni` is outside the master range for one ECAM cycle (error code 323).

Because the parameters are latched at start, changing `ECAMTableNum` mid-motion has no effect; it is therefore blocked while the axis is in motion. The current-cycle counter [ECAMCycCount](ECAMCycCount.md) is also indexed per pattern, so each pattern keeps its own cycle count.

## Examples

```text
AECAMTableNum=1      ; select cam pattern 1 (default)
AECAMTableNum        ; read the active cam pattern
```

### Walk-through: define and run one ECAM cycle

Load a small cam table into [GenData](../../20-arrays/GenData.md) at indices 1-5, configure cam pattern 1 to use those entries, and run a single cycle following axis B's [PosRef](../01-kinematics-status/PosRef.md). Axis A is assumed motor-on and not in motion.

```text
; --- 1) Load the cam pattern points into GenData ---
AGenData[1]=0
AGenData[2]=2500
AGenData[3]=5000
AGenData[4]=2500
AGenData[5]=0

; --- 2) Bind cam pattern 1 to the loaded indices ---
AECAMTableNum=1               ; select cam pattern 1 (scalar; pattern slot is set via the array index of the other keys)
AECAMStart[1]=1               ; first GenData index of the pattern
AECAMEnd[1]=5                 ; last  GenData index of the pattern
AECAMStartCyc[1]=1            ; start of the repeating segment
AECAMEndCyc[1]=5              ; end   of the repeating segment
AECAMGap[1]=1000              ; master step between adjacent table indices
AECAMCycles[1]=1              ; run the cycle once
AECAMMaster[1]=...            ; complex CAN code pointing at axis B's PosRef
AECAMMasterIni[1]=0           ; cam alignment at Begin (see ECAMMasterIni)

; --- 3) Arm ECAM motion on axis A ---
AMotionMode=7                 ; 7 = ECAM
ABegin                        ; controller latches the table, then follows the master

; --- 4) Observe the follower ---
AECAMCycCount[1]              ; current cycle index for pattern 1 (1..ECAMCycles)
APosRef                       ; follower reference shaped by the cam lookup
```

`Begin` is rejected if the indices for pattern 1 do not satisfy
`ECAMStart <= ECAMStartCyc < ECAMEndCyc <= ECAMEnd`,
if any of `ECAMStart`, `ECAMEnd`, `ECAMStartCyc`, `ECAMEndCyc`, `ECAMGap` or `ECAMCycles` is 0, or if `ECAMMaster` does not point at a valid variable.

## See also

- [ECAMStart](ECAMStart.md) / [ECAMEnd](ECAMEnd.md) — pattern bounds for the selected table
- [ECAMStartCyc](ECAMStartCyc.md) / [ECAMEndCyc](ECAMEndCyc.md) — repeating-segment bounds within the pattern
- [ECAMGap](ECAMGap.md) / [ECAMCycles](ECAMCycles.md) — master spacing and repetition count for the selected table
- [ECAMMaster](ECAMMaster.md) / [ECAMMasterIni](ECAMMasterIni.md) — master selection and initial alignment
- [ECAMCycCount](ECAMCycCount.md) — current-cycle index for the active pattern
- [GenData](../../20-arrays/GenData.md) — array that stores the cam pattern points
- [StopECAM](StopECAM.md) — exit ECAM motion while preserving the shrunk range
- [Motion mode – Electronic cam (ECAM)](00-overview.md) — ECAM motion overview
