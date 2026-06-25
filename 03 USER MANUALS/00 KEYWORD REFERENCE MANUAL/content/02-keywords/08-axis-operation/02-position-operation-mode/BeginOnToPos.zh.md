---
keyword: BeginOnToPos
summary: 进入位置模式时执行一次点到点移动的一次性标志。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 587
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BeginOnToPos

进入位置模式时执行一次点到点移动的一次性标志。

## 概述

`BeginOnToPos` 是一个一次性（自动清除）标志，若设为 1，则指示控制器在轴进入位置运行模式的时刻启动一次点到点运动。目标位置由 [RetractTarget](RetractTarget.md)（或 [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)）定义，最大速度由 [RetractSpeed](RetractSpeed.md) 定义。一旦移动被使能并触发，该标志即重置为 0，因此下次进入时必须重新设置。

该标志仅在为干净进入位置模式做准备的切换路径上生效：[GoToPosMode](GoToPosMode.md) 命令、内部反馈阈值切换（[PosPosFlag](PosPosFlag.md)/[PosPosTh](PosPosTh.md) 以及调度表结束），以及 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 的位置/电流或位置/力输入。当 [OperationMode](../01-general-keywords/OperationMode.md) 通过直接赋值更改时，该标志**无效**。

## 工作原理

每条将轴切换至位置模式的路径都会检查 `BeginOnToPos`；若其非零，控制器会清除它并启动共享的进入移动。进入路径为：

| 进入路径 |
|---|
| `GoToPosMode` 命令 |
| 从电流模式的内部切换 |
| 从力模式的内部切换 |
| `DInMode` 位置/电流输入（上升沿） |
| `DInMode` 位置/力输入（上升沿） |

### 进入移动

进入移动按标准点到点移动方式设置并启动：

1. **目标**——若 [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) ≠ 0，则绝对目标为进入时的参考值加 `RelTrgt`（相对于进入时的参考值）；否则为绝对 [RetractTarget](RetractTarget.md)。
2. **速度**——移动速度设为 [RetractSpeed](RetractSpeed.md)。
3. **启动**——若已使能条件启动输入，则运动等待输入，并在输入的上升沿真正开始；否则立即开始。加速度/减速度和加加速度来自轴的常规 PTP 曲线设置；应用摩擦补偿，并重置运动采样计数器。

由于这是一次普通的 PTP 移动，它与任何其他运动一样遵守软件位置限位（[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)）。

## 示例

```text
ARetractTarget=50000 ; absolute target for the entry move
ARetractSpeed=20000  ; speed for the entry move
ABeginOnToPos=1      ; arm the entry move (auto-clears after it starts)
AGoToPosMode         ; switch to position mode and start the move
```

相对进入移动（目标相对于进入时的参考值）：

```text
ARelTrgt=10000       ; +10000 user units from the entry reference
ARetractSpeed=20000  ; speed for the entry move
ABeginOnToPos=1      ; arm the entry move
AGoToPosMode         ; switch and start the relative move
```

### 边界情况

- **自动清除**——该标志在进入移动启动的时刻被清除；下次进入时需重新使能。
- **切换路径不遵守它**——只有上面列出的路径才会清除/检查该标志。直接 `OperationMode = 3` 赋值**不会**消耗 `BeginOnToPos`，也**不会**执行进入移动。
- **位置限位裁剪**——进入移动是普通的 PTP 移动；若 [RetractTarget](RetractTarget.md)（或 `RelTrgt`）超出 [FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md)/[RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)，则移动被裁剪。
- **超出范围**——`0`–`1` 范围之外的值会被拒绝。
- **保存**——不可保存至闪存；启动时重置为 `0`。

## 另请参阅

- [GoToPosMode](GoToPosMode.md) — 触发已使能移动的命令
- [RetractTarget](RetractTarget.md) — 进入移动的绝对目标
- [RetractSpeed](RetractSpeed.md) — 进入移动的速度
- [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md) — 相对目标覆盖
- [PosPosFlag](PosPosFlag.md) / [PosPosTh](PosPosTh.md) — 同样遵守该标志的内部阈值进入
- [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) — 同样遵守该标志的数字量输入模式切换
