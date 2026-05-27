---
keyword: EmulFilter
summary: Digital filter applied to the encoder emulation output signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 403
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
  - 15
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmulFilter

Digital filter applied to the encoder emulation output signal.

## Overview

`EmulFilter` sets the digital filter applied to the encoder emulation output. A higher value applies more filtering, smoothing the emulated quadrature edges. It works together with [EmulRat](EmulRat.md) (output ratio) and [EmulIndexType](EmulIndexType.md) (index pulse type) to configure the emulated encoder interface. The range is 0 to 15 (4-bit field), default 3. It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## How it works

`EmulFilter` and [EmulIndexType](EmulIndexType.md) share a single per-axis FPGA emulation-setting register, written by the special handler `SpEmulation` (`SpecialFuncs.c:431`). The register is packed as:

| Bits | Field | Source |
|---|---|---|
| 0–3 | Output filter level (0–15) | `EmulFilter` |
| 4–5 | Index pulse type | [EmulIndexType](EmulIndexType.md) |

`EmulFilter` occupies the low 4 bits, so values are masked to 0–15. Writing either keyword re-packs and re-writes the whole register, so the two settings always take effect together.

## Examples

```text
AEmulFilter=3        ; default filtering level
AEmulFilter=0        ; minimum filtering
AEmulFilter          ; query the configured filter level
```

## See also

- [EmulRat](EmulRat.md) — ratio between feedback counts and emulated quadrature output
- [EmulIndexType](EmulIndexType.md) — index pulse type on the emulated output
