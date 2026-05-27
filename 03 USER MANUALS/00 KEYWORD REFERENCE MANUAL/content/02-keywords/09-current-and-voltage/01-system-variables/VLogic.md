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

`VLogic` reports the 5 V logic-supply voltage measurement, in millivolts. It is a read-only status value with built-in protection: if `VLogic` leaves the range [4500, 5500] mV, the motor is disabled with a logic-voltage fault. It complements the bus-voltage reading [VBus](VBus.md) and the per-rail logic measurements in [DCDC](DCDC.md).

## How it works

`VLogic` is sampled once per group of 16 control cycles from the FPGA logic-voltage register and converted to millivolts with a per-variant scale factor (the divider and ADC reference differ between products, so each variant uses its own multiplier). On variants that have no 5 V sense, and on central-i remote units whose FPGA reports a firmware version below 3, the firmware substitutes a fixed `5000` mV so the protection cannot false-trip. On a central-i amplifier the 5 V reading instead arrives in the amplifier-sync message and is scaled by a per-axis calibration factor and offset.

Once per protection cycle the firmware checks the measured value against two fixed limits (these are firmware constants, **not** user-settable):

| Condition | Fault | [ConFlt](../../07-status-and-faults/ConFlt.md) code |
|-----------|-------|------|
| `VLogic > 5500` mV | Logic voltage too high | 1010 (`CON_FLT_LOGIC_OVER_VOLTAGE`) |
| `VLogic < 4500` mV | Logic voltage too low | 1011 (`CON_FLT_LOGIC_UNDER_VOLTAGE`) |

Either condition turns the motor off and logs the fault. The acceptable band is therefore:

$$
4500\ \text{mV} \le VLogic \le 5500\ \text{mV}
$$

> **Note:** the over-voltage limit is exclusive (`> 5500`) and the under-voltage limit is exclusive (`< 4500`), so the boundary values 4500 mV and 5500 mV are still accepted.

## Examples

```text
AVLogic             ; read the present 5 V logic voltage (mV)
```

## See also

- [DCDC](DCDC.md) — per-rail internal logic-voltage measurements (the 5 V rail also appears at index 6)
- [VBus](VBus.md) — amplifier DC bus voltage reading
- [ConFlt](../../07-status-and-faults/ConFlt.md) — faults 1010 / 1011 raised by the logic-voltage protection
