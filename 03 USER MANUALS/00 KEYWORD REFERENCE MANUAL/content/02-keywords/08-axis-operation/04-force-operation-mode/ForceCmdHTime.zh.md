---
keyword: ForceCmdHTime
summary: 每个力指令表条目的保持时间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 572
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2000000000
  - 2000000000
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceCmdHTime

每个力指令表条目的保持时间。

## 概述

`ForceCmdHTime` 定义力运行模式下力参考值的保持时间（以毫秒为单位）。其用法取决于 [ForceCmdSrc](ForceCmdSrc.md)：

- 若 `ForceCmdSrc` = 0（模拟量输入）：仅使用 `ForceCmdHTime[1]`，定义停留在力运行模式内的时间。
- 若 `ForceCmdSrc` = 1 或 2（用户自定义表）：每个数组元素定义对应 [ForceCmdVal](ForceCmdVal.md) 条目的保持时间。

## 工作原理

生成器每个周期读取当前条目的保持时间，并根据其符号进行分支处理：

| 值 | 描述 |
|---|---|
| < 0 | 源值无限期保持。轴在该条目上停留于力模式；对于表源，到位检测仍然运行。 |
| 0 | 轴退出力运行模式并进入位置运行模式。对于表源（`ForceCmdSrc` = 1 或 2），当 [ForcePIVOn](../../11-control-tuning/07-force-control/ForcePIVOn.md) 激活时，速度积分器在退出过程中被预置，以避免电流参考跳变。 |
| > 0 | 源值保持 `ForceCmdHTime` 时长，之后退出力运行模式（`ForceCmdSrc` = 0）或进入下一对（`ForceCmdSrc` = 1 或 2）。对于 `ForceCmdSrc` = 1 或 2，若 [ForceCmdIndex](ForceCmdIndex.md) 达到最后一个索引值且最后一个 `ForceCmdHTime` 条目大于 0，则轴无限期保持最后一个 `ForceCmdVal` 值。 |

保持时间由 [ForceCmdCntr](ForceCmdCntr.md) 计时，它仅在参考值处于目标值时计数（斜坡时间被排除）。对于模拟量源，仅参考 `ForceCmdHTime[1]`。

## 示例

```text
AForceCmdHTime[1]=400 ; hold first entry for 400 ms
AForceCmdHTime[2]=0   ; exit force mode after the second entry
```

### 边界情况

- **索引 0**——无效；有效索引为 `ForceCmdHTime[1]`–`ForceCmdHTime[20]`。
- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4）——**不查询**该表。
- **零值**——在该条目处退出力模式；对于表源（`ForceCmdSrc` = 1 或 2）且 `ForcePIVOn = 1` 时，速度积分器在退出时被预置，以避免电流参考跳变。
- **负值**——无限期保持；仅显式的模式更改才会离开该条目。
- **表尾（索引 20 且 HTime 为正）**——固件无限期保持最后一个值。
- **计数器饱和**——[ForceCmdCntr](ForceCmdCntr.md) 钳位在 2 000 000 000 处以避免翻转。
- **模拟量源**（[ForceCmdSrc](ForceCmdSrc.md) = 0）——仅参考 `ForceCmdHTime[1]`；数组其余部分未使用。
- **保存**——可保存至闪存。

## 另请参阅

- [ForceCmdVal](ForceCmdVal.md) —— 与这些保持时间配对的力值
- [ForceCmdIndex](ForceCmdIndex.md) —— 当前表条目
- [ForceCmdCntr](ForceCmdCntr.md) —— 与该值比较的已经过时间
