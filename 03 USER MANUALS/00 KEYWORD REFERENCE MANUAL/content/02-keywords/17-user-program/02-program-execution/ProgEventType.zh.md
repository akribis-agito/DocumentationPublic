---
keyword: ProgEventType
summary: 定义事件的触发类型（边沿、等于、不等于……）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 522
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 8
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventType

定义事件的触发类型（边沿、等于、不等于……）。

## 概述

`ProgEventType` 定义事件的触发条件类型——例如上升沿、等于或不等于比较。它是定义事件触发器的四个参数之一，与源参数 [ProgEventPar](ProgEventPar.md)、比较值 [ProgEventVal](ProgEventVal.md) 和位掩码 [ProgEventMask](ProgEventMask.md) 共同构成与数据记录触发器非常相似的结构。有效范围为 `1`–`8`（默认值 `1`）。该参数为非轴数组参数（索引 `[1]`–`[5]`，每个事件对应一个索引），保存至闪存。

## 工作原理

每个控制周期内，对于已置位并等待的事件，控制器获取被监控参数（[ProgEventPar](ProgEventPar.md)），对读数应用掩码（[ProgEventMask](ProgEventMask.md)），然后将此处选择的条件与阈值 [ProgEventVal](ProgEventVal.md) 进行评估。掩码仅应用于源读数，阈值本身不被掩码处理。下表中，*value* 为当前经掩码处理的源读数，*threshold* 为（已转换的）[ProgEventVal](ProgEventVal.md)：

| 值 | 条件 | 触发时机 |
|---|---|---|
| 1 | 大于 | value &gt; threshold |
| 2 | 等于 | value == threshold |
| 3 | 不等于 | value != threshold |
| 4 | 小于 | value &lt; threshold |
| 5 | 上升沿 | value 向上穿越 threshold（上一周期 &le; threshold，当前 &gt; threshold） |
| 6 | 下降沿 | value 向下穿越 threshold（上一周期 &ge; threshold，当前 &lt; threshold） |
| 7 | 手动 | **不支持用于程序事件**——该类型的感测循环不执行任何操作，且 [ProgEventStat](ProgEventStat.md) 唯一可写值为 `0`，因此类型为 `7` 的事件永远不会变为待处理状态。该值保留用于与数据记录器触发类型的编号对应。 |
| 8 | 已更改 | value 与事件置位时捕获的值不同 |

说明：

- **边沿类型（5、6）** 将当前读数与上一周期的读数进行比较，因此每次穿越只触发一次，而非在电平条件持续期间连续触发。"已更改"类型（8）与事件置位时捕获的读数进行比较。
- 比较在被监控参数的原生数据类型（整数或浮点数）中执行。掩码应用于整数源；浮点源的比较不应用掩码。

## 示例

```text
AProgEventType[1]=5  ; event 1 fires on a rising-edge crossing of ProgEventVal[1]
AProgEventType[1]=2  ; event 1 fires when the masked source equals ProgEventVal[1]
```

## 另请参阅

- [ProgEventPar](ProgEventPar.md) — 触发事件的参数
- [ProgEventVal](ProgEventVal.md) — 用于触发检测的值
- [ProgEventMask](ProgEventMask.md) — 应用于触发的位掩码
