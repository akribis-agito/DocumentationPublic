---
keyword: CIAutoConnect
summary: 启用时，在上电时自动建立 Central-i 连接。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 500
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CIAutoConnect

启用时，在上电时自动建立 Central-i 连接。

## 概述

`CIAutoConnect = 1` 使控制器在启动期间自动为本轴端口运行 Central-i 连接序列，无需上位机显式发出 [CIConnect](CIConnect.md)。`CIAutoConnect = 0`（默认）则使端口保持断开，直至上位机手动连接。该设置为轴相关参数并保存至闪存，因此在复位后仍然保留。

## 工作原理

在引导过程中，端口初始化完成后，控制器会扫描每个端口。如果**任何**端口设置了 `CIAutoConnect = 1`，则首先等待一段短暂的稳定时间，以便远程单元上电，随后对每个自动连接端口运行与 [CIConnect](CIConnect.md) 相同的连接序列：

- 对于真实远程单元，由于中断尚未运行，每端口状态机在一个紧凑循环中从复位一路驱动至同步状态（或错误状态）。成功后会运行连接时的特殊参数设置，端口开始周期数据交换。
- 对于**仿真**设备类型（[CIDeviceType](CIDeviceType.md) 设为某仿真类别），端口立即标记为已连接，[CIIdentity](CIIdentity.md) 以默认通道计数填充 —— 不会尝试建立物理链路。

由于自动连接发生在上位机介入之前，所得到的链路状态会通过 [CIStatus](CIStatus.md) 和 [CIGlobalStat](CIGlobalStat.md) 报告，上位机可在启动后轮询这些状态。

## 示例

```text
ACIAutoConnect=1     ; auto-connect this axis's Central-i port at startup
ACIAutoConnect=0     ; leave the port disconnected until CIConnect is issued
```

## 另请参阅

- [CIConnect](CIConnect.md) —— 此处触发的连接序列（手动运行）
- [CIDisconnect](CIDisconnect.md) —— 断开链路
- [CIDeviceType](CIDeviceType.md) —— 在自动连接时选择真实或仿真行为
- [CIStatus](CIStatus.md) / [CIGlobalStat](CIGlobalStat.md) —— 所得到的链路状态
