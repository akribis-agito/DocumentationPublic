---
keyword: StatRegExt
summary: 只读轴状态字，报告自适应直流母线补偿是否达到上限。
availability:
- controller
- ci-master
can_code: 966
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
last_updated: '2026-11-24'
doc_revision: '2026.11'
language: zh-CN
---
# StatRegExt

`StatRegExt` 报告所选轴最近一次电流环执行时的状态。电机运行时可读取此关键字，也可将其选为记录器通道。

| 位 | 置 1 的条件 |
| --- | --- |
| 0 | 无刷电机电流环将自适应直流母线补偿的最大倍率 1.2 应用于该轴的电压指令。 |
| 1–31 | 保留。 |

当电流环使用较低倍率、禁用或旁路补偿，或电机下使能时，位 0 清零。此位指示实际应用的补偿倍率；电压输出饱和另由 [StatReg](StatReg.zh.md) 报告。共用母线的控制器上，各轴使用相同的母线测量值，并分别报告自身电流环是否应用了最大倍率。

以 A 轴为例，读取 `AStatRegExt`，用 `AStatRegExt & 1` 检查位 0。同时记录 [VBusRatio](../09-current-and-voltage/01-system-variables/VBusRatio.zh.md) 和 [AdVBusEn](../09-current-and-voltage/01-system-variables/AdVBusEn.zh.md)，即可查看补偿达到上限的时段。使用旧版固件时，请先确认控制器支持 `StatRegExt`。
