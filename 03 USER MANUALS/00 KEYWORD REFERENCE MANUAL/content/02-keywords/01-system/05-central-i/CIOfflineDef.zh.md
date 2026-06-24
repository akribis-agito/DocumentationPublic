---
keyword: CIOfflineDef
summary: 定义哪些参数纳入 Central-i 离线数据集的轴级数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 507
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CIOfflineDef

定义哪些参数纳入 Central-i 离线数据集的轴级数组。

## 概述

`CIOfflineDef` 是一个轴级数组，用于为某个端口配置 Central-i **离线通道**——即用于对远程单元寄存器进行带地址读写的非周期信箱通道（这些事务由 [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md) 承载）。它是 [CISyncDef](CISyncDef.md) 的离线对应项，后者配置的是实时的、每周期的同步通道。该定义会保存至闪存。索引 `[0]` 未使用；配置字段为 `[1]` 和 `[2]`。

## 工作原理

| 索引 | 字段 | 含义 |
|-------|-------|---------|
| [1] | 频率 | 离线通道频率设置 |
| [2] | 滤波器长度 | 离线通道滤波器长度 |

这些元素用于参数化该端口离线通道的运行方式。每次事务的内容（读什么或写什么，以及回复）并不保存在此处——它们存放于 [CIOfflineData](CIOfflineData.md) 中；`CIOfflineDef` 仅承载通道级的定义。

> 注：在所检查的固件中，这两个配置字段虽已定义并存储，但活动的离线消息代码路径并不使用它们，该路径在 [CIConnect](CIConnect.md) 期间使用固定的信箱尺寸。请将这些字段视为通道定义；每条消息的行为由 [CIOfflineData](CIOfflineData.md) 驱动。

## 示例

```text
ACIOfflineDef[1]    ; read the offline-channel frequency setting
ACIOfflineDef[2]    ; read the offline-channel filter length
```

## 另请参阅

- [CIOfflineData](CIOfflineData.md) — 每次事务的请求/响应缓冲区
- [CIOfflineSend](CIOfflineSend.md) — 发送一次离线事务
- [CISyncDef](CISyncDef.md) — 同步（实时链路）通道定义
