---
keyword: ForceCmdSlope
summary: 朝向每个力指令表条目的斜坡变化速率（单位/秒）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 569
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceCmdSlope

朝向每个力指令表条目的斜坡变化速率（单位/秒）。

## 概述

`ForceCmdSlope` 定义从当前原始 [ForceRef](ForceRef.md) 值过渡到当前 [ForceCmdVal](ForceCmdVal.md) 条目的斜率，以每秒单位计。它仅在 [ForceCmdSrc](ForceCmdSrc.md) = 1 或 2 时适用。保持计时器 [ForceCmdCntr](ForceCmdCntr.md) 仅在斜坡变化完成后才从 0 开始计数。每个表条目都有自己的斜率（数组索引为 1 至 20，与相同索引的 [ForceCmdVal](ForceCmdVal.md) 配对）。

## 工作原理

当原始参考值尚未达到目标值时，生成器每个控制周期按 `ForceCmdSlope[ForceCmdIndex] * Ts` 将其朝目标值步进，其中 `Ts` 为周期时间：

$$
\Delta \text{ForceRef}\ [\text{unit}] = \text{ForceCmdSlope} \cdot T_{s}
$$

在斜坡变化期间，控制器将 [ForceInTStat](ForceInTStat.md) 设为 2（斜坡变化中）并将 [ForceCmdCntr](ForceCmdCntr.md) 保持为 0。步进被钳位，使参考值不会过冲目标 [ForceCmdVal](ForceCmdVal.md)。仅当原始参考值精确等于目标值时，保持计时器才开始计时并开始到位停留。由于 `ForceCmdSlope` 的最小值为 1，斜坡变化始终是有限的（值无法以瞬时阶跃方式施加）。

## 示例

```text
AForceCmdSlope[3]=700 ; ramp into entry 3 at 700 units/s
```

### 边界情况

- **索引 0**——无效；有效索引为 `ForceCmdSlope[1]`–`ForceCmdSlope[20]`。
- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4 或 [ForceCmdSrc](ForceCmdSrc.md) ∉ {1, 2}）——**不查询**该斜率。
- **超出范围**——`0` 和负值被拒绝；最小值为 `1` 以保证有进展。
- **大斜率**——单周期步进大于剩余距离时，使 `ForceRef` 在下一周期跳变到目标值。
- **斜坡中途重载**——在当前条目上写入新斜率会从下一周期改变速率。
- **保存**——可保存至闪存。

## 另请参阅

- [ForceCmdVal](ForceCmdVal.md) —— 目标力值
- [ForceCmdHTime](ForceCmdHTime.md) —— 每个条目的保持时间
- [ForceCmdCntr](ForceCmdCntr.md) —— 斜坡变化后开始的计时器
