---
keyword: MotorLearnOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 444
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 启用电机学习例程，以测量极对数和编码器分辨率。
---
# MotorLearnOn

**定义：**

MotorLearnOn 启用电机学习例程，该例程以开环方式驱动电机（按照 MotorLearnMod 所选模式，以 MotorLearnInc 步进量推进换相电角度），以测量并报告电机极对数（MotorLearnPl）和编码器分辨率（MotorLearnRes）；进度由 MotorLearnSta 报告。有效值为 0（关闭）和 1（开启）。将其设置为 1 会自动使能电机，并清除上次的控制器故障和电机关闭原因。该例程可对旋转或直线无刷电机产生结果。在自动模式下，一旦过程完成（MotorLearnSta = 3）或失败（MotorLearnSta = 4），控制器会将 MotorLearnOn 清零回 0 并关闭电机；若经过 20 个以上电气周期仍未找到两个连续索引脉冲，旋转轴的过程将失败。在轴处于运动中时，该参数不可更改；电机开启时可更改。这是一个轴相关参数，不保存至闪存。

**另请参阅：**

[MotorLearnMod](MotorLearnMod.md)、[MotorLearnSta](MotorLearnSta.md)、[MotorLearnRes](MotorLearnRes.md)、[MotorLearnInc](MotorLearnInc.md)
