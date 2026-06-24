---
summary: 经位掩码和方向处理后的绝对式编码器原始值。
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsVal/AuxEncAbsVal

经过位掩码和方向处理后的只读绝对式编码器读数。

## 概述

`EncAbsVal` 是绝对式编码器读数在移除低位（[EncAbsMB](EncAbsMB-AuxEncAbsMB.md)）并应用方向（[EncDir](EncDir-AuxEncDir.md)）之后、但在上电偏置（[EncAbsOff](EncAbsOff-AuxEncAbsOff.md)）**之前**的值。仅当编码器类型（[EncType](EncType-AuxEncType.md)）为绝对式编码器——EnDat 2.2（`EncType=3`）、BiSS-C（`EncType=6`）或 Tamagawa（`EncType=8`）时适用。它为只读且每个控制周期更新；它让你检查已处理的绝对字，例如用于决定偏置或验证方向。`AuxEncAbsVal` 是辅助编码器的对应关键字，工作方式相同。

## 工作原理

每个控制周期，固件从编码器接口读取原始绝对字，然后：

1. 右移 [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) 位以丢弃未使用的低位。
2. 若 [EncDir](EncDir-AuxEncDir.md) 为反向，则在一整圈范围内镜像：`Reading = ReadingCycle − Reading`，其中 `ReadingCycle = 2^(EncAbsBits − EncAbsMB)`。
3. 将结果存入 `EncAbsVal`。

因此 `EncAbsVal` 是掩码、方向修正后的读数——正是固件随后用 [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) 偏置并在上电时累积到位置中的值（参见 [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) 和 [Pos](../../10-motion/01-kinematics-status/Pos.md)）。公开它是为了让应用程序能读取实时绝对字并做出决策（例如计算使选定物理点读数为零所需的偏置）。对 `EncAbsVal` 的写入会被拒绝——它是只读的。

> [!note]
> 对于模拟位置反馈输入（`EncType=7`），固件使用同一代码路径以方向处理后的模拟读数填充 `EncAbsVal`，因此可以以相同方式回读。

### 辅助编码器（AuxEncAbsVal）

`AuxEncAbsVal` 是以相同方式捕获的、经掩码与方向处理的辅助绝对读数。

## 示例

```text
AEncAbsVal              ; read the processed absolute value
AAuxEncAbsVal           ; read the processed auxiliary absolute value
```

## 边界情况

- **电机失能。** 只要编码器接口处于活动状态，绝对读数就会运行；无论电机状态如何，`EncAbsVal` 都每周期更新。
- **上电初始化。** 在上电后的固定时段内，固件根据 `EncAbsVal + EncAbsOff` 初始化累积位置。在独立控制器上，此窗口由单个共享计数器控制，约持续一秒（在多轴控制器上相应更短）；在 Central-i 上，每个轴拥有自己的窗口（每当端口被重新配置时重新置位），大致跨越端口配置后的前 150 个周期。在所有情况下，初始化都在轴被使能之前充分完成。
- **首次读数被延迟。** 有效的绝对帧在第一个控制周期上不可用——编码器在短暂的链路延迟后才返回数据，因此首个可用读数在一个周期后出现。请在控制器稳定后（引导启动后数个周期）读取 `EncAbsVal`，以获得原始的掩码、方向处理后的字；在第一个周期上读取可能返回陈旧值。
- **编码器类型。** 对绝对式编码器（`EncType=3`、`6`、`8`）和模拟位置反馈（`EncType=7`，其模拟读数经过同一方向处理代码路径）有意义。对增量式/SIN-COS 类型不产生该值。
- **Central-i 断连。** 端口断连时（[CIStatus](../../01-system/05-central-i/CIStatus.md)`[1] ≠ 3`）无远程帧到达，固件无法刷新 `EncAbsVal`；该关键字保持其上次应用的值。
- **写入尝试。** 只读——赋值会被拒绝。
- **EncDir / EncAbsMB / EncAbsBits 更改后。** 重新读取一次；该值会根据新的掩码和方向，从下一周期开始重新计算。

## 另请参阅

- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — 在此值之前应用的位掩码
- [EncDir](EncDir-AuxEncDir.md) — 应用于读数的方向处理
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — 上电时加到此值上的偏置
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — 绝对字宽度
- [EncType](EncType-AuxEncType.md) — 编码器类型；`EncAbsVal` 适用于绝对式编码器
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 反馈位置；`Pos` 根据 `EncAbsVal + EncAbsOff` 初始化
