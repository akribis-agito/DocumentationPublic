---
summary: 上电时加到绝对式编码器原始读数上的偏置。
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsOff/AuxEncAbsOff

上电时加到绝对式编码器读数上的偏置。

## 概述

`EncAbsOff` 是在上电首次建立位置时加到绝对读数上的偏置。仅当编码器类型（[EncType](EncType-AuxEncType.md)）为绝对式编码器——EnDat 2.2（`EncType=3`）、BiSS-C（`EncType=6`）或 Tamagawa（`EncType=8`）时适用。其目的是将编码器报告的绝对位置与期望的机械零点对齐，使轴无需回零即可在已知位置启动。与增量式编码器不同，绝对式编码器允许 [Pos](../../10-motion/01-kinematics-status/Pos.md) 直接从编码器自身初始化，而非从零开始。`AuxEncAbsOff` 是辅助编码器的对应关键字，工作方式相同。

`EncAbsOff` 以用户单位表示；`AuxEncAbsOff` 以辅助用户单位表示。默认 0。

## 工作原理

在上电后的固定数量控制周期内，固件直接根据绝对读数加上此偏置来初始化累积位置，而非让其从零累积：

$$\text{EncoderPos}_{\text{init}} = \text{Reading}_{\text{masked}} + \text{EncAbsOff}$$

其中 `Reading_masked` 是经过 [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) 右移和 [EncDir](EncDir-AuxEncDir.md) 方向处理后的原始读数（即作为 [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) 报告的同一值）。同时增量被强制为 0，前一读数寄存器被预置，使轴从 `EncoderPos_init` 开始且不产生虚假跳变。该初始值流经正常反馈流程（误差映射、取模）成为 [Pos](../../10-motion/01-kinematics-status/Pos.md)。初始化窗口关闭后不再加偏置；位置仅累积每周期的增量。

在独立控制器上，此初始化窗口约为上电后一秒（由各绝对轴共享的单个计数器控制，因此在多轴控制器上相应更短；参见 [EncAbsVal](EncAbsVal-AuxEncAbsVal.md)）。在 central-i 上，它大致跨越端口配置后的前 150 个控制周期，且每个轴拥有自己的初始化窗口，每当端口被重新配置时重新置位。在所有情况下，初始化都在轴被使能之前充分完成。

因此 `EncAbsOff` 改变编码器的绝对零点在控制器位置坐标系中的落点。要将机械零点置于选定的物理点，请将 `EncAbsOff` 设为在该点观测到的掩码读数的相反数（从 [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) 读取）。

在无刷电机上更改 `EncAbsOff` 会使换相失效（它改变了位置到电角度的关系），因此控制器会标记需要重新换相。

### 辅助编码器（AuxEncAbsOff）

`AuxEncAbsOff` 在上电时以相同方式初始化辅助累积位置——`AuxPos_init = Reading_masked + AuxEncAbsOff`——无需回零即可将辅助反馈建立在已知值。

## 示例

```text
AEncAbsOff=1000         ; add an offset of 1000 to the absolute reading at power-up
AEncAbsOff=0            ; encoder absolute zero = machine zero
AAuxEncAbsOff=-50000    ; place auxiliary machine zero at reading 50000
```

## 边界情况

- **未验证的上电初始化。** 上电初始化取自编码器的首次读数，未验证帧。由 [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) 控制的 CRC / 错误 / 断连监测仅在初始化窗口关闭后才开始，因此一个损坏的上电帧可能将 [Pos](../../10-motion/01-kinematics-status/Pos.md) 初始化为错误的绝对值，并在重新上电后仍然保留。若绝对上电完整性至关重要，请在引导启动后数个周期内确认 [EncStatReg](EncStatReg.md) 干净，再依赖 [Pos](../../10-motion/01-kinematics-status/Pos.md)。

## 另请参阅

- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — 偏置所加到的掩码、方向处理后的读数
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — 绝对字宽度
- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — 在偏置应用前移除的低位
- [EncType](EncType-AuxEncType.md) — 编码器类型；`EncAbsOff` 适用于绝对式编码器
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 上电时根据 `reading + EncAbsOff` 初始化的反馈位置
- [EncStatReg](EncStatReg.md) — 在依赖上电初始化前确认状态干净
- [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) — 异常帧监测；仅在初始化窗口关闭后才开始
- [SetPosition](../../10-motion/03-kinematics-configuration/SetPosition.md) — 启动后预置反馈
