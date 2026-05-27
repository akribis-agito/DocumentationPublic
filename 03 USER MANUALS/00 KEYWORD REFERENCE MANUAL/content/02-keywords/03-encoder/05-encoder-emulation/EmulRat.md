---
keyword: EmulRat
summary: Ratio between feedback encoder counts and the quadrature pulses emitted on the emulation output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 69
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
  - -65536
  - 65536
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmulRat

Ratio between feedback encoder counts and the quadrature pulses emitted on the emulation output.

## Overview

`EmulRat` sets the divide ratio between the feedback encoder counts and the A/B quadrature pulses emitted on the encoder emulation interface. It lets the emulated output match the resolution a downstream device expects, and its sign selects the count direction of the emulated signal. It works together with [EmulFilter](EmulFilter.md) (output filtering) and [EmulIndexType](EmulIndexType.md) (index pulse type), and relates to the feedback resolution set by [EncRes](../01-general-settings/EncRes.md). It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion. The range is -65536 to 65536.

## How it works

`EmulRat` is applied by the FPGA emulation block. Writing the keyword runs the special handler `SpEmulRat` (`SpecialFuncs.c:4702`), which programs the per-axis emulation factor register and an output multiplexer that sets the A/B phase order:

| `EmulRat` | Emulation factor register | A/B phase (direction) |
|---|---|---|
| > 0 | `EmulRat − 1` | normal |
| 0 | `0` (behaves like a factor of 1) | normal |
| < 0 | `~EmulRat` (i.e. `−EmulRat − 1`) | inverted (A and B swapped) |

The hardware emits one quadrature edge per (factor + 1) internal counts, so a positive `EmulRat = N` divides the feedback by `N`. A value of 0 collapses to the same behaviour as `EmulRat = 1` (factor 0 — pass-through). A negative value uses the magnitude as the divide ratio while inverting the A/B phase, which reverses the apparent count direction at the downstream device.

On older FPGA revisions the emulation output also has to be muxed onto the differential output pins (the handler selects emulation vs. plain differential outputs); on current FPGA revisions the output mux is configured per axis as part of the same write.

## Examples

```text
AEmulRat=4           ; one quadrature step per 4 feedback counts, normal direction
AEmulRat=-4          ; same 1:4 ratio, reversed emulated direction
AEmulRat=1           ; pass-through (one emulated step per feedback count)
AEmulRat             ; query the configured ratio
```

## See also

- [EmulFilter](EmulFilter.md) — filter applied to the emulated output
- [EmulIndexType](EmulIndexType.md) — index pulse type on the emulated output
- [EncRes](../01-general-settings/EncRes.md) — feedback encoder resolution
