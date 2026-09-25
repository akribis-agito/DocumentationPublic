---
keyword: ECATDrvReset
summary: 请求 EtherCAT 通信模块复位驱动器的命令。
availability:
  standalone:
  - v5
  central-i: []
can_code: 888
attributes:
  access: ro
  scope: non-axis
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
last_updated: '2026-08-16'
doc_revision: '2026.08'
language: zh-CN
---
# ECATDrvReset

请求 EtherCAT 通信模块复位驱动器的命令。

## 概述

`ECATDrvReset` 是一条**命令**（不带数值）。执行该命令时，控制器通过内部链路向
EtherCAT 通信模块发送复位请求，由该模块执行复位；请求交出后控制器即刻回复。

> **仅限 EtherCAT 型号。** 该关键字仅存在于带 EtherCAT 硬件的控制器上。在其他型号
> 上未实现，将返回未知关键字错误。

[Reset](Reset.md) 重启的是控制器自身的固件，而 `ECATDrvReset` 作用于 EtherCAT
一侧。当需要在不重启控制器的情况下把现场总线接口恢复到已知状态时，使用该命令。

## 工作原理

1. 控制器将复位请求写入与 EtherCAT 模块通信所用的共享消息区。
2. 该模块执行复位。
3. 请求交出后，控制器回复 **OK**。

该回复仅确认请求已*发出*，并不表示驱动器已完成复位或已重新加入现场总线。请通过
主站查询 EtherCAT 状态以确认结果。

该命令在电机使能以及轴运动过程中均可接受。但它本身不会停止运动——在运动过程中复位
现场总线接口会中断周期性通信，因此除非确有意断开周期性链路，否则请先使轴停止。

## 另请参阅

- [Reset](Reset.md) — 重启控制器固件
- [DownloadFW](DownloadFW.md) — 固件更新，会重启单元
