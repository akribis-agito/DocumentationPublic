---
keyword: AutoGDownSm
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 359
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
  - 0
  - 6
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置自动增益辨识期间对运动数据所施加的降采样指数。
---
# AutoGDownSm

**定义：**

AutoGDownSm 设置在自动增益辨识过程中对采集的运动数据所施加的降采样指数。实际降采样因子为 2 的该值次幂，即有效采样时间乘以该因子（例如，值为 4 时降采样因子为 16）。增大该值可降低计算负载，但以牺牲频率分辨率为代价。轴处于运动中或电机使能时不可更改此参数。本参数为轴相关参数，保存至闪存。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGPosFilt](AutoGPosFilt.md)、[AutoGMinLen](AutoGMinLen.md)
