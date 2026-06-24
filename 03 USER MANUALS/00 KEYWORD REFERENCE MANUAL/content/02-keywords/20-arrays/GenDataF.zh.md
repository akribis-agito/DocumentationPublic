---
summary: 通用非轴 32 位单精度浮点数组，用于用户/上位机共享存储。
keyword: GenDataF
availability:
  standalone: []
  central-i:
  - v5
can_code: 719
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 101
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GenDataF

通用非轴 32 位单精度浮点数组，用于用户/上位机共享存储。

## 概述

`GenDataF` 是通用数据数组系列中的 32 位单精度浮点成员。它是一个通用非轴数组，提供与 [GenData](GenData.md) 相同类型的共享存储——用户程序和上位机均可访问，不与任何控制器功能关联，并保存至闪存——但存储的是实数（单精度浮点）值，而非 32 位整数。单精度精度足够时请使用此数组；如需更高精度，请使用双精度 [GenDataD](GenDataD.md)。

该数组可随时读写，包括在运动中和电机使能时。值通过常规写入设置。上位机间接写入机制（`IndirectArray` / `IndirectIndex` / `IndirectValue` 与 `IndirectDo`）无法目标此数组；该机制仅写入 32 位整数 [GenData](GenData.md)。在用户程序中，元素仍可使用计算（运行时）索引寻址——参见 [寻址](GenData.md#addressing)。数组为 1 索引：第一个可用元素为 `GenDataF[1]`（索引 0 保留，不可访问），共有 100 个可用元素。

## 示例

```text
AGenDataF[1]=1.5    ; store a single-precision value
AGenDataF[1]        ; read the first element
```

## 另请参阅

- [GenData](GenData.md) — 32 位整数通用数组
- [GenDataD](GenDataD.md) — 64 位双精度浮点变体
- [GenDataLL](GenDataLL.md) — long-long（64 位有符号整数）变体
