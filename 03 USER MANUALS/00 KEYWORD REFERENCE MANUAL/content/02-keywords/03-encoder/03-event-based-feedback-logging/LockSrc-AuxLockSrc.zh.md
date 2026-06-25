---
summary: 选择反馈记录的数字事件源和触发边沿。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LockSrc/AuxLockSrc

选择反馈记录的数字事件源和触发边沿。

## 概述

`LockSrc` 定义触发基于事件的反馈记录的数字事件源及其触发边沿。`LockSrc` 的符号选择边沿（正为上升沿，负为下降沿），其绝对值选择输入源。它与 [LockEn](LockEn-AuxLockEn.md)（用于使能记录）配合工作，并在每次事件时递增 [LockCntr](LockCntr-AuxLockCntr.md)。`AuxLockSrc` 是辅助编码器的对应项。

`LockSrc` 存储于闪存中，因此触发选择可在重新上电后保留；每当写入 `LockSrc` 以及每当使能 [LockEn](LockEn-AuxLockEn.md) 时，源/边沿都会被应用到触发硬件。有效范围为 `-38` 到 `38`。

## 工作原理

`LockSrc` 的符号定义触发边沿：

| 值 | 触发边沿 |
|-------|--------------|
| > 0   | 上升沿  |
| 0     | 主编码器索引，上升沿（见下文） |
| < 0   | 下降沿 |

`LockSrc` 的绝对值确定数字事件源。该映射因产品而异。

### LockSrc = 0

`LockSrc=0` 是一个便捷设置，它以正常（上升沿）极性选择**本轴的主编码器索引**，而无需知道每个产品的索引值。在通告支持该设置的固件/FPGA 版本上会被采纳；在较旧版本上，请改用下方表格中的显式索引值（例如，独立式 AGD101 上为 `32`，Central-i 产品上为 `16`）。

对于独立式产品（非 Central-i）：

| abs(Value) | AGD101 / AGD156 | AGD155 | AGD200 / AGC300 | AGD301 / AGC301 |
|:--:|:--:|:--:|:--:|:--:|
| 1 | Digital input 1 | Digital input 1 | Digital input 1 | Digital input 1 |
| 2 | Digital input 2 | Digital input 2 | Digital input 2 | Digital input 2 |
| 3 | Digital input 3 | Digital input 3 | Digital input 3 | Digital input 3 |
| 4 | Digital input 4 | Digital input 4 | Digital input 4 | Digital input 4 |
| 5 | Digital input 5 | Digital input 5 | Digital input 5 | Digital input 5 |
| 6 | Digital input 6 | Digital input 6 | Digital input 6 | Digital input 6 |
| 7 | Digital input 7 | Digital input 7 | Digital input 7 | Digital input 7 |
| 8 | Digital input 8 | Digital input 8 | Digital input 8 | Digital input 8 |
| 9 | Bidirectional differential digital I/O 1 (as digital input 9) | Digital input 9 | Digital input 9 | Digital input 9 |
| 10 | Bidirectional differential digital I/O 2 (as digital input 10) | Digital input 10 | Digital input 10 | Digital input 10 |
| 11 | Bidirectional differential digital I/O 3 (as digital input 11) | Digital input 11 | Digital input 11 | Digital input 11 |
| 12 | Bidirectional differential digital I/O 4 (as digital input 12) | Digital input 12 | Digital input 12 | Digital input 12 |
| 13 | - | Digital input 13 | - | Digital input 13 |
| 14 | - | Digital input 14 | - | Digital input 14 |
| 15 | - | Digital input 15 | Differential digital input 1 (as digital input 15) | Digital input 15 |
| 16 | - | Digital input 16 | Differential digital input 2 (as digital input 16) | Digital input 16 |
| 17 | - | Differential digital input 1 (as digital input 17) | Differential digital input 3 (as digital input 17) | Digital input 17 |
| 18 | - | Differential digital input 2 (as digital input 18) | Differential digital input 4 (as digital input 18) | Digital input 18 |
| 19 | - | Differential digital input 3 (as digital input 19) | Differential digital input 5 (as digital input 19) | Digital input 19 |
| 20 | - | Bidirectional differential digital I/O 1 (as digital input 20) | Differential digital input 6 (as digital input 20) | Digital input 20 |
| 21 | - | - | Differential digital input 7 (as digital input 21) | Digital input 21 |
| 22 | - | - | Differential digital input 8 (as digital input 22) | Digital input 22 |
| 23 | - | - | - | Digital input 23 |
| 24 | - | - | - | Digital input 24 |
| 25 | - | - | - | Digital input 25 |
| 26 | - | - | - | Digital input 26 |
| 27 | - | - | - | Digital input 27 |
| 28 | - | - | - | Bidirectional differential digital I/O 1 (as digital input 28) |
| 29 | - | - | - | Bidirectional differential digital I/O 2 (as digital input 29) |
| 30 | - | - | Axis C index | Axis C index |
| 31 | Auxiliary encoder index (from bidirectional differential digital I/O 4) | Auxiliary encoder index | Axis B index | Axis B index |
| 32 | Main encoder index | Main encoder index | Axis A index | Axis A index |
| 33 | - | - | - | Bidirectional differential digital I/O 3 (as digital input 30) |
| 34 | - | - | - | Bidirectional differential digital I/O 4 (as digital input 31) |
| 35 | - | - | - | Bidirectional differential digital I/O 5 (as digital input 32) |
| 36 | - | - | - | Bidirectional differential digital I/O 6 (as digital input 33) |
| 37 | - | - | - | Bidirectional differential digital I/O 7 (as digital input 34) |
| 38 | - | - | - | Bidirectional differential digital I/O 8 (as digital input 35) |

对于 Central-i 产品。反馈记录功能在 I/O 单元（AGIO01 和 AGIO02）以及反馈单元（AGFB01）上不可用。

| abs(Value) | AGA101 / AGA110 | AGA102 | AGA103 / AGL101 | AGA155 | AGL102 | AGL103 |
|---|---|---|---|---|---|---|
| 1 | Digital input 1 | Digital input 1 | Digital input 1 | Digital input 3 | Digital input 1 | Digital input 1 |
| 2 | Digital input 2 | Digital input 2 | Digital input 2 | Digital input 4 | Digital input 2 | Digital input 2 |
| 3 | Digital input 3 | Digital input 3 | Digital input 3 | - | Digital input 3 | Digital input 3 |
| 4 | Digital input 4 | Digital input 4 | Digital input 4 | - | Digital input 4 | Digital input 4 |
| 5 | Digital input 5 | Digital input 5 | Digital input 5 | - | Digital input 5 | Digital input 5 |
| 6 | Digital input 6 | Digital input 6 | Bidirectional differential digital I/O 1 (as digital input 6) | - | Digital input 6 | Bidirectional differential digital I/O 1 (as digital input 6) |
| 7 | Digital input 7 | Digital input 7 | Bidirectional differential digital I/O 1 (as digital input 7) | - | - | - |
| 8 | Digital input 8 | Bidirectional differential digital I/O 1 (as digital input 8) | - | - | - | - |
| 9 | Digital input 9 | - | - | - | - | - |
| 10 | Digital input 10 | - | - | Digital input 12 | - | - |
| 11 | Digital input 11 | - | - | Digital input 13 | - | - |
| 12 | Bidirectional differential digital I/O 1 (as digital input 12) | - | - | Digital input 14 | - | - |
| 13 | - | - | - | Digital input 15 | - | - |
| 14 | - | - | - | Bidirectional differential digital I/O 1 (as digital input 16) | - | - |
| 15 | Auxiliary encoder index | - | - | Auxiliary encoder index | - | Auxiliary encoder index |
| 16 | Main encoder index | Main encoder index | Main encoder index | Main encoder index | Main encoder index | Main encoder index |
| 17 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 |
| 18 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 |
| 19 | Event 3 | Event 3 | Event 3 | Event 3 | Event 3 | Event 3 |
| 20 | Central-i remote signal | Central-i remote signal | Central-i remote signal | Central-i remote signal | Central-i remote signal | Central-i remote signal |

### 选择如何到达硬件

在**独立式**产品上，源/边沿直接编码进驱动编码器硬件捕获的每轴选通设置寄存器中：所选输入被多路复用到选通引脚上，极性位设置上升沿与下降沿。该选通引脚与事件生成共享，因此选择某个 `LockSrc` 并使能 [LockEn](LockEn-AuxLockEn.md) 会从事件生成处取得该引脚的所有权。

在 **Central-i** 产品上，源/边沿被发送至远程驱动器的 FPGA lock 配置寄存器（输入选择位掩码加极性）。远程 FPGA 执行捕获，主控器通过离线邮箱回读锁存到的位置。

在两种情况下，绝对值都在内部转换为从零开始的输入索引（值 `1` → 第一个输入），因此上方表格是源到输入映射的权威来源。

### 源延迟（哪些源触发最快）

并非所有触发源到达捕获逻辑的延迟都相同：

- **分立数字输入和双向差分 I/O** 在能够触发捕获之前会先经过一个可配置的输入消抖/毛刺滤波器。该滤波器拒绝短噪声脉冲，但同时也会在物理边沿与锁存捕获之间增加一个小的、与滤波器相关的延迟。该延迟随输入滤波的配置方式而变化。
- **编码器索引线和霍尔传感器线**基本上以原始信号馈入捕获逻辑，没有消抖级，因此它们以最低的延迟触发。

这就是为什么当你需要最精确的配准时优先选择编码器索引：它以相对于真实边沿最小且一致的延迟捕获反馈位置，而经滤波的分立输入则以少许时序精度换取抗噪能力。

## 示例

```text
ALockSrc=32          ; main encoder index, rising edge (standalone AGD101)
ALockSrc=16          ; main encoder index, rising edge (Central-i)
ALockSrc=0           ; main encoder index, rising edge (where supported)
ALockSrc=-1          ; digital input 1, falling edge
ALockSrc              ; read back the configured source/edge
```

## 另请参阅

- [LockEn](LockEn-AuxLockEn.md) —— 使能基于事件的反馈记录
- [LockCntr](LockCntr-AuxLockCntr.md) —— 在每次 `LockSrc` 事件时递增
- [LockVal](LockVal-AuxLockVal.md) —— 每次事件时记录的反馈位置
