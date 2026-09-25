# Push Events

**概述：**

推送事件使控制器能够在某件事发生时**主动**通知上位机，而无需上位机通过轮询去发现。轮询会占用链路带宽和两端的 CPU，最多会滞后一个轮询周期，并且可能漏掉在两次轮询之间开始并结束的事件。推送的事件自带时间戳，该时间戳在检测到事件时于控制中断中获取。

事件通过控制器的**推送套接字**（TCP 端口 **50010**）传输，该连接同时承载用户程序 `printf` 的输出。由上位机发起连接，控制器只在该连接上发送数据。每个数据包都标记为推送事件数据（`SOURCE = 2`），因此同一个读取端可以将事件与 `printf` 文本区分开。

## 事件类型

本固件定义了一种事件类型。

| 类型 | 名称 | 作用范围 | 发送时机 | data1 | data2 | data3 | data4、data5 |
|---|---|---|---|---|---|---|---|
| `1` | Profile ended（曲线结束） | 轴 | 该轴 [MotionStat](../../10-motion/05-motion-status/MotionStat.md) 的运动中（in-motion）标志位由 1 变为 0 | 位置（[Pos](../../10-motion/01-kinematics-status/Pos.md)） | 位置误差（[PosErr](../../10-motion/01-kinematics-status/PosErr.md)） | [MotionReason](../../10-motion/05-motion-status/MotionReason.md) | `0` |

**Profile ended 标志的是指令轨迹的结束，而不是位置已稳定。** 当控制器停止对该运动发出指令时即发送该事件，无论运动是正常完成、被停止或中止，还是触发了限位；data3（`MotionReason`）说明是哪一种情况。此时轴可能仍在稳定过程中。如果必须在轴实际到达目标后才执行操作，请改为等待 [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md)。

事件按**边沿**检测，因此一次运动结束只产生一条记录。位置和位置误差以控制器的内部值（主编码器计数）发送，不换算为用户单位。

## 关键字一览

| 关键字 | 作用 |
|---|---|
| [PushEvEnable](PushEvEnable.md) | 总开关。任何 0 与 1 之间的切换都会清空事件队列 |
| [PushEvSelect](PushEvSelect.md) | 按轴设置的待发送事件类型掩码 |
| [PushEvSelSys](PushEvSelSys.md) | 控制器级事件类型的掩码（目前尚未定义此类类型） |
| [PushEvFlushMs](PushEvFlushMs.md) | 已入队事件在发送前的最长等待时间 |
| [PushEvFillPct](PushEvFillPct.md) | 强制发送的队列填充程度 |
| [PushEvStat](PushEvStat.md) | 事件队列中的空闲行数（只读） |
| [PushEvLost](PushEvLost.md) | 自上次发送数据包以来丢弃的事件数 |
| [PushEvTotLost](PushEvTotLost.md) | 自上电以来丢弃的事件总数 |

## 快速入门

```text
APushEvSelect[1]=1   ; axis A: send type 1 (Profile ended)
BPushEvSelect[1]=1   ; axis B: the same
APushEvEnable=1      ; start detecting and sending events
```

上位机可在开启之前或之后连接端口 50010。`PushEvSelect`、`PushEvSelSys`、`PushEvFlushMs` 和 `PushEvFillPct` 可通过 [Save](../02-operation/Save.md) 保存至闪存。`PushEvEnable` 不保存至闪存，因此上电后推送事件始终处于关闭状态，直到上位机将其开启。

## 工作原理

1. **检测。** 在每个控制周期中，控制器针对每个轴检查所选的事件类型。检测到的事件连同时间戳一起，作为一条固定大小的记录写入容量为 **64 行**的事件队列。此时不进行任何格式化或发送。
2. **发送。** 当任一触发条件满足时，控制器的后台循环发送队列：自上次成功发送以来已超过 [PushEvFlushMs](PushEvFlushMs.md)，或队列已至少达到 [PushEvFillPct](PushEvFillPct.md) 百分比的填充程度。每个后台轮次最多发送一个数据包，每包最多 28 个事件，按从旧到新的顺序发送。
3. **移除。** 只有在数据包成功发送之后，事件才会从队列中移除。如果发送失败（例如没有上位机连接），事件保留在队列中，控制器在下一轮次重试。

检测与连接状态无关。没有上位机连接时，事件仍会继续入队。队列已满时，每个**新**事件都会被丢弃，并计入 [PushEvLost](PushEvLost.md) 和 [PushEvTotLost](PushEvTotLost.md)；因此，在无人读取期间被填满的队列中保存的是**最早**的 64 个事件，而不是最近的 64 个。若要以空队列开始一次会话，请先写入 `PushEvEnable=0`，再写入 `PushEvEnable=1`。

当推送事件数据包和 `printf` 数据包同时就绪时，先发送事件数据包，`printf` 等待之后的轮次。`PushEvFlushMs` 和 `PushEvFillPct` 仅作用于事件；`printf` 输出保持其自身固定的发送时序。

> **连接推送端口的上位机必须持续读取。** 推送事件与 `printf` 使用相同的阻塞式发送。如果上位机已连接端口 50010 但停止读取，每次发送尝试都可能使控制器的后台循环停顿约 5 至 6 秒，在此期间控制器不执行来自上位机的关键字命令，包括关闭推送事件的命令。发送失败后会在下一轮次重试，而如果同一轮次中还有 `printf` 输出在等待，还可能再进行一次发送尝试，因此一个轮次最长可能停顿约 12 秒。如果一个轮次停顿超过 10 秒，后台看门狗将关闭所有电机，并报告 CPU 后台看门狗控制器故障。这些时间是根据固件设计推导得出的，尚未在硬件上实测。请勿让客户端连接端口 50010 却不读取。

## 数据包格式

大多数用户通过上位机软件读取事件。以下格式供编写自有客户端时参考。所有多字节值均为小端序且紧密排列，无填充。

```text
"1.2,1."          ASCII envelope: push version 1, SOURCE 2 (push events), data version 1
header   7 bytes
record  50 bytes  × n
'>' CR            terminator (0x3E 0x0D)
```

包头：

| 偏移 | 字段 | 类型 | 含义 |
|---|---|---|---|
| 0 | n | uint8 | 本数据包中的记录数（1-28） |
| 1 | missed | uint16 | 自上次成功发送以来丢弃的事件数；即构建数据包时 [PushEvLost](PushEvLost.md) 的值，上限为 65535 |
| 3 | freeRows | uint16 | 构建数据包时（这些记录被移除之前）队列的空闲行数（参见 [PushEvStat](PushEvStat.md)） |
| 5 | reserved | uint16 | 始终为 `0` |

记录：

| 偏移 | 字段 | 类型 | 含义 |
|---|---|---|---|
| 0 | type | uint8 | 事件类型（参见*事件类型*）。类型 `0` 从不发送 |
| 1 | axis | uint8 | 事件所属的轴（`0` = A，`1` = B，…），控制器级事件为 `0xFF` |
| 2 | timeSec | uint32 | 检测到事件时自上电以来的整秒数（即 [Time](../03-timing/Time.md) 的值） |
| 6 | timeTick | uint32 | 在该秒内的位置，单位为 1/16384 秒。以 16 为步长递增（约 1 ms） |
| 10 | data1 | double | 取决于类型 |
| 18 | data2 | double | 取决于类型 |
| 26 | data3 | double | 取决于类型 |
| 34 | data4 | double | 取决于类型 |
| 42 | data5 | double | 取决于类型 |

DATA 部分的长度始终为 `7 + 50 × n` 字节，因此客户端可以通过算术校验数据包。事件时间为 `timeSec + timeTick / 16384` 秒。某类型未使用的数据字段以 `0.0` 发送。

如果某次发送因上位机停止读取而超时，控制器会重试发送相同的事件，但先前那次尝试的部分或全部数据在上位机恢复读取后仍可能到达。因此，在发生此类停顿之后，客户端应预期某个数据包可能被重复接收，或数据流中出现一段不完整的数据包。请丢弃重复的记录（type、axis、`timeSec` 和 `timeTick` 均相同），如需重新同步，请查找下一个包封（`1.<SOURCE>,<version>.`；`SOURCE = 1` 的 `printf` 数据包共用同一数据流），并用 `n` 和 `7 + 50 × n` 的长度加以确认。

## 产品适用性

推送事件仅存在于 **AGM800**（Central-i 主控制器，v5）上。在其他所有产品上，以及在早于推送事件的 AGM800 固件上，这八个 `PushEv*` 关键字**不存在**：按名称读取或写入它们会返回未知关键字错误。因此，上位机可以通过尝试读取 `PushEvEnable` 来检测是否支持该功能。也可以检查 [Identity](../01-status/Identity.md)`[62]` 的 `0x40` 位，固件支持推送事件时该位置位。`Identity[75]` 报告事件队列深度（64）。

推送事件与[事件生成](../../18-event-generation/00-overview.md)是两回事，后者在硬件中产生与位置同步的输出脉冲。如果需要在轴经过某一位置的确切时刻输出信号，请使用事件生成。推送事件则通过以太网向上位机报告。
