---
keyword: CIDisconnect
summary: 终止所选轴端口上活动的 Central-i 链路的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 505
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CIDisconnect

终止所选轴端口上活动的 Central-i 链路的命令。

## 概述

`CIDisconnect` 终止所选轴端口上活动的 Central-i 链路。运行后，该端口停止周期实时数据交换，并保持断开状态，直到后续发出 [CIConnect](CIConnect.md)。它是一个函数关键字（无值），且在电机使能或运动中时无法运行。

## 工作原理

`CIDisconnect` 将端口的连接状态机移入断开状态（固件由此拆除链路），并立即清除该端口的每轴状态数组和身份数组：

- [CIStatus](CIStatus.md) 报告的每个元素均被清零，因此状态机读取为 `0`（已禁用），错误计数器复位；
- [CIIdentity](CIIdentity.md) 的每个元素均被清零，因为先前已连接设备的身份不再有效；
- 断开完成后，[CIGlobalStat](CIGlobalStat.md) 中该端口的已连接位被清除。

请注意，在端口已连接时无法更改 [CIDeviceType](CIDeviceType.md)（或 `AmpType`）——此类更改会被拒绝并返回错误 214。请先发出 `CIDisconnect`，然后更改值并重新连接。如果先前连接保存的设备类型与（现已断开的）端口不再匹配，固件会在下一次写入时自动清除残留的状态和身份。

## 示例

```text
ACIDisconnect        ; tear down the Central-i link on the selected axis
ACIStatus[1]         ; reads 0 (disabled) after the disconnect completes
```

## 另请参阅

- [CIConnect](CIConnect.md) — 发起链路
- [CIAutoConnect](CIAutoConnect.md) — 上电时自动连接
- [CIStatus](CIStatus.md) — 链路状态（被此命令清除）
- [CIIdentity](CIIdentity.md) — 设备身份（被此命令清除）
- [CIGlobalStat](CIGlobalStat.md) — 系统级连接汇总
