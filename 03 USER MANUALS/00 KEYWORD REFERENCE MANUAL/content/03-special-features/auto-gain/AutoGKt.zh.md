---
keyword: AutoGKt
summary: 存储自动增益整定算法所使用的电机转矩常数（Kt），用于在计算基于带宽的增益时将电流指令换算为力或力矩。
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
can_code: 362
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
  - 2147483647
  default: 38231
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AutoGKt

**定义：**

AutoGKt 存储自动增益整定算法所使用的电机转矩常数（Kt），用于在计算基于带宽的增益时将电流指令与力或力矩相关联。它与 AutoGJm 中的电机转动惯量值共同用于估算负载与电机的惯量比。有效范围为 1 至 2147483647，默认值为 38231。本参数为轴相关参数，保存至闪存，可随时更改。

**另请参阅：**

[AutoGBW](AutoGBW.md)、[AutoGJm](AutoGJm.md)、[AutoGOn](AutoGOn.md)
