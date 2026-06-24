---
keyword: SpringPHigh
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 594
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
  - -2147483648
  - 2147483647
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置弹簧补偿区域的位置上边界（用户单位）。
---
# SpringPHigh

**定义：**

SpringPHigh 以用户单位设置弹簧补偿区域的位置上边界。仅当位置参考值处于 [SpringPLow](SpringPLow.md) 到 SpringPHigh 的区间内时，才会施加弹簧补偿；高于 SpringPHigh 时不添加弹簧电流。该参数为轴相关参数，保存至闪存，可随时更改。

默认值为 10000 用户单位。区间判断将整形后的滤波位置参考（即指令曲线，而非测量的反馈位置）与 [SpringPLow](SpringPLow.md) 和 SpringPHigh 进行比较，两端点均包含在内。边界之间不进行范围校验：若将 SpringPHigh 设置为低于 SpringPLow，则区间为空，弹簧补偿将永远不被施加。

**参见：**

[SpringPLow](SpringPLow.md)、[SpringOn](SpringOn.md)、[SpringTable](SpringTable.md)、[SpringTableGp](SpringTableGp.md)
