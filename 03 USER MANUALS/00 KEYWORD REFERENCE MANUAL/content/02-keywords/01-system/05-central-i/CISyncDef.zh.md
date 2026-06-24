---
keyword: CISyncDef
summary: 逐轴数组，定义每个控制周期同步交换的参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 506
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
# CISyncDef

逐轴数组，定义每个控制周期同步交换的参数。

## 概述

`CISyncDef` 是一个逐轴数组，用于定义某个端口的 Central-i **同步通道**——即主站与远程单元每个控制周期交换的周期性、固定格式数据（向远程单元输出电流指令与控制位；返回编码器位置、电流、状态以及数字量/模拟量输入）。它是 [CIOfflineDef](CIOfflineDef.md) 的同步对应物，后者用于配置偶发的离线（邮箱）通道。该定义保存至闪存，并设计为在 [CIConnect](CIConnect.md) 建立链路时生效。索引 `[0]` 未使用；该定义占用 `[1]` 与 `[2]`。

## 工作原理

每类设备（驱动器或 I/O 单元）的同步报文布局由 Central-i 协议固定：主站在每个周期内发送主站到远程的帧并接收远程到主站的帧，帧字段与长度由所连接的设备类型决定。`CISyncDef` 保存逐端口的同步通道定义；实时帧内容由固件在控制中断中根据 [CIIdentity](CIIdentity.md) 报告的设备类别自动填入。

> 注意：在所检查的固件中，每周期同步帧布局是根据所连接的设备类别选择的，而非根据这两个数组元素——活动的同步代码并不读取 `CISyncDef`。该数组按端口定义并存储为同步通道定义；请在 [CILinkConfig](CILinkConfig.md) 中配置链路时序，在 [CIDeviceType](CIDeviceType.md) 中配置设备类别，以控制同步交换。

## 示例

```text
ACISyncDef[1]       ; read the first synchronous-channel definition element
ACISyncDef[2]       ; read the second synchronous-channel definition element
```

## 参见

- [CILinkConfig](CILinkConfig.md) — 同步（及离线）通道的帧时序
- [CIDeviceType](CIDeviceType.md) — 固定同步帧布局的设备类别
- [CIOfflineDef](CIOfflineDef.md) — 离线通道定义
- [CIConnect](CIConnect.md) — 发起链路
