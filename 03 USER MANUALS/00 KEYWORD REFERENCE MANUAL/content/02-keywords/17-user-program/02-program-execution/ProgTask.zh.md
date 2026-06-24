---
summary: 标记可调用用户程序任务起始位置的标签关键字。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgTask

标记可调用用户程序任务起始位置的标签关键字。

## 概述

`ProgTask` 在用户程序中用作标签，标记任务的入口点。任务通过 [ProgRun](ProgRun.md) 以 `AProgRun[thread], task no.` 的形式启动，该命令将在指定线程号下执行与 `AProgTask[task no.]` 标签对应位置之后的代码，直至遇到 [ProgHalt](ProgHalt.md)。任务与函数（[ProgFunc](ProgFunc.md)）的区别在于：任务作为线程启动运行，而不是被调用后再返回。

## 工作原理

`ProgTask[]` 是标记程序位置的标签，而非可执行指令——它记录任务的起始位置，以便 [ProgRun](ProgRun.md) 可按索引启动该任务。任务与函数的区别在于进入方式：

- **任务**（[ProgTask](ProgTask.md)）由 [ProgRun](ProgRun.md) *以线程方式启动*，随后与其他线程并发运行，各线程的执行时间由 [ProgPriority](ProgPriority.md) 调度分配。任务是独立并行执行的基本单元。
- **函数**（[ProgFunc](ProgFunc.md)）在单个线程内通过 [ProgFuncCall](ProgFuncCall.md) / [Return](Return.md) *调用并返回*，使用该线程的调用栈。

任务编号与线程编号相互独立：任务编号选择要运行的 `ProgTask[]` 标签，线程编号是运行该任务的槽位。同一任务可在不同线程上运行，任务编号 `1` 运行主程序（文件起始处的代码）；详见 [ProgRun](ProgRun.md)。任务在 [ProgHalt](ProgHalt.md) 处结束；若未使用 `ProgHalt`，执行将继续到文件的后续行。

> **注意：** 若不使用 `ProgHalt`，执行将线性延续至文件的下一行。

## 示例

```text
AProgTask[5]        ; 标签：任务 5 的起始位置
; 任务 5 的主体
AProgHaltThis       ; 结束正在执行该任务的线程

AProgRun[3],5       ; 在其他位置：将任务 5 以线程 3 运行
```

由于同一任务可在不同线程上启动，任务主体应以 [ProgHaltThis](ProgHaltThis.md) 结束，该指令停止当前正在执行该任务的线程。`AProgHalt[n]` 则停止特定线程 `n`，因此只有当该任务恰好运行于线程 `n` 时，才能结束该任务。

## 另请参阅

- [ProgRun](ProgRun.md) — 将任务作为线程运行
- [ProgPriority](ProgPriority.md) — 运行线程的调度份额
- [ProgHaltThis](ProgHaltThis.md) — 停止当前线程（任务主体的末尾）
- [ProgHalt](ProgHalt.md) — 按编号停止特定线程
- [ProgFunc](ProgFunc.md) — 可调用函数的标签
