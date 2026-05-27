---
keyword: VEncOn
summary: Enables or disables the software-generated virtual encoder for the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 613
attributes:
  access: rw
  scope: axis
  flash: true
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
# VEncOn

Enables or disables the software-generated virtual encoder for the axis.

## Overview

`VEncOn` enables or disables the virtual encoder for the axis. The virtual encoder (firmware: "True Virtual Encoder") is an **encoder-signal generator**: when enabled, the controller emits a real quadrature or pulse/direction signal on the axis's hardware encoder-emulation outputs that **tracks an internal source variable** in real time. The source is selected by [VEncSrc](VEncSrc.md), the output signal format by [VEncType](VEncType.md), the source-to-output scale by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md), and a pulse/direction setup delay by [VEncDelay](VEncDelay.md). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

This is different from the fixed encoder-emulation outputs ([EmulRat](../05-encoder-emulation/EmulRat.md)), which always mirror the axis's own feedback: the virtual encoder can track *any* selectable source variable.

> **Note:** the virtual encoder produces an *output* signal that mirrors a variable; it does **not** replace the axis's own position feedback ([Pos](../../10-motion/01-kinematics-status/Pos.md)). The generated count is exposed read-only as `VEncValue`.

## How it works

| VEncOn | State |
|---|---|
| 0 | Virtual encoder disabled; emulation output registers cleared. |
| 1 | Virtual encoder enabled; each control cycle the firmware reads the source, scales it, and drives the FPGA to emit the corresponding number of edges. |

Each control cycle (`AG300_CTL01ControlInterrupt.c`, around line 6296) the firmware:

1. Reads the source variable selected by [VEncSrc](VEncSrc.md) (handling its data type and any [ModRev](../04-modulo-mode/ModRev.md) roll-over of the source).
2. Multiplies it by [VEncFact](VEncFact.md) to move into the output plane.
3. Runs a PI tracking controller plus feed-forward so the emitted count `VEncValue × VEncFactDen` follows the scaled source with minimal lag, and computes the number of edges (`VEncDelta`) to emit this cycle.
4. Writes the pulse count, 50% duty period, and "clocks-to-first-pulse" (from [VEncDelay](VEncDelay.md)) to the FPGA.

If the required number of pulses in one cycle exceeds the hardware limit while the motor is on, the axis faults (`CON_FLT_VENC_MAX_NUM_PULSES_EXCEEDED`).

> **Availability:** in the current firmware the full generation path is implemented for the **AG300 controller**; the Central-i remote-output path is product-dependent (see firmware notes in `SpVEnc`).

## Examples

```text
AVEncOn=1            ; enable the virtual encoder
AVEncOn=0            ; disable the virtual encoder
```

## See also

- [VEncSrc](VEncSrc.md) — source variable the output tracks
- [VEncType](VEncType.md) — output signal format (pulse/direction or A-quad-B)
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — source-to-output scaling ratio numerator / denominator
- [VEncDelay](VEncDelay.md) — pulse/direction setup delay
- [EmulRat](../05-encoder-emulation/EmulRat.md) — fixed encoder emulation that mirrors the axis's own feedback
