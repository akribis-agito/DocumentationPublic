---
keyword: VEncValue
summary: 只读的虚拟编码器跟踪计数，采用经缩放的源参考坐标。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 623
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VEncValue

只读的虚拟编码器跟踪计数，采用经缩放的源参考坐标。

## 概述

`VEncValue` 是虚拟编码器的内部跟踪计数，包含输出增量、参考值初始化及取模调整。以 [VEncOn](VEncOn.md) 使能后，生成器驱动正交或脉冲/方向输出，跟踪按 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 缩放的 [VEncSrc](VEncSrc.md)。

它是只读的、按轴的，且不保存至闪存。它**不是**轴自身的反馈位置（[Pos](../../10-motion/01-kinematics-status/Pos.md)）——而是对所生成输出信号的计量。它上电时为 0。

## 工作原理

在 [VEncOn](VEncOn.md) = 1 期间，每个控制周期，生成器：

1. 读取由 [VEncSrc](VEncSrc.md) 选定的源变量，并按 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 对其缩放。
2. 运行一个跟踪控制器外加前馈，并在本周期发出相应数量的输出边沿。
3. 根据所跟踪的输出增量更新 `VEncValue`。

虚拟编码器首次开启时，`VEncValue` 被初始化为当前经缩放的源值。通过 [VEncModRev](VEncModRev.md) 检测到回绕时，该值会调整一个经缩放的范围。

在包含 [Firmware-Main #1103](https://github.com/akribis-agito/Firmware-Main/issues/1103) 修复的固件中，写入源或比例，以及源步长超过每采样周期的容量时，也会复位跟踪参考值。容量检查在取模补偿之后进行。复位可能改变 `VEncValue`，而不发出与该变化对应的边沿。后续跟踪及保留的电机使能保护，请参阅 [VEncOn](VEncOn.md)。

## 示例

```text
AVEncValue           ; read the virtual-encoder tracking count
```

## 另请参阅

- [VEncOn](VEncOn.md) — 使能虚拟编码器
- [VEncSrc](VEncSrc.md) — 输出所跟踪的源变量
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — 源到输出的缩放比例
- [VEncModRev](VEncModRev.md) — 用于回绕补偿的源取模范围
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 轴自身的反馈位置（与 `VEncValue` 不同）
