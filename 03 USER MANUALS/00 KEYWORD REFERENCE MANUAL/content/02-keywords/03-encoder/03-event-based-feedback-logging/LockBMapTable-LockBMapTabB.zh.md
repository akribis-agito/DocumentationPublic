---
summary: 在启用锁存 FIFO 构建的 Central-i 主站上，存储每个已记录数字事件映射前反馈位置的历史数组。
last_updated: '2026-10-20'
doc_revision: '2026.10'
language: zh-CN
---
# LockBMapTable/LockBMapTabB

在启用锁存 FIFO 构建的 Central-i 主站上，存储每个已记录数字事件映射前反馈位置的历史数组。

## 概述

`LockBMapTable`（CAN 代码 958）和 `LockBMapTabB`（CAN 代码 959）以用户单位存储在每个触发事件时捕获的**误差映射之前**的反馈位置（即 `LockValBefMap` 的值，CAN 代码 957）。它们是 [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB` 的映射前配套数组：同一事件写入相同的索引，因此 `LockBMapTable[n]` 与 `LockValTable[n]` 描述的是同一次捕获在映射前和映射后的值。

两个数组均为只读，按轴设置，不保存至闪存。

**可用性：**仅适用于固件在构建时启用锁存 FIFO 的 Central-i 主站（编译开关 `CFG_CI_LOCK_FIFO = 1`，默认关闭）。在其他所有构建中，CAN 代码 958 和 959 为未使用的占位项，读取它们会返回错误。

## 工作原理

两个数组均为 1 索引。在每个事件上，固件递增 [LockCntr](LockCntr-AuxLockCntr.md)，并将映射前位置写入由该计数器选定的数组，其索引与 [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB` 以及 [LockTimeTable](LockTimeTable-LockTimeTabB.md) / `LockTimeTabB` 相同：

| 条件 | 所用数组 | 对应索引 |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 65000$ | LockBMapTable | $\text{LockCntr}$ |
| $65001 \leq \text{LockCntr} \leq 130000$ | LockBMapTabB | $\text{LockCntr} - 65000$ |

一旦两个数组都已填满，记录即停止，而 [LockCntr](LockCntr-AuxLockCntr.md) 和 [LockVal](LockVal-AuxLockVal.md) 仍持续更新，与 `LockValTable` 完全相同。

每个条目为 32 位宽，与 `LockValTable` 相同。在 Central-i 主站上位置本身为 64 位宽，因此条目保存的是映射前位置的低 32 位。

## 示例

```text
ALockBMapTable[1]    ; read the before-map position of the first logged event
ALockValTable[1]     ; the same event after error mapping
```

## 另请参阅

- [LockValTable](LockValTable-LockValTabB.md) —— 映射后位置的历史数组（相同的索引方案）
- [LockTimeTable](LockTimeTable-LockTimeTabB.md) —— 时间戳历史数组（相同的索引方案）
- [LockCntr](LockCntr-AuxLockCntr.md) —— 用作数组索引的事件计数器
- [LockVal](LockVal-AuxLockVal.md) —— 最近一次事件的映射后位置
