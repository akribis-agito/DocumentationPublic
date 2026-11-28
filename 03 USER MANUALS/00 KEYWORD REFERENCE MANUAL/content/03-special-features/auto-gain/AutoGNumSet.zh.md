---
keyword: AutoGNumSet
summary: 选择自整定算法将计算所得参数写入的增益（控制）组。
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
can_code: 369
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
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# AutoGNumSet

**定义：**

AutoGNumSet 选择自整定算法将计算所得参数写入的增益（控制）组。四个整定参数（位置增益、速度增益、速度积分增益和加速度前馈增益）将被保存到所选组中，保存时机为全自动模式下的自动应用，或通过 AutoGCopy 手动应用结果时。在这四个参数中，只有在 AutoGMask 中启用的参数才会实际被写入。范围 1 至 5；默认值 1。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGQualTh](AutoGQualTh.md)、[AutoGOn](AutoGOn.md)、[AutoGStatus](AutoGStatus.md)
