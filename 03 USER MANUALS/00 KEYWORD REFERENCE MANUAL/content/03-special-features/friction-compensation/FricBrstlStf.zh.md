---
keyword: FricBrstlStf
summary: LuGre 刷毛刚度（σ0），供 FricMethod 4 使用（由 FricSigma0 更名）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 935
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
  - 0.0
  - 1000000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricBrstlStf

LuGre 刷毛刚度（σ0），供 FricMethod 4 使用（由 FricSigma0 更名）。

## 概述

`FricBrstlStf` 是 LuGre 模型的刷毛刚度 σ0。适用于 AGM800 和 AGM800-EC（central-i v5）。它取代 5.3.0-rc4 中的 `FricSigma0`（CAN 代码不变）。仅方法 4（LuGre）使用该参数。

## 工作原理

LuGre 把接触面看作许多在滑动前先弯曲的小刷毛。设刷毛变形为 $z$，速度反馈为 $v$：

$$
\frac{dz}{dt} = v - \frac{\sigma_0\,|v|\,z}{g(v)}, \qquad
I = \sigma_0 z + \sigma_1 \frac{dz}{dt} + \sigma_2 v
$$

其中 $g(v)$ 是由 [FricIPos](FricIPos.md)/[FricINeg](FricINeg.md)、[FricIStatPos](FricIStatPos.md)/[FricIStatNeg](FricIStatNeg.md) 和 [FricVStribPos](FricVStribPos.md)/[FricVStribNeg](FricVStribNeg.md) 构成的 Stribeck 曲线，σ0 为 [FricBrstlStf](FricBrstlStf.md)，σ1 为 [FricBrstlDmp](FricBrstlDmp.md)，σ2 为 [FricViscous](FricViscous.md)。

刷毛越硬（取值越大），模型对换向附近的微小运动响应越快。在 5.3.0-rc4 下保存的值不会被转换。从 rc4 升级后，请重新输入摩擦设置。

## 示例

```text
AFricBrstlStf=50      ; 刷毛刚度，mA 每 count
```

## 另请参阅

- [FricMethod](FricMethod.md)
- [摩擦前馈](00-overview.md)
