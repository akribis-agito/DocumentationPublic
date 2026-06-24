---
summary: 叠加在电机电流参考之上的电流参考偏置（mA）。
keyword: CurrRefOffset
availability:
  standalone: []
  central-i:
  - v5
can_code: 599
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -6400
  - 6400
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrRefOffset

叠加在电机电流参考之上的电流参考偏置（mA）。

## 概述

`CurrRefOffset` 是电流参考偏置，单位为毫安，叠加在电机的电流参考之上。由于它是在电流环（而非位置/速度环）中相加的，因此它是环路侧转矩补偿 [TorqCompMode](TorqCompMode.md)/[TorqCompFix](TorqCompFix.md) 在电流环中的对应项。其作用点参见 [Control tuning – Current control](../../11-control-tuning/06-current-control/00-overview.md)。

## 工作原理

在电流控制环中，当电机已使能且换相（自动定相）已完成时，固件会在每个控制周期将 `CurrRefOffset` 直接**加到**电流参考上：

$$
\text{CurrRef} \mathrel{+}= \text{CurrRefOffset}
$$

该偏置在无刷电机齿槽补偿项（[UPMVelTable](UPMVelTable.md)）之后、电流限制与饱和处理之前施加，因此它是电流参考上的一个恒定偏置，且仍受下游电流限制约束。固件特意只在换相完成后才施加它：任何引入直流偏置的电流注入都必须等待相位初始化，否则一台已使能但未定相的电机可能会失控飞车。

由于电流参考会成为磁场定向电流环的交轴（产生转矩）指令——[IqRef](../02-motor-variables/IqRef.md) 取用最终的电流参考，而直轴（励磁）参考 [IdRef](../02-motor-variables/IdRef.md) 保持为 0——`CurrRefOffset` 仅偏置 q 轴（产生转矩）参考，绝不偏置 d 轴（励磁）参考。

此关键字仅在 central-i v5 上存在，此时电流参考为浮点数。其范围受电流指令范围限定（其限值由驱动器的最大电流指令推导得出）。

## 示例

```text
ACurrRefOffset=500   ; add a 500 mA offset to the motor current reference
ACurrRefOffset      ; read the present offset
```

## 另请参阅

- [CurrRef](../02-motor-variables/CurrRef.md) — 偏置所施加的最终电机电流指令
- [TorqCompMode](TorqCompMode.md)、[TorqCompFix](TorqCompFix.md) — 环路侧电流补偿（施加较早，仅在位置/速度模式下）
- [UPMVelTable](UPMVelTable.md) — 按角度索引的电流补偿（在此恒定偏置之前施加）
