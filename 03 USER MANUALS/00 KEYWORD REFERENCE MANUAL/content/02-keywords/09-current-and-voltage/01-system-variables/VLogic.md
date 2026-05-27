---
keyword: VLogic
summary: Read-only 5 V logic-supply voltage; outside 4500–5500 mV disables the motor.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 37
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VLogic

Read-only 5 V logic-supply voltage; outside 4500–5500 mV disables the motor.

## Overview

`VLogic` reports the 5 V logic-supply voltage measurement, in millivolts. It is a read-only status value with built-in protection: if `VLogic` falls outside the range [4500, 5500] mV, the motor is disabled. It complements the bus-voltage reading [VBus](VBus.md) and the per-rail logic measurements in [DCDC](DCDC.md).

## How it works

The motor is disabled whenever `VLogic` is not within the range:

$$
4500\ \text{mV} \le VLogic \le 5500\ \text{mV}
$$

## Examples

```text
AVLogic             ; read the present 5 V logic voltage (mV)
```

## See also

- [DCDC](DCDC.md) — per-rail internal logic-voltage measurements
- [VBus](VBus.md) — amplifier DC bus voltage reading
