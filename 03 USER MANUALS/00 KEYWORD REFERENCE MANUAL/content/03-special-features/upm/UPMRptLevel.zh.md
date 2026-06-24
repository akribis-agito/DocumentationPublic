---
keyword: UPMRptLevel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 554
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 100
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置 UPM 重复补偿算法中模型范围（Q）低通滤波器的截止频率。
---
# UPMRptLevel

**定义：**

UPMRptLevel 设置 UPM 重复补偿算法所使用的模型范围（Q）低通滤波器的截止频率，以百分比表示，范围为 0 至 100%，线性映射至滤波器频率范围 30 Hz（对应 0%）至 500 Hz（对应 100%）。轴运动中或电机使能时不可更改。该参数为轴相关参数，保存至闪存。

> **版本说明：** 此为该参数的 v4 名称。在 v5 中，同一参数已重命名为 [UPMRptRange](UPMRptRange.md)，以 Hz 为单位表示频率范围。两者为同一底层参数——v4 控制器请使用 `UPMRptLevel`，v5 控制器请使用 `UPMRptRange`。

**另见：**

[UPMRptRange](UPMRptRange.md)、[UPMRptOn](UPMRptOn.md)、[UPMRptCalc](UPMRptCalc.md)、[UPMRptState](UPMRptState.md)
