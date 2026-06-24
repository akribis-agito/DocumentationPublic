---
keyword: ForceCmdCntr
summary: 力模式下或当前 ForceCmdVal 条目中已经过的时间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 574
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceCmdCntr

力模式下或当前 ForceCmdVal 条目中已经过的时间。

## 概述

`ForceCmdCntr` 是已经过的时间（以毫秒为单位），用于驱动力运行模式的时序表逻辑。其含义取决于 [ForceCmdSrc](ForceCmdSrc.md)：

1. 若 `ForceCmdSrc` = 0（模拟量输入）：在力运行模式下已经过的时间。
2. 若 `ForceCmdSrc` = 1 或 2（用户自定义表）：在当前 [ForceCmdVal](ForceCmdVal.md) 数组条目下已经过的时间。切换到下一个 `ForceCmdVal` 条目时，该值重置为 0。

在收到 [GoToForceMode](GoToForceMode.md) 命令时、在自动条件切换时，或在数字量输入切换至力运行模式时，`ForceCmdCntr` 重置为 0。这意味着当直接对 [OperationMode](../01-general-keywords/OperationMode.md) 赋值时，用户可将其预设为任意初始值，并从该值开始计时。

> **注意：** 在力运行模式下，用户可随时覆写 `ForceCmdCntr`。

## 工作原理

`ForceCmdCntr` 每个控制周期递增一次，并与 [ForceCmdHTime](ForceCmdHTime.md) 进行比较，以决定何时推进表条目或退出力模式。对于表源（[ForceCmdSrc](ForceCmdSrc.md) = 1 或 2），它仅在力参考值保持在其目标值时计数，而**在参考值仍在向目标值斜坡变化期间保持为 0**，因此它仅测量保持时间，而不测量斜坡时间。对于模拟量源（`ForceCmdSrc` = 0），只要 `ForceCmdHTime[1]` 大于或等于 0，它在力模式下每个控制周期都递增。内部计数器被钳位在 2,000,000,000 处以防止翻转。

当表索引推进到新条目时，计数器被清为 0；在**最后一个**条目上，它将保持运行，以便用户可以读取轴保持最终值的时长。

## 示例

```text
AForceCmdCntr       ; read elapsed time (ms)
AForceCmdCntr=0      ; restart the timer
```

### 边界情况

- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4）——不推进。
- **斜坡变化期间的源 1/2**——在 [ForceCmdSlope](ForceCmdSlope.md) 进行斜坡变化期间保持为 `0`；仅在 `ForceRef = ForceCmdVal[index]` 后才开始计数。
- **饱和**——钳位在 `2 000 000 000` 处以避免翻转。
- **索引被钳位（20）**——计数器保持运行，不重置。
- **手动写入**——在力模式下允许；可重启一次保持或缩短一次长保持。
- **GoToForceMode**——将计数器重置为 `0`；直接 `OperationMode = 4` 则不会。
- **保存**——不可保存至闪存。

## 另请参阅

- [ForceCmdHTime](ForceCmdHTime.md) —— 与该计数器比较的保持时间
- [ForceCmdIndex](ForceCmdIndex.md) —— 当前表条目
- [GoToForceMode](GoToForceMode.md) —— 进入时重置该计数器
