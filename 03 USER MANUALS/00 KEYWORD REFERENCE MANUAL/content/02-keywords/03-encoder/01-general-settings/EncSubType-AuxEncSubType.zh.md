---
summary: 选择数字增量式编码器子类型（AqB、脉冲方向、C0/C1、加/减计数）。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EncSubType/AuxEncSubType

选择数字增量式编码器子类型。

## 概述

`EncSubType` 选择控制器如何解码数字增量式编码器输入的脉冲。仅当编码器类型（[EncType](EncType-AuxEncType.md)）为 1（数字增量式编码器）时使用。`AuxEncSubType` 是辅助编码器的对应项，工作方式相同。

范围 0–3，默认 0（A quad B）。

## 工作原理

| 值 | 数字增量式编码器类型 |
|-------|----------------------------------|
| 0     | A quad B 编码器（AqB）           |
| 1     | 脉冲方向编码器          |
| 2     | C0/C1 位                       |
| 3     | 加/减计数脉冲                   |

写入 `EncSubType` 时，控制器会将所选方案配置到编码器解码硬件中。该子类型与输入滤波器（[EncFilt](EncFilt-AuxEncFilt.md)）和方向（[EncDir](EncDir-AuxEncDir.md)）一起打包进单个 32 位配置字：子类型占据低 16 位，接下来的 16 位保存滤波器（位 16–23，即 `EncFilt` 的低 8 位）和方向标志（位 24，在高位字中为 `EncDir << 8`）。在 central-i 上，该字作为远程编码器配置消息发送；在独立控制器上，则将等效位写入编码器设置寄存器。由于子类型、滤波器和方向共享一个字，更改其中任何一项都会重写整个配置。

> [!note]
> `EncSubType` 仅控制**增量式**解码（`EncType=1`）。对于绝对式编码器，协议/子协议由 [EncType](EncType-AuxEncType.md) 本身选择（EnDat 2.2、BiSS-C、Tamagawa）；它们没有单独的子类型关键字。

### 辅助编码器（AuxEncSubType）

`AuxEncSubType` 使用相同的取值表选择辅助增量式编码器的解码方案，并与 `AuxEncFilt` 和 `AuxEncDir` 一起打包进辅助编码器配置字。

## 示例

```text
AEncSubType=0           ; A quad B (AqB) encoder
AEncSubType=1           ; pulse-direction encoder
AAuxEncSubType=3        ; auxiliary encoder uses up/down pulses
```

## 另请参阅

- [EncType](EncType-AuxEncType.md) — 编码器类型；`EncSubType` 适用于 `EncType=1`
- [EncFilt](EncFilt-AuxEncFilt.md) — 数字输入滤波器（与子类型打包在一起）
- [EncDir](EncDir-AuxEncDir.md) — 编码器方向（与子类型打包在一起）
