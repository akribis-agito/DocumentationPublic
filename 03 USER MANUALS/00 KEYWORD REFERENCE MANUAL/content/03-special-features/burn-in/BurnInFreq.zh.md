---
keyword: BurnInFreq
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 425
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 100000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
summary: 设置老化测试运动的电气旋转（换相）频率，单位为 0.01 Hz（例如，1000 = 10 Hz）。
---
# BurnInFreq

**定义：**

BurnInFreq 设置老化测试运动的电气旋转（换相）频率，单位为 0.01 Hz（例如，1000 = 10 Hz）。范围为 1（0.01 Hz）至 100000（1000 Hz）；默认值为 1000（10 Hz）。轴运动中不可修改；电机使能时可修改。这是一个轴相关参数，保存至闪存。

老化测试期间，控制器以此频率开环旋转电机的电角度（换相角），每秒完成 `BurnInFreq` × 0.01 次电气旋转（例如，`1000` = 10 电气 Hz）。该速率与控制采样率无关。对于旋转无刷电机，实际机械转速等于电气频率除以极对数：机械转速 (rev/s) = (`BurnInFreq` × 0.01) / [PolePrs](../../02-keywords/02-motor-and-amplifier/PolePrs.md)。

**另请参阅：**

[BurnInMode](BurnInMode.md)
