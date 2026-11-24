---
keyword: GantryMode
summary: 选择龙门轴对的坐标系及启用时的偏摆参考值。
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 916
availability:
- controller
- ci-master
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
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# GantryMode

请在已实现的电机轴对的主轴（第一个轴）上设置模式。设置前须关闭龙门，且所有切换均已完成。AGM800 的轴对为 A/B、C/D、E/F 和 G/H，辅助端口 I 至 L 不配对。三轴控制器仅 A/B 配对。

| 值 | 启用龙门时的行为 |
| --- | --- |
| 0 | 使用传统坐标，在启用时自动捕获主轴偏置。 |
| 1 | 使用对称的直线/偏摆坐标。偏摆参考从转换后的偏摆参考值开始。 |
| 2 | 使用与模式 1 相同的对称坐标。初始偏摆参考设为零，以使轴对对齐。 |

模式 1 和 2 可在启用前分别设置两轴偏置。向偏摆轴或没有配对的轴写入非零模式会返回错误 8。为兼容参数文件，这些轴可写零；对于已配对的轴，仍须满足切换状态检查。此参数按轴保存到闪存，默认值为 0。CAN 编号为 916。[GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.zh.md)
