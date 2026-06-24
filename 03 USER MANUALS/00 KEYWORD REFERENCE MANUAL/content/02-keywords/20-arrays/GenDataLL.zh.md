---
summary: 通用非轴 64 位有符号整数数组，用于用户/上位机共享存储。
keyword: GenDataLL
availability:
  standalone: []
  central-i:
  - v5
can_code: 775
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 101
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GenDataLL

通用非轴 64 位有符号整数数组，用于用户/上位机共享存储。

## 概述

`GenDataLL` 是通用数据数组系列中的 64 位有符号整数（long-long）成员。它是一个通用非轴数组，提供与 [GenData](GenData.md) 相同类型的共享存储——用户程序和上位机均可访问，不与任何控制器功能关联，并保存至闪存——但存储的是 64 位整数，适用于超出 [GenData](GenData.md) 32 位范围的整数值。

该数组可随时读写，包括在运动中和电机使能时。值通过常规写入设置。上位机间接写入机制（`IndirectArray` / `IndirectIndex` / `IndirectValue` 与 `IndirectDo`）无法目标此数组；该机制仅写入 32 位整数 [GenData](GenData.md)。在用户程序中，元素仍可使用计算（运行时）索引寻址——参见 [寻址](GenData.md#addressing)。数组为 1 索引：第一个可用元素为 `GenDataLL[1]`（索引 0 保留，不可访问），共有 100 个可用元素。虽然以 64 位整数存储，但接受的值范围限制为 -2251799813685248 至 2251799813685247（52 位有符号范围），以确保每个值均可精确表示为双精度浮点数，供上位机数据记录使用。

## 示例

```text
AGenDataLL[1]=1000000000000   ; store a large 64-bit integer
AGenDataLL[1]                 ; read the first element
```

## 另请参阅

- [GenData](GenData.md) — 32 位整数通用数组
- [GenDataD](GenDataD.md) — 64 位双精度浮点变体
- [GenDataF](GenDataF.md) — 32 位单精度浮点变体
