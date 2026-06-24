---
keyword: SpringCurrFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 596
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000000
  - 64000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 弹簧补偿叠加的与位置无关的恒定前馈电流（单位：微安）。
---
# SpringCurrFFW

**定义：**

SpringCurrFFW 设置一个恒定的、与位置无关的前馈电流（单位：微安），由弹簧补偿叠加。当位置参考处于 [SpringPLow](SpringPLow.md) 与 [SpringPHigh](SpringPHigh.md) 定义的区间内时，该偏置电流始终有效，且不随位置变化；弹簧补偿中与位置成比例的部分由 [SpringPosFFW](SpringPosFFW.md) 提供。该参数为轴相关参数，保存至闪存，可随时更改。

默认值为 0（无恒定偏置）。允许范围从负到正轴最大电流指令值（以微安表示，即最大电流指令（mA）乘以 1000）。输入的微安值在叠加至电流参考之前会乘以 0.001 转换为毫安，因此仍受下游正常电流与转矩限制的约束。

**参见：**

[SpringOn](SpringOn.md)、[SpringPosFFW](SpringPosFFW.md)、[SpringTable](SpringTable.md)
