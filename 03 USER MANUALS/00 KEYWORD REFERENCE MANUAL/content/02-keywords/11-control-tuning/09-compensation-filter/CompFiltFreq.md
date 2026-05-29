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

The low-pass acts on the difference between the measured force and the table-predicted force. A higher cut-off lets the output follow the measured force sensor over a wider (faster) band; a lower cut-off restricts the sensor to only the slowest corrections and lets the smooth, table-predicted force govern the faster variation.

This keyword is available from v5 (central-i v5).

## How it works

The value is interpreted as a frequency in hertz and converted internally into a single-pole low-pass coefficient using the controller sample period; the resulting filter has its -3 dB point at the frequency you specify. The coefficient is recomputed whenever the frequency is changed, so updates take effect without disabling the filter.

The firmware accepts a range of 1 to 1000 Hz with a default of 200 Hz.

### Filter math

The cut-off frequency $f_c$ is mapped to the exponential-smoothing coefficient
$$\alpha = e^{-2\pi f_c\,T_s}$$
where $T_s$ is the controller sample period. The difference between the measured force $F_m$ and the table-predicted force $F_t$, $d_k = F_{m,k} - F_{t,k}$, is then run through the one-pole recurrence
$$d_{\text{filt},k} = \alpha\,d_{\text{filt},k-1} + (1-\alpha)\,d_k$$
and the output handed to force control is $d_{\text{filt},k} + F_{t,k}$. A higher $f_c$ makes $\alpha$ smaller, so the filtered difference reacts faster (a wider band of the measured sensor passes through); a lower $f_c$ pushes $\alpha$ toward 1, so the difference is smoothed more heavily and only the slowest corrections from the sensor survive.

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
