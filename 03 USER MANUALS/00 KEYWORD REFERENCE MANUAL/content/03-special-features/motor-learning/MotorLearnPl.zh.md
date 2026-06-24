---
keyword: MotorLearnPl
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 447
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 50
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 自动模式电机学习完成后报告的极对数（旋转电机）或固定值 1（直线电机）。
---
# MotorLearnPl

**定义：**

MotorLearnPl 是自动模式电机学习过程完成后（MotorLearnSta = 3）报告的只读结果。对于旋转电机，它是学习到的极对数（即一个机械转动周期内所包含的电气周期数，范围为 1 至 50）；对于直线电机，该值报告为 1。它仅由自动模式学习更新，不受手动模式学习影响。该参数为轴相关状态变量，不保存至闪存。

**参见：**

[MotorLearnOn](MotorLearnOn.md)、[MotorLearnSta](MotorLearnSta.md)、[MotorLearnRes](MotorLearnRes.md)
