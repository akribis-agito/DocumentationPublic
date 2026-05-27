---
keyword: CalcFilters
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 360
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
---
# CalcFilters

**Definition:**

CalcFilters is the command that instructs the controller to recalculate the internal filter coefficients for customisable filters. This command should be run only after all the filter changes are consolidated.

Below is an example of good and bad orders of messages, when configuring velocity filter 1 to be notch filter at 450Hz, 6dB attenuation and 40Hz width.

1.  Good message order

> BM: VelFiltDef\[1\] = 8; VelFiltDef\[2\] = 45000; VelFiltDef\[3\]=6; VelFiltDef\[4\]=4000; **CalcFilters**

2.  Bad message order

> BM: VelFiltDef\[1\] = 8; VelFiltDef\[2\] = 45000; **CalcFilters**; VelFiltDef\[3\]=6; VelFiltDef\[4\]=4000

| Parameters | Initial values | Good message order, upon receipt of CalcFilters | Bad message order, upon receipt of CalcFilters |
|---|---|---|---|
| VelFiltOn[1] | 1 | 1 | 1 |
| VelFiltDef[1] | 1 | 8 | 8 |
| VelFiltDef[2] | 20000 | 45000 | 45000 |
| VelFiltDef[3] | 0 | 6 | 0 |
| VelFiltDef[4] | 0 | 4000 | 0 |
| VelFiltDef[5] | 0 | 0 | 0 |
| Interpretation | Velocity filter 1 - first-order low-pass filter at 200Hz - turned on | Velocity filter 1 - notch filter at 450Hz, 6dB depth and 40Hz width - turned on **The changes are accepted.** | Velocity filter 1 - notch filter at 450Hz, 0dB depth and 0Hz width - turned on **The changes will be rejected as they define invalid filter setting!** **VelFilDef[1] and VelFiltDef[2] will revert to initial values (velocity filter 1 is still a low-pass filter).** **VelFiltDef[3] and VelFiltDef[4] will be the unapplied changes.** |

The following is the list of keywords that require CalcFilters command upon change in value:

1.  PosFiltDef/PosFiltOn (position filters)

2.  VelFiltDef/VelFiltOn (velocity filters)

3.  FFFiltDef/FFFiltOn (feedforward filter)

4.  ForceFiltDef/ForceFiltOn (force filters)
