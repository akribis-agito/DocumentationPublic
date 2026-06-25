---
keyword: IndirectIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 434
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
  - 1000
  default: 1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 1
    - 10000
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 保存间接访问机制所使用的数组索引。
---
# IndirectIndex

**定义：**

IndirectIndex 保存间接访问机制所使用的数组索引。在执行 IndirectDo 之前需先写入该值，以选择 IndirectArray 所指定数组中的目标元素。索引从 1 开始，最小值为 1，默认值为 1；最大值为所选数组中用户元素的数量（GenData 数组的大小取决于控制器型号）。若在 IndirectDo 执行时索引小于 1 或超出数组大小，写操作将被拒绝并返回错误 116。该参数为非轴参数，不保存至闪存。

**另请参阅：**

[IndirectArray](IndirectArray.md)、[IndirectValue](IndirectValue.md)、[IndirectDo](IndirectDo.md)
