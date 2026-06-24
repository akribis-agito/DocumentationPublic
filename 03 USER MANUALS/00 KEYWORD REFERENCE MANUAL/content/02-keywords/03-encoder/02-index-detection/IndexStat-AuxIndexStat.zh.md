---
summary: 指示编码器索引脉冲是否已被检测到的标志。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# IndexStat/AuxIndexStat

指示编码器索引脉冲是否已被检测到的标志。

## 概述

`IndexStat` 指示在最近一个控制周期是否看到了编码器索引脉冲：`0` 表示未检测到，`1` 表示已检测到。仅当编码器类型（[EncType](../01-general-settings/EncType-AuxEncType.md)）为 1（数字增量式）或 4（SIN/COS）时才有意义，因为只有增量式编码器带有索引标志。它为只读、轴范围，且不保存至闪存。当检测到索引时，控制器将反馈位置锁存到 [IndexPos](IndexPos-AuxIndexPos.md) 并置位此标志 —— 通常用于回零。`AuxIndexStat` 是辅助编码器的对应项。

## 工作原理

`IndexStat` 在每个控制周期重新评估。在每次控制中断的开头，固件先假定无索引（`IndexStat = 0`），然后测试索引输入；若被置位，则将 `IndexStat` 设为 1 并捕获 [IndexPos](IndexPos-AuxIndexPos.md)（在独立控制器上来自专用索引输入，在 central-i 上来自逐轴状态位）。由于该标志在每个周期开始时被清除，它只反映*当前*周期 —— 在用户清除之前并不会被锁存。需要对单个索引事件作出响应的使用方（例如回零）会在该标志被置位的那个周期内读取它。

| IndexStat | Meaning |
|---|---|
| 0 | Index not detected this control cycle |
| 1 | Index detected this control cycle |

该标志驱动两项固件特性：

- **Stop on index**（[StopOnIndex](../../16-homing/StopOnIndex.md)）：在点动/手柄运动期间，若设置了 `StopOnIndex` 且 `IndexStat` 为 1，规划器发出停止请求并报告运动结束原因为“index”。
- **回零/换相：** 回零步骤通过 `IndexStat`/`IndexPos` 引用索引；对于霍尔加索引的换相方法，固件等待 `IndexStat` 以将换相角设为零。

## AuxIndexStat

`AuxIndexStat` 是辅助编码器的对应项，具有相同的 0/1 含义。辅助索引硬件仅存在于单轴硬件型号上；在多轴控制器上不检测辅助索引（参见[本章节概述](00-overview.md)）。

## 示例

```text
AIndexStat          ; check whether the index was detected this cycle
```

## 边界情况

- **电机失能。** 只要在读取编码器信号，检测就会运行；即使电机被禁用，只要手动移动轴，索引仍可被检测到（并捕获 `IndexPos`）。
- **慢速与快速运动。** 由于索引每个控制周期轮询一次，它必须保持置位长于一个采样才能被看到。在假定索引为 1 节距宽时，速度应保持低于（每节距编码器计数）×（控制器采样频率）—— 参见[本章节概述](00-overview.md)。
- **编码器类型。** 仅对 `EncType=1`（增量式）和 `EncType=4`（SIN/COS）有意义。绝对式编码器不带索引标志，因此 `IndexStat` 不会置位。
- **多轴硬件上的辅助编码器。** `AuxIndexStat` 仅在单轴硬件型号上接线；在多轴控制器上不检测辅助索引 —— `AuxIndexStat` 不会置位。
- **Central-i。** 远程驱动器在其逐轴状态字中标记索引；主站每个周期将其镜像到 `IndexStat`，并采用相同的一周期检测规则。
- **每个周期清除。** 该标志在每次控制中断开始时被重新置位；使用方（回零、`StopOnIndex`）必须在索引发生的那个周期内作出响应，或使用 [LockEn](../03-event-based-feedback-logging/LockEn-AuxLockEn.md) 进行锁存式捕获。

## 参见

- [IndexPos](IndexPos-AuxIndexPos.md) —— 检测到索引时捕获的位置
- [EncType](../01-general-settings/EncType-AuxEncType.md) —— 编码器类型；索引检测适用于 `EncType=1` 或 `4`
- [StopOnIndex](../../16-homing/StopOnIndex.md) —— 在下一个索引脉冲处停止轴
- [00-overview](00-overview.md) —— 索引检测轮询与最大点动速度
