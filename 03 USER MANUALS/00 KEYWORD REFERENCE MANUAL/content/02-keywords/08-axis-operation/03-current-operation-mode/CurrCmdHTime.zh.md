---
keyword: CurrCmdHTime
summary: 每个电流指令表条目的保持时间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 332
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
# CurrCmdHTime

每个电流指令表条目的保持时间。

## 概述

`CurrCmdHTime` 定义电流控制模式下电流参考的保持时间，单位为毫秒。其用法取决于 [CurrCmdSrc](CurrCmdSrc.md)：

- 若 `CurrCmdSrc` = 0 或 3（模拟量输入或从轴驱动器）：仅使用 `CurrCmdHTime[1]`，定义停留在电流控制模式内的时间。
- 若 `CurrCmdSrc` = 1 或 2（用户自定义表）：每个数组元素定义对应 [CurrCmdVal](CurrCmdVal.md) 条目的保持时间。

## 工作原理

| 值 | 说明 |
|---|---|
| < 0 | 源值无限期保持。 |
| 0 | 轴退出电流控制模式并进入位置控制模式。 |
| > 0 | 源值保持 `CurrCmdHTime`，之后退出电流控制模式（`CurrCmdSrc` = 0 或 3）或进入下一对（`CurrCmdSrc` = 1 或 2）。对于 `CurrCmdSrc` = 1 或 2，若 [CurrCmdIndex](CurrCmdIndex.md) 达到最后一个可用条目（20）且该条目的 `CurrCmdHTime` 大于 0，则轴无限期保持最后一个 `CurrCmdVal` 值。 |

保持时间由 [CurrCmdCntr](CurrCmdCntr.md) 计数器累计，该计数器每个控制周期递增一次。对于源 1 和 2，计数器仅在 `CurrRef` 完成向该条目 [CurrCmdVal](CurrCmdVal.md) 的斜坡变化后才开始计数（参见 [CurrCmdSlope](CurrCmdSlope.md)）；对于源 0 和 3，计数器在进入模式时立即开始。当计数器达到 `CurrCmdHTime[1]`（源 0/3）时，轴切换到位置模式；当计数器达到 `CurrCmdHTime[index]`（源 1/2）时，轴前进到下一个表条目。

## 示例

```text
ACurrCmdHTime[1]=500 ; hold first entry for 500 ms
ACurrCmdHTime[2]=0   ; exit current mode after the second entry
```

### 边界情况

- **索引 0** — 无效；有效索引为 `CurrCmdHTime[1]`–`CurrCmdHTime[20]`。`CurrCmdHTime[0]` 不存在。
- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 1）— 不查询该表；值会被存储但不计时。
- **零值** — 在对应 `CurrCmdVal` 条目结束时从电流模式退出到位置模式。**当 `CurrCmdSrc` = 0 / 3 时，`CurrCmdHTime[1] = 0` 会在进入电流模式时立即返回位置模式**。
- **负值** — 无限期保持该值；只有显式的模式切换（[GoToPosMode](../02-position-operation-mode/GoToPosMode.md)、直接写入 `OperationMode` 或 DInMode）才能离开该条目。
- **表末尾** — 当 `CurrCmdIndex` 达到 `20` 且该条目的 `CurrCmdHTime > 0` 时，固件无限期保持最后一个值，而不会越过 20 继续前进。
- **计数器最大值** — `2 000 000 000` 是用户可*写入* [CurrCmdCntr](CurrCmdCntr.md) 的最大值，而非运行时上限。在电流控制模式下，计数器只是每个控制周期累计一次，没有运行时饱和。
- **HTime > CurrCmdHTime 最大值** — 超出 ±2 000 000 000 范围的值将被拒绝。
- **保存** — 可保存至闪存。

## 参见

- [CurrCmdVal](CurrCmdVal.md) — 与这些保持时间配对的电流值
- [CurrCmdIndex](CurrCmdIndex.md) — 活动表条目
- [CurrCmdCntr](CurrCmdCntr.md) — 与该值比较的已用时间
