---
keyword: VelIntLim
summary: 设置各增益调度组的速度环积分电流上限。
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 915
availability:
- controller
- ci-master
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 2147483647
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# VelIntLim

每个数组元素以 mA 表示指定轴速度环积分电流分量的最大幅值，正负方向使用同一限值。默认值 2147483647 表示不增加积分电流钳位；设为零时，该分量被钳位为零。

请为使用的各增益组设置相应元素。逐组切换时使用活动组的值；采用插值调度时，对相邻两组的限值进行插值。普通调度与龙门调度均适用。读取 `ScheduleGains[7]` 可查看当前生效的限值。此参数按轴保存到闪存，适用于已集成该功能的独立控制器和 Central-i 产品。CAN 编号为 915。

例如，`AVelIntLim[1]=1500` 将 A 轴增益组 1 的限值设为 1,500 mA。[ScheduleGains](../01-general-keywords/ScheduleGains.zh.md)
