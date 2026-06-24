# 通用关键字

通用关键字可跨控制整定的不同部分使用。

可自定义滤波器（位于位置、速度、前馈和力控制路径中）在定义更改后需重新计算内部滤波器系数方可生效。CalcFilters 用于命令重新计算，FilterStatus 用于显示内部系数的计算状态，与滤波器定义关键字（PosFiltDef、VelFiltDef、ForceFiltDef 等）相关联。

增益调度允许根据各种条件（运动状态、温度、输入/输出等）切换有效的位置、速度和前馈增益，从而通过使控制器适应变化的被控对象来提升运动性能。以下增益支持调度：

1.  PosGain

2.  VelGain

3.  VelKi

4.  VelFFW

5.  AccFFW

6.  PosKi（仅限 central-i v5）

用户可通过 ScheduleMode 选择增益调度方式。根据 ScheduleMode 的不同，需配置相关增益调度参数（如 SchedulePos）。满足特定条件时，有效整定增益组将从一组切换至另一组，所有可调度增益同时切换。有效调度组及增益值可通过 ScheduleSet 和 ScheduleGains 查看。

所有可调度整定增益均为参数数组类型，数组长度为 5。默认情况下（无增益调度），控制使用第一个数组元素的增益值（例如：PosGain\[1\]、VelGain\[1\] 等）。

下表为通用控制关键字汇总。

| 序号 | 关键字 | 说明 |
|----|----|----|
| 1 | [CalcFilters](../../../02-keywords/11-control-tuning/01-general-keywords/CalcFilters.md) | 命令可自定义滤波器系数重新计算 |
| 2 | [ClearIntegral](../../../02-keywords/11-control-tuning/01-general-keywords/ClearIntegral.md) | 将速度环积分器清零的命令 |
| 3 | [FilterStatus](../../../02-keywords/11-control-tuning/01-general-keywords/FilterStatus.md) | 可自定义滤波器的计算状态 |
| 4 | [ScheduleGains](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleGains.md) | 当前使用的可调度增益值 |
| 5 | [ScheduleGntry](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleGntry.md) | 将增益调度与龙门控制状态关联（仅限 central-i v5） |
| 6 | [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) | 增益调度模式 |
| 7 | [SchedulePos](../../../02-keywords/11-control-tuning/01-general-keywords/SchedulePos.md) | 基于位置的增益调度的位置范围 |
| 8 | [ScheduleSet](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleSet.md) | 当前使用的增益/整定组索引 |
| 9 | [ScheduleTemp](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleTemp.md) | 基于温度的增益调度的温度范围 |
| 10 | [ScheduleTime](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleTime.md) | 增益调度的时间变量 |
| 11 | [ScheduleVel](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleVel.md) | 基于速度的增益调度的速度范围 |
