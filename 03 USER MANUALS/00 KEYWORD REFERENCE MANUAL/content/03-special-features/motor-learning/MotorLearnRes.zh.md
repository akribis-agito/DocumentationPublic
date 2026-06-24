---
keyword: MotorLearnRes
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 446
attributes:
  access: ro
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
  - 10000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 电机学习过程完成后报告的编码器分辨率测量结果。
---
# MotorLearnRes

**定义：**

MotorLearnRes 是电机学习过程完成后报告的只读结果：学习过程中测量到的编码器分辨率。对于旋转电机，该值为两个相邻索引（标记）脉冲之间的编码器计数，即每机械转动一周的计数值；该值仅在自动模式学习完成后报告（MotorLearnSta = 3）。对于直线电机，该值为基于一个电气周期内行程距离估算出的分辨率。该参数为轴相关状态变量，不保存至闪存。

**参见：**

[MotorLearnOn](MotorLearnOn.md)、[MotorLearnSta](MotorLearnSta.md)、[MotorLearnPl](MotorLearnPl.md)
