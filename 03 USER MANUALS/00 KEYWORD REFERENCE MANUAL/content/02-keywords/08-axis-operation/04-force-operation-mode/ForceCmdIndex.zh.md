---
keyword: ForceCmdIndex
summary: 当前 ForceCmdVal / ForceCmdHTime 表条目的索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 573
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 20
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceCmdIndex

当前 ForceCmdVal / ForceCmdHTime 表条目的索引。

## 概述

`ForceCmdIndex` 是当前正在使用的 [ForceCmdVal](ForceCmdVal.md) 和 [ForceCmdHTime](ForceCmdHTime.md) 值的索引。它仅在 [ForceCmdSrc](ForceCmdSrc.md) = 1 或 2（用户自定义表）时适用。

在收到 [GoToForceMode](GoToForceMode.md) 命令时、在自动条件切换时，或在数字量输入切换至力运行模式时，`ForceCmdIndex` 重置为 1。这意味着当直接对 [OperationMode](../01-general-keywords/OperationMode.md) 赋值时，用户可将其预设，使参考表从期望的 `ForceCmdVal`/`ForceCmdHTime` 对开始。

> **注意：** 在力运行模式下，用户可随时覆写 `ForceCmdIndex`。这会立即切换正在使用的 `ForceCmdVal`，而不重置 [ForceCmdCntr](ForceCmdCntr.md) 计时器。

## 工作原理

当当前条目的保持时间耗尽时，生成器自动递增 `ForceCmdIndex`。它被钳位至最后一个可用条目（20）：如果它将推进越过数组末尾，则保持在该处，使轴停留在最终的 [ForceCmdVal](ForceCmdVal.md) 上，而不是回绕。推进到新条目时，保持计时器 [ForceCmdCntr](ForceCmdCntr.md) 被清零，以便下一条目的 [ForceCmdHTime](ForceCmdHTime.md) 从零开始计时。

正常进入时重置为 `1` 的操作由 [GoToForceMode](GoToForceMode.md) 以及自动 / 数字量输入切换路径执行。

## 示例

```text
AForceCmdIndex      ; read the active table entry
AForceCmdIndex=3     ; jump to the third entry
```

### 边界情况

- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4 或 [ForceCmdSrc](ForceCmdSrc.md) ∉ {1, 2}）——**不查询** `ForceCmdIndex`。
- **超出范围**——`1`–`20` 之外的值被拒绝。
- **斜坡中途写入**——覆写索引会在下一周期切换到新目标，而不重置 [ForceCmdCntr](ForceCmdCntr.md)。
- **GoToForceMode**——始终将 `ForceCmdIndex` 重置为 1；直接 `OperationMode = 4` 则不会。
- **表尾**——钳位在 `20`；钳位时固件不重置计数器。
- **保存**——不可保存至闪存。

## 另请参阅

- [ForceCmdVal](ForceCmdVal.md) —— 力值表
- [ForceCmdHTime](ForceCmdHTime.md) —— 每个条目的保持时间
- [ForceCmdCntr](ForceCmdCntr.md) —— 当前条目的计时器
