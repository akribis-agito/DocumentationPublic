---
keyword: CompFiltFreq
summary: Cut-off frequency, in hertz, of the compensation filter's first-order low-pass stage.
availability:
  standalone: []
  central-i:
  - v5
can_code: 835
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1.0
  - 1000.0
  default: 200.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CompFiltFreq

Cut-off frequency, in hertz, of the compensation filter's first-order low-pass stage.

## Overview

When the compensation filter is enabled with [CompFiltOn](CompFiltOn.md), the difference between the measured force and the force predicted from the compensation table is passed through a first-order low-pass filter before being added back to the predicted force. `CompFiltFreq` sets that filter's cut-off frequency in hertz.

A higher cut-off lets more of the measured force's high-frequency content through, so the output tracks the live sensor more closely. A lower cut-off leans more heavily on the smooth, table-predicted force.

This keyword is available from v5 (central-i v5).

## How it works

The value is interpreted as a frequency in hertz and converted internally into a single-pole low-pass coefficient using the controller sample period; the resulting filter has its -3 dB point at the frequency you specify. The coefficient is recomputed whenever the frequency is changed, so updates take effect without disabling the filter.

The firmware accepts a range of 1 to 1000 Hz with a default of 200 Hz.

## Examples

Set the compensation filter cut-off to 150 Hz on an axis:

```
ACompFiltFreq[1]=150
```

Read back the configured cut-off:

```
ACompFiltFreq[1]
```

## See also

- [CompFiltOn](CompFiltOn.md)
- [CompFiltTble](CompFiltTble.md)
- [00-overview](00-overview.md)
