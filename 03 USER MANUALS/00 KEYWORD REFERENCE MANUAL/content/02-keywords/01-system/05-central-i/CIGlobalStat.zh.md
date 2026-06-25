---
keyword: CIGlobalStat
summary: 编码所有 Central-i 端口连接状态的只读寄存器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 510
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
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
# CIGlobalStat

编码所有 Central-i 端口连接状态的只读寄存器。

## 概述

`CIGlobalStat` 是一个只读、非轴寄存器，在一个值中汇总每个 Central-i 端口的连接状态，以便上位机无需在每个轴上读取 [CIStatus](CIStatus.md) 即可轮询系统级状态。每个端口占用**两位**，按端口号打包：

- 该对中的**低**（偶数）位在端口已连接时置位；
- 该对中的**高**（奇数）位在该轴处于*仿真*模式时置位（[MotorType](../../02-motor-and-amplifier/MotorType.md) 设置为仿真，值为 5）。

## 工作原理

对于端口 `n`（从 0 开始计数），已连接位为位 `2n`，仿真位为位 `2n+1`：

| Port | Connected bit | Simulation bit | Connected mask |
|------|---------------|----------------|----------------|
| 0 | 0 | 1 | 0x00000001 |
| 1 | 2 | 3 | 0x00000004 |
| 2 | 4 | 5 | 0x00000010 |
| 3 | 6 | 7 | 0x00000040 |
| n | 2n | 2n+1 | `1 << (2n)` |

主控制器最多支持 12 个 Central-i 端口（端口索引 0-11；较小的产品暴露的端口较少），因此最多只有低 24 位有意义——端口 11 使用已连接位 22 和仿真位 23。其余高位始终为 0，因此上位机只需扫描到其产品端口数量为止的位对即可。

固件在端口达到同步状态时（通过 [CIConnect](CIConnect.md) 或 [CIAutoConnect](CIAutoConnect.md)）设置已连接位，并在复位/[CIDisconnect](CIDisconnect.md) 时清除它。仿真位独立受控：当该轴的 [MotorType](../../02-motor-and-amplifier/MotorType.md) 设置为仿真（值 5）时置位，否则清除；它在写入 `MotorType` 时更新，且不依赖于 [CIConnect](CIConnect.md)/[CIDisconnect](CIDisconnect.md)。位对读取为 `01`（二进制）的端口是活动链路；`11` 是已连接的仿真轴；`00` 是已断开。

要测试单个端口，请用其已连接位进行掩码——例如，当 `(CIGlobalStat & 0x4)` 非零时，端口 1 已连接。

## 示例

```text
ACIGlobalStat       ; system-wide Central-i connection state
```

在用户程序中，通过用 `0x1` 掩码检查端口 0 是否已连接，通过用 `0x2` 掩码检查它是否为仿真。

## 另请参阅

- [CIStatus](CIStatus.md) — 详细的每轴链路状态和错误码
- [CIConnect](CIConnect.md) / [CIDisconnect](CIDisconnect.md) — 设置/清除已连接位
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 值 5（仿真）驱动每端口仿真位
