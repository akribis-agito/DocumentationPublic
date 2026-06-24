---
keyword: UPMDistFilter
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 606
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
  - 300
  - 3000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置 UPM 扰动抑制环路中加速度反馈低通滤波器的截止频率（Hz）。
---
# UPMDistFilter

**定义：**

UPMDistFilter 设置 UPM 扰动抑制环路中对测量加速度信号施加的低通滤波器截止频率，单位为 Hz，用于平滑该反馈信号以防止噪声放大。该滤波器为二阶低通滤波器，固定阻尼比为 0.8。其范围为 300 至 3000，默认值为 1000。轴运动中或电机使能时不可更改。该参数为轴相关参数，保存至闪存。

**另见：**

[UPMDistOn](UPMDistOn.md)、[UPMDistReject](UPMDistReject.md)、[UPMDistSystem](UPMDistSystem.md)
