---
summary: 选择点到点运动规划器的阶次；参见运动配置中的 JerkMode。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# JerkMode

选择点到点运动规划器的阶次；参见运动配置中的 `JerkMode`。

## 概述

`JerkMode` 选择点到点运动所用运动规划器的阶次。完整说明及取值表保存在运动配置章节的主条目 [JerkMode](../02-motion-configuration/JerkMode.md) 中。

该取值决定每个控制周期运行哪个规划器：

| `JerkMode` | 规划器 | 所用 jerk 参数 |
|------------|----------|----------------------|
| 0 | 二阶梯形 + 滑动平均平滑 | [Jerk](Jerk.md)（boxcar 窗口 2^Jerk 个周期） |
| 1 | 三阶结构化（双 S 型）规划器 | [JerkInAcc](JerkInAcc.md) / [JerkInDec](JerkInDec.md) |

请注意，紧急停止、限位开关停止或受控停止会覆盖此项选择：无论配置的 `JerkMode` 为何，控制器都会针对该次停止强制采用二阶（模式 0）行为，并以 [EmrgDec](EmrgDec.md) 制动。`JerkMode` 不能在轴运动时更改。

## 参见

- [JerkMode](../02-motion-configuration/JerkMode.md) — 包含完整取值表的主条目
- [Jerk](Jerk.md) — 二阶 jerk 设置（模式 0）
- [JerkInAcc](JerkInAcc.md) — 加速阶段的 jerk（模式 1）
- [JerkInDec](JerkInDec.md) — 减速阶段的 jerk（模式 1）
- [EmrgDec](EmrgDec.md) — 无论此设置如何，紧急停止都强制采用模式 0
