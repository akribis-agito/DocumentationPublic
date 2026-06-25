---
keyword: VEncType
summary: 设置虚拟编码器的输出格式或信号类型。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 615
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# VEncType

设置虚拟编码器的输出格式或信号类型。

## 概述

`VEncType` 设置虚拟编码器在使能时（[VEncOn](VEncOn.md) = 1）所发出的物理信号格式。同一生成计数（由 [VEncSrc](VEncSrc.md) 经 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 缩放后构建）既可以脉冲/方向形式输出，也可以 A-quad-B 正交形式输出。取值范围为 0 到 1，默认值为 0。它是轴相关参数，保存至闪存，并可在电机使能或运动中更改。

## 工作原理

`VEncType` 选择控制器驱动到虚拟编码器硬件上的输出信号格式：

| 值 | 输出信号 |
|---|---|
| 0 | 脉冲 + 方向（一条脉冲线，一条方向线）。 |
| 1 | A-quad-B 正交（两路相移通道）。 |

该格式影响 [VEncDelay](VEncDelay.md) 的使用方式：建立延时（方向变化时至第一个脉冲的时钟数）仅对脉冲/方向（`VEncType=0`）生效。对于 A-quad-B，该延时被强制为 0，因为 A 与 B 永不会同时切换，无需线间建立时间。

## 示例

```text
AVEncType=0          ; pulse/direction output (default)
AVEncType=1          ; A-quad-B quadrature output
```

## 另请参阅

- [VEncOn](VEncOn.md) — 使能虚拟编码器
- [VEncSrc](VEncSrc.md) — 虚拟编码器的源变量
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — 缩放比例的分子 / 分母
- [VEncDelay](VEncDelay.md) — 脉冲/方向建立延时（仅用于 `VEncType=0`）
