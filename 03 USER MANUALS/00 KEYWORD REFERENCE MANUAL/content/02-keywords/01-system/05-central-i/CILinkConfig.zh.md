---
keyword: CILinkConfig
summary: 配置 Central-i 端口物理和协议参数的每轴数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 539
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CILinkConfig

配置 Central-i 端口物理和协议参数的每轴数组。

## 概述

`CILinkConfig` 是一个轴相关数组，用于设置 Central-i 端口的**帧时序**：在每个通信周期内主控制器向远程发送以及接收回复的时间点，涵盖周期性*同步*流量和*离线*（邮箱）流量两者。这些值是从周期开始处测量的时钟计数。它们保存至闪存，并在 [CIConnect](CIConnect.md)（或 [CIAutoConnect](CIAutoConnect.md)）初始化链路时写入端口的硬件时序寄存器，因此请在连接之前进行配置。索引 `[0]` 未使用；六个时序元素从 `[1]` 到 `[6]`。

## 工作原理

每个通信周期具有固定的周期长度。在其内部，主控制器必须打开其发送窗口，然后将线路调转方向以接收远程的回复，先为同步（每周期）通道执行，再为离线（邮箱）通道执行。这六个元素是这些窗口的时钟偏移：

| Index | Element | Meaning |
|-------|---------|---------|
| [1] | Sync send-start | 主控制器开始发送同步（主到远程）帧的时间 |
| [2] | Sync receive-start | 主控制器打开窗口以接收远程到主的同步帧的时间 |
| [3] | Sync receive-end | 主控制器关闭同步接收窗口（线路调转）的时间 |
| [4] | Offline send-start | 主控制器开始发送离线（邮箱）消息的时间 |
| [5] | Offline receive-start | 主控制器打开窗口以接收离线回复的时间 |
| [6] | Offline receive-end | 主控制器关闭离线接收窗口的时间 |

任何保持为 `0` 的元素会在上电时被固件针对该时序的内置默认值替换：在参数初始化期间，固件用其默认值覆盖每个为零的元素，并将该值存回数组，因此一个 `CILinkConfig` 全部加载为零的端口会以合理的默认值启动，且随后的读取返回默认值而非 `0`。（在上电后你写入 `0` 的值在下一次上电之前不会重新默认化，并会作为 `0` 应用。）这些值必须在周期内保持一致的顺序（发送先于接收开始，接收开始先于接收结束）；不正确的时序会在 [CIStatus](CIStatus.md) 中表现为同步或离线错误。

通道比特率本身由固件在连接时设置为其默认值（它不是这些元素之一）；这些元素调整每次传输在周期内*何时*发生，这取决于电缆长度和远程设备。

## 示例

```text
ACILinkConfig[1]    ; read the sync send-start time for this port
ACILinkConfig[4]    ; read the offline send-start time for this port
```

## 另请参阅

- [CIDeviceType](CIDeviceType.md) — 端口的期望设备类别
- [CIConnect](CIConnect.md) — 链路建立时应用这些时序
- [CIStatus](CIStatus.md) — 时序不当导致的同步/离线错误
- [CISyncDef](CISyncDef.md) — 同步数据定义
