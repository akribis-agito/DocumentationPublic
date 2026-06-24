---
summary: 设置编码器反馈的计数方向。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EncDir/AuxEncDir

设置编码器反馈的计数方向。

## 概述

`EncDir` 配置编码器读数的计数方向，使编码器计数与期望的正运动方向对齐。从概念上讲，控制器每个周期按原始反馈的增量对位置（[Pos](../../10-motion/01-kinematics-status/Pos.md)）进行加减——`EncDir=0` 保持编码器的原生方向，`EncDir=1` 将其反向。

仅当编码器类型（[EncType](EncType-AuxEncType.md)）不为 4（SIN/COS）时才使用 `EncDir`。对于 SIN/COS 编码器（`EncType=4`），请改为通过 [SinCosSetup](SinCosSetup-AuxSinCosSet.md) 配置方向。在设置过程中，必须在执行电机定相之前配置好 `EncDir` 以获得期望的方向。`AuxEncDir` 是辅助编码器的对应项，其工作方式相同。

## 工作原理

对于**增量式**编码器，方向反转在**正交解码硬件**中实现，而非作为软件后处理步骤：

- **独立控制器**——`EncDir` 写入解码器控制寄存器的正交交换位。置位会在硬件中交换 A 和 B 通道，从而反转解码后的计数方向。
- **Central-i 远程单元**——`EncDir` 被打包到发送给远程单元的远程编码器配置字（位 24）中，硬件在正交解码器内部通过**反转解码后的计数方向**来反向计数。A 和 B 输入不进行物理交换；而是将加/减判定反转，对计数的净效果相同。（在独立控制器上，等效的设置则是在解码器处交换 A 和 B 通道；两者都实现相同的方向反转。）

对于**绝对式**编码器，没有可供交换的正交解码器，因此固件每个周期在软件中应用反转：在原始字按 [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) 右移之后，当 `EncDir = 1` 时，将掩码处理后的读数替换为 `ReadingCycle − reading`。对 [Pos](../../10-motion/01-kinematics-status/Pos.md) 的净效果与增量式编码器相同。

| EncDir | 对位置的影响 |
|---|---|
| 0 | 位置按编码器的原生方向计数。 |
| 1 | 位置按反向计数（增量式：独立控制器在解码器处交换 A/B，Central-i 反转解码后的计数方向；绝对式：掩码处理后 `ReadingCycle − reading`）。 |

必须在电机定相/换相之前设置 `EncDir`，因为定相后更改它会反转位置与电气角度的关系，从而需要重新定相。

## 示例

```text
AEncDir=0            ; count in the encoder's native direction
AEncDir=1            ; reverse the counting direction
```

## 边界情况

- **电机使能 / 运动中。** 当电机使能或轴处于运动中时，写入将被拒绝。请先禁用电机；对于无刷电机，之后将需要重新定相。
- **编码器类型 4（SIN/COS）。** `EncDir` 被忽略；请改为通过 [SinCosSetup](SinCosSetup-AuxSinCosSet.md) 索引 [10] 设置方向。
- **增量式与绝对式。** 对于增量式（`EncType=1`），反转发生在解码硬件中（独立控制器交换 A/B；Central-i 远程单元则改为反转解码后的计数方向，通过位 24 配置）。对于绝对式编码器（`EncType=3/6/8`），反转在每个周期由软件应用，即在 [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) 右移之后执行 `ReadingCycle − reading`；对 [Pos](../../10-motion/01-kinematics-status/Pos.md) 的净效果相同。
- **上电 / 保存 / 复位。** 该设置保存至闪存；硬件交换或软件反转在初始化期间应用，因此新值在 [Save](../../01-system/02-operation/Save.md) + [Reset](../../01-system/02-operation/Reset.md) 之后生效。
- **Central-i 断开。** 方向位被打包到远程编码器配置字中，并在 [CIConnect](../../01-system/05-central-i/CIConnect.md) 期间发送；在断开的端口上，远程单元保持其上次应用的方向。

## 参见

- [EncType](EncType-AuxEncType.md) — 编码器类型；`EncDir` 不适用于 `EncType=4`
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — SIN/COS 编码器的方向设置
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 受 `EncDir` 影响的反馈位置
