---
keyword: FIFOValue
summary: 只读数组，报告与每条 FIFO 运动条目配对的数据值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 280
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 129
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# FIFOValue

只读数组，报告与每条 FIFO 运动条目配对的数据值。

## 概述

`FIFOValue` 报告 FIFO 运动队列中每条当前存储条目的数据值。每条队列条目由一个**类型**（由 [FIFOType](FIFOType.md) 报告）和一个**值**（由本关键字报告）组成。在相同索引处读取两个数组，即可完整描述一条排队条目。数组共有 129 个元素（索引 0 保留；通信索引从 1 开始），与 [FIFOType](FIFOType.md) 保持一致。

完整的 FIFO 运动模式说明及所有相关关键字，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

值的含义取决于 [FIFOType](FIFOType.md) 在同一索引处报告的条目类型：

| 类型（来自 `FIFOType`） | 值的含义 |
|----|----|
| 1 — 按位置增量的线性片段 | 片段期间行进的位置增量。 |
| 2 — 按速度的线性片段 | 片段期间保持不变的速度参考值。 |
| 3 — 按位置增量的抛物线片段 | 片段期间行进的位置增量。 |
| 4 — 按加速度的抛物线片段 | 片段期间保持不变的加速度参考值。 |
| 5 — 周期时间 | 以控制周期采样数表示的片段时长，应用于其后的片段。 |

此处存储的值与提供给对应 `FIFOPush*` 函数的值完全相同。若要检查已排队条目，请在相同索引处读取 `FIFOType` 和 `FIFOValue`。

## 示例

```text
AFIFOValue[1]       ; read the value of the first entry currently in the queue
```

## 另请参阅

- [FIFOType](FIFOType.md) — 与每条 FIFO 条目值配对的类型；FIFO 模式完整说明
- [FIFOStatus](FIFOStatus.md) — 队列深度及空闲/已用条目数
