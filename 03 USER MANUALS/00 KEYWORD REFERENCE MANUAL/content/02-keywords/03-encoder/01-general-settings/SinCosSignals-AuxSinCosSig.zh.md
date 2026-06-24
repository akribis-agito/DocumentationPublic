---
summary: 报告 SIN/COS 信号插值状态的只读数组。
last_updated: '2026-05-27'
doc_revision: '2026.06'
language: zh-CN
---
# SinCosSignals/AuxSinCosSig

报告 SIN/COS 信号插值状态的只读数组。

## 概述

`SinCosSignals` 是显示 SIN/COS 信号插值状态的只读参数数组。仅当编码器类型（[EncType](EncType-AuxEncType.md)）为 4（SIN/COS 编码器）时使用。根据产品不同，每个数组元素表示不同的状态，这对于在校准期间检查原始信号电平和象限解码很有用。`AuxSinCosSig` 是辅助编码器的对应项。

对于所有支持 SIN/COS 的 Agito 产品（AGFB01 除外），`SinCosSignals` 仅在进入模拟测试模式（`SinCosSetup[20] = 1`）时可用。

## 工作原理

对于所有支持 SIN/COS 编码器的 Agito 产品（**AGFB01 除外**）：

| 索引 | 描述 |
|---|---|
| 1 | 原始 SIN+ 信号读数，单位为毫伏（mV） |
| 2 | 原始 SIN- 信号读数，单位为毫伏（mV） |
| 3 | 原始 SIN+ 与 SIN- 读数之差，单位为 mV。等于 `SinCosSignals[1] - SinCosSignals[2]` |
| 4 | 原始 COS+ 信号读数，单位为毫伏（mV） |
| 5 | 原始 COS- 信号读数，单位为毫伏（mV） |
| 6 | 原始 COS+ 与 COS- 读数之差，单位为 mV。等于 `SinCosSignals[4] - SinCosSignals[5]` |

对于 **AGFB01**：

| 索引 | 描述 |
|---|---|
| 1 | **象限对齐状态**（默认 0）。将由比较器推断的象限与由原始 SIN/COS 信号的 atan2 运算推断的象限进行比对。`0` = 正常；`-1` = 失败（无效的象限差）。 |
| 2 | **来自数字通路的原始象限计数器**（默认 0）。SIN/COS 信号经比较器形成数字 A/B 信号；内部计数器在尊重方向的前提下对所经过的象限数进行计数。例如，从象限 2 进入象限 3 使计数器递增，而从象限 2 进入象限 1 使其递减。 |
| 3 | **原始正弦信号读数**（默认 0），单位为微伏（µV），已应用 `SinCosSetup` 定义的幅值和相位偏置。 |
| 4 | **来自比较器（数字通路）的象限代码**（默认 0）。在 SIN/COS 信号与 0 比较以形成数字 A/B 信号处确定。以象限代码（非象限编号）报告；参见下表。 |
| 5 | **来自 SIN/COS 数值（模拟通路）的象限代码**（默认 0）。在由 atan2 公式计算角度处确定。以象限代码（非象限编号）报告；参见下表。 |
| 6 | **原始余弦信号读数**（默认 0），单位为微伏（µV），已应用 `SinCosSetup` 定义的幅值和相位偏置。 |

`SinCosSignals[4]` 的象限代码（数字 / 比较器通路）：

| 象限代码 | 象限 | 比较器 A (SIN) | 比较器 B (COS) | 角度 [degrees] |
|---|---|---|---|---|
| 3 | 第一 | 1 (SIN > 0) | 1 (COS > 0) | [0, 90) |
| 2 | 第二 | 1 (SIN > 0) | 0 (COS ≤ 0) | [90, 180) |
| 1 | 第三 | 0 (SIN ≤ 0) | 0 (COS ≤ 0) | [180, 270) |
| 0 | 第四 | 0 (SIN ≤ 0) | 1 (COS > 0) | [270, 360) |

`SinCosSignals[5]` 的象限代码（模拟 / atan2 通路）：

| 象限代码 | 象限 | SIN 符号 | COS 符号 | 角度 [degrees] |
|---|---|---|---|---|
| 3 | 第一 | + | + | [0, 90) |
| 2 | 第二 | + | - | [90, 180) |
| 1 | 第三 | - | - | [180, 270) |
| 0 | 第四 | - | + | [270, 360) |

## 示例

```text
ASinCosSignals[3]       ; read the SIN+ minus SIN- difference (mV)
ASinCosSignals[6]       ; read the COS+ minus COS- difference (mV)
```

## 另请参阅

- [EncType](EncType-AuxEncType.md) — 编码器类型；`SinCosSignals` 适用于 `EncType=4`
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — SIN/COS 配置数组（通过索引 20 启用测试模式）
