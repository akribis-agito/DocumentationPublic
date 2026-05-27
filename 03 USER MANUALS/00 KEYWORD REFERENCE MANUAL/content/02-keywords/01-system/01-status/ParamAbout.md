---
keyword: ParamAbout
summary: Function returning a parameter's metadata (CAN code, name, attributes, range, default).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 499
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ParamAbout

Function returning a parameter's metadata (CAN code, name, attributes, range, default).

## Overview

`ParamAbout` is a function that returns the **valid range and default** of a single parameter — its minimum value, maximum value, and default value — together with a code identifying the connected controller. It lets host software and diagnostic tools discover a parameter's limits at runtime instead of hard-coding them. Unlike [About](About.md), which dumps every parameter, `ParamAbout` targets one.

## How it works

The parameter to inspect is selected by passing its **CAN code** as the function argument (the valid range 0–1023 matches the controller's CAN-code space). The firmware looks the code up in its keyword table and builds a reply containing:

- a fixed `"AxSt;"` tag,
- a word identifying the connected controller type (for a directly connected standalone unit, or the Central-i master / remote amplifier when reached through Central-i),
- the parameter's **minimum**, **maximum**, and **default** values.

If the selected keyword is non-axis, any axis prefix on the request is ignored. The reply is byte-segmented for Ethernet and 32-bit-word-segmented for CAN/RS-232, so the same values are delivered in the encoding each transport expects. For Central-i parameters whose limits are per-port rather than fixed, the reply uses the port's parameter properties when available, otherwise the constant table limits.

## Examples

```text
AParamAbout=100      ; select the parameter with CAN code 100
AParamAbout         ; read back its min / max / default descriptor
```

## See also

- [About](About.md) — full parameter dump (Agito PCSuite internal use)
- [ParamCS](ParamCS.md) — checksum over the parameter set
- [Identity](Identity.md) — controller identification and features
