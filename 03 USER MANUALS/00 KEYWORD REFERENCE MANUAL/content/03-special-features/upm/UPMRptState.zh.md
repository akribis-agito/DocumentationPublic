---
keyword: UPMRptState
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 557
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range: null
    default: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 只读参数，报告 UPM 重复补偿函数的当前运行状态。
---
# UPMRptState

**定义：**

UPMRptState 是一个只读参数，报告 UPM 重复补偿函数的当前运行状态。轴在运动中时不可更改；电机使能时可更改。该参数为轴相关状态变量，不保存至闪存。

上报值如下：

| 值 | 状态 | 含义 |
|-------|-------|---------|
| 0 | 空闲 | 重复补偿未激活（UPMRptOn 已关闭，或当前运动已结束）。这是默认状态。 |
| 1 | 激活，首次周期 | UPMRptOn 设为 1 且运动已启动；控制器正在记录首次周期的误差。 |
| 2 | 激活，重复 | UPMRptOn 设为 2 且运动已启动；控制器正在回放并自适应已学习修正，覆盖重复周期。 |

状态在运动开始时根据 UPMRptOn 设为 1 或 2，运动结束时返回 0（空闲）：对于首次周期情况，在 UPMRptTime 设定的记录尾部倒计时结束后、回放索引达到已记录周期长度时、记录达到存储数组上限时，或电机关断时。UPMRptState 仅反映此运行状态；UPMCalcCoeff 或 UPMRptCalc 不会改变该状态，也不存在单独的"已收敛"或"错误"状态。该关键字的上报范围为 0 至 4，但实际运行中只出现 0、1 和 2。

**另请参阅：**

[UPMRptOn](UPMRptOn.md)、[UPMRptCalc](UPMRptCalc.md)、[UPMRptLevel](UPMRptLevel.md)
