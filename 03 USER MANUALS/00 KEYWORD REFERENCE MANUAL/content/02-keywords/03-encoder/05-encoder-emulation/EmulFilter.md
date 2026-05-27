---
keyword: EmulFilter
summary: Digital filter applied to the encoder emulation output signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

`EmulFilter` sets the digital filter applied to the encoder emulation output. A higher value applies more filtering to reduce high-frequency noise on the emulated quadrature output. It works together with [EmulRat](EmulRat.md) (output ratio) and [EmulIndexType](EmulIndexType.md) (index pulse type) to configure the emulated encoder interface. It is an axis-scope parameter saved to flash and can be changed while the motor is on or in motion.

## Examples

```text
EmulFilter=3        ; default filtering level
EmulFilter=0        ; no filtering
```

## See also

- [EmulRat](EmulRat.md) — ratio between feedback counts and emulated quadrature output
- [EmulIndexType](EmulIndexType.md) — index pulse type on the emulated output
