---
keyword: IndirectArray
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 436
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 选择间接访问机制所操作的目标数组。
---
# IndirectArray

**定义：**

IndirectArray 用于选择间接访问的目标数组。其值为数组选择器，而非 CAN 码；当前唯一支持的选项为 1（GenData），有效范围为 1..1，默认值为 1。IndirectArray 与 IndirectIndex 和 IndirectValue 共同构成三寄存器间接访问机制，可实现动态数组寻址。该参数为非轴参数，不保存至闪存。

**另请参阅：**

[IndirectIndex](IndirectIndex.md)、[IndirectValue](IndirectValue.md)、[IndirectDo](IndirectDo.md)
