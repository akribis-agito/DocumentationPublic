---
keyword: EmulIndexType
summary: Selects the type of index pulse generated on the encoder emulation output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 402
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
# EmulIndexType

Selects the type of index pulse generated on the encoder emulation output.

## Overview

`EmulIndexType` selects the type of index (Z) pulse generated on the encoder emulation output. The value range is 0 to 1, with a default of 0. It works together with [EmulRat](EmulRat.md) (output ratio) and [EmulFilter](EmulFilter.md) (output filtering) to configure the emulated encoder interface. It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

`EmulIndexType` and [EmulFilter](EmulFilter.md) share a single per-axis emulation-setting register. The register is packed as:

| Bits | Field | Source |
|---|---|---|
| 0–3 | Output filter level | [EmulFilter](EmulFilter.md) |
| 4–5 | Index pulse type | `EmulIndexType` |

`EmulIndexType` is written into bits 4–5 of the register (masked to 2 bits); the keyword value range exposed to the user is 0–1. Writing either keyword re-packs and re-writes the whole register, so both settings take effect together. The bit field selects how the emulated Z pulse is generated:

| Value | Emulated index (Z) behavior |
|---|---|
| 0 | Pass-through. The incoming index pulse is emitted directly on the emulated index output, unchanged. |
| 1 | Regenerated and aligned. The index pulse is re-derived from the emulated A/B quadrature edges and asserted across a fixed, narrow span (a few emulated edges wide), so its edges line up with the emulated quadrature output rather than the raw incoming index. |

## Examples

```text
AEmulIndexType=0     ; default index pulse type
AEmulIndexType       ; query the configured index pulse type
```

## See also

- [EmulRat](EmulRat.md) — ratio between feedback counts and emulated quadrature output
- [EmulFilter](EmulFilter.md) — filter applied to the emulated output
