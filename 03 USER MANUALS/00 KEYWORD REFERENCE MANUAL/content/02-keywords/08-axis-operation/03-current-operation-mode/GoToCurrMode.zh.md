---
keyword: GoToCurrMode
summary: 用于平稳进入电流运行模式的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 335
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GoToCurrMode

用于平稳进入电流运行模式的命令。

## 概述

`GoToCurrMode` 指示控制器以平稳的方式进入电流运行模式。有关进入电流模式的其他方法，请参见 [OperationMode](../01-general-keywords/OperationMode.md)。

## 工作原理

收到该命令时，固件会执行以下操作，且全程禁用中断，以使切换具有原子性：

1. **已处于电流模式** — 不做任何操作并回复 OK。
2. **属于某个 CNC（多轴）运动的成员** — 拒绝该命令并返回错误；不能从协调运动中进入电流模式。
3. **其他情况：**
   - 若轴正在运动中，运动会立即结束，原因码为“end / go-to-current”，并存储规划器采样时间。
   - [CurrCmdIndex](CurrCmdIndex.md) 复位为 1（第一个表项），[CurrCmdCntr](CurrCmdCntr.md) 复位为 0。
   - [OperationMode](../01-general-keywords/OperationMode.md) 被设置为电流控制（值 1），当前位置被记录为模式切换位置，并清除到位计数器。

`GoToCurrMode` **不会**清除 [CurrCmdVal](CurrCmdVal.md)、[CurrCmdSlope](CurrCmdSlope.md) 或 [CurrCmdHTime](CurrCmdHTime.md) 表 —— 这些表保留其已配置的值，因此每次进入该模式时序列都从表项 1 开始运行。这与固件在某个阈值条件自动进入电流模式时所执行的准备工作相同。

## 示例

```text
AGoToCurrMode        ; gracefully switch to current operation mode
```

### 操作演练：切换至电流模式进行力测试

施加一个较小的指令电流，以验证机械/线圈极性，或在执行器上施加一个已知的力。从电机使能的位置模式开始，使用表源切换到电流模式，并观察结果。

```text
AOperationMode            ; expect 3 (position) — start from a safe known state
AMotorOn                  ; expect 1 (servo on)
ACurrCmdSrc=1             ; use the user-defined CurrCmdVal table
ACurrCmdVal[1]=500        ; first table entry — 500 mA (adjust to your motor and rig)
ACurrCmdHTime[1]=2000     ; hold for 2000 ms
ACurrCmdVal[2]=0          ; second entry — back to zero
ACurrCmdHTime[2]=1000     ; hold for 1000 ms
ACurrCmdHTime[3]=0        ; HTime = 0 ends the sequence
AGoToCurrMode             ; graceful switch; CurrCmdIndex resets to 1, CurrCmdCntr to 0
                          ; ... observe the response ...
AMotorCurr                ; live motor current feedback (mA)
ACurrCmdCntr              ; ramp/hold counter for the active entry
                          ; ... when done ...
AGoToPosMode              ; bumpless return to position control
```

`GoToCurrMode` 在 CNC（多轴）运动中会被拒绝，若轴已处于电流模式则不做任何操作。它还会保持 `CurrCmdVal` / `CurrCmdSlope` / `CurrCmdHTime` 表不变 —— 序列始终从表项 1 重新开始。

### 边界情况

- **已处于电流模式** — 空操作，返回 OK。
- **CNC 成员**（[MotionStat](../../10-motion/05-motion-status/MotionStat.md) 第 10 位 = CNCA 成员，或第 13 位 = CNCB 成员）— 以错误 191（“Can't go to Current or Force mode when in CNC motion”）拒绝。请先停止该 CNC 组。
- **Vector 成员** — 在此入口处不被阻止（只有 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 代码 18 的派发会阻止 vector 成员）。对 vector 成员发出 `GoToCurrMode` 会被接受；可考虑先显式停止 vector。
- **运动中** — 接受；运动立即结束，[MotionReason](../../10-motion/05-motion-status/MotionReason.md) = 14（运动因 GoToCurrMode 命令而结束），并更新 `MotionSamples[1]`。
- **从速度模式** — 接受；不运行任何特殊准备（在新模式的电流指令接管之前，速度环继续向电流环供给）。
- **从力模式** — 接受；力模式状态保持原样，`OperationMode` 翻转为电流模式；先前运行的力指令序列停止施加。
- **电机失能** — 接受；模式标志改变，但在 `MotorOn = 1` 之前不施加任何功率。
- **表保持不变** — `CurrCmdVal` / `CurrCmdSlope` / `CurrCmdHTime` **不会**被该命令清除；派发器始终从 `CurrCmdIndex = 1` 重新开始。
- **原子性** — 固件在模式切换前后禁用中断，使该变更在单个控制周期内对所有环路可见。

## 另请参见

- [OperationMode](../01-general-keywords/OperationMode.md) — 当前激活的控制模式
- [CurrCmdSrc](CurrCmdSrc.md) — 进入模式后电流参考的来源
- [Current operation mode](00-overview.md) — 电流模式行为概述
