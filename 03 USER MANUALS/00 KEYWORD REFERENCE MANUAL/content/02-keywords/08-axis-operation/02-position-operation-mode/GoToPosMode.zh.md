---
keyword: GoToPosMode
summary: 平滑进入位置运行模式的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 336
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GoToPosMode

平滑进入位置运行模式的命令。

## 概述

`GoToPosMode` 指示控制器以平滑、无冲击的方式进入位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 3）。命令被处理的时刻的位置反馈（[Pos](../../10-motion/01-kinematics-status/Pos.md)）被记录到 [ModeSwitchPos](ModeSwitchPos.md) 的索引 2 中。

`GoToPosMode` 只能将轴**从电流模式（1）或力模式（4）**切换过来，因为只有这些模式才会持续准备干净切换所需的变量。从速度模式（2）调用会被拒绝，若轴已处于位置模式（3）则不执行任何操作。通过 [BeginOnToPos](BeginOnToPos.md) 标志，该命令还可在进入时启动一次点到点移动，目标由 [RetractTarget](RetractTarget.md)（或 [RelTrgt](../../10-motion/13-motion-mode-ptp/RelTrgt.md)）设置，速度为 [RetractSpeed](RetractSpeed.md)。关于到达位置模式的其他方式（直接 [OperationMode](../01-general-keywords/OperationMode.md) 赋值、通过 [PosPosFlag](PosPosFlag.md)/[PosPosTh](PosPosTh.md) 的内部条件检查，或 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 数字量输入），请参见 [OperationMode](../01-general-keywords/OperationMode.md)。

## 工作原理

`GoToPosMode` 是一个函数关键字。被命令时，控制器根据当前的 [OperationMode](../01-general-keywords/OperationMode.md) 分支：

| 源 `OperationMode` | 动作 |
|---|---|
| 1（电流）或 4（力） | 设置 `OperationMode = 3`（位置）；记录 [ModeSwitchPos](ModeSwitchPos.md)[2] = `Pos`；若 [BeginOnToPos](BeginOnToPos.md) = 1，清除它并启动进入移动。 |
| 2（速度） | 报错被拒绝（无法从速度模式切换到位置模式）。 |
| 3（位置） | 无效果（已处于位置模式）。 |

### 无冲击切换

切换之所以无冲击，是因为在轴处于源模式的整个期间，位置参考始终与反馈保持对齐，因此在切换的瞬间位置误差没有阶跃：

- **从电流模式**——在仅电流控制期间，位置/速度环开环，参考被保持为跟踪反馈，因此在切换时 `PosRef ≈ Pos`，位置误差约为 0。
- **从力模式**——力环相对于进入力模式时捕获的位置（[ModeSwitchPos](ModeSwitchPos.md)[1] 锚点）持续重新生成位置参考。由于参考已经位于反馈所在之处，位置控制恢复时不会产生跳变。

只要在电流（或力）运行模式下每个周期都已做好准备，运行模式即可直接更改。参考管线请参见 [PosRef](../../10-motion/01-kinematics-status/PosRef.md)。

### 可选的进入移动

若 [BeginOnToPos](BeginOnToPos.md) 已使能，`GoToPosMode` 会启动与内部切换算法和 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 所用相同的进入移动。移动细节请参见 [BeginOnToPos](BeginOnToPos.md)。

> **注意：** `GoToPosMode` 不能在轴处于速度运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2）时使用。

## 示例

```text
AGoToPosMode         ; gracefully switch to position operation mode
AModeSwitchPos[2]   ; read the position recorded on entry to position mode
```

### 边界情况

- **从速度模式**——被拒绝（错误 157，"Can't GoToPosMode from Velocity Operation Mode. Only from Current Operation Mode"）。推荐路径是禁用电机，设置 [OperationMode](../01-general-keywords/OperationMode.md) = 3，然后重新使能。
- **已处于位置模式**——无操作；返回 OK。
- **电机关闭**——接受；模式标志更改，但在 `MotorOn = 1` 之前不施加任何功率。
- **运动中（电流或力）**——切换时源模式的指令序列停止施加；进入移动（若 [BeginOnToPos](BeginOnToPos.md) = 1）立即开始，否则轴保持在 `Pos`。
- **CNC / 矢量成员**——在此进入点不被阻止；考虑先停止组，以避免组内其余成员进入意外状态。
- **`BeginOnToPos` 自清除**——当进入移动启动时，`BeginOnToPos` 被重置为 `0`；下次进入时需重新使能。
- **模式切换位置锚点**——[ModeSwitchPos](ModeSwitchPos.md)`[2]` 在每次成功进入时被覆盖；先前的值会丢失。
- **DInMode 并行**——[DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 代码 18 和 22 在上升沿执行相同的进入位置切换，但分别只从电流（18）或力（22）模式进行；与 `GoToPosMode` 本身一样，进入位置的方向不检查矢量/CNC 成员资格（检查矢量/CNC 成员的是相反的下降沿切换，即返回电流/力模式时）。

## 参见

- [BeginOnToPos](BeginOnToPos.md) — 进入时可选地执行一次移动
- [ModeSwitchPos](ModeSwitchPos.md) — 模式切换时记录的位置
- [OperationMode](../01-general-keywords/OperationMode.md) — 当前激活的控制模式
- [PosPosFlag](PosPosFlag.md) / [PosPosTh](PosPosTh.md) — 从电流/力模式自动反馈阈值进入
- [RetractSpeed](RetractSpeed.md) / [RetractTarget](RetractTarget.md) — 可选进入移动的运动学参数
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — 切换时记录的反馈
