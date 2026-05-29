---
keyword: VBus
summary: Read-only amplifier DC bus voltage measurement, in millivolts.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 36
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
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VBus

Read-only amplifier DC bus voltage measurement, in millivolts.

## Overview

`VBus` reports the amplifier DC bus voltage measurement, in millivolts. It is a read-only status value that reflects the supply voltage available to the power stage. The same measurement drives every bus-voltage decision in the firmware: the protection limits [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) / [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../../06-protections/02-current-and-voltage/MaxVBusAbs.md), the regeneration thresholds [RegenOn](../05-regeneration/RegenOn.md) / [RegenOff](../05-regeneration/RegenOff.md), and the multi-level VBus warning reported in [StatReg](../../07-status-and-faults/StatReg.md).

## How it works

On a built-in (PWM) amplifier the bus voltage is sampled once per group of 16 control cycles, the raw ADC reading is converted to millivolts with a fixed scale factor, and a low-pass filter is then applied to suppress measurement spikes. The filter is a first-order IIR with a roughly 8-sample (≈8 ms) time constant:

$$
\text{VBus}_{new} = \frac{\text{VBus}_{raw} + 7 \cdot \text{VBus}_{old}}{8}
$$

The raw-to-mV scale factor depends on the drive variant (each variant has a different sense-resistor divider and ADC reference), so the same raw count maps to different voltages on different hardware; the correct multiplier is applied per product. The filtered result is the value you read as `VBus`.

On a **central-i** remote axis the amplifier does not own the ADC: the bus voltage arrives in the periodic amplifier-sync message and is scaled by a per-axis calibration factor and offset before being stored as `VBus`.

Once `VBus` is updated, the controller uses it to drive regeneration switching and to set the over-/under-voltage status bits in `StatReg`; the actual disabling fault is then raised in the protection step.

## Examples

```text
AVBus               ; read the present bus voltage (mV)
```

## See also

- [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) — maximum bus-voltage protection limit (uses this measurement)
- [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) — minimum bus-voltage protection limit (uses this measurement)
- [RegenOn](../05-regeneration/RegenOn.md), [RegenOff](../05-regeneration/RegenOff.md) — regeneration thresholds compared against `VBus`
- [StatReg](../../07-status-and-faults/StatReg.md) — bits 3/4/6 (over/under VBus) and bits 7–8 (VBus warning level)
- [VLogic](VLogic.md) — logic-supply voltage reading
- [DCDC](DCDC.md) — internal logic-rail measurements
