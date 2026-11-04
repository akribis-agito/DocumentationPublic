---
keyword: AutoGPosFilt
summary: 设置自动增益辨识算法所用一阶低通滤波器的截止频率。
availability:
- controller
- ci-master
products:
- agc300-et
- agc301-et
- agc301-et-bioxtreme
- agd155-af-2a06
- agd155-af-2a10
- agd200-et-2d01
- agd200-et-2d02
- agd200-et-2d05
- agd200-et-2d05-71
- agd301-et-2d01
- agd301-et-2d02
- agd301-et-2d05
- agd301-et-2d09
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
---
# AutoGPosFilt

**定义：**

AutoGPosFilt 设置自动增益辨识算法所用一阶低通滤波器的截止频率。该滤波器同时作用于算法所使用的位置信号和电流指令信号；修改此值将重新计算滤波器系数。数值越大，截止频率越高。范围为 1 至 1000，默认值为 50。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGAccTh](AutoGAccTh.md)、[AutoGVelTh](AutoGVelTh.md)
