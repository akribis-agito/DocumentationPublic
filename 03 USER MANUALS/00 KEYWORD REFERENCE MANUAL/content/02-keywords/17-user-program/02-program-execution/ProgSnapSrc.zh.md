---
keyword: ProgSnapSrc
summary: 选择程序快照机制所捕获的参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 537
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 33
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgSnapSrc

选择程序快照机制所捕获的参数。

## 概述

`ProgSnapSrc` 配置程序快照机制所捕获的控制器参数——它是用户程序的调试对应项，对应于由 [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md) 配置的故障快照。当用户程序线程发生运行时错误时，控制器会将程序状态的逐线程快照冻结至 [ProgSnapVal](ProgSnapVal.md)；`ProgSnapSrc` 选择其中的用户可配置参数，使您可以精确捕获诊断故障所需的变量。该参数为非轴数组，保存至闪存（默认值 `0`）。

## 工作原理

每个线程拥有 **4 个用户可配置的源槽位**。数组按线程布局，每个线程 4 个槽位，独立控制器最多支持 8 个线程，Central-i 主控最多支持 12 个：线程 1 使用 `ProgSnapSrc[1]…[4]`，线程 2 使用 `[5]…[8]`，以此类推（索引 `[0]` 未使用，因此索引从 1 开始）。这四个槽位填充该线程 [ProgSnapVal](ProgSnapVal.md) 块的用户部分；每个块的其余部分由固定的程序状态值自动填充，无需在此配置（参见 [ProgSnapVal](ProgSnapVal.md)）。

每个槽位保存一个[复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md)，用于指定要捕获的参数，编码包含三个字段：

| 位 | 字段 |
|---|---|
| 0–9 | 参数的 CAN 代码 |
| 10–14 | 轴号（0 = A；非轴参数忽略此字段） |
| 16–31 | 数组索引（对于数组参数；标量使用 0） |

对于轴 A 上的标量参数，复合代码即为普通 CAN 代码。向槽位写入 `0` 将其禁用（其 [ProgSnapVal](ProgSnapVal.md) 条目保持为 `-1`）。非零选择在写入时经过验证，若不符合以下条件则返回错误而被拒绝：指定的参数不存在（错误 `279`）、指定了无效轴或对标量提供了非零数组索引（错误 `280`）、数组索引超出 `1` 到参数数组大小的范围（错误 `281`），或指定了命令而非参数（错误 `282`）。接受后，控制器解析内部指针及缩放因子以供快速捕获，并**将所有 [ProgSnapVal](ProgSnapVal.md) 条目重置为 `-1`**，丢弃任何之前的快照——因此请在需要诊断的错误发生之前配置好源。已缩放参数的捕获值以原始（内部）单位存储。

## 示例

```text
AProgSnapSrc[1]=<complex CAN code of parameter to capture>   ; 线程 1，第一个用户快照源
AProgSnapSrc[1]=0   ; 禁用线程 1 的第一个用户槽位
AProgSnapSrc        ; 读取整个快照源配置
```

## 另请参见

- [ProgSnapVal](ProgSnapVal.md) — 快照机制捕获的值
- [ProgError](ProgError.md) — 触发捕获的逐线程运行时错误
- [ConFltSnapSrc](../../07-status-and-faults/ConFltSnapSrc.md) — 故障快照源选择
