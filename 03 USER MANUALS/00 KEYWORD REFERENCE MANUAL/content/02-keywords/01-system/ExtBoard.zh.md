---
keyword: ExtBoard
summary: 选择所连接的外部扩展板的硬件配置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 612
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ExtBoard

选择所连接的外部扩展板的硬件配置。

## 概述

`ExtBoard` 告诉固件控制器上安装了哪种外部扩展板，以便其能正确配置该板的资源。它是一个保存至闪存的非轴参数；由于它声明所安装的硬件，请先设置该参数，然后执行 [Reset](02-operation/Reset.md) 以确保所有板资源完全重新配置。它无法在电机使能或运动中更改。在没有扩展板选项的控制器上，唯一有效值为 `0`（无板）；在支持扩展板的硬件上，非零值选择所安装的板类型。

## 工作原理

| 取值 | 含义 |
|-------|---------|
| 0 | 无扩展板（默认） |
| （非零） | 控制器硬件所支持的特定扩展板类型 —— 例如更高分辨率的模拟量输入（ADC）子板 |

当 `ExtBoard` 选择某个受支持的板时，固件会在其硬件设置寄存器中置位相应的板使能位，并调整受影响的资源。对于更高分辨率的 ADC 板，模拟量输入（[AInPort](../05-inputs-outputs/02-analog-inputs/AInPort.md) 1-4）的满量程范围会从约 +/-12175 mV 改为 +/-12500 mV，以使读数被正确缩放。当 `ExtBoard = 0` 时，该使能位被清除，并使用默认的模拟量范围。

有效值的集合取决于硬件：大多数控制器变体仅接受 `0`，而在物理上支持该板的变体也接受其选择值。由于该设置声明所安装的硬件，请更改它并执行复位，以确保在依赖这些资源之前所有板资源完全重新配置。

## 示例

```text
AExtBoard           ; query the configured expansion-board type
AExtBoard=0         ; no expansion board (default)
```

## 参见

- [Reset](02-operation/Reset.md) —— 应用已更改的 `ExtBoard` 设置
- [AInPort](../05-inputs-outputs/02-analog-inputs/AInPort.md) —— 模拟量输入端口映射
- [DInPort](../05-inputs-outputs/04-digital-inputs/DInPort-DInPortHigh.md) —— 数字量输入端口映射
