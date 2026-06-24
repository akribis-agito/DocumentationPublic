---
summary: 报告正在执行的用户程序任务的当前源代码行号。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgLine

报告正在执行的用户程序任务的当前源代码行号。

## 概述

`ProgLine` 报告正在执行的用户程序线程的当前源代码行号——这是在原始程序源文件中可读的位置，与 [ProgPointer](ProgPointer.md) 给出的原始字节偏移量不同。它是一个调试辅助工具，供 Agito PCSuite 用于高亮显示线程所在的行。

## 工作原理

控制器本身仅将位置作为已存储程序中的字节偏移量进行跟踪；该值由 [ProgPointer](ProgPointer.md) 报告。从该偏移量到原始源文件中行号的映射，通过程序编译时生成的调试信息完成。由于控制器不存储原始源代码，该转换由上位机工具（PCSuite）而非控制器执行，这也是为何在不使用该工具时，`ProgPointer` 是需要读取的底层值。

> **注意：** 在本参考手册所依据的固件中，`ProgLine` 并不作为控制器关键字出现——控制器上仅 [ProgPointer](ProgPointer.md) 可用。在直接依赖 `ProgLine` 之前，请对照当前固件和 PCSuite 确认其可用性。

## 另请参阅

- [ProgPointer](ProgPointer.md) — 以字节偏移量表示的当前位置（控制器侧的值）
- [ProgStat](ProgStat.md) — 线程的运行状态
- [ProgBreaks](ProgBreaks.md) — 与行号/位置读取配合使用的断点
