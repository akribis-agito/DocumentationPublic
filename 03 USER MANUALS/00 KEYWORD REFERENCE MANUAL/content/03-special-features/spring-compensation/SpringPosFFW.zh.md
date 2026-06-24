---
keyword: SpringPosFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 595
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
  - -100000
  - 100000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置位置前馈增益，用于缩放叠加到控制输出的位置相关弹簧修正电流。
---
# SpringPosFFW

**定义：**

SpringPosFFW 设置位置前馈增益，用于缩放叠加到控制输出的位置相关弹簧修正电流。该参数为轴相关参数，保存至闪存，可随时更改。

有效的弹簧补偿采用线性（位置比例加常量）模型，而非查找表。当 [SpringOn](SpringOn.md) 非零且位置参考位于 [SpringPLow](SpringPLow.md) 到 [SpringPHigh](SpringPHigh.md) 区间内时，在速度环输出处（紧接电流/转矩环之前）向轴电流参考叠加一个补偿电流：

$$ I_{spring} = (P_{ref} - \text{SpringPLow}) \cdot \text{SpringPosFFW} \cdot 0.001 + \text{SpringCurrFFW} \cdot 0.001 \;\; [\text{mA}] $$

其中 $P_{ref}$ 为整形后的滤波位置参考（即指令曲线，而非测量的反馈位置），SpringPosFFW 的单位为微安/位置计数，SpringCurrFFW 的单位为微安。SpringPLow 和位置参考以用户单位输入，内部转换为位置计数。叠加的电流被求和至电流参考（单位 mA），因此仍受下游正常电流和转矩限值的约束。在区间外不添加任何弹簧电流。

**另请参阅：**

[SpringOn](SpringOn.md)、[SpringCurrFFW](SpringCurrFFW.md)、[SpringTable](SpringTable.md)
