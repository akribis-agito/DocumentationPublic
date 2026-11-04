---
keyword: AutoGOn
summary: 使能自动增益整定过程。
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
can_code: 361
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
---
# AutoGOn

**定义：**

AutoGOn 用于使能自动增益整定过程。设置为 1 时，控制器开始采集运动数据，并根据已配置的 AutoG 参数计算最优伺服增益。设置回 0 时，过程停止，其累积的数据与状态将被清除；重新使能后，内部滤波器需经过若干计算周期重新稳定，之后报告的结果才重新有效。该参数为轴相关参数，不保存至闪存。

**另请参阅：**

[AutoGMode](AutoGMode.md)、[AutoGStatus](AutoGStatus.md)、[AutoGBW](AutoGBW.md)、[AutoGCopy](AutoGCopy.md)
