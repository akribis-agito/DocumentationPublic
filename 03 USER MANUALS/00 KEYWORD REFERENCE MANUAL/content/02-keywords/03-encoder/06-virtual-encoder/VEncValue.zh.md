---
keyword: VEncValue
summary: 只读，虚拟编码器发出的累计计数，跟踪经缩放的源信号。
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

只读，虚拟编码器发出的累计计数，跟踪经缩放的源信号。

## 概述

`VEncValue` 是虚拟编码器在其编码器仿真输出上已发出的运行计数。虚拟编码器是一种编码器**信号生成器**：当以 [VEncOn](VEncOn.md) 使能时，它驱动一个正交或脉冲/方向输出，跟随所选的源变量。`VEncValue` 反映迄今为止生成的边沿数量，因此它在应用了源到输出的缩放 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 之后跟踪源（[VEncSrc](VEncSrc.md)）。

它是只读的、按轴的，且不保存至闪存。它**不是**轴自身的反馈位置（[Pos](../../10-motion/01-kinematics-status/Pos.md)）——而是对所生成输出信号的计量。它上电时为 0。

## 工作原理

在 [VEncOn](VEncOn.md) = 1 期间，每个控制周期，生成器：

1. 读取由 [VEncSrc](VEncSrc.md) 选定的源变量，并按 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 对其缩放。
2. 运行一个跟踪控制器外加前馈，并在本周期发出相应数量的输出边沿。
3. 将这些已发出的边沿累加到 `VEncValue`。

虚拟编码器首次开启时，`VEncValue` 被初始化为当前经缩放的源值，因此它从与源对齐处开始，而不是从任意偏移开始。如果源在取模下环绕且设置了 [VEncModRev](VEncModRev.md)，则 `VEncValue` 在环绕处按一个经缩放的跨度步进，从而保持连续。由于输出是闭环跟踪的，`VEncValue` 以极小滞后跟随经缩放的源，而不是一个自由运行的计数器。

## 示例

```text
AVEncValue           ; read the count emitted by the virtual encoder
```

## 另请参阅

- [VEncOn](VEncOn.md) — 使能虚拟编码器
- [VEncSrc](VEncSrc.md) — 输出所跟踪的源变量
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — 源到输出的缩放比例
- [VEncModRev](VEncModRev.md) — 用于保持 `VEncValue` 连续的源取模跨度
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 轴自身的反馈位置（与 `VEncValue` 不同）
