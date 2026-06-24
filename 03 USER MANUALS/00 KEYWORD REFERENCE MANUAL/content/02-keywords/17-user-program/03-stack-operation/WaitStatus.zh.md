---
keyword: WaitStatus
summary: 使用户程序线程保持等待，直到所选状态达到所需值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 194
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 34
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# WaitStatus

使用户程序线程保持等待，直到所选状态达到所需值。

## 概述

`WaitStatus` 是一个底层用户程序关键字，仅用于用户程序编译；不能通过通信通道正常发命令。`WaitStatus` 使用户程序线程保持等待，直到所选状态达到所需值。它是 [WaitTime](WaitTime.md)（等待固定时间）的状态驱动对应指令。等待的状态由数组索引选择，所需值为赋值操作的值。

## 工作原理

在条件尚未满足时，`WaitStatus` 将线程标记为等待并让出执行权，线程在每次调度轮次中重新检查状态，而不占用程序引擎；其他线程继续运行。一旦状态匹配所需值，等待结束，线程继续执行下一条指令。对于计数器类状态，等待在计数器到达请求值时结束（减计数器减至该值，加计数器加至该值）；对于位类状态，所需值为等待的位状态（0 或 1）。

`WaitStatus` 与轴相关：属于电机或轴的位类条件在线程当前操作的轴上求值（参见 [ChooseAxis](../02-program-execution/ChooseAxis.md)）。

数组索引选择线程等待的状态计数器或位：

| 状态类型 | 描述 | 所需值 |
|----|----|----|
| 1 | 减计数器 1 | 计数器目标值（≥ 0） |
| 2 | 减计数器 2 | 计数器目标值（≥ 0） |
| 3 | 减计数器 3 | 当前固件中**未实现**——选择此索引将引发"无此操作"用户程序错误 |
| 4 | 减计数器 4 | 当前固件中**未实现**——选择此索引将引发"无此操作"用户程序错误 |
| 5 | 加计数器 1 | 计数器目标值（≥ 0） |
| 6 | 加计数器 2 | 计数器目标值（≥ 0） |
| 7 | 运动中 | 0 或 1 |
| 8 | 重复等待中 | 0 或 1 |
| 9 | 重复停止中 | 0 或 1 |
| 10 | 停止请求中 | 0 或 1 |
| 11 | 加速中 | 0 或 1 |
| 12 | 减速中 | 0 或 1 |
| 13 | 等待结束平滑中 | 0 或 1 |
| 14 | ECAM 停止中 | 0 或 1 |
| 15 | FIFO 停止中 | 0 或 1 |
| 16 | 换相完成 | 0 或 1 |
| 17 | 到位 | 0 或 1（轴稳定到位时等待始终结束，即 [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md) 达到 `4`（目标到达）；提供的值进行范围检查，但不改变所测试的条件） |
| 18 | 记录触发已检测 | 示波器编号 `1` 或 `2`——当该示波器的 [RecStat](../../19-data-recording/RecStat.md) 达到 `3`（触发已检测）时等待结束 |
| 19 | 记录已完成 | 示波器编号 `1` 或 `2`——当该示波器的 [RecStat](../../19-data-recording/RecStat.md) 达到 `4`（记录完成）时等待结束；无触发的停止使状态停留在 `5` 或 `6`，等待**不会**结束 |
| 20 | 数字量输入 1 | 0 或 1 |
| 21 | 数字量输入 2 | 0 或 1 |
| 22 | 数字量输入 3 | 0 或 1 |
| 23 | 数字量输入 4 | 0 或 1 |
| 24 | 数字量输入 5 | 0 或 1 |
| 25 | 数字量输入 6 | 0 或 1 |
| 26 | 数字量输入 7 | 0 或 1 |
| 27 | 数字量输入 8 | 0 或 1 |
| 28 | 数字量输入 9 | 0 或 1 |
| 29 | 数字量输入 10 | 0 或 1 |
| 30 | 数字量输入 11 | 0 或 1 |
| 31 | 数字量输入 12 | 0 或 1 |
| 32 | 数字量输入 13 | 0 或 1 |
| 33 | 数字量输入 14 | 0 或 1 |

## 示例

```text
AWaitStatus[17],1   ; hold until the axis settles in target (in-target status reaches "target reached"; the assigned value is range-checked but does not change the test)
AWaitStatus[7],0    ; hold until motion has stopped (In motion = 0)
AWaitStatus[20],1   ; hold until digital input 1 is high
```

## 另请参阅

- [WaitTime](WaitTime.md) — 使任务等待固定时间而非状态条件
