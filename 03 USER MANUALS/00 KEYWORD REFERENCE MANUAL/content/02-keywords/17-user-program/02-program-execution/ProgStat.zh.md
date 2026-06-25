---
keyword: ProgStat
summary: 报告指定用户程序线程的运行状态。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 259
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
  - 1
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgStat

报告指定用户程序线程的运行状态。

## 概述

`ProgStat` 是一个只读数组参数，按线程索引，报告单个用户程序线程的运行状态。它是 [ProgStatAll](ProgStatAll.md)（所有线程的综合状态）的逐线程补充，在诊断线程停止原因时与 [ProgError](ProgError.md) 配合使用。索引范围为 `[1]` 至 `[8]`（Central-i 主控为 `[12]`）。该参数为非轴状态变量，不保存至闪存。

## 工作原理

控制器在调度器服务各线程时维护每个线程的状态：

| 值 | 含义 |
|----|----|
| -1 | 控制器中没有已加载的用户程序 |
| 0 | 已加载但该线程未运行（已停止、已暂停、已重置或因错误停止） |
| 1 | 该线程正在运行 |

运行中（`1`）并非在线程启动的瞬间写入；它在调度器下次服务该线程行时设置。由于服务频率受 [ProgPriority](ProgPriority.md) 控制——较高的优先级值使线程在各行之间等待更多调度轮次——启动线程与 `ProgStat` 读到 `1` 之间可能存在短暂延迟。`0` 值在所有停止路径上（暂停、重置、断点、单步和错误停止）都会被立即写入。启动线程（例如通过 [ProgRun](ProgRun.md)）也会将该线程的 [ProgError](ProgError.md) 清除为 `0`。

当线程因运行时错误停止时，`ProgStat` 返回 `0`——没有单独的"错误"值——原因保留在该线程的 [ProgError](ProgError.md) 中。要区分正常停止和错误停止，请读取相同索引的 `ProgError`。

## 示例

```text
AProgStat[1]        ; 线程 1 运行中返回 1，已停止返回 0，无程序返回 -1
```

## 另请参阅

- [ProgStatAll](ProgStatAll.md) — 所有线程的综合状态
- [ProgError](ProgError.md) — 每个线程的最近错误代码
- [ProgRun](ProgRun.md) — 以线程方式运行任务
- [ProgPointer](ProgPointer.md) — 每个线程的当前位置
