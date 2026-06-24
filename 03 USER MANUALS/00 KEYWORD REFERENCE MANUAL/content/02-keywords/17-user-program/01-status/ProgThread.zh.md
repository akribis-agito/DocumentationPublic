---
keyword: ProgThread
summary: 报告当前正在执行的用户程序线程编号。
availability:
  standalone: []
  central-i:
  - v5
can_code: 737
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgThread

报告当前正在执行的用户程序线程编号。

## 概述

`ProgThread` 是一个只读状态关键字，返回当前正在执行的用户程序线程编号。用户程序支持多线程：控制器依次运行每个活动线程，每个调度周期推进其中一个线程。`ProgThread` 告知当前正在推进的是哪个线程，使程序或上位机能够获知"我正在运行，且在哪个线程上？"——例如通过 [ProgStat](../02-program-execution/ProgStat.md)、[ProgError](../02-program-execution/ProgError.md) 或 [ProgPointer](../02-program-execution/ProgPointer.md) 索引各线程状态。该参数为非轴作用域，不保存至闪存。

此关键字从 v5（Central-i）起可用。

## 工作原理

控制器以轮询顺序调度活动线程，每个周期执行一个线程的一条指令（受每个线程的 [ProgPriority](../02-program-execution/ProgPriority.md) 影响）。`ProgThread` 报告当前线程的编号。线程编号从 `1` 开始，主线程为线程 `1`。从正在运行的用户程序内部读取时，返回值为该程序自身的线程编号，这是共享代码获知自身所在线程的自然方式。

`ProgThread` 设计用于从运行中的程序内部读取，此时返回该程序自身的线程编号。由上位机直接读取的值无法标识某个特定的运行线程。

默认值为 `1`。报告的编号始终在该型号所支持的线程范围内。

## 示例

```text
AProgThread         ; 读取当前正在执行的线程编号
```

## 另请参见

- [ProgStat](../02-program-execution/ProgStat.md) — 指定线程的运行/停止状态
- [ProgPriority](../02-program-execution/ProgPriority.md) — 各线程的调度优先级
- [ProgError](../02-program-execution/ProgError.md) — 指定线程的运行时错误码
- [ProgPointer](../02-program-execution/ProgPointer.md) — 指定线程的当前程序偏移量
