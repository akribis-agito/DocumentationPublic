---
keyword: HomingOn
summary: 启动并报告轴的当前回零过程。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 340
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# HomingOn

启动并报告轴的当前回零过程。

## 概述

`HomingOn` 是内置回零过程的触发器。上电或复位时清零为 `0`。写入 `1` 将启动 [HomingDef](HomingDef.md) 中定义的回零序列，进度和任何错误由 [HomingStat](HomingStat.md) 报告。当过程结束时——无论成功完成还是因错误中止——控制器自动将 `HomingOn` 清回 `0`。

由于轴运动中不可写入，`HomingOn` 须在轴静止时置位以启动回零运行。它与 [HomingDef](HomingDef.md)（步骤定义）和 [HomingStat](HomingStat.md)（状态）共同构成回零接口的核心。

## 工作原理

回零引擎在控制中断内运行，当 `HomingOn == 1` 时每个控制器周期执行一次：

1. **上升沿（刚置为 1）。** 当前运动学参数——[Speed](../10-motion/03-kinematics-configuration/Speed.md)、加速度、减速度、紧急减速度及加加速度模式——被复制至内部"镜像"变量，且回零期间强制关闭加加速度模式。随后每个回零步骤使用其 [HomingDef](HomingDef.md) 参数中的值覆盖运动学参数。内部步骤指针设为步骤 1，"步骤首次周期"标志置位。
2. **每个周期。** 引擎执行当前步骤（各步骤行为见 [HomingDef](HomingDef.md)），并将步骤编号更新至 [HomingStat](HomingStat.md) 和 [HomingStep](HomingStep.md)。
3. **完成。** 到达"结束回零"步骤时，`HomingOn` 清回 `0`，`HomingStat` 设为 `100`。任何失败（超时、电机意外失能、运动中、运动结束原因不符等）同样将 `HomingOn` 清零并将对应的负错误码写入 `HomingStat`。
4. **下降沿（刚被清除）。** 镜像的运动学参数（Speed、加速度、减速度、紧急减速度）和加加速度模式被恢复，因此一次回零运行不会改变轴的正常运动设置。

当 `HomingOn` 为 `0` 时，引擎将内部指针保持在步骤 1，以确保下一次写入 `1` 时始终从头开始。

## 示例

```text
AHomingOn=1          ; 启动 HomingDef 定义的回零过程
AHomingOn           ; 回零激活时为 1，完成后清为 0
```

## 另请参阅

- [HomingDef](HomingDef.md) — 定义运行的回零步骤
- [HomingStat](HomingStat.md) — 报告运行的进度和错误状态
- [HomingStep](HomingStep.md) — 引擎已到达的回零步骤编号
