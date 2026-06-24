---
keyword: CurrCmdCntr
summary: 在电流模式下或在当前激活的 CurrCmdVal 条目中经过的时间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 334
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CurrCmdCntr

在电流模式下或在当前激活的 CurrCmdVal 条目中经过的时间。

## 概述

`CurrCmdCntr` 是以毫秒为单位经过的时间，用于驱动电流运行模式的计时表逻辑。其含义取决于 [CurrCmdSrc](CurrCmdSrc.md)：

1. 若 `CurrCmdSrc` = 0 或 3（模拟量输入，或本轴所跟随其电流参考的主轴）：在电流运行模式下经过的时间。
2. 若 `CurrCmdSrc` = 1 或 2（用户自定义表）：在现有 [CurrCmdVal](CurrCmdVal.md) 数组条目下经过的时间。当切换到下一个 `CurrCmdVal` 条目时，此值复位为 0。

`CurrCmdSrc` = 3（跟随另一轴的电流参考）仅在 **central-i (v5)** 上可用；在 v4 上，[CurrCmdSrc](CurrCmdSrc.md) 的有效范围为 0–2。

`CurrCmdCntr` 在收到 [GoToCurrMode](GoToCurrMode.md) 命令、发生自动条件切换、或数字量输入切换到电流运行模式时复位为 0。这意味着当直接对 [OperationMode](../01-general-keywords/OperationMode.md) 赋值时，用户可以将其预置为任意初始值，并从该值开始计时。

## 工作原理

计数器每个控制周期前进一次。因此，一个计数对应的精确毫秒数取决于控制环采样时间。其行为取决于来源：

- **来源 0 和 3（模拟 / 主轴）：** 若 [CurrCmdHTime](CurrCmdHTime.md)`[1]` 非负，则计数器每个控制周期递增，当它超过 `CurrCmdHTime[1]` 时，轴切换回位置运行模式。若 `CurrCmdHTime[1]` 为负，则无限期使用该来源，计数器不前进。（来源 3 仅适用于 central-i v5。）
- **来源 1 和 2（用户表）：** 当 `CurrRef` 正向当前激活的 [CurrCmdVal](CurrCmdVal.md) 条目斜坡变化时，计数器保持为 0；只有当 `CurrRef` 到达该条目后才开始计数，并在索引前进到下一条目时复位为 0。当表用尽且索引被钳位到最后一个条目时，计数器**不**复位 —— 因此它会持续增长，从而反映轴保持最终值已有多久。

> **注意：** 在电流运行模式下，用户可随时覆盖 `CurrCmdCntr`。

## 示例

```text
ACurrCmdCntr        ; read elapsed time (ms)
ACurrCmdCntr=0       ; restart the timer
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 1）—— 计数器不前进；该值反映在电流模式下的最后一个周期。
- **来源 1/2 斜坡期间** —— 当 [CurrCmdSlope](CurrCmdSlope.md) 正在对 `CurrRef` 进行斜坡变化时保持为 `0`；只有当 `CurrRef = CurrCmdVal[index]` 后才开始计数。
- **最大值** —— `2 000 000 000` 是用户可*写入* `CurrCmdCntr` 的最大值；它不是运行时上限。在电流运行模式下，计数器仅每个控制周期递增一次，没有运行时饱和（与**索引被钳位 (20)** 的边界情况一致，此时计数器会在最终条目处持续增长）。
- **索引被钳位 (20)** —— 当 [CurrCmdIndex](CurrCmdIndex.md) 停留在 `20` 时，计数器**不**复位；它会持续增长。
- **手动写入** —— 在电流模式下允许写入 `CurrCmdCntr`；可用于重新开始保持或提前前进到下一条目。
- **GoToCurrMode** —— 将计数器复位为 `0`；直接 `OperationMode = 1` 则不会。
- **保存** —— 不可保存至闪存。

## 另请参阅

- [CurrCmdHTime](CurrCmdHTime.md) —— 与此计数器比较的保持时间
- [CurrCmdIndex](CurrCmdIndex.md) —— 当前激活的表条目
- [GoToCurrMode](GoToCurrMode.md) —— 进入时复位此计数器
