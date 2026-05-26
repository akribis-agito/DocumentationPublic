---
keyword: AInPort
summary: Read-only analog-input readings — processed values and raw ADC values.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 35
attributes:
  access: ro
  scope: axis
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
overrides: {}
---
# AInPort

Read-only analog-input readings — processed values and raw ADC values.

## Overview

`AInPort` holds the analog-input readings. Its length is twice the number of analog inputs: the first half holds the **processed** readings (after filter, offset, first deadband, gain, and second deadband), and the second half holds the **original** values straight from the ADC. See the [analog-input signal path](00-overview.md) for the full processing chain.

| Data | Analog input 1 | Analog input 2 | Analog input 3 | Analog input 4 |
|------|----------------|----------------|----------------|----------------|
| Processed input | AInPort[1] | AInPort[2] | AInPort[3] | AInPort[4] |
| Original input | AInPort[5] | AInPort[6] | AInPort[7] | AInPort[8] |

## Examples

```text
AInPort[1]?         ; processed reading of analog input 1
AInPort[5]?         ; raw (post-ADC) reading of analog input 1
```

## See also

- [AInFilt](AInFilt.md), [AInOffset](AInOffset.md), [AInDB](AInDB.md), [AInGain](AInGain.md), [AInMuteRange](AInMuteRange.md) — the processing chain
- [AInMode](AInMode.md) — assign a function to an analog input
