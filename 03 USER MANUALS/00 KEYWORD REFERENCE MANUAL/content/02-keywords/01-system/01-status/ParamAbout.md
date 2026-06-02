---
keyword: ParamAbout
summary: Function returning a single parameter's minimum, maximum and default values, selected by CAN code.
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ParamAbout

Function returning a single parameter's minimum, maximum and default values, selected by CAN code.

## Overview

`ParamAbout` is a function that returns the **valid range and default** of a single parameter — its minimum value, maximum value, and default value — together with a code identifying the connected controller. It lets host software and diagnostic tools discover a parameter's limits at runtime instead of hard-coding them. Unlike [About](About.md), which dumps every parameter, `ParamAbout` targets one.

## How it works

The parameter to inspect is selected by passing its **CAN code** as the function argument, in the assignment form `AParamAbout=<CAN code>` (the valid range 0–1023 matches the controller's CAN-code space). The argument is mandatory: this is a function that requires a parameter, so calling it without an argument is rejected with an error, and a CAN code outside 0–1023 is rejected as out of range. The reply is produced by the same call that supplies the argument — there is no separate read step. The firmware looks the code up in its keyword table and builds a reply containing:

- a fixed tag,
- a word identifying the connected controller type (for a directly connected standalone unit, or the Central-i master / remote amplifier when reached through Central-i),
- the parameter's **minimum**, **maximum**, and **default** values.

If the selected keyword is non-axis, any axis prefix on the request is ignored. The reply is byte-segmented for Ethernet and word-segmented for CAN/RS-232, so the same values are delivered in the encoding each transport expects. For Central-i parameters whose limits are per-port rather than fixed, the reply uses the port's parameter properties when available, otherwise the constant table limits.

## Examples

```text
AParamAbout=100     ; inspect CAN code 100: returns its min / max / default descriptor
```

## See also

- [About](About.md) — full parameter dump (Agito PCSuite internal use)
- [ParamCS](ParamCS.md) — checksum over the parameter set
- [Identity](Identity.md) — controller identification and features
