---
keyword: PVAJVelTol
summary: PVAJValidate 使用的速度连续性容差。
availability:
  standalone: []
  central-i:
  - v5
can_code: 885
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: counts/second
  default: 100.0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
language: zh-CN
---
# PVAJVelTol

[PVAJValidate](PVAJValidate.md) 允许的速度容差：即某一 [PVAJList](PVAJList.md) 行所声明的值，与相邻行之间的五次多项式在该点所隐含的值之间的偏差。单位为 counts/秒。

完整校验在速度项上失败时报告错误 `397`。

默认值 `100.0` —— 按比例而言比 [PVAJPosTol](PVAJPosTol.md) 宽松，因为速度列通常是轨迹生成器微分的产物，会带有该微分过程的噪声。当 [PVAJValidate](PVAJValidate.md) 以 `2`（不检查）或 `3`（部分）调用时不应用该容差。
