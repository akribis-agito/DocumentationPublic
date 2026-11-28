---
keyword: AutoGAccTh
summary: 设置加速度阈值（用户单位/秒²），低于该值的运动数据将被排除在自动增益辨识过程之外。
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
can_code: 353
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  agm800-ec:
    units: scaling
    scaling: 1.048576
last_updated: '2026-05-25'
doc_revision: '2026.06'
language: zh-CN
---
# AutoGAccTh

**定义：**

AutoGAccTh 设置加速度阈值，单位为用户单位每秒平方，低于该阈值的运动数据将被排除在自动增益辨识过程之外。该参数用于过滤低激励段，以免产生不可靠的惯量估算。它是一个保存至闪存的轴相关参数，可随时更改。

**另请参阅：**

[AutoGVelTh](AutoGVelTh.md)、[AutoGOn](AutoGOn.md)、[AutoGMinLen](AutoGMinLen.md)
