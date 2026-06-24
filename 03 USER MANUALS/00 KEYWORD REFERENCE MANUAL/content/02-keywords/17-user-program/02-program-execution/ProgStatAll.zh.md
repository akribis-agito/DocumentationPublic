---
keyword: ProgStatAll
summary: 返回所有用户程序任务的综合状态字。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 298
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgStatAll

返回所有用户程序任务的综合状态字。

## 概述

`ProgStatAll` 是一个只读参数，返回一个单一值，汇总所有用户程序线程的执行状态。它是 [ProgStat](ProgStat.md) 的聚合对应项——后者仅报告一个线程——可用于快速检查整个程序的健康状态，而无需逐个读取每个线程。该参数属于非轴域状态变量，不保存至闪存。

## 工作原理

控制器大约每秒扫描一次所有线程并重新计算该汇总值。任意线程上的错误优先于任意线程的运行状态，因此报告的是所有线程中最严重的状态：

| 值 | 含义 |
|----|----|
| -1 | 控制器中未加载用户程序 |
| 0 | 程序已加载，但无线程正在运行 |
| 1 | 至少一个线程正在运行（且无线程发生错误） |
| 2 | 至少一个线程因错误而停止 |

汇总值的计算过程为：从 `-1`（无程序）开始，程序存在时提升至 `0`，若任意线程的 [ProgStat](ProgStat.md) 处于运行状态则设为 `1`，一旦发现任意线程的 [ProgError](ProgError.md) 非零则设为 `2`。错误状态是通过 `ProgError` 检测的，而非通过 `ProgStat` 的某个"错误"值（`ProgStat` 不含错误值），因此无论线程扫描顺序如何，错误（`2`）均优先于运行（`1`）。

值得注意的是：因错误停止的线程，其 [ProgStat](ProgStat.md) 读取为 `0`（线程停止时 `ProgStat` 被设置为"未运行"），但 `ProgStatAll` 仍读取为 `2`，因为非零的 [ProgError](ProgError.md) 才是提升汇总值的依据。当 `ProgStatAll` 读取为 `2` 时，应逐线程读取 `ProgError` 以确认哪个线程失败及失败原因。由于该值以一秒为周期更新，非常短暂的运行状态可能无法在此处显示；如需立即获取各线程状态，请使用 [ProgStat](ProgStat.md)。

## 示例

```text
AProgStatAll        ; -1 无程序，0 空闲，1 某线程运行中，2 某线程发生错误
```

## 另请参阅

- [ProgStat](ProgStat.md) — 单个线程的运行状态
- [ProgError](ProgError.md) — 每个线程的最近错误码
- [ProgPointer](ProgPointer.md) — 每个线程的当前位置
- [ProgReset](ProgReset.md) — 将线程重置到初始状态
