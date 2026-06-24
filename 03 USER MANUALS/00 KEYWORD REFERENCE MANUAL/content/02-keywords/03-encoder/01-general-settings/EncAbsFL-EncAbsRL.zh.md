---
summary: 在上电时将超出范围的绝对式编码器位置重新解释的正向/反向限值（仅限定制固件）。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsFL/EncAbsRL

在上电时将超出范围的绝对式编码器位置重新解释的正向/反向限值（仅限定制固件）。

## 概述

`EncAbsFL` 和 `EncAbsRL` 在上电时对绝对式编码器位置进行偏移，使得靠近无符号范围上端的读数被解释为一个较小的负位置。`EncAbsFL` 定义允许行程的正向限值，`EncAbsRL` 定义反向限值。它们在绝对偏置（[EncAbsOff](EncAbsOff-AuxEncAbsOff.md)）之后应用。本功能用于行程受机械硬限位约束、配备绝对式编码器的旋转电机。

> **注意：** 这些关键字属于定制功能，仅在定制固件版本中实现。使用前请确认其可用性。

## 工作原理

绝对式编码器位置以无符号整数读取，因此略低于零的位置会显示为接近范围上端的较大值。`EncAbsFL` 和 `EncAbsRL` 告诉控制器哪些读数应被视为负位置：

考虑一台旋转电机，其机械硬限位仅允许在 +90 deg 与 -90 deg 之间运动。若上电时轴处于 -45 deg，绝对式编码器会报告 315 deg（因为值为无符号）。此时一条移动到 0 deg 的指令将驱动轴反向运动 315 deg（而非正向 45 deg），并撞上机械硬限位。

将 `EncAbsFL` 设为 90 deg、`EncAbsRL` 设为 -90 deg，即告知控制器 315 deg 超出允许范围，应改为解释为 -45 deg。

这些限值仅作用于**上电**时的绝对位置——即标准固件根据绝对读数加上 [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) 来初始化位置的同一处（参见 [Pos](../../10-motion/01-kinematics-status/Pos.md)）。它们在偏置**之后**应用，因此顺序为：掩码读数 → 方向 → `+ EncAbsOff` → 对照 `EncAbsFL`/`EncAbsRL` 重新解释。启动之后位置正常累积，限值不再生效。

> **注意：** 此重新解释纯粹是一种反馈初始化辅助手段。它不会创建软件行程限位；运动限位需单独配置。仅对机械范围窄于一个绝对旋转周的受限行程旋转轴才有意义。

## 示例

```text
AEncAbsFL=90         ; forward limit (customized firmware)
AEncAbsRL=-90        ; reverse limit (customized firmware)
```

## 另请参阅

- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — 绝对偏置，在这些限值之前应用
- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — 这些限值所重新解释的已处理绝对读数
- [EncType](EncType-AuxEncType.md) — 编码器类型；这些限值适用于绝对式编码器
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 上电时建立的反馈位置
