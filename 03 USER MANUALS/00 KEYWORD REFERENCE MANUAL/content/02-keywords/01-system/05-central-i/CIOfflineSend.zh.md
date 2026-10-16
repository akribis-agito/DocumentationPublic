---
keyword: CIOfflineSend
summary: 在所选轴端口上发送 Central-i 离线数据包的命令。
availability:
  standalone:
  - v4
  central-i: []
can_code: 502
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
removed_in:
- v5
last_updated: '2026-10-16'
doc_revision: '2026.10'
language: zh-CN
---
# CIOfflineSend

在所选轴端口上发送 Central-i 离线数据包的命令。

## 概述

`CIOfflineSend` 在所选轴端口上执行一次 Central-i **离线**事务：它将由 [CIOfflineData](CIOfflineData.md) 构建的带地址信箱消息发送给所连接的远程单元，等待回复，并将结果写回 [CIOfflineData](CIOfflineData.md)。这是上位机在周期性同步数据交换之外，直接读取或写入远程单元内某个寄存器的方式。它是一个函数关键字（无值）。

## 使用信箱队列的 AGM800 与 AGM800-EC

本节适用于包含信箱 2 队列的固件。较早固件的行为见下方旧实现说明。命令仍为同步调用：只有自己的请求完成或失败后才返回。

- 端口必须已连接。未连接时返回错误 `159`，不发送请求。
- 固件复制请求，并将其加入每端口有界 FIFO，与内部信箱 2 请求共用该队列。队列满时返回通信错误 `151`；已接受请求保持入队顺序。
- 查询成功后更新 `CIOfflineData[4]`；失败时保留该值。应同时检查命令回复与 `CIOfflineData[5]`：零表示成功，非零表示远程拒绝或本地固件错误。
- 超时、CRC 错误或无效回复会停止该端口后续离线发送。后续命令返回 `151`，不会把先前请求的迟到回复当作本次结果。执行 `CIDisconnect`，再执行 `CIConnect` 以恢复；固件会先排空旧信箱，再重新识别远程单元。失败的写操作不会自动重发。
- 已接受的事务在最终完成时写入 `OfflineBLog`，包括最终失败的事务。入队前被拒绝的请求不代表一次实际传输。

信箱 1 仍专用于位置锁存与事件通道。队列由前台服务，中断中的电机控制不会等待离线回复。

## 旧实现

`CIOfflineSend` 使用端口的**第二个**离线信箱（上位机通道），将第一个信箱留给固件自身的后台通信。被调用时它会：

1. 检查信箱是否空闲（既未在发送，也未持有未读回复）。
2. 由 [CIOfflineData](CIOfflineData.md) 构建外发消息：消息类型（[1]，查询或赋值）、opcode/寄存器地址（[2]），以及——对于赋值——待写入的值（[3]）。
3. 将消息写入信箱，从而触发向远程的发送。
4. 等待（最长至超时）回复。成功时它将返回值存入 [CIOfflineData](CIOfflineData.md)`[4]`（用于查询），将确认/错误码存入 `[5]`；超时或非确认回复则报告通信错误。出现任何通信错误时，它还会递增端口的离线错误计数 [CIStatus](CIStatus.md)`[3]`，将时间记录到 [CIStatus](CIStatus.md)`[5]`，并将最后错误码 [CIStatus](CIStatus.md)`[6]` 置为 `5`（离线消息错误）。
5. 将整个交换过程——发送方、类型、opcode、外发值、传入值、确认/错误、时间、采样计数器和端口——记录到 port-B 离线日志 [OfflineBLog](OfflineBLog.md) 中。

由于期望收到回复，发送之前端口应处于已连接状态（[CIStatus](CIStatus.md) 显示已连接）。

## 示例

```text
ACIOfflineData[1]=0   ; query
ACIOfflineData[2]=...  ; remote register address
ACIOfflineSend         ; run the transaction
ACIOfflineData[4]      ; value returned by the remote
```

## 边界情况

以下边界情况描述未使用信箱队列的较早固件。

- **端口断开。** `CIOfflineSend` 不以连接状态为前提，因此可在断开的端口上发出。若无远程响应，事务只是以通信超时结束：命令报告通信错误，确认字段 [CIOfflineData](CIOfflineData.md)`[5]` 保持为 `0`，故障记录在 [CIStatus](CIStatus.md) 的离线错误计数器中（`[3]`/`[5]`/`[6]`，码 `5`）。若远程作出回复但拒绝该请求，则会在 [CIOfflineData](CIOfflineData.md)`[5]` 中返回其错误码。
- **电机使能 / 运动中。** 该命令在电机使能或运动时均允许执行——离线信箱独立于控制环。回复仍会在同一周期窗口内到达 [CIOfflineData](CIOfflineData.md)。
- **上电。** 离线通道只有在 [CIConnect](CIConnect.md)（或 [CIAutoConnect](CIAutoConnect.md)）使端口上线之后才可用；在此之前无可寻址的远程，调用将超时。
- **仿真设备。** 当 [CIDeviceType](CIDeviceType.md) 设为仿真类时，端口被标记为已连接但并无真实远程——`CIOfflineSend` 将超时，仿真端口路径意在供上位机工具使用，而非用于真实寄存器访问。
- **独立式（v4）。** 在独立式 v4 以及 central-i v4/v5 上均可用；该事务跨链路面向远程上的一个寄存器。

## 版本间差异

该事务在 v4 与 v5 中均存在且行为相同：它不以连接状态为前提，且回复必须在超时内返回方可成功。[CIOfflineData](CIOfflineData.md) 中的请求/响应字段布局以及向 [OfflineBLog](OfflineBLog.md) 的记录在两个版本之间保持不变。

> **Frontmatter 标志。** 生成器填充的 frontmatter 将此关键字列为 `removed_in: v5` 且 central-i 可用性为空。该事务本身在 v5 中**并未**被移除——v5 固件仍定义并运行它（CAN 码 502，行为相同）。该 frontmatter 条目是一个分类层面的产物，而非真正的移除；下文正文描述的是实际的 v5 行为。

## 另请参阅

- [CIOfflineData](CIOfflineData.md) — 此命令所发送的请求/响应缓冲区
- [CIOfflineDef](CIOfflineDef.md) — 离线通道定义
- [OfflineBLog](OfflineBLog.md) — 此命令所发送事务的日志
- [CIConnect](CIConnect.md) — 发送前先使链路上线
