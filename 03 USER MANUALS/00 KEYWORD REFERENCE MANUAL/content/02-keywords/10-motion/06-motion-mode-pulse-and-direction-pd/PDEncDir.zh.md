---
keyword: PDEncDir
summary: 配置 PDPos 累积相对于方向信号的符号（方向）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 63
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides:
  central-i.v5:
    access: rw
    units: none
    range:
    - 0
    - 1
    implemented: final
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# PDEncDir

配置 PDPos 累积相对于方向信号的符号（方向）。

## 概述

`PDEncDir` 反转 [PDPos](PDPos.md) 累积的符号，即翻转给定方向信号下计数器的运动方向。它无需重新接线即可反转脉冲方向解码的感知方向，且与 [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) 设置的幅值缩放相互独立。它与反馈方向关键字 [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) 类似，但作用于 P/D *输入*而非编码器反馈。

> **适用范围：** `PDEncDir` 仅在 **v5（central-i）** 上实现。在 v4 上为保留/未实现——参见下方*版本间变更*。

## 工作原理

`PDEncDir` 直接以符号因子 `(1 − 2·PDEncDir)` 作用于每周期累积中已缩放的增量。因此 `PDEncDir = 0` 得到 `+1`（增量被加上），`PDEncDir = 1` 得到 `−1`（增量被减去）。由于符号作用于已缩放的增量，它仅翻转方向——幅值不受影响。

| 值 | 对 PDPos 的影响 |
|---|---|
| 0 | **正常。** 方向信号为逻辑高电平时，`PDPos` 按 `pulses × PDFact/PDFactDen` 递增；逻辑低电平时递减。 |
| 1 | **反转。** 方向信号为逻辑高电平时，`PDPos` 递减；逻辑低电平时递增。 |

这与 `PDFact` 的符号组合使用：负的 `PDFact` 与 `PDEncDir = 1` 相互抵消。轴在运动中或电机使能时不能更改 `PDEncDir`。

## 示例

```text
APDEncDir=0          ; normal accumulation direction (default)
APDEncDir=1          ; inverted accumulation direction
```

## 版本间变更

`PDEncDir` 仅适用于 **central-i v5**。在 v4 上该关键字为保留（未实现）。在 v5（central-i）上，它是一个读/写闪存参数，范围为 0–1，应用上述符号。v5 仅适用于 central-i，因此独立产品不提供 `PDEncDir`。

## 另请参阅

- [PDPos](PDPos.md) — 本关键字设置其累积方向的计数器
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — 缩放因子幅值（其符号与 `PDEncDir` 组合）
- [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) — 编码器反馈的类似方向控制
