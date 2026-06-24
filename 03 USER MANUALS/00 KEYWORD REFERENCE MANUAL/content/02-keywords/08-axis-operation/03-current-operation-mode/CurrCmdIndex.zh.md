---
keyword: CurrCmdIndex
summary: 活动 CurrCmdVal / CurrCmdHTime 表条目的索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 333
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
# CurrCmdIndex

活动 CurrCmdVal / CurrCmdHTime 表条目的索引。

## 概述

`CurrCmdIndex` 是当前使用的 [CurrCmdVal](CurrCmdVal.md) 和 [CurrCmdHTime](CurrCmdHTime.md) 值的索引。它仅在 [CurrCmdSrc](CurrCmdSrc.md) = 1 或 2（用户自定义表）时适用。

`CurrCmdIndex` 在收到 [GoToCurrMode](GoToCurrMode.md) 命令时、自动条件切换时或数字量输入切换到电流控制模式时复位为 1。这意味着当直接赋值 [OperationMode](../01-general-keywords/OperationMode.md) 时，用户可以预设该索引，使参考表从所需的 `CurrCmdVal`/`CurrCmdHTime` 对开始。

## 工作原理

有效范围为 1 到 20（[CurrCmdVal](CurrCmdVal.md) / [CurrCmdHTime](CurrCmdHTime.md) 表保存 20 个可用条目）。固件自动推进该索引：

- 当保持计时器 [CurrCmdCntr](CurrCmdCntr.md) 达到 `CurrCmdHTime[index]`（正值）时，`CurrCmdIndex` 递增，且计数器为新条目复位为 0。
- 若递增将超过 20，则索引被**钳位到 20** — 此时轴无限期保持最后一个条目的 `CurrCmdVal`（前提是该条目的 `CurrCmdHTime` 非零）。在此钳位状态下，计数器被有意**不**复位，以便用户观察轴停留在最后一个条目上的时长。
- 一个 `CurrCmdHTime` 为 0 的条目会停止该序列并退出到位置模式（索引不会越过它前进）；`CurrCmdHTime` 为负值则永久保持该条目。

> **注意：** 用户可在电流控制模式下随时改写 `CurrCmdIndex`。这会立即切换正在使用的 `CurrCmdVal`，而不会复位 [CurrCmdCntr](CurrCmdCntr.md) 计时器。

## 示例

```text
ACurrCmdIndex       ; read the active table entry
ACurrCmdIndex=3      ; jump to the third entry
```

### 边界情况

- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 1 或 [CurrCmdSrc](CurrCmdSrc.md) ∉ {1, 2}）— 不查询 `CurrCmdIndex`；写入会被存储，并在下次进入电流模式时生效。
- **超出范围** — 超出 `1`–`20` 的值会被参数表拒绝。
- **斜坡过程中写入** — 在斜坡进行过程中改写索引会在下一周期切换到新目标值，而不复位 [CurrCmdCntr](CurrCmdCntr.md)；下一段斜坡从当前 `CurrRef` 开始。
- **钳位在 20** — 钳位时固件**不**复位计数器，以便用户监视轴停留在最后一个条目上的时长。
- **GoToCurrMode** — 始终复位 `CurrCmdIndex = 1`；直接 `OperationMode = 1` 则不会。
- **保存** — 不可保存至闪存。

## 参见

- [CurrCmdVal](CurrCmdVal.md) — 电流值表
- [CurrCmdHTime](CurrCmdHTime.md) — 每个条目的保持时间
- [CurrCmdCntr](CurrCmdCntr.md) — 活动条目的计时器
