---
summary: 记录最近一次已记录数字事件的反馈位置。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# LockVal/AuxLockVal

记录最近一次已记录数字事件的反馈位置。

## 概述

`LockVal` 保存在最近一次触发事件时锁存的反馈位置（事件源由 [LockSrc](LockSrc-AuxLockSrc.md) 设置）。其以用户单位报告。每个事件还会在索引 [LockCntr](LockCntr-AuxLockCntr.md) 处将该值追加到位置历史数组 [LockValTable](LockValTable-LockValTabB.md)。`AuxLockVal` 是其辅助编码器对应项。

`LockVal` 为只读，且即使在历史表已满之后，仍会在每次触发事件时持续更新。

## 工作原理

位置如何被捕获取决于编码器类型：

- **数字增量式 / SIN-COS 编码器** —— 编码器计数在触发边沿的精确时刻由硬件锁存。固件读取该锁存的计数并将其换算到用户反馈单位，因此 `LockVal` 对触发时刻而言是精确的，且不受控制周期抖动的影响。这是用于打标 / 探测的预期用法。
- **绝对式 / 其他非增量式编码器** —— 硬件锁存不可用，因此 `LockVal` 被设为最近一次轮询的反馈位置（[Pos](../../10-motion/01-kinematics-status/Pos.md)）。触发必须持续足够长的时间，以便在控制周期速率下被检测到，所捕获的值对轮询时刻的位置而言是精确的，但相对于真实触发时刻略有延迟。对于该方法，应使轴速度足够低，以免在两个控制周期之间漏掉某个索引 / 触发。

所捕获的值参照与 [Pos](../../10-motion/01-kinematics-status/Pos.md) 相同的反馈流水线：固件会补偿原始硬件捕获计数器与用户单位反馈值之间的偏移，因此 `LockVal` 可直接与 `Pos` 比较。

## 示例

```text
ALockVal             ; read the position of the most recent captured event
```

## 另请参阅

- [LockSrc](LockSrc-AuxLockSrc.md) —— 定义更新 `LockVal` 的触发事件
- [LockValTable](LockValTable-LockValTabB.md) —— 捕获位置的历史数组
- [LockCntr](LockCntr-AuxLockCntr.md) —— 捕获事件的计数
- [Pos](../../10-motion/01-kinematics-status/Pos.md) —— 被捕获的反馈位置
