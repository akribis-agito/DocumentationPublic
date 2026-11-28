---
keyword: AutoGBW
summary: 设置自动增益整定算法的目标闭环带宽（Hz）。
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
can_code: 358
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
  - 2000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-25'
doc_revision: '2026.06'
language: zh-CN
---
# AutoGBW

**定义：**

AutoGBW 设置自动增益整定算法的目标闭环带宽，单位为 Hz。整定器使用该值计算所需的伺服增益，以实现指定带宽。它是一个保存至闪存的轴相关参数，可随时更改。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGMode](AutoGMode.md)、[AutoGJm](AutoGJm.md)、[AutoGKt](AutoGKt.md)
