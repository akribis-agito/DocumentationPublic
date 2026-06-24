---
keyword: EthernetPort
summary: 用于以太网通信的 TCP 端口。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 601
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
  - 65535
  default: 50000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EthernetPort

用于以太网通信的 TCP 端口。

## 概述

`EthernetPort` 定义控制器接受以太网连接所使用的 TCP 端口号。该字段接受完整 TCP 端口范围（0–65535）内的任意值，默认值为 **50000**。它会保存至闪存并在启动时读取，因此更改需要执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md)。

该值的使用方式取决于平台：

- **Standalone 控制器**在所配置的端口上侦听主连接（“all-to-default”恢复 DIP 设置会强制使用端口 50000，而不论存储的值如何）。
- **Central-i 控制器**在固定端口（50000）上接受主连接，并在身份信息中报告所配置的 `EthernetPort` 值，而不是将其用作侦听端口。

在正常使用中，此关键字保持其默认值 50000。

## 示例

```text
AEthernetPort       ; read the configured port
AEthernetPort=50000 ; set the TCP port (default), then Save and Reset
```

## 参见

- [EthernetIP](EthernetIP.md) — IP 地址
- [EthernetMAC](EthernetMAC.md) — MAC 地址
