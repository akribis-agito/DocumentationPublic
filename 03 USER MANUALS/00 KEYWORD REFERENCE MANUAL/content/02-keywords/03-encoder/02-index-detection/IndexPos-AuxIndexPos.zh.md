---
summary: 记录最近一次检测到编码器索引时的位置。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# IndexPos/AuxIndexPos

记录最近一次检测到编码器索引时的位置。

## 概述

`IndexPos` 记录最近一次检测到编码器索引（参考标志）时捕获的反馈位置。仅当编码器类型（[EncType](../01-general-settings/EncType-AuxEncType.md)）为 1（数字增量式）或 4（SIN/COS）时才有意义，因为只有增量式编码器带有索引标志。它为只读、轴范围，且不保存至闪存。它通常用于回零，与检测标志 [IndexStat](IndexStat-AuxIndexStat.md) 配合使用。`AuxIndexPos` 是辅助编码器的对应项。

## 工作原理

索引每个控制周期采样一次。在每次控制中断开始时，固件先将 [IndexStat](IndexStat-AuxIndexStat.md) 清零，然后测试该轴的索引输入。当索引被置位时，将 `IndexStat` 设为 1，并将当前反馈位置锁存到 `IndexPos`：

- **独立控制器：** 索引线从每个轴的编码器索引输入读取。检测到时，`IndexStat = 1` 且 `IndexPos = Pos`（上一采样的反馈位置）。
- **Central-i：** 索引作为逐轴远程报文中的一个状态位传送；当该位被置位时，发生相同的 `IndexStat = 1` / `IndexPos = Pos` 捕获。

捕获到的值是*上一*采样的反馈位置，而非边沿处的精确子采样位置，因此锁存值精确到一个控制周期以内。由于检测每个周期轮询一次，索引脉冲必须保持置位足够长的时间才能被看到 —— 由此产生的最大点动速度参见[本章节概述](00-overview.md)。

`IndexPos` 直接为回零提供输入。在“移动至索引”的回零步骤中，固件将绝对目标（[AbsTrgt](../../10-motion/13-motion-mode-ptp/AbsTrgt.md)）设为捕获到的索引位置，使轴精确移动到锁存的索引位置。

## AuxIndexPos

`AuxIndexPos` 是辅助编码器的对应项，行为完全相同，会在辅助索引事件上锁存辅助反馈位置。辅助索引硬件仅在单轴硬件型号上接线；在多轴控制器上不检测辅助索引（参见[本章节概述](00-overview.md)中的注意事项）。

## 版本间变更

| | v4 | v5 (central-i) |
|---|---|---|
| Stored width | 32-bit | 64-bit |

在 **v5** 中，索引位置以 64 位值保存，与该固件中其他位置计数器所用的更宽位宽相匹配；**v4** 存储 32 位值。除此之外，该关键字的取值与用法保持不变。**v5 仅限 central-i。**

## 示例

```text
AIndexPos           ; read the position of the last detected index
```

## 边界情况

- **电机失能。** 只要在读取编码器，捕获机制就会运行；即使电机被禁用，在手动移动轴时索引仍可被锁存。
- **速度限制。** 检测每个控制周期轮询一次，因此捕获位置存在最多一个周期的不确定性。运动速度应足够慢，使索引脉冲至少跨越一个采样 —— 参见[本章节概述](00-overview.md)。
- **编码器类型。** 仅对 `EncType=1` 和 `EncType=4` 有意义。绝对式编码器不带索引 —— `IndexPos` 对其不会更新。
- **多轴硬件上的辅助编码器。** `AuxIndexPos` 仅在单轴硬件型号上更新；在多轴控制器上不检测辅助索引。
- **Central-i 断开。** 主站每个周期镜像远程单元的逐轴索引位；当端口断开（[CIStatus](../../01-system/05-central-i/CIStatus.md)`[1] ≠ 3`）时，没有远程帧到达，因此 `IndexPos` 不会更新。
- **一次运动中出现多个索引。** 每个检测到的脉冲都会用最新捕获的位置覆盖 `IndexPos`。如需逐事件的历史记录，请使用基于事件的记录（[LockValTable](../03-event-based-feedback-logging/LockValTable-LockValTabB.md)）。

## 参见

- [IndexStat](IndexStat-AuxIndexStat.md) —— 指示索引是否已被检测到的标志
- [EncType](../01-general-settings/EncType-AuxEncType.md) —— 编码器类型；索引检测适用于 `EncType=1` 或 `4`
- [StopOnIndex](../../16-homing/StopOnIndex.md) —— 在下一个索引脉冲处停止轴
- [00-overview](00-overview.md) —— 索引检测轮询与最大点动速度
