---
keyword: IndirectValue
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 435
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 保存间接访问操作的源值。
---
# IndirectValue

**定义：**

IndirectValue 保存间接访问操作的源值。在执行 IndirectDo 之前，将待写入的值设置到 IndirectValue 中，IndirectDo 将把该值写入所选数组元素。IndirectValue 接受完整的 32 位有符号范围，即 -2147483648 至 2147483647，默认值为 0。该参数为非轴参数，不保存至闪存。

**参见：**

[IndirectIndex](IndirectIndex.md)、[IndirectArray](IndirectArray.md)、[IndirectDo](IndirectDo.md)
