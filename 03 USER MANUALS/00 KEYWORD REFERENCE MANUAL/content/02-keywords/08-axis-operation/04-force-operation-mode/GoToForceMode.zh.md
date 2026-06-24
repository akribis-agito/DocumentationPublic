---
keyword: GoToForceMode
summary: 平稳进入力运行模式的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 575
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
# GoToForceMode

平稳进入力运行模式的命令。

## 概述

`GoToForceMode` 指示控制器以平稳方式进入力运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 4）。与直接赋值 `OperationMode = 4` 不同，该命令执行受控的交接过程，使得控制环切换时执行器不会跳变。关于进入力模式的其他方式（直接赋值、自动条件或数字量输入），参见 [Force operation mode](00-overview.md)。

> **注意：** 如果轴已处于力模式，`GoToForceMode` 不执行任何操作；当轴处于电流运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 1）时，或当其属于某个 CNC（多轴）运动组时，该命令将被**拒绝**。

## 工作原理

当命令被接受时，执行以下交接过程：

1. **结束任何活动的运动**（报告为 [MotionReason](../../10-motion/05-motion-status/MotionReason.md) = 17，即因 GoToForceMode 命令导致运动结束）并存储移动规划器时间，使得在力环接管时轴不再处于运动中。
2. **复位指令序列状态** —— [ForceCmdIndex](ForceCmdIndex.md) 被置为 `1`（第一个表条目），[ForceCmdCntr](ForceCmdCntr.md) 被清零为 `0`。
3. **从当前电流参考为力环积分器赋初值**，使得指令电流在切换过程中保持连续，电机不会跳变。
4. **将 [OperationMode](../01-general-keywords/OperationMode.md) 切换为力控制** 并记录切换位置。

由于该命令复位 [ForceCmdIndex](ForceCmdIndex.md) 和 [ForceCmdCntr](ForceCmdCntr.md)，力指令序列总是从第一个 [ForceCmdVal](ForceCmdVal.md) 条目重新开始。（直接赋值 `OperationMode = 4` **不会**复位它们，因此可以从预设条目继续。）

## 示例

```text
AGoToForceMode       ; gracefully switch to force operation mode
```

### 边界情况

- **从电流模式进入** —— 被拒绝；不能直接从电流模式进入力模式（只能从位置或速度模式进入）。请先经由位置模式（例如通过 [GoToPosMode](../02-position-operation-mode/GoToPosMode.md)）再调用 `GoToForceMode`。
- **已处于力模式** —— 空操作；返回 OK。
- **CNC 成员** —— 被拒绝；当轴属于某个 CNC 运动组时不能进入力模式（参见 [MotionStat](../../10-motion/05-motion-status/MotionStat.md) 的第 10 位和第 13 位）。请先停止该 CNC 组。
- **矢量成员** —— 此处不阻止（只有 [DInMode](../../05-inputs-outputs/04-digital-inputs/DInMode.md) 代码 22 的派发会拒绝矢量成员）。
- **从速度模式进入** —— 被接受；力环赋初值的工作方式相同（`CurrRef` 处于已定义状态）。
- **从位置模式进入** —— 被接受（常见情况）；遵守运动中检查。
- **电机失能** —— 被接受；模式标志改变，但在 `MotorOn = 1` 之前不施加功率。
- **PIV 模式**（[ForcePIVOn](../../11-control-tuning/07-force-control/ForcePIVOn.md) = 1）—— 力积分器赋初值为 `0`，而非来自 `CurrRef`；PIV 结构自行处理积分。
- **表保持不变** —— `ForceCmdVal` / `ForceCmdSlope` / `ForceCmdHTime` 不会被清除；派发器总是从 `ForceCmdIndex = 1` 重新开始。
- **直接赋值与 `GoToForceMode` 的对比** —— 写入 [OperationMode](../01-general-keywords/OperationMode.md) = `4` **不会**复位 `ForceCmdIndex` / `ForceCmdCntr`；它可以继续进行中的序列。`GoToForceMode` 总是从条目 1 重新开始。
- **原子性** —— 固件在积分器赋初值和模式切换前后禁用中断，使该变更在单个控制周期内对所有控制环可见。

## 参见

- [OperationMode](../01-general-keywords/OperationMode.md) —— 当前活动的控制模式
- [ForceCmdSrc](ForceCmdSrc.md) —— 进入模式后力参考的来源
- [ForceCmdIndex](ForceCmdIndex.md) / [ForceCmdCntr](ForceCmdCntr.md) —— 该命令复位的序列状态
- [Force operation mode](00-overview.md) —— 力模式行为概述
