---
keyword: MotorLearnInc
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 445
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1200
  default: 600
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range: null
    default: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 电机学习例程中换相电角度的步进量。
---
# MotorLearnInc

**定义：**

MotorLearnInc 设置电机学习例程所使用的换相角步进量：在学习过程中，电机以开环方式驱动时，每一步换相电角度的推进量。默认值约为 90 电气度，上限约为 180 电气度。在轴处于运动中或电机开启时，该参数不可更改。这是一个保存至闪存的轴相关参数。

**另请参阅：**

[MotorLearnOn](MotorLearnOn.md)、[MotorLearnMod](MotorLearnMod.md)、[MotorLearnPl](MotorLearnPl.md)
