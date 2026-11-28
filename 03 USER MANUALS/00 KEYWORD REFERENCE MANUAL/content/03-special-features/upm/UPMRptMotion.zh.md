---
keyword: UPMRptMotion
summary: 选择 UPM 重复补偿函数所使用的已学习运动槽位，从中选取与当前运动匹配的存储前馈修正表。
availability:
- controller
- ci-master
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 4
  agd155-ec:
    range:
    - 0
    - 4
  agd155-ec-var34:
    range:
    - 0
    - 4
  agd155-ec-var34-3:
    range:
    - 0
    - 4
  agd156-ec:
    range:
    - 0
    - 4
  agd101-ec-34a:
    range:
    - 0
    - 4
  agd101-ec-17a:
    range:
    - 0
    - 4
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# UPMRptMotion

**定义：**

UPMRptMotion 选择 UPM 重复补偿函数所使用的已学习运动槽位，从中选取与当前运动匹配的存储前馈修正表。其范围为 0 到（可学习运动数量 - 1）；可用槽位数量取决于控制器型号。轴在运动中时不可更改；电机使能时可更改。该参数为轴相关参数，不保存至闪存。

**另请参阅：**

[UPMRptOn](UPMRptOn.md)、[UPMRptTime](UPMRptTime.md)、[UPMRptCalc](UPMRptCalc.md)
