---
keyword: RegenCurr
summary: 流经再生电阻的电流（只读）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 349
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RegenCurr

流经再生电阻的电流（只读）。

## 概述

`RegenCurr` 是一个只读状态值，报告流经再生（制动）电阻的电流。当母线电压升至 [RegenOn](RegenOn.md) 以上且制动斩波器晶体管导通时，它可让您监测再生电路在制动期间耗散了多少能量。当斩波器关断时，其读数接近零。它不保存至闪存。

## 工作原理

在具有再生电流检测的产品上，每组控制周期读取一次再生电流，并以固定的比例和偏置将原始 ADC 计数转换为电流。该转换是如下形式的仿射映射

$$
\text{RegenCurr} = \text{offset} - \text{gain} \cdot \text{reading}
$$

——即传感器位于中量程零点附近，因此原始计数被一个固定增益缩放，再从一个常数偏置中减去，从而得到带符号的结果。不具有再生电流检测的产品不会更新该值。

仅当再生处于激活状态时（即 [StatReg](../../07-status-and-faults/StatReg.md) bit 1 置位时）该值才有意义；其他时候电阻处于断开状态，读数仅反映传感器的零点。

## 示例

```text
ARegenCurr          ; read the present regen-resistor current
```

## 版本间变更

在 central-i v5 上，`RegenCurr` 以**浮点**值（`float32`，无固定整数范围）报告，而非 v4 上所用的缩放整数。底层测量相同；仅通过通信返回的数据类型发生变化，因此 v5 读取可能包含小数部分。

## 另请参阅

- [RegenOn](RegenOn.md)、[RegenOff](RegenOff.md) — 再生激活/停用阈值
- [RegenUsed](RegenUsed.md) — 启用再生电路
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 1 指示再生处于激活状态
