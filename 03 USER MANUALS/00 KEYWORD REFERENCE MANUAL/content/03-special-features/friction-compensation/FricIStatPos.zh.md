---
keyword: FricIStatPos
summary: 正方向的起动（静）摩擦电平，单位为 mA。
availability:
  standalone: []
  central-i:
  - v5
can_code: 933
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
  - -64000
  - 64000
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricIStatPos

正方向的起动（静）摩擦电平，单位为 mA。

## 概述

`FricIStatPos` 是使轴挣脱静止并开始向正方向运动所需的电流。它是以 mA 表示的绝对电平，而不是叠加在库仑电平之上的增量。适用于 AGM800 和 AGM800-EC（central-i v5）。

## 工作原理

方法 4（LuGre）和 5（Stribeck）在低速时从该电平开始，速度越过 [FricVStribPos](FricVStribPos.md) 后衰减到库仑电平（[FricIPos](FricIPos.md)）。它们只使用其幅值。象限切换补偿（[FricQSCOn](FricQSCOn.md)）以差值 |`FricIStatPos`| − |FricIPos| 作为冲击的大小。方法 1 至 3 不使用该参数。

请将其设为不低于库仑电平；低于库仑电平的值按等于库仑电平处理。

该关键字按方向分别设置，因此可以匹配两个方向负载不同的轴。在 5.3.0-rc4 下保存的值不会被转换。从 rc4 升级后，请重新输入摩擦设置。

## 示例

```text
AFricIStatPos=180  ; 正方向起动电平，mA
```

## 另请参阅

- [FricIStatNeg](FricIStatNeg.md) — 另一方向的同一电平
- [FricMethod](FricMethod.md)
- [摩擦前馈](00-overview.md) — 整定顺序
