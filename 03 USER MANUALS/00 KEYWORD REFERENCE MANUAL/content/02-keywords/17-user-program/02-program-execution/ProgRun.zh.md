---
keyword: ProgRun
summary: 以指定线程号运行（或恢复）一个任务。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 198
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 254
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgRun

以指定线程号运行（或恢复）一个任务。

## 概述

`ProgRun[Thread no.], Task no.` 在指定线程上启动（或恢复）一个用户程序任务。控制器可同时运行多个用户程序线程，每个线程拥有独立的程序指针、调用栈和数值栈，从而使独立任务可以并行运行。`ProgRun` 通过数组索引选择驱动哪个线程，通过值选择该线程应执行哪个任务。该命令为非轴命令，不保存至闪存。

## 工作原理

控制器在内置的轮询调度器下运行用户程序线程。独立控制器最多支持 **8 个线程**，Central-i 主控最多支持 **12 个**；索引范围为 `[1]` 至 `[8]`（或 `[12]`）。在每个调度轮次中，控制器轮询推进到下一个到期的活动线程，并为该单一线程执行**一条底层指令**，然后继续——线程以协作方式共享处理器，每轮次执行一条指令。各线程被服务的相对频率由 [ProgPriority](ProgPriority.md) 控制。

传递给 `ProgRun` 的**值**用于选择任务：

| 任务值 | 效果 |
|----|----|
| 0 | **恢复**线程从当前位置继续执行——用于继续被 [ProgHalt](ProgHalt.md) 暂停的线程。指针和栈保持不变。 |
| 1 | 运行**主程序**（任务 1）——从程序文件开头开始执行的代码。 |
| 2 至 30（独立控制器）或 2 至 254（Central-i 主控） | 运行指定编号的任务。任务由 [ProgTask](ProgTask.md) 标签标记。 |

当任务值为 1–30（独立控制器）或 1–254（Central-i 主控）时，线程首先被重新初始化（指针设置到该任务起始位置，调用栈和数值栈清空，错误清除），然后启动——从任务入口点全新运行。任务值为 0 时，所有线程状态保持不变，仅重新使能执行，这使得已暂停的线程能够从停止的确切指令处继续执行。若要强制已暂停的线程从头开始运行而非恢复，请先使用 [ProgReset](ProgReset.md)。

以下情况下 `ProgRun` 将被拒绝并返回错误：没有已存储的程序、已存储程序校验和验证失败、请求的任务不存在，或请求的线程已在运行中。若线程指针已到达程序末尾，恢复操作（任务值 `0`）同样会被拒绝——已没有可继续的内容，请重置或启动一个任务。线程运行期间，[ProgStat](ProgStat.md) 对该线程报告 `1`，[ProgPointer](ProgPointer.md) 跟踪其当前位置。

## 示例

```text
AProgRun[1],1       ; 以线程 1 运行主程序（任务 1）
AProgRun[3],5       ; 以线程 3 运行任务 5
AProgRun[1],0       ; 从 ProgHalt 停止处恢复线程 1
```

## 另请参见

- [ProgTask](ProgTask.md) — 标记任务起始位置的标签
- [ProgHalt](ProgHalt.md) — 暂停线程（可通过 `ProgRun[thread],0` 恢复）
- [ProgReset](ProgReset.md) — 重置线程，使下次运行从头开始
- [ProgPriority](ProgPriority.md) — 调度器服务每个线程的频率
- [ProgStat](ProgStat.md) — 线程的运行状态
- [AutoExec](../../01-system/02-operation/AutoExec.md) — 启动时自动运行主程序
