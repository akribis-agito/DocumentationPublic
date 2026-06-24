---
summary: 每轴矢量到编码器缩放比分子（VecEncFactNu / VecEncFactDn）。
language: zh-CN
keyword: VecEncFactNu
availability:
  standalone: []
  central-i:
  - v5
can_code: 712
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# VecEncFactNu

每轴矢量到编码器缩放比分子（VecEncFactNu / VecEncFactDn）。

## 概述

`VecEncFactNu` 是协调矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）中每轴编码器缩放比的分子。该轴的有效比值为 `VecEncFactNu / VecEncFactDn`，将矢量路径单位映射到各轴编码器计数，使编码器分辨率不同的各轴能够参与同一协调运动，同时保持合成路径的几何精度。该参数为轴相关参数，保存至闪存，与分母 [VecEncFactDn](VecEncFactDn.md) 成对使用，在轴运动过程中不可更改。这是单值关键字 [VecEncRatio](VecEncRatio.md) 所提供的同一补偿的分子/分母形式。

## 工作原理

将该对参数设置为使 `VecEncFactNu / VecEncFactDn` 等于该轴所需的分辨率比。当分子与分母相等（默认值 `1` / `1`）时，比值为 1，不进行缩放。两个关键字均接受范围为 `1`-`2000` 的整数，因此可以表达大范围的有理比（例如 `3` / `2` 表示 1.5:1 的分辨率差异）。在开始运动前，请在每个成员轴上配置好该对参数，因为运动过程中不可更改。

> 在当前固件版本中，矢量路径插值不应用此比值。`VecEncFactNu` / [VecEncFactDn](VecEncFactDn.md) 按轴存储，但矢量运动纯粹根据路径几何计算各成员轴的运动；在依赖矢量编码器分辨率补偿之前，请针对您的固件版本验证实际行为。

## 示例

```text
AVecEncFactNu=1        ; numerator = 1 on axis A (default)
AVecEncFactNu=3        ; with VecEncFactDn = 2 gives a 3/2 (1.5:1) scaling ratio
AVecEncFactNu          ; read the current numerator on axis A
```

## 另请参阅

- [VecEncFactDn](VecEncFactDn.md) — 缩放比的分母
- [VecEncRatio](VecEncRatio.md) — 单值编码器分辨率补偿
- [VecMemberAxes](VecMemberAxes.md) — 构成矢量组的各轴
- [VecSpeed](VecSpeed.md) — 指令合成速度
