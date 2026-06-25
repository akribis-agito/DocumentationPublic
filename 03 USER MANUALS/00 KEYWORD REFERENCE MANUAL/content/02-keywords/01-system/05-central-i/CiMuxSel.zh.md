---
keyword: CiMuxSel
summary: 逐轴数组，选择通过 Central-i 多路复用器路由的物理端口。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 552
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CiMuxSel

逐轴数组，选择通过 Central-i 多路复用器路由的物理端口。

## 概述

`CiMuxSel` 是一个逐轴（逐端口）数组，用于选择 Central-i I/O 多路复用器在该端口上路由**哪个信号**——主站端与远程端可分别独立选择。它是多路复用器的“什么”；[CiMuxDir](CiMuxDir.md) 则是“哪个方向”。二者共同使一个主站能在其各端口间共享一路被路由的 I/O 信号。该数组保存至闪存。索引 `[0]` 未使用；两个选择元素为 `[1]` 与 `[2]`。

## 工作原理

| 索引 | 元素 | 含义 |
|-------|---------|---------|
| [1] | 主站端选择 | 写入此端口在主站 FPGA 中的多路复用器寄存器 |
| [2] | 远程端选择 | 发送至远程单元（与 [CiMuxDir](CiMuxDir.md) 方向位组合）并写入远程单元的多路复用器寄存器 |

当写入 [CiMuxDir](CiMuxDir.md) 时（它驱动多路复用器更新），固件会将每个端口的 `CiMuxSel[1]` 写入主站的端口多路复用器寄存器，并对每个*已连接、非仿真*的端口，在携带方向位的同一条离线消息中将 `CiMuxSel[2]` 发送至远程单元（远程单元将选择与方向存储在单个 32 位寄存器中）。单独写入 `CiMuxSel` 仅更新所存储的值；配置会在设置 [CiMuxDir](CiMuxDir.md) 时推送至硬件。

## 示例

```text
ACiMuxSel[1]        ; read the master-side multiplexer select for this port
ACiMuxSel[2]        ; read the remote-side multiplexer select for this port
```

## 另请参阅

- [CiMuxDir](CiMuxDir.md) — 多路复用器方向（触发硬件更新）
- [CIConnect](CIConnect.md) — 端口必须已连接才能发送其远程选择
- [CIGlobalStat](CIGlobalStat.md) — 哪些端口已连接
