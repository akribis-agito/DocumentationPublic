---
keyword: EmulIndexType
summary: Selects the type of index pulse generated on the encoder emulation output.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

> **Documentation pending:** the exact behaviour of each option value (0 and 1) is not documented here.

## Examples

```text
EmulIndexType=0     ; default index pulse type
```

## See also

- [EmulRat](EmulRat.md) — ratio between feedback counts and emulated quadrature output
- [EmulFilter](EmulFilter.md) — filter applied to the emulated output
