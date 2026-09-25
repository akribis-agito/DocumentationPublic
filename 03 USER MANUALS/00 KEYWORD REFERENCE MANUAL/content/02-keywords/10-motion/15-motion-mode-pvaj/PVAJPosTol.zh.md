---
keyword: PVAJPosTol
summary: PVAJValidate 使用的位置连续性容差。
availability:
  standalone: []
  central-i:
  - v5
can_code: 884
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: counts
  default: 1.0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
language: zh-CN
---
# PVAJPosTol

[PVAJValidate](PVAJValidate.md) 允许的位置容差：即某一 [PVAJList](PVAJList.md) 行所声明的值，与相邻行之间的五次多项式在该点所隐含的值之间的偏差。单位为 counts。

若列表由精度低于控制器自身运算的工具生成，可调大该值以接受；若需要更严格的拟合，则调小该值。完整校验在位置项上失败时报告错误 `396`。

默认值 `1.0`。当 [PVAJValidate](PVAJValidate.md) 以 `2`（不检查）或 `3`（部分）调用时不应用该容差，这两者均不检查连续性。
