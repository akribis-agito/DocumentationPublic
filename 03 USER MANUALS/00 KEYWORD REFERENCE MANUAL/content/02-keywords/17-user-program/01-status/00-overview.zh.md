# 状态

本节是用户程序状态的**阅读导航页**。实际关键字页面位于 [程序执行](../02-program-execution/00-overview.md) 下的运行/停止/复位关键字旁，但通常最需要的三个"是否成功？"读取关键字在此直接列出，以免翻阅更大的表格。

| 需要了解时… | 读取 |
|---|---|
| …特定线程是否正在运行、已停止或没有程序 | [ProgStat](../02-program-execution/ProgStat.md)`[thread]` — 值为 `-1` / `0` / `1` |
| …所有线程的一次性概览（以最差状态为准；约每秒刷新一次） | [ProgStatAll](../02-program-execution/ProgStatAll.md) — 值为 `-1` / `0` / `1` / `2` |
| …已停止线程的停止原因（运行时错误码，在失败指令处锁存） | [ProgError](../02-program-execution/ProgError.md)`[thread]` — `0` 表示无错误 |
| …当前运行的程序正在哪个线程上执行（"我是否在运行，在哪个线程？"） | [ProgThread](./ProgThread.md) — 仅限 Central-i v5 |

[ProgThread](./ProgThread.md) 是本文件夹中唯一的关键字；与上述 v4 可用读取不同，它仅在 Central-i v5 产品上可用，并报告当前正在执行的线程编号。

典型的轮询与诊断流程：读取 [ProgStatAll](../02-program-execution/ProgStatAll.md)；若为 `2`，则逐线程读取 [ProgStat](../02-program-execution/ProgStat.md) 以找出停在错误上的线程，然后读取该线程的 [ProgError](../02-program-execution/ProgError.md) 以及失败偏移量的 [ProgPointer](../02-program-execution/ProgPointer.md)；同一错误也会在 [ErrLog](../../07-status-and-faults/ErrLog.md) 中标记线程编号。如需逐步调试，参见 [ProgSnapSrc](../02-program-execution/ProgSnapSrc.md) / [ProgSnapVal](../02-program-execution/ProgSnapVal.md)，它们在错误发生时冻结每个线程的程序状态快照。
