---
keyword: EthernetIP
summary: 控制器 IP 地址，每个数组元素存储一个字节。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 600
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EthernetIP

控制器 IP 地址，每个数组元素存储一个字节。

## 概述

`EthernetIP` 将控制器的 IPv4 地址保存为四个字节，每个数组元素存储一个，各自取值范围为 0–255。（数组的维数使得可用索引从 `[1]` 开始；索引 `[0]` 不使用。）元素 `[1]` 是最高有效字节，`[4]` 是最低有效字节。它保存至闪存并在启动时读取，因此设置各字节后需执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md)，新地址才能生效。

例如，地址 `192.168.0.10` 存储为：

| 元素 | 值 |
|---------|-------|
| EthernetIP[1] | 192 |
| EthernetIP[2] | 168 |
| EthernetIP[3] | 0 |
| EthernetIP[4] | 10 |

## 工作原理

以太网启动时，固件将四个字节重新组装为网络协议栈使用的点分四段地址。在保存前设置全部四个元素以定义有效地址；地址写入不完整（某些字节仍保留先前的值）将产生非预期的地址。

如果四个字节全部保持为 0（从未配置的状态），控制器会回退到内置的默认地址 `172.1.1.101`，因此出厂状态的控制器在网络上仍可访问。

控制器的硬件地址 DIP 设置会被加到形成地址时的最后一个字节上。在独立控制器上，该偏移应用于活动地址（`EthernetIP[4]` + DIP 地址），因此同一子网上多个相同单元会获得不同的地址。在 Central-i 上，控制器按所写入的存储字节进行应答；DIP 偏移仅反映在回报的（标识）地址中。

## 示例

```text
AEthernetIP[1]=192
AEthernetIP[2]=168
AEthernetIP[3]=0
AEthernetIP[4]=10    ; sets 192.168.0.10 (Save + Reset to apply)
AEthernetIP[1]       ; read the most significant octet
```

## 参见

- [EthernetPort](EthernetPort.md) — TCP 端口号
- [EthernetMAC](EthernetMAC.md) — MAC 地址
