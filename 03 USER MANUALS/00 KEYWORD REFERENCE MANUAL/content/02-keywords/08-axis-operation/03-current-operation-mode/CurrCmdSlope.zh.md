---
keyword: CurrCmdSlope
summary: 向每个电流指令表条目变化的斜率（mA/s）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 568
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
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CurrCmdSlope

向每个电流指令表条目变化的斜率（mA/s）。

## 概述

`CurrCmdSlope` 定义从起始 `CurrRef` 值过渡到活动 [CurrCmdVal](CurrCmdVal.md) 条目的斜率，单位为毫安每秒。它仅在 [CurrCmdSrc](CurrCmdSrc.md) = 1 或 2 时适用。保持计时器 [CurrCmdCntr](CurrCmdCntr.md) 仅在斜坡完成后才从 0 开始计数。该数组索引为 1 到 20，与 `CurrCmdVal` / `CurrCmdHTime` 条目一一配对。

## 工作原理

每个控制周期，控制器向 `CurrRef` 加上（或减去，取决于 `CurrRef` 低于还是高于目标）一个 `CurrCmdSlope[index] x sample_time` 的增量，使其向 `CurrCmdVal[index]` 移动：

- 在 standalone/v4 上，`CurrRef` 为整数，每周期增量的小数部分会在内部余量累加器中结转，因此即使每周期步进小于 1 mA，有效斜率仍保持精确。在 central-i v5 上，`CurrRef` 为浮点数，增量直接施加，没有舍入也没有余量累加器。
- 当 `CurrRef` 仍在斜坡变化（尚未等于目标）时，[CurrCmdCntr](CurrCmdCntr.md) 被强制为 0；只有当 `CurrRef` 精确等于 `CurrCmdVal[index]` 时，保持计时器才开始递增。
- 当某个周期内斜坡到达或超过目标时，`CurrRef` 被吸附到 `CurrCmdVal[index]`（并且在 standalone/v4 上，余量累加器被清除）。

由于斜率是按条目独立施加的，因此进入每个 `CurrCmdVal` 步进的速率可以不同。在 standalone/v4 上，最小值为 1（不允许斜率为 0，这保证斜坡始终推进）；central-i v5 将最小值降低到接近零的值，因此允许小于 1 mA/s 的分数斜率（参见[版本间变化](#版本间变化)）。

## 示例

```text
ACurrCmdSlope[3]=700 ; ramp into entry 3 at 700 mA/s
```

实例 — 若 `CurrCmdIndex` = 2、`CurrCmdCntr` = `CurrCmdHTime[2]`（当前条目结束）、`CurrRef` = `CurrCmdVal[2]` = 340、`CurrCmdVal[3]` = -500、`CurrCmdSlope[3]` = 700，则从 340 mA 到 -500 mA 的斜坡开始并在 1.2 秒内完成。

### 边界情况

- **索引 0** — 无效；有效索引为 `CurrCmdSlope[1]`–`CurrCmdSlope[20]`。`CurrCmdSlope[0]` 不存在。
- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 1 或 [CurrCmdSrc](CurrCmdSrc.md) ∉ {1, 2}）— 不查询斜率；存储但不使用。
- **超出范围** — `0` 和负值会被拒绝。在 standalone/v4 上最小值为 `1` 以保证推进；central-i v5 将最小值降低到接近零的值，允许小于 1 mA/s 的分数斜率。
- **大斜率** — 会产生大于到目标剩余距离的每周期步进的值，会使 `CurrRef` 在下一周期吸附到目标；保持计时器立即开始。
- **斜坡过程中重载** — 在活动条目上写入新斜率会从下一周期改变速率。在 standalone/v4 上，余量累加器保持不变，因此没有不连续；在 central-i v5 上没有余量需要保留。
- **保存** — 可保存至闪存。
- **平台** — v5 以 `float32` 存储，无上限；v4 以 `int32` 存储，最大为 `2 147 483 647`。

## 版本间变化

central-i v5 将 `CurrCmdSlope` 以 32 位浮点数存储。这既移除了固定的上限范围，又将最小值从 1 降低到接近零的值，因此小于 1 mA/s 的分数斜率成为可能（standalone/v4：32 位整数，范围 1 到 2147483647）。

## 参见

- [CurrCmdVal](CurrCmdVal.md) — 目标电流值
- [CurrCmdHTime](CurrCmdHTime.md) — 每个条目的保持时间
- [CurrCmdCntr](CurrCmdCntr.md) — 斜坡完成后开始的计时器
