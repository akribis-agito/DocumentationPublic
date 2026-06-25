---
keyword: RetractSpeed
summary: 进入位置模式时点到点运动的最大速度。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 608
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -1300000000
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RetractSpeed

进入位置模式时点到点运动的最大速度。

## 概述

`RetractSpeed` 是进入位置运行模式时所运行点到点运动的最大速度，单位为用户单位/秒。该运动仅在 [BeginOnToPos](BeginOnToPos.md) 已置位时运行，朝向由 [RetractTarget](RetractTarget.md)（或 [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)）定义的目标。它是一个保存至闪存的设置，因此重新上电后保持。

## 工作原理

当进入运动被启动时，`RetractSpeed` 被直接复制到活动的 PTP 运动速度中。该运动随后作为普通的点到点曲线运行——`RetractSpeed` 仅设置巡航（最大）速度；加速度、减速度和加加速度取自轴的常规运动曲线设置。

该关键字为有符号且可为负；其值为规划器的指令速度，无论符号如何都朝向目标运动。默认值为 1000。范围关于零对称；确切限值参见前言。

## 版本间的变化

在 **v5（central-i）** 中运动流水线为 64 位，因此 `RetractSpeed` 以 64 位值保存；速度复制行为不变。**v5 仅适用于 central-i**，因此在 standalone 上 `RetractSpeed` 仍为 v4 的 32 位值。

## 示例

```text
ARetractSpeed=20000  ; entry-move speed (user units/s)
ARetractTarget=50000 ; entry-move target
ABeginOnToPos=1      ; arm the move
AGoToPosMode         ; switch and start the move
```

### 边界情况

- **未置位时不使用** — 仅在 [BeginOnToPos](BeginOnToPos.md) 已设置且发生进入模式切换时才被读取。
- **方向与符号无关** — 规划器从目标推断方向；`RetractSpeed` 的符号即为指令巡航速率。
- **超出范围** — 平台范围之外的值将被拒绝。
- **保存** — 可保存至闪存。
- **平台** — v5 扩展为 64 位；v4 为 32 位。

## 另请参阅

- [BeginOnToPos](BeginOnToPos.md) — 置位进入运动
- [RetractTarget](RetractTarget.md) — 进入运动的目标
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) — 进入运动的相对目标覆盖
- [GoToPosMode](GoToPosMode.md) — 触发该运动的命令之一
