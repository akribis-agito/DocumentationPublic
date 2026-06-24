---
keyword: ProgHalt
summary: 暂停指定的用户程序线程；之后可从停止处恢复执行。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 197
attributes:
  access: ro
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
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgHalt

暂停指定的用户程序线程；之后可从停止处恢复执行。

## 概述

`ProgHalt[Thread no.]` 暂停指定线程。暂停与复位不同：线程保留其程序指针、调用栈和数值栈，因此后续的 `ProgRun[thread],0` 将从停止处的确切指令继续执行。若要同时暂停所有活动线程，使用 [ProgHaltAll](ProgHaltAll.md)；若要暂停发出该指令的任务本身，使用 [ProgHaltThis](ProgHaltThis.md)。`ProgHalt` 也常放置于非循环程序的末尾，以防止执行进入函数定义区域（参见 [ProgFunc](ProgFunc.md)）。这是一个非轴指令，不保存至闪存。

## 工作原理

`ProgHalt` 将线程从调度器的轮询中移除，而不清除其已保存的位置。线程的状态（由 [ProgStat](ProgStat.md) 报告）立即降为 `0`（未运行）。由于没有任何内容被清除，暂停与复位的区别如下：

| 操作 | 指针与栈 | 下次 `ProgRun` |
|----|----|----|
| `ProgHalt[thread]` | 保留 | `ProgRun[thread],0` 从停止点恢复 |
| [ProgReset](ProgReset.md)`[thread]` | 清除（指针回到主程序起始处） | 从任务起始处重新执行 |

线程编号必须在可用范围内（`[1]` 到 `[8]`，或 Central-i 主控上为 `[12]`）；超出范围的索引将被拒绝。

## 示例

```text
AProgHalt[1]        ; pause thread 1; AProgRun[1],0 later resumes from this point
```

## 参见

- [ProgRun](ProgRun.md) — 运行线程，或使用 `ProgRun[thread],0` 恢复执行
- [ProgHaltAll](ProgHaltAll.md) — 暂停所有活动线程
- [ProgHaltThis](ProgHaltThis.md) — 暂停发出该指令的任务
- [ProgReset](ProgReset.md) — 复位线程（与暂停不同）
- [ProgStat](ProgStat.md) — 线程的运行状态
