---
keyword: CIDeviceType
summary: 选择某轴上 Central-i 端口的角色/类别。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 503
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CIDeviceType

选择某轴上 Central-i 端口的角色/类别。

## 概述

`CIDeviceType` 声明主机期望在本轴 Central-i 端口上找到的远程设备类别 —— 驱动器、I/O 单元，或两者之一的*仿真*版本。它是轴相关参数并保存至闪存。它决定端口如何连接（真实链路或仿真），以及当 [CIConnect](CIConnect.md) 运行时主机要校验什么：如果实际存在的设备与所声明的类别不符，连接将以设备类型错误失败。请在连接之前将其与 [CILinkConfig](CILinkConfig.md) 一同配置。

## 工作原理

该值是一个分为两个 16 位字段的 32 位字：

| Bits | 字段 | 含义 |
|------|-------|---------|
| 15–0 | 设备类别 | 远程单元的种类（驱动器 / I/O / 仿真）—— 参见类别表 |
| 31–16 | 设备子类型 | 该类别内的具体设备变体 |

### 设备类别（低 16 位）

| Value | 类别 | 备注 |
|-------|-------|-------|
| 0x1 | 驱动器 | 真实远程驱动器（驱动电机） |
| 0x2 | I/O 单元 | 真实远程 I/O 单元 |
| 0x3 | 仿真驱动器 | 无物理链路；端口以默认通道计数标记为已连接 |
| 0x4 | 仿真 I/O 单元 | 同上，针对 I/O 单元 |

（v5 固件新增了一个真实设备类别 —— 参见 *版本间变更*。）

子类型字段标识该类别内的具体产品变体（不同的驱动器型号、适配器/直线远程变体，或 I/O 单元型号）。具体的子类型代码与设备相关；主机仅用它们来应用正确的通道大小与限值，并确认已连接的单元就是所声明的那一个。

### 连接时及更改时的行为

- 在 [CIConnect](CIConnect.md) 期间，主机读取远程单元报告的类别/子类型并与 `CIDeviceType` 比较。真实驱动器类别还要求轴的 `AmpType` 为兼容的驱动模式（驱动器为内置 PWM，适配器为模拟）；不匹配会以错误终止连接（参见 [CIStatus](CIStatus.md) 错误码）。
- 在无法驱动电机的端口上设置**驱动器**类别会被 [CIConnect](CIConnect.md) 拒绝。
- **仿真**类别会使 [CIConnect](CIConnect.md) 和 [CIAutoConnect](CIAutoConnect.md) 立即将端口标记为已连接并以默认计数填充 [CIIdentity](CIIdentity.md)，而不运行物理链路序列。
- 当端口处于**已连接**状态时，写入与当前值不同的 `CIDeviceType` 值会**被拒绝**，返回错误 214（"Changing the value of CIDeviceType or AmpType is not allowed while the Central-i communication with the port is active"）。请先发出 [CIDisconnect](CIDisconnect.md)，再更改该值，然后重新连接。（同一规则适用于 `AmpType`。）当端口*未*连接时，写入成功，并且先前连接的不同类型设备遗留的任何残留 [CIStatus](CIStatus.md)/[CIIdentity](CIIdentity.md) 会被自动清除。
- 上电默认值为 `0x00010001` —— 真实驱动器（类别 0x1），子类型 1。在多端口主机上，仅低位端口可驱动电机；在仅 I/O 端口上声明驱动器类别会被 [CIConnect](CIConnect.md) 以错误 170（"Can't connect an amplifier to this port"）拒绝。

## 示例

```text
ACIDeviceType        ; query the configured device class/sub-type for this axis
```

要将端口设置为*仿真*驱动器，请使用类别 `0x3` 且子类型字段为零。仿真类别按**完整 32 位字**匹配，因此子类型字段（位 31-16）必须为 `0`：

```text
ACIDeviceType=0x00000003
```

仿真 I/O 单元使用 `0x00000004`。（与使用子类型字段的真实驱动器/I/O 类别不同，仿真类别要求该字段为 0。）

## 版本间变更

v5 是仅 Central-i 的 64 位固件。它在上述驱动器/I/O/仿真类别之外新增了一个真实设备类别（值 0x5），并增加了额外的驱动器适配器子类型变体。类别编码以及驱动器/I/O/仿真值在其他方面保持不变。

## 参见

- [CIConnect](CIConnect.md) —— 对照此值校验已连接的设备
- [CILinkConfig](CILinkConfig.md) —— 物理/协议参数
- [CIIdentity](CIIdentity.md) —— 设备实际报告的标识
- [CIStatus](CIStatus.md) —— 设备类型错误码（9 和 7）
- [CISyncDef](CISyncDef.md) —— 同步数据定义
