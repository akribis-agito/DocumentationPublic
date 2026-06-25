---
keyword: MotorLearnMod
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 449
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 选择电机学习例程所使用的模式，该例程以开环方式驱动电机，以测量极对数和编码器分辨率。
---
# MotorLearnMod

**定义：**

MotorLearnMod 选择电机学习例程所使用的模式，该例程以开环方式驱动电机，以测量极对数和编码器分辨率。在轴处于运动中时，该参数不可更改；电机开启时可更改。这是一个轴相关参数，不保存至闪存。

| 值 | 含义 |
|---|---|
| 0 | 自动 |
| 1 | 手动（手动查找极对数） |

**另请参阅：**

[MotorLearnOn](MotorLearnOn.md)、[MotorLearnInc](MotorLearnInc.md)、[MotorLearnPl](MotorLearnPl.md)
