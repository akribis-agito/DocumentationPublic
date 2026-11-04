---
keyword: SpringCurrFFW
summary: 弹簧补偿叠加的与位置无关的恒定前馈电流（单位：微安）。
availability:
- controller
- ci-master
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
  - -16000000
  - 16000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000000
    - 64000000
  agc300-et:
    range:
    - -4000000
    - 4000000
  agc301-et:
    range:
    - -4000000
    - 4000000
  agc301-et-bioxtreme:
    range:
    - -4000000
    - 4000000
  agd200-et-2d01:
    range:
    - -4000000
    - 4000000
  agd200-et-2d02:
    range:
    - -8000000
    - 8000000
  agd301-et-2d01:
    range:
    - -4000000
    - 4000000
  agd301-et-2d02:
    range:
    - -8000000
    - 8000000
  agd301-et-2d09:
    range:
    - -25500000
    - 25500000
  agd155-af-2a06:
    range:
    - -25500000
    - 25500000
  agd155-af-2a10:
    range:
    - -28500000
    - 28500000
  agd155-ec:
    range:
    - -25500000
    - 25500000
  agd155-ec-var34:
    range:
    - -28500000
    - 28500000
  agd155-ec-var34-3:
    range:
    - -42500000
    - 42500000
  agd156-ec:
    range:
    - -12726000
    - 12726000
  agd101-ec-34a:
    range:
    - -28280000
    - 28280000
  agd101-ec-17a:
    range:
    - -14140000
    - 14140000
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# SpringCurrFFW

**定义：**

SpringCurrFFW 设置一个恒定的、与位置无关的前馈电流（单位：微安），由弹簧补偿叠加。当位置参考处于 [SpringPLow](SpringPLow.md) 与 [SpringPHigh](SpringPHigh.md) 定义的区间内时，该偏置电流始终有效，且不随位置变化；弹簧补偿中与位置成比例的部分由 [SpringPosFFW](SpringPosFFW.md) 提供。该参数为轴相关参数，保存至闪存，可随时更改。

默认值为 0（无恒定偏置）。允许范围从负到正轴最大电流指令值（以微安表示，即最大电流指令（mA）乘以 1000）。输入的微安值在叠加至电流参考之前会乘以 0.001 转换为毫安，因此仍受下游正常电流与转矩限制的约束。

**另请参阅：**

[SpringOn](SpringOn.md)、[SpringPosFFW](SpringPosFFW.md)、[SpringTable](SpringTable.md)
