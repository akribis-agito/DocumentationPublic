# General keywords

General keywords can be used across different parts of control tuning.

Customisable filters (in position, velocity, feedforward and force controls) require recalculation of internal filter coefficients upon change in order to take effect. CalcFilters will command recalculation, while FilterStatus will display the calculation status of internal coefficients, in relation to filter definition keywords (PosFiltDef, VelFiltDef, ForceFiltDef, etc.).

Gain scheduling allows switching of active position, velocity and feedforward gains as a function of various conditions (motion, temperature, input/output, etc.). It can improve on the motion performance, by adapting the controller to the changing plant. Below is the list of gains that can be scheduled:

1.  PosGain

2.  PosKi

3.  VelGain

4.  VelKi

5.  VelFFW

6.  AccFFW

User can select on how gain scheduling is done through ScheduleMode. Depending on ScheduleMode, related gain scheduling parameters (e.g. SchedulePos) must be configured. Upon satisfying certain conditions, active tuning gains set will be changed from one to the other, where all schedulable gains will change at the same time. The active scheduling set and gain value can be checked through ScheduleSet and ScheduleGains.

All schedulable tuning gains are of parameter array type with array length of 5. By default (no gain scheduling), the gain value of the first array element is used for control (e.g.: PosGain\[1\], VelGain\[1\], etc.).

The table below shows the summary of general control keywords.

| No. | Keywords | Summary |
|----|----|----|
| 1 | [CalcFilters](../../../02-keywords/11-control-tuning/01-general-keywords/CalcFilters.md) | Command for customisable filter coefficient recalculation |
| 2 | [FilterStatus](../../../02-keywords/11-control-tuning/01-general-keywords/FilterStatus.md) | Customisable filter calculation status |
| 3 | [ScheduleGains](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleGains.md) | Schedulable gains value in use |
| 4 | [ScheduleGntry](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleGntry.md) |  |
| 5 | [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) | Gain scheduling mode |
| 6 | [SchedulePos](../../../02-keywords/11-control-tuning/01-general-keywords/SchedulePos.md) | Position range of position-based gain scheduling |
| 7 | [ScheduleSet](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleSet.md) | Index of gain/tuning set in use |
| 8 | [ScheduleTemp](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleTemp.md) | Temperature range of temperature-based gain scheduling |
| 9 | [ScheduleTime](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleTime.md) | Timing variable for gain scheduling |
| 10 | [ScheduleVel](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleVel.md) | Velocity range of velocity-based gain scheduling |
