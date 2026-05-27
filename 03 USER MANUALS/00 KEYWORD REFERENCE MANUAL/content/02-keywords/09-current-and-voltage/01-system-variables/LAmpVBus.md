---
keyword: LAmpVBus
summary: Read-only bus-voltage measurements of the built-in linear amplifier (AmpType = 4).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 253
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LAmpVBus

Read-only bus-voltage measurements of the built-in linear amplifier (AmpType = 4).

## Overview

`LAmpVBus` reports the two bus-voltage rails of the built-in linear amplifier, in millivolts, as a read-only array. It applies only when [AmpType](../../02-motor-and-amplifier/AmpType.md) = 4 (built-in linear amplifier). For the standard switching (PWM) amplifier bus voltage, see [VBus](VBus.md), which is not populated on a linear amplifier.

## How it works

A linear amplifier runs from a split (bipolar) supply, so it has a positive and a negative motor rail. When `AmpType` = 4, the firmware samples both rails from the FPGA in the current-read step and scales each raw reading to millivolts:

| Index | Rail | Description                              |
|-------|------|------------------------------------------|
| 1     | +Vm  | Positive linear-amplifier bus voltage    |
| 2     | −Vm  | Negative linear-amplifier bus voltage (reported as a negative value) |

The array is sized for two rails plus an unused index 0 (so that communication indexes start at 1). The negative rail is read from a separate FPGA register and negated, so a healthy −Vm reads as a negative millivolt value.

> **Note:** on a linear amplifier the bus-voltage protection limits ([MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) / [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md)) and the [VBus](VBus.md) reading do not apply; the firmware explicitly bypasses the standard VBus path for this amplifier type.

## Examples

```text
ALAmpVBus[1]        ; read the +Vm linear-amplifier bus voltage (mV)
ALAmpVBus[2]        ; read the -Vm linear-amplifier bus voltage (mV, negative)
```

## See also

- [VBus](VBus.md) — switching-amplifier DC bus voltage reading (not used on a linear amplifier)
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — amplifier type selection (= 4 selects the linear amplifier)
