---
summary: 一阶滤波器系数（1-64），在直接脉冲/方向模式下对 PDPos 进行平滑后送入 PosRef。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PDFiltFact

一阶滤波器系数（1-64），在直接脉冲/方向模式下对 PDPos 进行平滑后送入 PosRef。

## 概述

Agito 控制器支持以脉冲/方向输入端口定义期望电机位置的运动模式。请参阅 [MotionMode](../02-motion-configuration/MotionMode.md) 参数，即直接（3）和间接（4）脉冲/方向运动模式。

脉冲/方向输入端口的值可通过参数 [PDPos](PDPos.md) 读取，等于输入脉冲数（已考虑方向）乘以缩放比例 [PDFact](PDFact.md)/[PDFactDen](PDFactDen.md)。

在直接脉冲/方向运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 3）中，`PDPos` 直接用于设置位置参考（`PosRef`，即期望位置）。然而，为避免 `PosRef` 产生大幅阶跃（尤其是当 [PDFact](PDFact.md) 较大时），在将 `PDPos` 的变化量赋给 `PosRef` 之前，会对其应用一阶滤波器。`PDFiltFact` 是该滤波器的**整数系数**——当脉冲流较粗糙或速度较快时，其作用最为明显。

`PDFiltFact` 是一个内部系数，**不由用户直接设置**：它由截止频率关键字 [PDPosFilt](PDPosFilt.md) 自动计算得出。请通过 `PDPosFilt` 配置滤波器；`PDFiltFact` 是控制器由此推导出的值。

## 工作原理

### 滤波器

在直接模式下，每个控制周期，滤波后的参考偏移量按如下方式更新，对自运动开始以来的*累积* P/D 偏移量进行一阶低通滤波：

$$
\text{Offset}_k = \frac{(\text{PDPos}_k - \text{PDPos}_{\text{Begin}}) \cdot \text{PDFiltFact} + \text{Offset}_{k-1} \cdot (64 - \text{PDFiltFact})}{64}
$$

滤波器的输入为当前 `PDPos` 与在 [Begin](../04-motion-command/Begin.md) 时锁存值之间的累积差值（而非每个周期的变化量），滤波结果是叠加到 `Begin` 时锁存的参考值上、从而构成 `PosRef` 的偏移量。

`PDFiltFact` 的范围为 **1**（最慢滤波，平滑最重）至 **64**（无滤波——`PosRef` 直接跟随输入）。常数 64 是一个固定的历史缩放因子。

> **注意：** 由于输入和滤波后的偏移量均相对于 `Begin` 时锁存的值进行测量，滤波器在运动开始时以干净的零偏移量启动。

### 从 PDPosFilt 推导的方法

当写入 [PDPosFilt](PDPosFilt.md)（以 Hz × 100 为单位的截止频率）时，控制器使用 `w / (s + w)` 的后向欧拉离散化方法将其转换为系数：

$$
\text{PDFiltFact} = 64 \cdot \frac{2\pi\,T_s\,\text{PDPosFilt}}{100 + 2\pi\,T_s\,\text{PDPosFilt}}
$$

其中 `Ts` 为采样时间。早期固件在分母中省略了 `2π` 因子（使用 `100 + Ts·PDPosFilt`），导致相同 `PDPosFilt` 值对应的系数略大；例如，默认值 `PDPosFilt = 12800` 在早期固件中得到 `PDFiltFact = 3`，而在修正后的公式中为 `2`。`PDPosFilt` 的下限（4150）的存在是为了确保计算出的 `PDFiltFact` 永远不会舍入为 0（该值在两种形式下均产生 `PDFiltFact = 1`）。

## 示例

`PDFiltFact` 不可直接写入；请通过 [PDPosFilt](PDPosFilt.md) 配置滤波器：

```text
APDPosFilt=25000     ; 250 Hz cut-off -> controller computes the PDFiltFact coefficient
APDPosFilt=12800     ; 128 Hz cut-off (default)
```

## 另请参阅

- [PDPosFilt](PDPosFilt.md) — 设置此系数的截止频率关键字
- [PDPos](PDPos.md) — 变化量被滤波的缩放脉冲/方向计数器
- [PDFact](PDFact.md) — 应用于输入脉冲的缩放系数
- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择直接（3）/间接（4）脉冲/方向运动
