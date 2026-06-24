---
keyword: ForceSamples
summary: 上一次完成的 ForceCmdVal 应用的各项时序，以控制器周期为单位。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 736
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceSamples

上一次完成的 ForceCmdVal 应用的各项时序，以控制器周期为单位。

## 概述

`ForceSamples` 报告上一次完成的 [ForceCmdVal](ForceCmdVal.md) 应用的各项时序，是 [MotionSamples](../../10-motion/05-motion-status/MotionSamples.md) 在力模式下的对应项。它仅在 [ForceCmdSrc](ForceCmdSrc.md) = 1 或 2 时适用。单位为控制器周期数，其中一个周期即采样周期 $T_{s} = \frac{1}{16384\ \text{Hz}} \approx 61.035\ \mu s$。这四项时序在 [ForceInTStat](ForceInTStat.md) 达到 4（已稳定）的时刻一起记录，使用内部周期计数器和驻留时间 [ForceInTTime](ForceInTTime.md)。

当电机失能时，每个元素都被初始化为 `-1`，因此 `-1` 表示“尚无已完成的应用”。该数组使用索引 1 至 4（1-indexed）。

## 工作原理

每个数组元素表示一段不同的经过时间，从新的目标力应用开始时（索引推进到该条目时）起测量：

| 索引 | 说明 |
|----|----|
| 1 | 原始力参考从初始值到达目标值（ForceCmdVal）所需的时间——即斜坡 / “移动”时间。 |
| 2 | `ForceErr` **首次进入** ForceInTTol 窗口（并停留足够长以最终稳定）所需的时间——即“移动并稳定”时间。 |
| 3 | `ForceErr` 被**判定为稳定**（在 ForceInTTol 内停留至少 ForceInTTime）所需的时间——即“移动、稳定并到位”时间。 |
| 4 | 从原始参考到达目标起，到 `ForceErr` 首次进入 ForceInTTol 窗口为止的时间——即单独的“稳定”时间。 |

总结如下：

$$
\text{ForceSamples}[2] = \text{ForceSamples}[1] + \text{ForceSamples}[4]
$$

$$
\text{ForceSamples}[3] = \text{ForceSamples}[2] + \text{ForceInTTime}
$$

（`ForceInTTime` 以与各采样相同的控制器周期为单位表示。）

## 示例

```text
AForceSamples[1]    ; move time, in controller cycles
AForceSamples[3]    ; move + settle + in-target time
```

### 边界情况

- **电机失能** —— 所有四个元素都重置为 `-1`。在下一次稳定完成之前，读取返回 `-1`。
- **不在力模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4）—— 力指令引擎不运行，因此 `ForceSamples` 不会更新；其值保持上一次锁存的内容。
- **`ForceCmdSrc` = 0（模拟量源）** —— 没有定义可供稳定的目标；不运行到位检测，`ForceSamples` 保持为 `-1`。
- **从未稳定** —— 如果 [ForceInTStat](ForceInTStat.md) 从未达到 `4`（力在窗口内未持续驻留至稳定），则不记录任何时序，其值保持为 `-1`。
- **索引越界** —— `ForceSamples` 是 1-indexed，有效索引为 `[1]`–`[4]`；索引 `[0]` 无效。

## 参见

- [ForceInTStat](ForceInTStat.md) —— 到位状态（其达到 4 时记录各采样）
- [ForceInTTol](ForceInTTol.md) —— 稳定窗口
- [ForceInTTime](ForceInTTime.md) —— 窗口内所需的驻留时间
- [MotionSamples](../../10-motion/05-motion-status/MotionSamples.md) —— 位置/速度移动的等效时序
