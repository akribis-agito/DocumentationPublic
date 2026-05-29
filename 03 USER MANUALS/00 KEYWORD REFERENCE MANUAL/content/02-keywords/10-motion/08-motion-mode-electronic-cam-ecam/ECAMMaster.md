---
keyword: ECAMMaster
summary: Complex CAN code selecting the master-variable source for each ECAM cam pattern.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 309
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
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
# ECAMMaster

Complex CAN code selecting the master-variable source for each ECAM cam pattern.

## Overview

`ECAMMaster` is the [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) (CCC) defining the source of the master variable in ECAM motion. It is an array of 10 cam patterns, one element per pattern. As the master value changes, the axis (slave) position reference tracks the cam pattern stored in [GenData](../../20-arrays/GenData.md), spaced by [ECAMGap](ECAMGap.md).

The CCC encodes the keyword, axis number and array index of any readable keyword, so the master can be the position of another axis ([Pos](../01-kinematics-status/Pos.md) or [PosRef](../01-kinematics-status/PosRef.md)), an auxiliary encoder ([AuxPos](../01-kinematics-status/AuxPos.md)), a counter, a general-storage element, or any other readable parameter. The selected source must be a parameter (not a command/function); the CCC's axis number and array index must be valid for that keyword. The default value `0` is not a usable master and must be set before ECAM motion can start.

## How it works

The master source is resolved once, when ECAM motion starts ([Begin](../04-motion-command/Begin.md)), from the CCC held for the active cam pattern ([ECAMTableNum](ECAMTableNum.md)). The controller then follows the *change* in the master value each control cycle rather than its absolute value:

- The master value is sampled every cycle and the change since the previous cycle is accumulated into an internal master position. Tracking the delta lets ECAM work even when the master source wraps past its numeric limits — useful for endless cam motion (see [ECAMCycles](ECAMCycles.md)) driven by a free-running counter or auxiliary position.
- The accumulated master position is then mapped, through [ECAMGap](ECAMGap.md), to a fractional index into the cam table; the slave reference is read from [GenData](../../20-arrays/GenData.md) at that index with linear interpolation between entries (see [ECAMGap](ECAMGap.md) for the index calculation).
- On **v5** the master can be a 32-bit or 64-bit integer, a single-precision or a double-precision value, and the controller reads it in its native type. On **v4** the master source is always read as a 32-bit value, so a 64-bit, single-precision, or double-precision master source is only read correctly on v5.

If the source keyword's CCC is invalid (unknown keyword, out-of-range axis, out-of-range index, or a command instead of a parameter), the [Begin](../04-motion-command/Begin.md) is rejected with an error and ECAM motion does not start.

## Examples

```text
AECAMMaster[1]      ; read the master-variable CCC for cam pattern 1
```

## See also

- [ECAMGap](ECAMGap.md) — spacing of master values and the master-to-index mapping
- [ECAMMasterIni](ECAMMasterIni.md) — initial master-value offset at start of motion
- [ECAMTableNum](ECAMTableNum.md) — selects which cam pattern (and thus which `ECAMMaster`) is active
- [GenData](../../20-arrays/GenData.md) — array storing the cam pattern
- [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) — how the source keyword is encoded
