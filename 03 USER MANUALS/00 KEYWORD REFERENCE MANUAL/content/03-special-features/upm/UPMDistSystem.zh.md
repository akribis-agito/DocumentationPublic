---
keyword: UPMDistSystem
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 604
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
  - 1
  - 100000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置 UPM 扰动抑制算法所使用的标量被控对象增益估计值。
---
# UPMDistSystem

**定义：**

UPMDistSystem 设置 UPM 扰动抑制算法所使用的标量被控对象增益估计值。控制器将指令电流乘以该增益以预测预期加速度；同时，抑制强度与该值成反比。其范围为 1 至 100000000，默认值为 1000。轴运动中或电机使能时不可更改。该参数为轴相关参数，保存至闪存。

**另见：**

[UPMDistOn](UPMDistOn.md)、[UPMDistReject](UPMDistReject.md)、[UPMDistFilter](UPMDistFilter.md)
