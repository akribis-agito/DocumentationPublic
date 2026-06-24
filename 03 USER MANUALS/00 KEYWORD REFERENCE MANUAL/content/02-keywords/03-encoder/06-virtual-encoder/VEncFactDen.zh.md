---
keyword: VEncFactDen
summary: 应用于虚拟编码器源信号的缩放比值的分母。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 618
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
  - 1
  - 500000000
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VEncFactDen

应用于虚拟编码器源信号的缩放比值的分母。

## 概述

`VEncFactDen` 是应用于虚拟编码器源的缩放比值的分母。它与 [VEncFact](VEncFact.md) 一起定义了精确的有理缩放因子（`VEncFact / VEncFactDen`），用于在虚拟编码器启用（[VEncOn](VEncOn.md) = 1）时将源变量转换为所发出的编码器计数。其范围为 1 到 500,000,000，且必须为正（方向反向通过为 [VEncFact](VEncFact.md) 取负值来实现）。它是一个保存至闪存的轴相关参数，可在电机使能或运动中更改。

## 工作原理

$$\text{Output count} = \text{Source} \cdot \frac{\text{VEncFact}}{\text{VEncFactDen}}$$

固件为逐周期的跟踪计算保留了一个预先计算好的 `1 / VEncFactDen`，每当写入缩放因子时即更新。默认值 `VEncFactDen = 65536`（配合 `VEncFact = 65536`）给出单位缩放，并与旧固件使用的固定 `/65536` 因子相匹配。

## 示例

```text
AVEncFactDen=65536       ; unity scale when VEncFact=65536
```

## 另请参阅

- [VEncFact](VEncFact.md) —— 缩放比值的分子（取负值可反转方向）
- [VEncOn](VEncOn.md) —— 启用虚拟编码器
- [VEncSrc](VEncSrc.md) —— 被缩放的源变量
