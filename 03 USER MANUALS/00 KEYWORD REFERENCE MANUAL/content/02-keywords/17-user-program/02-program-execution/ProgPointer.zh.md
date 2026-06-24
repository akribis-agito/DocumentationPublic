---
keyword: ProgPointer
summary: 报告每个用户程序任务的当前指令指针。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 279
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
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgPointer

报告每个用户程序任务的当前指令指针。

## 概述

`ProgPointer` 是一个按线程索引的只读数组参数，报告每个用户程序线程的当前指令指针（程序计数器）。值为 `-1` 表示无程序。它是 [ProgLine](ProgLine.md) 的底层对应项，后者将相同位置映射回可读的源代码行号；在调试时与 [ProgBreaks](ProgBreaks.md)/[ProgBreakThis](ProgBreakThis.md) 和 [ProgStat](ProgStat.md) 配合使用。索引范围为 `[1]` 至 `[8]`（在 Central-i 主站上为 `[12]`）。该参数为非轴状态变量，不保存至闪存。

## 工作原理

指针以**从已存储程序起始处的字节偏移量**形式报告（范围为 `-1` 至 2147483647）：

| 值 | 含义 |
|----|----|
| -1 | 未加载用户程序 |
| 0 及以上 | 线程将要执行的下一条指令的字节偏移量 |

每条指令执行完毕后，控制器将线程的指针推进至下一条指令，因此在线程运行时读取 `ProgPointer` 可跟踪其执行进度。以下两种情况会使指针保持在原位而不推进：

- **发生运行时错误时**，指针停留在出错指令处（参见 [ProgError](ProgError.md)），以便检查或重新执行。
- **执行 [ProgHaltThis](ProgHaltThis.md) 时**，指针保留在暂停指令处，执行不会继续；由于指针停留在该行，后续的 `ProgRun[thread],0` 会重新执行 `ProgHaltThis` 并再次暂停，除非先移动指针。

来自 [ProgBreaks](ProgBreaks.md) 的断点与同一偏移量进行匹配：当线程的指针到达某个断点值时，线程被暂停。使用 [ProgReset](ProgReset.md) 重置线程会将其指针重置至主程序的起始处。

## 示例

```text
AProgPointer[1]     ; byte offset of thread 1's next instruction (-1 = no program)
```

## 另请参阅

- [ProgLine](ProgLine.md) — 以源代码行号表示的相同位置
- [ProgStat](ProgStat.md) — 线程的运行状态
- [ProgError](ProgError.md) — 发生运行时错误时指针停留处
- [ProgBreaks](ProgBreaks.md) — 与该偏移量匹配的断点
