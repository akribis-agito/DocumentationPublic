---
keyword: MotorLearnSta
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 448
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
  - 0
  - 5
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 报告电机学习过程当前状态的只读参数。
---
# MotorLearnSta

**定义：**

MotorLearnSta 是报告电机学习过程当前状态的只读参数。该参数为轴相关状态变量，不保存至闪存。

| 值 | 含义 |
|---|---|
| 0 | 未激活（无学习进行中） |
| 1 | 自动模式学习进行中 |
| 2 | 手动模式学习进行中 |
| 3 | 自动模式学习成功完成 |
| 4 | 自动模式学习失败 |
| 5 | 已停止——学习过程中电机意外关闭（参见 [MotorReason](../../02-keywords/07-status-and-faults/MotorReason.md)） |

**另请参阅：**

[MotorLearnOn](MotorLearnOn.md)、[MotorLearnRes](MotorLearnRes.md)、[MotorLearnPl](MotorLearnPl.md)
