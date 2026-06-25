---
keyword: SpringPLow
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 593
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
  default: -10000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置弹簧补偿区域的位置下边界（用户单位）。
---
# SpringPLow

**定义：**

SpringPLow 以用户单位设置弹簧补偿区域的位置下边界。仅当位置参考值处于 SpringPLow 到 [SpringPHigh](SpringPHigh.md) 的区间内时，才会施加弹簧补偿；低于 SpringPLow 时不添加弹簧电流。SpringPLow 同时作为由 [SpringPosFFW](SpringPosFFW.md) 缩放的位置比例项的参考零点：该项在 SpringPLow 处为零，并随参考值高于该点而增大。该参数为轴相关参数，保存至闪存，可随时更改。

默认值为 -10000 用户单位。区间判断将整形后的滤波位置参考（即指令曲线，而非测量的反馈位置）与 SpringPLow 和 [SpringPHigh](SpringPHigh.md) 进行比较。无迟滞处理：当参考值离开区间时，全部弹簧补偿量（位置比例项 [SpringPosFFW](SpringPosFFW.md) 和常量偏置 [SpringCurrFFW](SpringCurrFFW.md)）将立即移除，而不会在区间边沿保持或限幅。

**另请参阅：**

[SpringPHigh](SpringPHigh.md)、[SpringOn](SpringOn.md)、[SpringTable](SpringTable.md)、[SpringTableGp](SpringTableGp.md)
