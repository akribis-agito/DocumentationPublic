---
keyword: PDPos
summary: Read-only scaled pulse-and-direction counter, accumulated every controller cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 4
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: pd_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDPos

Read-only scaled pulse-and-direction counter, accumulated every controller cycle.

## Overview

`PDPos` is the pulse-and-direction (P/D) input counter. Every controller cycle the firmware reads the number of pulses the FPGA decoded since the previous cycle, scales them by [PDFact](PDFact.md)/[PDFactDen](PDFactDen.md), applies the [PDEncDir](PDEncDir.md) sign, and adds the result to an accumulator. `PDPos` is the high-bits view of that accumulator and is the core value of P/D decoding: in **direct** P/D motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 3) the change in `PDPos` since the start of motion drives the position reference [PosRef](../01-kinematics-status/PosRef.md); in **indirect** P/D motion (`MotionMode` = 4) the same change drives the profiler target [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md).

`PDPos` is read-only over the bus but can be re-zeroed or preset with [SetPDPos](SetPDPos.md). It powers up at 0.

![Pulse-and-direction input chain](pd-input-chain.svg)

## How it works

### Per-cycle accumulation

The reading and scaling are done by the `M_READ_CALCULATE_PDPOS` macro, called once per axis from the control interrupt (macro defined in `AG300_CTL01ControlInterrupt.h:1265`; invoked at `AG300_CTL01ControlInterrupt.c:1743`, `1760`, `1775`). Each cycle it:

1. Reads the signed pulse delta for this cycle from the FPGA. Older FPGAs (`IDENTITY_FPGA_VERSION_INDEX < 3036`) expose a single counter register (`FPGA_PD_COUNTER_REG`); newer FPGAs have a per-axis register (`FPGA_PD_A_AXIS_COUNTER_REG + axis`). The raw delta is a 16-bit signed value.
2. Scales the delta by the floating-point factor `gfPDFact = PDFact / PDFactDen` (precomputed in `SpPDFactors`, `SpecialFuncs.c:3948`), and adds the fixed-point **remainder carried over from the previous cycle** so fractional pulses are never lost over time.
3. Computes that cycle's exact remainder using full 64-bit integer math and stores it in `glPDPosDeltaRemainderPrev` for the next cycle — this is why a fractional `PDFact/PDFactDen` ratio does not drift.
4. Accumulates into the internal counter, applying the direction sign as `× (1 − 2·PDEncDir)` (so `PDEncDir = 0` adds, `PDEncDir = 1` subtracts):

   ```text
   gllPDPos += gllPDPosDelta * (1 - 2*PDEncDir)
   glPDPos   = gllPDPos >> 32
   glPDVel   = gllPDPosDelta >> (32 - 14)
   ```

The accumulator `gllPDPos` is held in **32.32 fixed-point** (`AG300_CTL01ControlInterrupt.c:163`); `PDPos` is its top 32 bits (`>> 32`) and [PDVel](PDVel.md) is derived from the per-cycle delta. Accumulating every control cycle guarantees no pulses are dropped between reads.

### How PDPos becomes the reference

`Begin` latches the current accumulator into `gllPDPosInitial` (`AG300_CTL01Funcs.c:1411`, `1438`) so motion is measured **relative to the instant motion started**:

- **Direct (MotionMode = 3):** `PosRef` is built from `(gllPDPos − gllPDPosInitial)` shifted from 32.32 into the reference's 50.14 scaling, passed through the first-order filter [PDFiltFact](PDFiltFact.md) (set via [PDPosFilt](PDPosFilt.md)), then added to the reference latched at `Begin` (`AG300_CTL01Profiler.c:1251`). If the result hits a software travel limit the motion is aborted (further pulses would be lost).
- **Indirect (MotionMode = 4):** the same delta sets the profiler target `gllAbsTrgt` (`AG300_CTL01Profiler.c:1304`), and the controller's own second-order profiler drives `PosRef` toward it subject to `Speed`/`Accel`/`Decel`.

### Modulo

If [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0, when the feedback wraps the firmware shifts the whole 32.32 accumulator by `ModRev` (`gllPDPos ∓= ModRev << 32`, `AG300_CTL01ControlInterrupt.c:13158`, `13213`) together with the rest of the reference frame, so the P/D following error is preserved across the wrap.

### Auxiliary-encoder reuse

When the P/D inputs are repurposed as an auxiliary encoder (`AuxAsPDPosOn = 1`), the firmware copies `PDPos`/`PDVel` into the auxiliary feedback ([AuxPos](../01-kinematics-status/AuxPos.md)/`AuxVel`) instead of using them for P/D motion (`AG300_CTL01ControlInterrupt.c:1755`).

### Reading in user units

When queried over a communication channel, `PDPos` is converted from internal counts to pulse-direction user units by [PDUsrUnits](PDUsrUnits.md). This scaling affects the reported value only, not the internal computation.

## Examples

```text
APDPos              ; read the current scaled P/D counter (pulse-direction units)
```

## See also

- [PDVel](PDVel.md) — rate of change of `PDPos`
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — scaling-factor numerator/denominator
- [PDEncDir](PDEncDir.md) — accumulation direction (sign)
- [PDFiltFact](PDFiltFact.md) / [PDPosFilt](PDPosFilt.md) — direct-mode smoothing of the delta into `PosRef`
- [SetPDPos](SetPDPos.md) — preset/re-zero the counter
- [PDUsrUnits](PDUsrUnits.md) — query unit conversion
- [PosRef](../01-kinematics-status/PosRef.md) / [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — what `PDPos` drives in direct / indirect mode
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects direct (3) vs. indirect (4) P/D motion
