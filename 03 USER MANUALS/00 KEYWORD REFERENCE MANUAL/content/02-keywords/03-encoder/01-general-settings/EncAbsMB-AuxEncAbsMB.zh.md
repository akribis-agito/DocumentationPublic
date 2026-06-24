---
summary: 从绝对式编码器读数中移除（右移）的最低有效位数量。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsMB/AuxEncAbsMB

从绝对式编码器读数中移除（右移）的最低有效位数量。

## 概述

`EncAbsMB` 定义从原始绝对读数中丢弃多少个最低有效位：读数在使用前先右移 `EncAbsMB` 位。仅当编码器类型（[EncType](EncType-AuxEncType.md)）为绝对式编码器——EnDat 2.2（`EncType=3`）、BiSS-C（`EncType=6`）或 Tamagawa（`EncType=8`）时适用。移除低位会丢弃未使用或过细的分辨率位，使累积位置仅使用有意义的位，并使循环回绕模数被正确设置。`AuxEncAbsMB` 是辅助编码器的对应关键字，工作方式相同。

范围 0–8，默认 0（不移除任何位）。

## 工作原理

每个控制周期对新的绝对读数应用的第一个操作就是右移：

$$\text{Reading}_{\text{masked}} = \text{Reading}_{\text{raw}} \gg \text{EncAbsMB}$$

这发生在方向处理之前、捕获 [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) 之前，以及偏置和累积之前。因此每个下游值都已反映该掩码读数。

`EncAbsMB` 也会移位循环回绕模数。*掩码*字一整圈的宽度为

$$\text{ReadingCycle} = 2^{\,\text{EncAbsBits} - \text{EncAbsMB}}$$

在写入 `EncAbsMB`（或 [EncAbsBits](EncAbsBits-AuxEncAbsBits.md)）时预先计算。`EncAbsMB` 每增加 1，`ReadingCycle` 减半，这是一致的：丢弃一个低位会使字中不同计数的数量减半。累加器使用 `ReadingCycle`（及其 25 %/75 % 标记）来检测掩码读数何时环绕，并加上或减去一个完整周期，使位置连续计数。

由于 `EncAbsMB` 改变了计数到电角度的缩放关系，在无刷电机上更改它会使换相失效，控制器会标记需要重新换相。

> [!note]
> `EncAbsMB` 从字的**底部**（最低有效位）移除位。剩余的低位表示单圈位置，高位表示多圈计数，如 [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) 位布局图所示。
>
> `EncAbsMB` **不是**多圈位的计数，也不会告诉控制器如何将字拆分为多圈和单圈两部分。控制器从不单独解码这两半——它将掩码读数视为一个连续的无符号位置，并直接丢弃 `EncAbsMB` 个低位。请将 `EncAbsMB` 设为你希望丢弃的细分位数量，而非编码器的多圈位数量。

### 辅助编码器（AuxEncAbsMB）

`AuxEncAbsMB` 按相同规则右移辅助绝对读数，并据此设置辅助循环回绕模数 `2^(AuxEncAbsBits − AuxEncAbsMB)`。

## 示例

```text
AEncAbsMB=2             ; discard the 2 least significant bits of the reading
AEncAbsMB               ; query the configured number of removed bits
AAuxEncAbsMB=0          ; keep all bits of the auxiliary absolute reading
```

## 另请参阅

- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — 总位数；与 `EncAbsMB` 共同设置循环回绕模数
- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — 经过此掩码与方向处理后的读数
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — 上电时加到掩码读数上的偏置
- [EncDir](EncDir-AuxEncDir.md) — 在掩码之后应用的方向处理
- [EncType](EncType-AuxEncType.md) — 编码器类型；`EncAbsMB` 适用于绝对式编码器
