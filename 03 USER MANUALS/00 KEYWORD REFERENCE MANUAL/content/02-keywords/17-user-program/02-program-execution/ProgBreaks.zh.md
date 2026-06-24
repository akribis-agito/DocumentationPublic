---
keyword: ProgBreaks
summary: 用户程序调试的每线程断点设置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 294
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 4
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
# ProgBreaks

用户程序调试的每线程断点设置。

## 概述

`ProgBreaks` 是一个可读写数组，在调试用户程序时最多保存 **3 个断点**（索引 `[1]`–`[3]`）。每个元素保存一个程序位置（[ProgPointer](ProgPointer.md) 值），执行应在该位置停止；默认值 `-1` 表示该槽为空。断点是全局的——适用于到达该位置的任意线程——通常由 PC Suite 调试器与 [ProgSingle](ProgSingle.md)（单步执行）和 [ProgBreakThis](ProgBreakThis.md)（中断当前运行任务）配合管理。它是一个非轴参数，不保存至闪存。

## 工作原理

在执行任意运行线程的下一条指令之前，控制器将该线程的当前程序位置（[ProgPointer](ProgPointer.md)）与 `ProgBreaks` 列表进行比较。从索引 `[1]` 开始扫描列表；遇到第一个空槽（`-1`）时终止扫描，因此应从 `[1]` 开始连续设置断点。若线程位置与某个断点匹配，该线程将在该指令处停止：停止运行但保留其状态，可使用 [ProgPointer](ProgPointer.md)、[ProgCallStack](ProgCallStack.md) 和程序快照（[ProgSnapVal](ProgSnapVal.md)）检查，然后通过 [ProgRun](ProgRun.md) 恢复或通过 [ProgSingle](ProgSingle.md) 单步执行。

在 [ProgRun](ProgRun.md) 或 [ProgSingle](ProgSingle.md) 指令之后第一条指令上触发的断点会被忽略，因此停在断点上的线程可以被恢复跨过该断点，而不会立即再次停止。将某槽设为 `-1` 即可删除该断点。

## 示例

```text
AProgBreaks[1]=<program location to break at>  ; set the first breakpoint
AProgBreaks[1]=-1                              ; clear the first breakpoint
AProgBreaks                                    ; read the breakpoint list
```

## 另请参阅

- [ProgBreakThis](ProgBreakThis.md) — 在正在运行的任务上设置断点
- [ProgSingle](ProgSingle.md) — 线程的单步执行
- [ProgPointer](ProgPointer.md) — 每个任务的当前指令指针
