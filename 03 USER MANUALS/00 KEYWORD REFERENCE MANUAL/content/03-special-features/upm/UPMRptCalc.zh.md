---
keyword: UPMRptCalc
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 560
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 1
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 触发根据累积位置误差数据计算 UPM 重复补偿表的命令。
---
# UPMRptCalc

**定义：**

UPMRptCalc 是一条触发命令，用于根据累积的位置误差数据计算 UPM 重复补偿表。轴运动中不可更改；电机使能时可更改。该命令为轴相关命令，不保存至闪存。

若 UPM 重复计算没有可用的有效被控对象模型，则计算返回错误 236；若捕获的运动长度加上扩展的 UPMRptTime 尾部超出 UPM 重复数组的可用空间，则返回错误 150。

**另请参阅：**

[UPMRptOn](UPMRptOn.md)、[UPMRptState](UPMRptState.md)、[UPMRptLevel](UPMRptLevel.md)
