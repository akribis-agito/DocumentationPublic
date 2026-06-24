---
keyword: DOutLog
summary: 应用于最终数字量输出状态的逐输出逻辑取反（XOR）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 212
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# DOutLog

应用于最终数字量输出状态的逐输出逻辑取反（XOR）。

## 概述

`DOutLog` 以位域形式（从 0 起算：bit 0 = 输出 1）对选定的数字量输出进行逻辑取反。每个位：`0` = 默认，`1` = 取反。取反在 [DOutPort](DOutPort.md)（以及任何硬件/软件功能）之后应用，产生驱动物理输出的最终输出字。

## 工作原理

每个控制周期，在写入物理引脚之前，将输出字与 `DOutLog` 进行 XOR 运算：

$$
\text{Final output word} = \text{DOutPort} \oplus \text{DOutLog}
$$

`DOutLog` 中为 `1` 的位会对该输出取反；为 `0` 的位则原样通过。其结果即硬件数字量输出级所接收的内容。在具有可选灌/拉电流引脚的产品上，先计算出最终字，然后由 [DOutType](DOutType.md) 将其拆分到灌电流和拉电流驱动器中——因此极性是在灌/拉路由**之前**应用的。

**示例：** 当 `DOutPort = 7`（`…0111`）且 `DOutLog = 3`（`…0011`）时，最终输出字为 `4`（`…0100`）——bit 0 和 bit 1（输出 1 和输出 2）被取反。

## 说明

1. `DOutLog` 应用于最终字，因此无论底层 `DOutPort` 位是如何设置的，它都会对输出取反——无论是手动写入、[DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md)，还是 [DOutMode](DOutMode.md) 软件功能，所看到的取反都相同。
2. 它不影响通过 [DOutSelect](DOutSelect.md) 路由到*硬件*功能（事件、P/D、UserPWM）的输出，这些输出在硬件中绕过 `DOutPort`/`DOutLog` 字。
3. 保存至闪存，因此极性在重新上电后仍然保持。

### 边界情况

- **硬件功能输出**——[DOutSelect](DOutSelect.md) 非零的位**绕过** `DOutLog`；这些引脚的极性在硬件功能本身中设置。
- **超出产品输出数量的位**——存储在 32 位字中，但没有可影响的引脚。
- **电机使能/失能**——与 `MotorOn` 无关；取反每个周期都运行。
- **模式无关性**——与 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 无关。
- **回读**——读取取反掩码；与 `DOutPort` 结合以计算最终引脚电平。
- **保存**——可保存至闪存；启动时重新应用。

## 参见

- [DOutPort](DOutPort.md) — 取反前的输出状态（与 DOutLog 进行 XOR 的操作数）
- [DOutType](DOutType.md) — 在 XOR 之后应用的灌/拉电流路由
- [DOutMode](DOutMode.md) — 软件功能也会经过此取反
