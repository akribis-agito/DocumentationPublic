---
summary: 只读的环路侧电流参考，取自解耦矩阵、注入与补偿之前。
keyword: CurrRefCtrl
availability:
  standalone: []
  central-i:
  - v5
can_code: 717
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-27'
doc_revision: '2026.06'
language: zh-CN
---
# CurrRefCtrl

只读的环路侧电流参考，取自解耦矩阵、注入与补偿之前。

## 概述

`CurrRefCtrl` 是控制环的电流参考（区别于电机的电流参考 [CurrRef](CurrRef.md)）。它是解耦矩阵、电流注入以及电流相关补偿之前的值。其含义取决于运行模式：

- **位置、速度和力运行模式：** `CurrRefCtrl` 是反馈环的电流参考、前馈以及环路补偿之和。
- **电流运行模式：** `CurrRefCtrl` 是由 [CurrCmdSrc](../../08-axis-operation/03-current-operation-mode/CurrCmdSrc.md) 所定义的源（模拟量输入、[CurrCmdVal](../../08-axis-operation/03-current-operation-mode/CurrCmdVal.md) 数组等）给出的电流参考。

关于 `CurrRefCtrl` 在信号路径中的位置，请参见 [控制整定 – 速度控制](../../11-control-tuning/04-velocity-control/00-overview.md)、[控制整定 – 前馈](../../11-control-tuning/05-feedforwards/00-overview.md) 和 [控制整定 – 力控制](../../11-control-tuning/07-force-control/00-overview.md)。

## 工作原理

`CurrRefCtrl` 报告环路侧的电流参考，即在应用解耦矩阵、电流注入和电流相关补偿之前的值。经补偿和注入的结果，在电流限制和 [CurrDir](CurrDir.md) 符号修正之后，成为最终的电机电流指令 [CurrRef](CurrRef.md)。在电机侧，该指令对于三相电机成为交轴参考 [IqRef](IqRef.md)，对于有刷电机成为 A 相参考 [IaRef](IaRef.md)。`CurrRefCtrl` 仅在 central-i (v5) 上报告。

## 示例

```text
ACurrRefCtrl        ; read the loop-side current reference
```

## 参见

- [CurrRef](CurrRef.md) — 经解耦/补偿后的最终电机电流指令
- [CurrCmdSrc](../../08-axis-operation/03-current-operation-mode/CurrCmdSrc.md) — 电流运行模式下的电流指令源
- [IqRef](IqRef.md)、[IaRef](IaRef.md) — 在方向修正之后由 CurrRefCtrl 导出的参考值
