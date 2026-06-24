---
keyword: CANAddr
summary: 控制器节点的 CAN 基地址。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 67
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
  - 2032
  default: 64
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CANAddr

控制器节点的 CAN 基地址。

## 概述

`CANAddr` 设置控制器在 CAN 总线上的 CAN 基地址。请将其设为 **16 的倍数**，因为每个控制器为自身保留一个由 16 个连续 CAN 标识符组成的块。它保存至闪存并在启动期间应用，因此更改后需 [Save](../02-operation/Save.md) 并 [Reset](../02-operation/Reset.md) 才能生效。允许范围一直延伸到 11 位 CAN 标识符上限，为每控制器的 16 标识符块预留空间。

## 工作原理

启动时，固件将存储的基地址与控制器的硬件地址 DIP 拨码开关组合，形成 **CAN 初始地址**：

$$
\text{initial address} = \text{CANAddr} + 16 \cdot (\text{DIP address})
$$

从该初始地址开始，控制器分配其 CAN 邮箱：

| 相对初始地址的偏移 | 用途 |
|---|---|
| +0 | 接收（上位机 → 控制器 命令） |
| +1 | 回复（控制器 → 上位机 响应） |
| +15 | 推送状态消息 |

这就是为什么基地址必须是 16 的倍数、且每个节点占用一个 16 标识符块的原因：DIP 开关以 16 为单位步进该块，使多个相同的控制器可以共享一条总线而不重叠。一个专用的"全部恢复默认"DIP 设置会覆盖存储的值，并强制使用众所周知的默认基地址 64，这在恢复一个存储地址未知的控制器时很有用。

CAN 标识符为 11 位宽，因此地址必须保持在该范围内；可配置的最大值为顶部的 16 标识符块预留空间。完整的寻址方案请参阅通信手册。

## 示例

```text
ACANAddr=64          ; set the CAN base address (a multiple of 16), then Save and Reset
```

## 参见

- [CANBaud](CANBaud.md) — CAN 总线波特率
- [CANDelay](CANDelay.md) — CAN 回复消息之间的最小间隔
- [ChainAddress](ChainAddress.md) — 串行菊花链拓扑中的地址
- [RemoteCANSend](RemoteCANSend.md) — 向另一节点发送 CAN 写/读
