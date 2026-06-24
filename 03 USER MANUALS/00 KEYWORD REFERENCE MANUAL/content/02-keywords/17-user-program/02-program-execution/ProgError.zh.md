---
keyword: ProgError
summary: 报告每个用户程序线程的最近一次解释器错误代码。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 199
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgError

报告每个用户程序线程的最近一次解释器错误代码。

## 概述

`ProgError` 是一个只读数组参数，按线程索引，报告用户程序线程最近一次因错误停止时所产生的错误代码。值为 `0` 表示无错误。在诊断意外停止的线程时，它与 [ProgStat](ProgStat.md) 和 [ProgStatAll](ProgStatAll.md) 配合使用。索引范围为 `[1]` 至 `[8]`（在 Central-i 主控上为 `[12]`）。它是一个非轴状态变量，不保存至闪存。

## 工作原理

当线程中的某条指令执行失败——例如栈溢出或下溢、调用不存在的任务或函数，或发生任何其他运行时错误——控制器将：

1. 将错误代码存入该线程对应的 `ProgError` 中。
2. 暂停该线程，并将其 [ProgStat](ProgStat.md) 设置为 `0`（未运行），同时将 [ProgPointer](ProgPointer.md) 保留在出错指令处，以便检查或重新执行。
3. 将错误添加至控制器错误日志，并标注来源为该用户程序线程，因此该错误也会出现在 [ErrLog](../../07-status-and-faults/ErrLog.md) 中。在 `ErrLog` 中，用户程序错误以来源 `16 + n` 标记（例如线程 1 为 `17`）。

`ProgError` 将保留该值，直到该线程再次运行——通过 [ProgRun](ProgRun.md) 或 [ProgSingle](ProgSingle.md) 启动或单步执行线程，或通过 [ProgReset](ProgReset.md) 复位线程，均会将其错误清除为 `0`。非活动线程的错误保持锁存，因此可在事后读取。由于任意线程发生错误都会使 [ProgStatAll](ProgStatAll.md) 变为 `2`，该聚合值可快速检测是否有线程需要检查 `ProgError`。

> **注意：** 各错误代码编号在用户程序语言手册中定义，本参考手册不予重复列出。

## 示例

```text
AProgError[1]       ; error code for thread 1 (0 = no error)
```

## 另请参阅

- [ProgStat](ProgStat.md) — 线程的运行状态
- [ProgStatAll](ProgStatAll.md) — 所有线程的汇总状态（2 = 某线程发生错误）
- [ProgPointer](ProgPointer.md) — 保留在出错指令处的位置
- [ProgReset](ProgReset.md) — 复位线程（清除其错误）
- [ErrLog](../../07-status-and-faults/ErrLog.md) — 控制器错误日志；用户程序错误按线程标注
