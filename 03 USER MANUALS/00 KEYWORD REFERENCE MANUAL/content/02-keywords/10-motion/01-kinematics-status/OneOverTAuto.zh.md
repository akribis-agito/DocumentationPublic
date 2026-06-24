---
keyword: OneOverTAuto
summary: 用于 1/T 速度测量的保留关键字（未实现）。
availability:
  standalone:
  - v4
  central-i: []
can_code: 188
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
  implemented: not_implemented
overrides: {}
removed_in:
- v5
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# OneOverTAuto

用于 1/T 速度测量的保留关键字（未实现）。

## 概述

`OneOverTAuto` 是 1/T 速度测量组中的一个保留关键字。它仅在 standalone 产品上、且仅在使用数字增量式编码器（[EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`）时受支持。它与其他 1/T 配置关键字 [OneOverTOn](OneOverTOn.md)、[OneOverTFreq](OneOverTFreq.md) 和 [OneOverTGap](OneOverTGap.md) 相关，它们共同控制 [Vel](Vel.md)`[4]` 测量。

> **文档待补充：** `OneOverTAuto` 是保留关键字且**未实现**（`implemented: not_implemented`）。它注册为一个参数，范围为 `0`–`1`，默认值为 `0`，但没有任何地方读取它——写入它没有任何效果。

## 工作原理

该关键字目前没有运行时行为。其预期用途是自动设置 [OneOverTFreq](OneOverTFreq.md) 和 [OneOverTGap](OneOverTGap.md)，以在无溢出的情况下获得最佳分辨率。

实现后，`OneOverTAuto = 1` 将因此让控制器自动选择 [OneOverTFreq](OneOverTFreq.md)（定时器频率分频器）和 [OneOverTGap](OneOverTGap.md)（计数间隔）——选取在速度变化时仍可避免捕获定时器溢出的最精细分辨率——而无需手动设置这两个值。在此之前，请直接使用 [OneOverTFreq](OneOverTFreq.md) 和 [OneOverTGap](OneOverTGap.md) 配置 1/T 测量。

## 另请参阅

- [OneOverTOn](OneOverTOn.md) — 启用/禁用 1/T 速度计算
- [OneOverTFreq](OneOverTFreq.md) — 1/T 定时器频率分频器（在此期间手动设置）
- [OneOverTGap](OneOverTGap.md) — 每个 1/T 采样的编码器计数间隔（在此期间手动设置）
- [Vel](Vel.md) — 反馈速度数组（`Vel[4]` 为 1/T 方法）
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — 必须为数字增量式编码器
