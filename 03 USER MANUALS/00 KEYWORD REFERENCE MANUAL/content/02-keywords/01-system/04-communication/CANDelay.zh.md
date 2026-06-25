---
keyword: CANDelay
summary: 施加于 CAN 消息的延迟，以采样为单位。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 222
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
  - 0
  - 1000
  default: 6
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CANDelay

施加于 CAN 消息的延迟，以采样为单位。

## 概述

`CANDelay` 设置连续两条发出的 CAN 消息之间的最小间隔，以控制中断采样为单位计量。这仅影响消息*时序*——它**不会**改变波特率（[CANBaud](CANBaud.md)）。它保存至闪存。当较慢的 CAN 上位机无法跟上控制器连续不断的回复、需要消息之间有确定间隔时，可使用该参数。

## 工作原理

控制器维护一个倒计数器，在每次控制中断时减 1（采样时钟以每秒 16384 采样运行，因此一个采样约为 61 µs）。在发送 CAN 消息之前，固件会等待直到倒计数器达到 0，然后立即用 `CANDelay` 值重新载入它。等待发生在两次发送**之间**，而不是叠加到正在进行的发送上，因此 `CANDelay` 强制从一次发送请求到下一次发送请求之间保持最小间隔：

$$
\text{minimum spacing} \approx \text{CANDelay} \cdot 61\ \mu\text{s}
$$

值为 0 时禁用该间隔（消息以总线允许的最快速度发送）。最大值为 1000 采样（约 61 ms）。关于何时需要延迟的指导，请参阅通信手册。

## 示例

```text
ACANDelay=6          ; require at least ~0.37 ms between CAN messages
ACANDelay=0          ; no enforced spacing
```

## 另请参阅

- [CANAddr](CANAddr.md) — CAN 基地址
- [CANBaud](CANBaud.md) — CAN 总线波特率
