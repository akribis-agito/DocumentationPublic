---
summary: 存储每个已记录数字事件的控制器周期时间的历史数组。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LockTimeTable/LockTimeTabB

存储每个已记录数字事件的控制器周期时间的历史数组。

## 概述

`LockTimeTable` 和 `LockTimeTabB` 存储每个触发事件发生的时间，以自反馈记录使能以来经过的控制周期数表示（当 [LockEn](LockEn-AuxLockEn.md) 从禁用变为使能时，经过周期计时器复位为 0，并每个控制周期递增一次）。它们是位置历史数组 [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB` 的时间戳对应项，在相同的索引 [LockCntr](LockCntr-AuxLockCntr.md) 处写入。当 `LockTimeTable` 填满时，记录继续写入 `LockTimeTabB`。

要将存储值转换为秒，需乘以控制周期时间（控制采样间隔）。在标准产品上，控制环以 16384 Hz 运行，因此每个计数为 1/16384 s ≈ 61.035 µs；在快速采样产品上，它以 65536 Hz 运行，因此每个计数为 1/65536 s ≈ 15.259 µs。例如，标准产品上存储值为 1000 对应于记录使能后 1000 × 61.035 µs ≈ 61.0 ms。

时间戳本身就是经过周期计数，因此其分辨率恰好为一个控制周期。在不同周期捕获的两个事件总是至少相差一个计数，而一个事件的时间戳反映的是它被处理的那个周期，而非触发边沿的精确子周期时刻。由于每个控制周期最多记录一个事件（见 [LockCntr](LockCntr-AuxLockCntr.md)），落在同一周期内的任何触发边沿共享该单一时间戳。

## 工作原理

两个数组均为 1 索引。每次事件时，固件递增 [LockCntr](LockCntr-AuxLockCntr.md) 并将计时器写入由该计数器选择的数组。容量因产品而异：独立式产品上每个数组容纳 50 个条目，Central-i 产品上容纳 65000 个条目。

**独立式**（50 + 50 = 100 个事件）：

| 条件 | 使用的数组 | 对应索引 |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 50$ | LockTimeTable | $\text{LockCntr}$ |
| $51 \leq \text{LockCntr} \leq 100$ | LockTimeTabB | $\text{LockCntr} - 50$ |

**Central-i**（65000 + 65000 = 130000 个事件）：

| 条件 | 使用的数组 | 对应索引 |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 65000$ | LockTimeTable | $\text{LockCntr}$ |
| $65001 \leq \text{LockCntr} \leq 130000$ | LockTimeTabB | $\text{LockCntr} - 65000$ |

一旦两个数组都填满，时间戳记录停止，而 [LockCntr](LockCntr-AuxLockCntr.md) 和 [LockVal](LockVal-AuxLockVal.md) 继续更新。

## 示例

在 Central-i 产品上，当某个事件触发记录且 `LockCntr` 达到 70000 时，`LockTimeTabB[5000]` 存储经过周期时间。在独立式产品上，当 `LockCntr` 达到 70 时，使用 `LockTimeTabB[20]`。

```text
ALockTimeTable[1]    ; read the time stamp (in control cycles) of the first captured event
```

## 参见

- [LockValTable](LockValTable-LockValTabB.md) —— 位置历史数组（相同的索引方案）
- [LockCntr](LockCntr-AuxLockCntr.md) —— 用作数组索引的事件计数器
- [LockEn](LockEn-AuxLockEn.md) —— 使能记录；复位经过周期计时器
