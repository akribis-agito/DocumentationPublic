---
keyword: ProgSnapVal
summary: 保存程序快照机制捕获的值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 538
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgSnapVal

保存程序快照机制捕获的值。

## 概述

`ProgSnapVal` 是一个只读数组，保存当用户程序线程发生运行时错误时，程序快照机制所捕获的值。它是 [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md) 中故障快照值的程序调试对应项：错误发生后读取该值，可获得线程在故障瞬间程序状态的冻结快照。元素默认值为 `-1`，表示该槽位尚未捕获任何内容（重新配置 [ProgSnapSrc](ProgSnapSrc.md) 后也会恢复此状态）。该参数为非轴状态变量，不保存至闪存。

## 工作原理

快照在用户程序线程引发运行时错误的瞬间一次性完成——与设置该线程 [ProgError](ProgError.md)、向 [ErrLog](../../07-status-and-faults/ErrLog.md) 追加记录并暂停线程是同一事件。

数组以每线程 **10 个元素为一个块**组织（独立控制器最多 8 个线程，Central-i 主控最多 12 个）：线程 1 占用 `ProgSnapVal[1]…[10]`，线程 2 占用 `[11]…[20]`，以此类推（索引 `[0]` 未使用，因此索引从 1 开始）。每个线程块内的布局固定；仅前四个条目来自 [ProgSnapSrc](ProgSnapSrc.md) 配置：

| 块内槽位 | 捕获值 | 来源 |
|---|---|---|
| 1 | 用户选择的参数 1 | [ProgSnapSrc](ProgSnapSrc.md) 槽位 1 |
| 2 | 用户选择的参数 2 | [ProgSnapSrc](ProgSnapSrc.md) 槽位 2 |
| 3 | 用户选择的参数 3 | [ProgSnapSrc](ProgSnapSrc.md) 槽位 3 |
| 4 | 用户选择的参数 4 | [ProgSnapSrc](ProgSnapSrc.md) 槽位 4 |
| 5 | 程序位置（[ProgPointer](ProgPointer.md)） | 固定 |
| 6 | 数值（表达式）栈剩余空间（[ProgExpDepth](ProgExpDepth.md)） | 固定 |
| 7 | 调用栈剩余空间（[ProgCallDepth](ProgCallDepth.md)） | 固定 |
| 8 | 保留 | 固定 |
| 9 | 运行时错误代码（[ProgError](ProgError.md)） | 固定 |
| 10 | 捕获时间（自上电以来的秒数） | 固定 |

[ProgSnapSrc](ProgSnapSrc.md) 条目为 `0`（已禁用）的用户槽位保持为 `-1`。已缩放参数的捕获值以原始（内部）单位存储。

要读取指定线程的值，计算其槽位：`(线程号 − 1) × 10 + 块内槽位号`。例如，线程 2 的运行时错误代码位于 `ProgSnapVal[19]`。

## 示例

```text
AProgSnapVal[1]     ; 线程 1，第一个用户选择的快照源
AProgSnapVal[9]     ; 线程 1，捕获时的运行时错误代码（ProgError）
AProgSnapVal[10]    ; 线程 1，捕获时间（自上电以来的秒数）
AProgSnapVal[19]    ; 线程 2，运行时错误代码
AProgSnapVal        ; 读取整个快照
```

## 版本间变更

在 v4 中，捕获值为 32 位。在 v5（Central-i）中，捕获值为 64 位：宽值以完整分辨率捕获，浮点参数以位模式存储而非截断为整数。上述逐线程块布局在两个版本中相同。

## 另请参阅

- [ProgSnapSrc](ProgSnapSrc.md) — 选择每个线程的四个用户参数
- [ProgError](ProgError.md) — 触发捕获的运行时错误（也捕获于块中）
- [ConFltSnapVal](../../07-status-and-faults/ConFltSnapVal.md) — 故障快照捕获值
