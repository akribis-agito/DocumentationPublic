---
keyword: ChainAddress
summary: 控制器以菊花链拓扑运行时使用的 CAN 地址。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 159
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
  - -1
  - 8
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ChainAddress

控制器以菊花链拓扑运行时使用的 CAN 地址。

## 概述

`ChainAddress` 在菊花链串行总线上为本控制器分配一个地址，使多个控制器能够共享一条多点串行线路（RJ45 串口），且各自仅响应针对它的命令。这是控制器的“扩展协议”/多点寻址模式。默认值 `-1` 禁用该功能——控制器不属于链的一部分，并响应其端口上的每条命令。它保存至闪存，并在启动时锁存一次，因此更改仅在执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md) 后才生效。

## 工作原理

当 `ChainAddress` 不为 `-1` 时，串行总线上的每条命令必须以单个地址数字开头。控制器将该前导数字与它自身的 `ChainAddress` 进行比较：

| 前导地址 | 行为 |
|---|---|
| 等于本控制器的 `ChainAddress`（0–7） | 该命令针对本单元：剥离地址数字，命令的其余部分正常执行，并发送回复。 |
| 8（静默广播） | 链上的每个单元都执行该命令，但**没有**单元回复（避免共享总线上的回复冲突）。 |
| 任何其他有效地址（0–7） | 该命令针对其他单元，本单元忽略它。 |

地址之后的单独回车（无命令）被视为无操作的保活信号。因此有效范围为 `-1`（禁用）和 `0`–`8`，其中 `8` 保留为静默广播地址。实际使用的地址会通过标识数据回报。

寻址**仅适用于 RJ45 串口**。串行 mini-USB 端口没有地址前缀处理，因此无论 `ChainAddress` 设为何值，它始终响应不带地址数字的命令。当 `ChainAddress` 不为 `-1` 时，RJ45 端口在启动时以 RS-485 半双工链路方式启用：控制器仅在回复时驱动总线的发送使能（方向）线，其余时间则释放它。正是这种半双工方向切换，使多个单元能够共享一对双绞线而其发送器不会冲突。

由于地址仅在启动时读取，因此无法在运行中将控制器移动到新的链位置——必须执行 Save 和 Reset。

## 示例

```text
AChainAddress=1      ; this unit answers to address "1"; Save and Reset to apply
AChainAddress=-1     ; disable chain addressing (respond to all commands)
```

## 另请参阅

- [CANAddr](CANAddr.md) — CAN 基地址（CAN 总线寻址，与串行链独立）
- [RSBaud](RSBaud.md) — 链所使用的串口波特率
- [CANBaud](CANBaud.md) — CAN 总线波特率
