---
keyword: PushEvTotLost
summary: 自上电以来丢弃的推送事件总数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 910
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvTotLost

自上电以来丢弃的推送事件总数。

## 概述

`PushEvTotLost` 统计自上电以来控制器因事件队列已满而丢弃的所有[推送事件](00-overview.md)。它与 [PushEvLost](PushEvLost.md) 同时递增，但与 `PushEvLost` 不同，它**从不自动清零**：成功发送和 [PushEvEnable](PushEvEnable.md) 的切换都不会改变它。

它是非轴计数器，不保存至闪存，上电后读数为 0。该关键字可写，因此上位机可以通过写入 0 将其复位。

无论是否有上位机连接推送套接字，事件都会被检测并入队。因此，即使对于只读取关键字的用户，`PushEvTotLost` 持续增加也表明事件正在发生但未被接收。

## 示例

```text
APushEvTotLost       ; total events dropped since power-on
APushEvTotLost=0     ; reset the total
```

## 另请参阅

- [PushEvLost](PushEvLost.md) — 自上次成功发送以来丢弃的事件数
- [PushEvStat](PushEvStat.md) — 队列中的空闲行数
- [Push Events 概述](00-overview.md)
