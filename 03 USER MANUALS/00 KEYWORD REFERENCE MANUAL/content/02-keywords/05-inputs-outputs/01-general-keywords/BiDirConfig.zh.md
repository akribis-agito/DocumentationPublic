---
keyword: BiDirConfig
summary: 将每个双向 I/O 引脚配置为输入或输出的位域。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 495
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
  - 4294967295
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    range:
    - -2147483648
    - 2147483647
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BiDirConfig

将每个双向 I/O 引脚配置为输入或输出的位域。

## 概述

`BiDirConfig` 设置控制器双向 I/O 引脚的方向——哪些引脚作为输入、哪些作为输出。该值的每一位对应一个双向通道。它保存至闪存，并可随时更改。在对这些通道使用数字量输入或数字量输出关键字之前，先在此处配置引脚方向。

双向引脚的数量是**与产品相关**的：某些产品仅提供单个差分双向 I/O，另一些则最多提供八个。超出某一产品实际具有的引脚之外的位不产生任何作用。

## 工作原理

写入 `BiDirConfig` 时，该值被直接传递给硬件的双向方向寄存器：

- **单轴控制器**——低 16 位被直接写入硬件方向寄存器。
- **Central-i**——该值作为一条 “assign” 消息排队，并发送到所寻址的远程 I/O 单元，在该单元中配置其引脚。这就是该关键字在 Central-i 上为轴范围的原因：每个 I/O 模块都通过其自身的轴索引来访问。

每一位选择一个引脚的方向；硬件寄存器解释该位模式。配置为输入的引脚随后通过数字量输入关键字读取（其位出现在 [DInPort-DInPortHigh](../04-digital-inputs/DInPort-DInPortHigh.md) 的双向部分中），配置为输出的引脚则通过 [DOutPort](../05-digital-outputs/DOutPort.md) 驱动。在依赖这些关键字处理双向通道之前，先设置 `BiDirConfig`。

> 该值被原样写入硬件寄存器，因此每位的极性（置位表示“输入”还是“输出”）由硬件定义。在驱动输出之前，请确认您产品的约定。

## 示例

```text
ABiDirConfig        ; read the current direction configuration
ABiDirConfig=0      ; default configuration (all pins in their default direction)
```

### 边界情形

- **每引脚极性**——在某些硬件上置位 = “输入”，在另一些硬件上 = “输出”；**务必**对照产品手册核实。
- **超出可用引脚之外的位**——参数表会接受，但在硬件寄存器处被忽略。
- **运行时更改方向**——可接受；引脚立即被重新配置，但另一侧任何已接线的逻辑在稳定前可能看到瞬态。
- **电机使能/失能**——与 `MotorOn` 无关。
- **保存**——可保存至闪存；在引导时重新载入硬件方向寄存器。
- **平台**——central-i 将该值作为一条 assign 消息发送到所寻址的远程单元；standalone 直接写入 FPGA 寄存器。

## 另请参阅

- [DInPort-DInPortHigh](../04-digital-inputs/DInPort-DInPortHigh.md) —— 数字量输入端口状态（配置为输入的双向引脚在此出现）
- [DOutPort](../05-digital-outputs/DOutPort.md) —— 数字量输出端口状态（驱动配置为输出的双向引脚）
