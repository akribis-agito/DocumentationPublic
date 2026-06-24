---
keyword: ForceCmdSrc
summary: 在力模式下选择力参考的来源。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 570
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceCmdSrc

在力模式下选择力参考的来源。

## 概述

`ForceCmdSrc` 设置力参考（[ForceRef](ForceRef.md)）的来源。模式切换逻辑会读取该值，以决定如何生成力参考以及轴何时退出力模式（参见[力运行模式](00-overview.md)）。

## 工作原理

每个周期，力指令生成器根据 `ForceCmdSrc` 进行分支，以构建原始力参考并决定何时退出力模式。支持的取值如下：

| 取值 | 来源 |
|----|----|
| 0 | 模拟量力参考输入（通过 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) 被分配为力指令功能的通道）。参考值跟随模拟信号；[ForceCmdHTime](ForceCmdHTime.md)`[1]` 设置轴保持在力模式中的时长。 |
| 1 | 用户自定义序列：逐项遍历 [ForceCmdVal](ForceCmdVal.md) 表，每项保持 [ForceCmdHTime](ForceCmdHTime.md)，并以 [ForceCmdSlope](ForceCmdSlope.md) 的速率到达。 |
| 2 | 在当前固件中与取值 1 相同。 |

> **注意：** 在本固件版本中，取值 1 和 2 行为相同；插值变体保留用于未来增强。请使用 `ForceCmdSrc = 1` 来文档化和配置用户自定义表。

当 `ForceCmdSrc = 0` 时，模拟量参考可由[力运行模式](00-overview.md)中描述的模式切换条件自动进入/退出。当 `ForceCmdSrc = 1` 或 `2` 时，轴根据 [ForceCmdHTime](ForceCmdHTime.md) 表退出力模式（值为 `0` 的项强制返回位置模式）。

## 示例

```text
AForceCmdSrc=0       ; follow the analog force reference input
AForceCmdSrc=1       ; use the user-defined ForceCmdVal table
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4）——不会读取 `ForceCmdSrc`；写入立即生效，但新来源仅在轴进入力模式后才适用。
- **超出范围**——`0`–`2` 之外的取值会被参数表拒绝。
- **来源 0 但无模拟量映射**——若未通过 [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md) 将任何模拟量输入映射到功能 4（力指令），则 `ForceRef` 读取为 `0`。
- **无主轴来源等价项**——与 [CurrCmdSrc](../03-current-operation-mode/CurrCmdSrc.md) 不同，力模式**没有**主轴来源（不存在 `ForceCmdSrc = 3`）。
- **到位检测**——仅当 `ForceCmdSrc = 1` 或 `2` 时才更新 [ForceInTStat](ForceInTStat.md)；当 `ForceCmdSrc = 0` 时没有定义的稳定到位目标，因此 `ForceInTStat` 保持在电机使能状态。
- **保存**——可保存至闪存；在引导时重新加载。
- **电机失能**——任何时候均可接受；该来源标志不需要电机。

## 另请参阅

- [ForceCmdVal](ForceCmdVal.md) —— 用户自定义力值（来源 1/2）
- [ForceRef](ForceRef.md) —— 生成的力参考
- [力运行模式](00-overview.md) —— 总体模式行为
