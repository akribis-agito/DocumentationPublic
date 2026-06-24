---
keyword: ForceInTTime
summary: 力控制判定到位前必须在稳定窗口内保持的最小驻留时间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 733
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: null
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceInTTime

力控制判定到位前必须在稳定窗口内保持的最小驻留时间。

## 概述

`ForceInTTime` 定义了力误差（[ForceErr](ForceErr.md)）必须持续保持在稳定窗口（[ForceInTTol](ForceInTTol.md)）内的最小时间（单位：毫秒），之后轴才在 [ForceInTStat](ForceInTStat.md) 中被视为已到位。仅当 [ForceCmdSrc](ForceCmdSrc.md) = 1 或 2 时适用。

## 工作原理

内部驻留计数器仅在 [ForceInTStat](ForceInTStat.md) = 3 时激活。控制器每个周期测试 `|ForceErr| <= ForceInTTol`；若为真则递增计数器，否则将其重新清零。一旦计数器达到 `ForceInTTime`，轴即被视为已到位（`ForceInTStat` = 4），且对该指令项不再检查稳定条件。

值为 `0` 表示一旦 `ForceErr` 首次进入窗口，轴即被判定为已到位（无需驻留）。

## 示例

```text
AForceInTTime=50     ; require 50 ms within the settling window
```

### 边界情况

- **错误模式 / 错误源**——仅当 [OperationMode](../01-general-keywords/OperationMode.md) = 4 且 [ForceCmdSrc](ForceCmdSrc.md) ∈ {1, 2} 时使用；其他情况下忽略。
- **零值**——一旦误差进入 [ForceInTTol](ForceInTTol.md) 一个周期即锁存到位（驻留为零）。
- **超出容差**——在驻留期间离开窗口会将驻留计数器重新清零；驻留必须连续累计。
- **超出范围**——超出 `0`–`163840` 的值将被拒绝。
- **保存**——可保存至闪存。

## 另请参阅

- [ForceInTTol](ForceInTTol.md) —— 稳定窗口
- [ForceInTStat](ForceInTStat.md) —— 由该定时器驱动的到位状态
- [ForceErr](ForceErr.md) —— 与窗口比较的误差
