---
keyword: SpringTable
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 597
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 41
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 保留的、尚未实现的数组关键字（大小为 41，可用索引为 1 至 40）。
---
# SpringTable

**定义：**

SpringTable 是一个保留的、尚未实现的数组关键字（大小为 41，可用索引为 1 至 40），当前对弹簧补偿无任何效果。有效的补偿为由 [SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)、[SpringPosFFW](SpringPosFFW.md) 和 [SpringCurrFFW](SpringCurrFFW.md) 定义的线性模型。实现后，其各元素将以 1 为起始索引保存每段的电流修正值。该参数为轴相关数组参数，保存至闪存，可随时更改。

**另请参阅：**

[SpringOn](SpringOn.md)、[SpringTableGp](SpringTableGp.md)、[SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)
