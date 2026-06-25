---
keyword: RSBaud
summary: 每个端口的串口（RS232/USB）波特率，从固定表中选择。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 79
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 5
  default: 4
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 1
    - 4
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RSBaud

每个端口的串口（RS232/USB）波特率，从固定表中选择。

## 概述

`RSBaud` 选择控制器各串口的波特率，每个端口对应一个数组元素。（该数组的维度设定使可用索引从 `[1]` 开始；索引 `[0]` 不使用。）

- `RSBaud[1]` — micro-USB 端口
- `RSBaud[2]` — RJ45 端口

该值是下表中的索引，而不是速率本身。默认值 `4` 对应 115200 bit/s。它会保存至闪存并在启动时应用，因此更改后请执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md) 以使其生效。

| RSBaud | Baud rate [bit/s] |
|--------|-------------------|
| 1 | 9600 |
| 2 | 19200 |
| 3 | 38400 |
| 4 | 115200 |
| 5 | 57600 |

请注意，索引 `5`（57600 bit/s）在数值顺序上是乱序的——它是在原有四种速率之后追加的。

## 工作原理

每个端口在启动时根据其 `RSBaud` 元素独立配置。固件在上表中查找该索引，并据此设定串行外设的波特率分频值。如果存储的值超出表范围，固件会回退到 115200 bit/s。串行链路的两端必须使用相同的波特率。

更多信息请参阅通信手册。

## 版本间变更

在 central-i（v5）上，`57600` 条目（索引 `5`）**不可用**——有效范围仅为 `1`–`4`。在 standalone/v4 上，支持完整范围 `1`–`5`（包括 `5` = 57600）。

## 示例

```text
ARSBaud[1]=4         ; set the micro-USB port to 115200 bit/s
ARSBaud[2]=1         ; set the RJ45 port to 9600 bit/s
```

## 另请参阅

- [CANBaud](CANBaud.md) — CAN 总线波特率
- [ChainAddress](ChainAddress.md) — 在此端口上运行的多点串行寻址
- [EthernetPort](EthernetPort.md) — 以太网 TCP 端口
