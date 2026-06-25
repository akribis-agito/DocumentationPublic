---
keyword: CANBaud
summary: CAN 总线波特率，从固定表中选择。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 68
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 6
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CANBaud

CAN 总线波特率，从固定表中选择。

## 概述

`CANBaud` 从包含六个条目的固定表中选择 CAN 总线波特率。该值是一个索引，而非速率本身。默认值 `6` 对应 1 Mbit/s。它保存至闪存并在启动时应用，因此更改后需执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md) 才能生效。**总线上的所有节点必须使用相同的波特率。**

| CANBaud | Baud rate [kbit/s] |
|---------|--------------------|
| 1 | 31.25 |
| 2 | 62.5 |
| 3 | 125 |
| 4 | 250 |
| 5 | 500 |
| 6 | 1000 |

## 工作原理

启动时，固件读取 `CANBaud`，并使用该速率对应的预先计算配置对 CAN 控制器的位定时寄存器进行编程。如果存储的值超出表范围，固件将回退到 1 Mbit/s（索引 6）。实际应用的速率会通过标识数据回报，因此上位机可以确认当前使用的链路速度。

更多信息请参阅通信手册。

## 示例

```text
ACANBaud=6           ; 1 Mbit/s (default), then Save and Reset
ACANBaud=4           ; 250 kbit/s
```

## 另请参阅

- [CANAddr](CANAddr.md) — CAN 基地址
- [CANDelay](CANDelay.md) — CAN 回复消息之间的最小间隔
- [RSBaud](RSBaud.md) — 串口波特率
