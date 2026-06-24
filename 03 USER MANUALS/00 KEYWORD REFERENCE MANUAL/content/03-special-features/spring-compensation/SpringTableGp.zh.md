---
keyword: SpringTableGp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 598
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 1
  - 10000000
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 保留的、尚未实现的关键字，表示相邻 SpringTable 条目之间的位置间距（用户单位），当前对弹簧补偿无效。
---
# SpringTableGp

**定义：**

SpringTableGp 是一个保留的、尚未实现的关键字，以用户单位表示，与同样尚未实现的 [SpringTable](SpringTable.md) 相关联。其预期作用是相邻 SpringTable 条目之间的位置间距（间隔），取值范围为 1 至 10000000，默认值为 100。当前对弹簧补偿无任何效果；有效的补偿为由 [SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)、[SpringPosFFW](SpringPosFFW.md) 和 [SpringCurrFFW](SpringCurrFFW.md) 定义的线性模型。该参数为轴相关参数，以用户单位表示，保存至闪存，可随时更改。

**另请参阅：**

[SpringTable](SpringTable.md)、[SpringPLow](SpringPLow.md)、[SpringPHigh](SpringPHigh.md)
