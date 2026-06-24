---
keyword: AutoGPosFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 354
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
  - 1
  - 1000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置自动增益辨识算法所用一阶低通滤波器的截止频率。
---
# AutoGPosFilt

**定义：**

AutoGPosFilt 设置自动增益辨识算法所用一阶低通滤波器的截止频率。该滤波器同时作用于算法所使用的位置信号和电流指令信号；修改此值将重新计算滤波器系数。数值越大，截止频率越高。范围为 1 至 1000，默认值为 50。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGAccTh](AutoGAccTh.md)、[AutoGVelTh](AutoGVelTh.md)
