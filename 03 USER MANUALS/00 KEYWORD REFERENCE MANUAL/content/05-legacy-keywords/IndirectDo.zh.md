---
keyword: IndirectDo
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 437
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 执行间接数组写操作的命令。
---
# IndirectDo

**定义：**

IndirectDo 是一个用于执行间接数组写操作的命令。触发时，它将 IndirectValue 中保存的值写入 IndirectArray 所选数组中由 IndirectIndex 指定的元素。若 IndirectArray 指定的数组不受支持，写操作将被拒绝并返回错误 115。若 IndirectIndex 小于 1 或超出所选数组的大小，写操作将被拒绝并返回错误 116。当目标为 GenData 数组时，不进行值范围检查，因为该数组可存储任意值。该命令为非轴命令，不保存至闪存。

**参见：**

[IndirectArray](IndirectArray.md)、[IndirectIndex](IndirectIndex.md)、[IndirectValue](IndirectValue.md)
