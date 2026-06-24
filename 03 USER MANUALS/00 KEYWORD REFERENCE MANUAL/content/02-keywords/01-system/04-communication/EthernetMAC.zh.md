---
keyword: EthernetMAC
summary: 控制器 MAC 地址，以十进制八位字节存储，每个数组元素存放一个。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 602
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 7
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EthernetMAC

控制器 MAC 地址，以十进制八位字节存储，每个数组元素存放一个。

## 概述

`EthernetMAC` 以六个**十进制**八位字节保存控制器的 MAC 地址，每个数组元素存放一个。（该数组的维度设定使可用索引从 `[1]` 开始；索引 `[0]` 不使用。）MAC 地址通常以十六进制书写，因此每对十六进制数字必须先转换为对应的十进制值再写入此处。同一网络上的每个控制器都必须具有唯一的 MAC 地址。它会保存至闪存并在启动时读取，因此请设置各八位字节，然后执行 [Save](../02-operation/Save.md) 和 [Reset](../02-operation/Reset.md) 以使其生效。

例如，占位地址 `AA:BB:CC:DD:EE:FF` 存储为：

| Element | Hex | Decimal |
|---------|-----|---------|
| EthernetMAC[1] | AA | 170 |
| EthernetMAC[2] | BB | 187 |
| EthernetMAC[3] | CC | 204 |
| EthernetMAC[4] | DD | 221 |
| EthernetMAC[5] | EE | 238 |
| EthernetMAC[6] | FF | 255 |

## 工作原理

固件读取这六个十进制八位字节，并将它们组装成网络接口对外通告的硬件 MAC 地址。要将一个十六进制八位字节转换为十进制，将第一个十六进制数字乘以 16 再加上第二个（例如 `CC` = 12 × 16 + 12 = 204）。

如果六个八位字节全部保持为 0（从未配置的状态），控制器会在启动时替换为一个内置的默认 MAC，使该单元仍拥有有效的硬件地址。在 standalone 控制器上该回退值为 `3E:30:6C:A2:45:5E`；在 Central-i 上为 `01:01:01:01:01:01`。由于该回退值对每个未配置单元都相同，请为同一网络上的每个控制器赋予唯一的 MAC，而不要依赖默认值。

## 示例

```text
AEthernetMAC[1]=170 ; first octet (AA in hex)
AEthernetMAC[3]     ; read the third octet (decimal)
```

## 参见

- [EthernetIP](EthernetIP.md) — IP 地址
- [EthernetPort](EthernetPort.md) — TCP 端口号
