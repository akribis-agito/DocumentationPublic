---
keyword: UPMRptMotion
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 562
attributes:
  access: rw
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 选择 UPM 重复补偿函数所使用的已学习运动槽位。
---
# UPMRptMotion

**定义：**

UPMRptMotion 选择 UPM 重复补偿函数所使用的已学习运动槽位，从中选取与当前运动匹配的存储前馈修正表。其范围为 0 到（可学习运动数量 - 1）；可用槽位数量取决于控制器型号。轴在运动中时不可更改；电机使能时可更改。该参数为轴相关参数，不保存至闪存。

**另请参阅：**

[UPMRptOn](UPMRptOn.md)、[UPMRptTime](UPMRptTime.md)、[UPMRptCalc](UPMRptCalc.md)
