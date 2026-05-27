---
keyword: VEncType
summary: Sets the output format or signal type of the virtual encoder.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 615
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
# VEncType

Sets the output format or signal type of the virtual encoder.

## Overview

`VEncType` sets the physical signal format emitted by the virtual encoder when it is enabled ([VEncOn](VEncOn.md) = 1). The same generated count (built from [VEncSrc](VEncSrc.md) scaled by [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md)) can be output either as pulse/direction or as A-quad-B quadrature. The value range is 0 to 1, with a default of 0. It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

`VEncType` maps to the firmware `VENC_TYPE_*` constants and is written into the FPGA virtual-encoder settings register (`SpVEnc`, `SpecialFuncs.c:5148`):

| Value | Firmware constant | Output signal |
|---|---|---|
| 0 | `VENC_TYPE_PD` | Pulse + direction (one pulse line, one direction line). |
| 1 | `VENC_TYPE_AQB` | A-quad-B quadrature (two phase-shifted channels). |

The format affects how [VEncDelay](VEncDelay.md) is used: a setup delay (clocks-to-first-pulse on a direction change) is applied only for pulse/direction (`VEncType=0`). For A-quad-B the delay is forced to 0, since A and B are never switched simultaneously and no inter-line setup time is needed.

## Examples

```text
AVEncType=0          ; pulse/direction output (default)
AVEncType=1          ; A-quad-B quadrature output
```

## See also

- [VEncOn](VEncOn.md) — enables the virtual encoder
- [VEncSrc](VEncSrc.md) — source variable for the virtual encoder
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — scaling ratio numerator / denominator
- [VEncDelay](VEncDelay.md) — pulse/direction setup delay (used only for `VEncType=0`)
