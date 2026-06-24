---
keyword: UnitStat
summary: 报告本单元硬件与固件健康状态的只读位域。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 75
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# UnitStat

报告本单元硬件与固件健康状态的只读位域。

## 概述

`UnitStat` 是一个只读状态字，用于报告本单元硬件与固件的健康状态。每个位标记一项特定的故障或镜像不匹配情况；值为 `0` 表示它们均未置位。由于其作用域为非轴，`UnitStat` 描述的是整个控制器/驱动器单元，而非任何单个轴，并且它不保存至闪存 —— 它始终反映实时状态。

在固件或 FPGA 更新后，或在诊断某单元为何无法运行时，读取 `UnitStat`，以确认各镜像一致且不存在硬件故障。

## 工作原理

`UnitStat` 是一个在启动期间逐步构建的单个 32 位字。当控制器初始化时，它会依次检查每项硬件/镜像情况，并在该情况为真时将相应位**或**入该字；稍后会重新检查的情况（例如动态制动固件/FPGA 匹配）会在通过时清除其自身的位。因此一个正常的单元读取为 `0`。每个标志均为产品特定 —— 某位仅在该检查适用的产品上才会置位 —— 因此未置位的位意味着“未故障”或“不适用于本型号”。

固件内部也使用该字：例如，FPGA 故障位会阻止单元上线。上位机软件在编程后读取该字，以确认固件与 FPGA 镜像是匹配且有效的一组。

## 状态位

| 位 | 状态 |
|-----|--------|
| 0 | FPGA 故障 |
| 1 | AGD155 固件与 FPGA 不匹配 |
| 2 | AGD301 固件与 FPGA 不匹配 |
| 3 | 不存在黄金镜像 |
| 4 | 动态制动固件与 FPGA 不匹配 |

## 应对告警

- 对于不应携带黄金镜像的单元，可忽略**无黄金镜像（位 3）**。
- 对于 **FPGA 故障或任何固件/FPGA 不匹配**（位 0–2、4），请从 Agito 获取最新的匹配固件与 FPGA 并重新编程 —— 参见 [DownloadFW](../02-operation/DownloadFW.md) 与 [DownloadFPGA](../02-operation/DownloadFPGA.md)。

## 示例

```text
AUnitStat           ; read the current unit status word
```

## 另请参阅

- [FWInfo](FWInfo.md) —— 固件版本与构建信息
- [Identity](Identity.md) —— 控制器标识与已实现功能
- [DownloadFW](../02-operation/DownloadFW.md) / [DownloadFPGA](../02-operation/DownloadFPGA.md) —— 重新编程固件 / FPGA 镜像
