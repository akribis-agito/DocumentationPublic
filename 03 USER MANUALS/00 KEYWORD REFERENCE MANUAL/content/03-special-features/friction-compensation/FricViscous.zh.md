---
keyword: FricViscous
summary: 粘性摩擦斜率：每 count/s 速度反馈对应的附加电流。
availability:
  standalone: []
  central-i:
  - v5
can_code: 932
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
  - -1.0
  - 1.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricViscous

粘性摩擦斜率：每 count/s 速度反馈对应的附加电流。

## 概述

`FricViscous` 叠加与速度成正比的电流，用于随速度增大的摩擦（润滑剂阻力、密封）。单位为 mA 每 count/s。适用于 AGM800 和 AGM800-EC（central-i v5）。

## 工作原理

该环节在方法 1、2、3 和 5 上叠加 `FricViscous` × 速度反馈。无论 [FricVelSrc](FricVelSrc.md) 如何设置，它始终使用速度反馈。LuGre（方法 4）把它用作粘性系数（σ2）。默认值为 0（无粘性项）。

请在偏置和各方向电平之后最后整定：让轴以几个恒定速度运行，设置斜率，使剩余电流不再随速度增大。

## 示例

```text
AFricViscous=0.002   ; 每 1000 counts/s 额外 2 mA
```

## 另请参阅

- [FricMethod](FricMethod.md)
- [摩擦前馈](00-overview.md) — 整定顺序
