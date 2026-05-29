---
keyword: AInPort
summary: Read-only analog-input readings — processed values and raw ADC values.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 35
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
    range: null
---
# AInPort

Read-only analog-input readings — processed values and raw ADC values.

## Overview

`AInPort` holds the analog-input readings, in millivolts. Its length is twice the number of analog inputs: the first half holds the **processed** readings (after filter, offset, first deadband, gain, and second deadband), and the second half holds the **original** values straight from the ADC. See the [analog-input signal path](00-overview.md) for the full processing chain.

| Data | Analog input 1 | Analog input 2 | Analog input 3 | Analog input 4 |
|------|----------------|----------------|----------------|----------------|
| Processed input | AInPort[1] | AInPort[2] | AInPort[3] | AInPort[4] |
| Original input | AInPort[5] | AInPort[6] | AInPort[7] | AInPort[8] |

The index is fixed to the physical input — `AInPort[1]` is always analog input 1, `AInPort[2]` is input 2, and so on. On 2-input products only inputs 1–2 (processed) and the corresponding raw entries exist; the others read 0.

## How it works

Each control cycle, the ADC reading for one input is taken into a working value, stored unchanged in the raw entry (`AInPort[5]`–`AInPort[8]`), then run through the conditioning chain and stored in the processed entry (`AInPort[1]`–`AInPort[4]`). See the [analog-input signal path](00-overview.md) for the conditioning stages. The raw count is scaled to millivolts by a fixed hardware factor (e.g. ±12500 mV over ±32768 counts), so both halves of `AInPort` are in mV.

Update rate depends on the platform:

- **Standalone (CONTROLLER) v4** — all four inputs are conditioned every single sample (16 384 Hz). On the AG100 single-axis variant, only inputs 1–2 exist.
- **Central-i v4 / v5** — the four inputs are conditioned one per 16-sample slot, so each input is refreshed at roughly 1 024 Hz on each connected remote unit.

The analog-input converter is a 16-bit converter and the reading is signed (two's complement), so the raw entry spans the full −32768…+32767 count range. On standalone products each control cycle the converter takes one new fully-settled sample per input: the conversion is started by the controller's sample tick and completes in roughly 4–5 µs, far inside the ~61 µs control cycle (16 384 Hz), and there is no internal oversampling or block-averaging — `AInPort[5]`–`AInPort[8]` is a single point sample of the input captured each cycle. (On central-i remote I/O the four inputs are refreshed in rotation as described above, roughly 1 024 Hz per input, but each value is still a single point sample, not a block average.) To smooth noisy inputs, use the digital filter [AInFilt](AInFilt.md) rather than relying on converter averaging.

The processed value is what control functions consume once an input is routed with [AInMode](AInMode.md); the raw value is used directly only by the analog position-feedback function ([AInMode](AInMode.md) code 10). Both are read-only.

## Examples

```text
AAInPort[1]         ; processed reading of analog input 1
AAInPort[5]         ; raw (post-ADC) reading of analog input 1
```

### Edge cases

- **Index 0** — invalid; valid indices are `AInPort[1]`–`AInPort[8]`. `AInPort[0]` does not exist.
- **2-input products (AG100)** — only `AInPort[1]`, `AInPort[2]`, `AInPort[5]`, `AInPort[6]` are populated; indices 3, 4, 7, 8 read `0`.
- **Motor on/off and mode independence** — sampling and conditioning run every cycle regardless of `MotorOn` or [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md); the values are valid even when the axis is disabled.
- **Reading the raw value** — `AInPort[5]`–`AInPort[8]` are the millivolt-scaled ADC value before any filter / offset / deadband / gain / mute, useful when a function (e.g. [AInMode](AInMode.md) code 10 position feedback) needs the unprocessed reading.
- **Read-only** — writes to `AInPort` are rejected; modify the input behaviour via [AInGain](AInGain.md) / [AInOffset](AInOffset.md) / [AInDB](AInDB.md) / [AInMuteRange](AInMuteRange.md) / [AInFilt](AInFilt.md).
- **Platform** — on central-i v5 the values are 32-bit floats with the same mV scaling.

## See also

- [AInFilt](AInFilt.md), [AInOffset](AInOffset.md), [AInDB](AInDB.md), [AInGain](AInGain.md), [AInMuteRange](AInMuteRange.md) — the processing chain that produces `AInPort[1]`–`AInPort[4]`
- [AInMode](AInMode.md) — assign a function to an analog input
