---
keyword: UPMDistReject
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 605
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 100
  - 2000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置 UPM 扰动抑制环路的抑制增益，控制估计扰动的消除力度。
---
# UPMDistReject

**定义：**

UPMDistReject 设置 UPM 扰动抑制环路的抑制增益，控制对估计扰动的消除力度。其范围为 100 至 2000，默认值为 1000。该参数为轴相关参数，保存至闪存，可在任意时刻更改，包括运动中和电机使能时。

当 UPMDistOn 使能后，控制器在每个控制周期持续运行一个积分扰动观测器环路：计算指令电流（电流参考值乘以被控对象增益 UPMDistSystem）所对应的预期加速度与经 UPMDistFilter 低通滤波后的测量加速度之差，将该差值乘以此处设置的有效增益后积分；积分器输出成为新的电流参考值。有效积分器增益与 UPMDistReject 成正比，与 UPMDistSystem 成反比，因此较大的 UPMDistReject 将更积极地抑制扰动，而较大的 UPMDistSystem 则会降低抑制力度。该环路持续作用于估计的扰动，并不特定于周期性扰动。

**另请参阅：**

[UPMDistOn](UPMDistOn.md)、[UPMDistSystem](UPMDistSystem.md)、[UPMDistFilter](UPMDistFilter.md)
