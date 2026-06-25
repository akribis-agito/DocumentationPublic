---
keyword: UPMDistOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 603
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 使能 UPM 扰动抑制功能。
---
# UPMDistOn

**定义：**

UPMDistOn 使能 UPM 扰动抑制功能。激活后，控制器运行一个扰动观测器式加速度反馈环路：将指令电流（电流参考值乘以被控对象增益 UPMDistSystem）所对应的预期加速度与经低通滤波的测量加速度进行比较，然后对差值进行积分；积分器输出成为新的电流参考值，从而抑制估计的扰动。UPMDistOn 为 0/1 使能开关，为轴相关参数，不保存至闪存；可在任意时刻更改。

**另请参阅：**

[UPMDistSystem](UPMDistSystem.md)、[UPMDistReject](UPMDistReject.md)、[UPMDistFilter](UPMDistFilter.md)、[UPMVelOn](UPMVelOn.md)
