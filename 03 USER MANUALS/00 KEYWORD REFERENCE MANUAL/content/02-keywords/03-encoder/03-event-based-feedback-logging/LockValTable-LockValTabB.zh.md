---
summary: 存储每个已记录数字事件反馈位置的历史数组。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LockValTable/LockValTabB

存储每个已记录数字事件反馈位置的历史数组。

## 概述

`LockValTable` 和 `LockValTabB` 以用户单位存储在每个触发事件时捕获的反馈位置（即 [LockVal](LockVal-AuxLockVal.md) 的每个相继值）。它们在运行索引 [LockCntr](LockCntr-AuxLockCntr.md) 处写入，并且是时间戳数组 [LockTimeTable](LockTimeTable-LockTimeTabB.md) / `LockTimeTabB` 的位置配套数组。当 `LockValTable` 填满时，记录将继续写入 `LockValTabB`。

## 工作原理

两个数组均为 1 索引，并在与其时间戳配套数组相同的索引处写入。在每个事件上，固件递增 [LockCntr](LockCntr-AuxLockCntr.md) 并将 [LockVal](LockVal-AuxLockVal.md) 写入由该计数器选定的数组。容量取决于产品：每个数组在独立产品上保存 50 条，在 Central-i 产品上保存 65000 条。

**独立产品**（50 + 50 = 100 个事件）：

| 条件 | 所用数组 | 对应索引 |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 50$ | LockValTable | $\text{LockCntr}$ |
| $51 \leq \text{LockCntr} \leq 100$ | LockValTabB | $\text{LockCntr} - 50$ |

**Central-i**（65000 + 65000 = 130000 个事件）：

| 条件 | 所用数组 | 对应索引 |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 65000$ | LockValTable | $\text{LockCntr}$ |
| $65001 \leq \text{LockCntr} \leq 130000$ | LockValTabB | $\text{LockCntr} - 65000$ |

一旦两个数组都已填满，位置记录即停止，而 [LockCntr](LockCntr-AuxLockCntr.md) 和 [LockVal](LockVal-AuxLockVal.md) 仍持续更新。

## 示例

在 Central-i 产品上，当某个事件触发记录且 `LockCntr` 达到 71000 时，`LockValTabB[6000]` 存储所捕获的位置。在独立产品上，当 `LockCntr` 达到 71 时，使用 `LockValTabB[21]`。

```text
ALockValTable[1]     ; read the captured position of the first event
```

## 另请参阅

- [LockVal](LockVal-AuxLockVal.md) —— 存入这些数组的值
- [LockTimeTable](LockTimeTable-LockTimeTabB.md) —— 时间戳历史数组（相同的索引方案）
- [LockCntr](LockCntr-AuxLockCntr.md) —— 用作数组索引的事件计数器
