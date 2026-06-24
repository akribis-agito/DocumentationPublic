---
keyword: CiMuxDir
summary: 设置 Central-i 多路复用器的方向（共享总线路由到哪个端口）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 551
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
  - 4095
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CiMuxDir

设置 Central-i 多路复用器的方向（共享总线路由到哪个端口）。

## 概述

`CiMuxDir` 设置 Central-i I/O 多路复用器的**方向**，每个端口对应一位。Central-i 网络承载一路多路复用的 I/O 信号，该信号既可从主站流向远程单元，也可从远程单元流回主站；`CiMuxDir` 选择该信号在每个端口上的流向。它与 [CiMuxSel](CiMuxSel.md)（用于选择路由*哪个*信号）共同构成完整的多路复用器配置，使一个主站能在其各端口间共享一路被路由的 I/O 信号。这是一个保存至闪存的非轴参数。（此功能在支持它的主站硬件上实现。）

## 工作原理

`CiMuxDir` 是一个**位域**——位 `n` 即端口 `n` 的方向。写入该参数时，固件会：

1. 将逐端口选择值 [CiMuxSel](CiMuxSel.md)`[1]` 写入每个主站端口的多路复用器寄存器；
2. 对每个*已连接、非仿真*的端口，向远程单元发送一条离线（邮箱）消息，携带该端口的方向位以及远程端选择值 [CiMuxSel](CiMuxSel.md)`[2]`（二者在远程单元中共用一个 32 位寄存器）。方向语义在远程端被**反转**，使得一端驱动而另一端接收；
3. 将 `CiMuxDir` 写入主站自身的多路复用器方向寄存器，从而设置所有端口的主站端方向。

由于主站与远程单元的方向是在不同步骤中配置的，可能存在两端同时驱动该线路的短暂时刻；硬件收发器可容忍这一短暂重叠，直至主站端方向被设置完成。

12 位范围允许为硬件提供的每个端口设置一个方向位。

## 示例

```text
ACiMuxDir=1          ; route port 0 in one direction; other ports the other way
ACiMuxDir            ; read the current per-port direction bit field
```

## 参见

- [CiMuxSel](CiMuxSel.md) — 路由哪个信号（主站端与远程端选择）
- [CIConnect](CIConnect.md) — 端口必须已连接才能发送其远程方向
- [CIGlobalStat](CIGlobalStat.md) — 哪些端口已连接
