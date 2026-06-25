---
keyword: UPMVelOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 407
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 使能 UPM 齿槽补偿功能，将角度索引修正表（UPMVelTable）应用于电流参考以抵消齿槽转矩。
---
# UPMVelOn

**定义：**

UPMVelOn 使能 UPM 齿槽补偿功能，该功能将一个以角度为索引的修正表（UPMVelTable）应用于电流参考，以消除齿槽转矩。该表以换相（电气）角度（度）为索引，在每个控制周期将对应的表项叠加至电流参考。该补偿仅适用于无刷电机。UPMVelOn 为 0/1 使能开关。该参数为轴相关参数，不保存至闪存；可随时更改。

**另请参阅：**

[UPMDistOn](UPMDistOn.md)、[UPMRptOn](UPMRptOn.md)
