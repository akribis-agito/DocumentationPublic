---
keyword: BeginSkipProt
summary: 选择 Orbit FR 对支持的 Begin 运动的软位置限位处理方式。
last_updated: '2026-11-24'
doc_revision: '2026.11'
language: zh-CN
can_code: 917
availability:
- ci-master
products:
- agm800
attributes:
  access: rw
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BeginSkipProt

此按轴关键字仅存在于 Orbit FR 版 AGM800 固件中，默认值为 0。值为 0 时，执行常规软位置限位检查。值为 1 时，对于受支持的点到点、重复和矢量 Begin 运动，Orbit 运动代码跳过目标位置的正反向软限位检查，并跳过相应的点到点目标限幅。硬限位检查仍然有效，其他运动保护仍按各自条件执行。

此设置不保存至闪存。读取 `ABeginSkipProt` 可查看 A 轴当前值。CAN 编号为 917。[FwdPLim](FwdPLim.zh.md)
