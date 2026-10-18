---
keyword: FricIPos
summary: 正方向的库仑（滑动）摩擦电平，单位为 mA。
availability:
  standalone: []
  central-i:
  - v5
can_code: 928
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
# FricIPos

正方向的库仑（滑动）摩擦电平，单位为 mA。

## 概述

`FricIPos` 是轴越过死区带后，在正方向保持运动所需的摩擦电流，单位为 mA。适用于 AGM800 和 AGM800-EC（central-i v5）。

## 工作原理

方法 1、2 和 3 把 `FricIPos` 作为带符号的电平使用：通常为正值。方法 4 和 5 只使用其幅值，符号取自运动方向。象限切换补偿用它计算起动超出量（|[FricIStatPos](FricIStatPos.md)| − |FricIPos|）。

不要用这个电平承载重力或其他恒定偏置；请将其放入 [TorqCompFix](../../02-keywords/09-current-and-voltage/03-current-compensation/TorqCompFix.md)，`FricIPos` 只用于摩擦。

该关键字按方向分别设置，因此可以匹配两个方向负载不同的轴。在 5.3.0-rc4 下保存的值不会被转换。从 rc4 升级后，请重新输入摩擦设置。

## 示例

```text
AFricIPos=120     ; 正方向库仑电平，mA
```

## 另请参阅

- [FricINeg](FricINeg.md) — 另一方向的同一电平
- [FricMethod](FricMethod.md)
- [摩擦前馈](00-overview.md) — 整定顺序
