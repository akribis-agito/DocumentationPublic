---
keyword: DOutPort
summary: 数字量输出的位打包手动状态（在 DOutLog 取反之前）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 211
attributes:
  access: rw
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# DOutPort

数字量输出的位打包手动状态（在 DOutLog 取反之前）。

## 概述

`DOutPort` 以位域形式（从 0 起算的位位置：bit 0 = 输出 1）保存数字量输出的手动状态。每个位：`1` = 开，`0` = 关。它是任何 [DOutLog](DOutLog.md) 取反*之前*的值。

对 `DOutPort` 的写入总是被接受，但它仅在处于手动控制下的位上*持续生效*——即 [DOutSelect](DOutSelect.md)`[x] = 0` **且** [DOutMode](DOutMode.md)`[x] = 0` 的位。由功能拥有的位每个周期都会被重新驱动，因此对它们的手动写入几乎会立即被覆盖。`DOutPort` 不保存至闪存，因此上电后必须重新应用手动状态。

## 工作原理

`DOutPort` 是每个周期驱动到物理输出引脚上的单个字。在每个控制周期结束时，计算出*最终*输出字并直接写入硬件数字量输出级：

$$
\text{Final output word} = \text{DOutPort} \oplus \text{DOutLog}
$$

因此 `DOutPort` 是原始的开/关意图，而 [DOutLog](DOutLog.md) 是在其之上应用的逐位极性。在输出级具有可选灌/拉电流引脚（开集电极输出）的控制器上，最终字随后由 [DOutType](DOutType.md) 拆分：灌电流驱动器获得 `DOutType = 0` 的位，拉电流驱动器获得 `DOutType = 1` 的位。差分输出占用同一字的高位。

`DOutPort` 不仅由你写入。当一个输出通过 [DOutMode](DOutMode.md) 被分配了软件功能时，控制器*本身*每个周期都会置位或清除相应的 `DOutPort` 位以镜像所选状态——这就是为什么一旦该输出的 `DOutMode` 非零，你手动写入的位就会被覆盖。因此，手动控制要求 `DOutMode[x] = 0`，使其他任何机制都不拥有该位。

`DOutPort` 的宽度（有多少位是真实输出）取决于产品——例如在小型控制器上为 8 位（4 个开集电极 + 4 个差分），在较大型号上最多可达 21 位。超出产品输出数量的位没有效果。

## 示例

```text
ADOutPort=6          ; binary …0110 — turn outputs 2 and 3 on, all others off
ADOutPort            ; read the present manual output word
```

## 说明

1. 写入整个字（`ADOutPort=value`）会一次性替换每个位。若要在保持其他位不变的情况下更改单个位，诸如 `DOutPort = DOutPort | mask` 的读—改—写可以做到，但对控制器**并不安全**，因为控制器可能在你的读和写之间写入 `DOutPort`（用于 `DOutMode` 功能）。请优先使用 [DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) 操作，它们以原子方式执行位更改。
2. 不保存至闪存——上电后重新应用手动状态。
3. 最终物理状态为 `DOutPort XOR DOutLog`，在具有可选灌/拉电流输出的产品上随后由 `DOutType` 路由。

### 边界情况

- **处于功能控制下的输出**——[DOutMode](DOutMode.md)`[x] ≠ 0` 或 [DOutSelect](DOutSelect.md)`[x] ≠ 0` 的位每个周期都会被控制器重写；对这些位的手动写入会在下一个周期被覆盖。
- **超出产品输出数量的位**——被参数表接受（存储为 32 位），但在引脚上没有效果。
- **与控制器竞争**——直接的 `DOutPort = DOutPort | mask` 不安全；请使用 [DOutPortSBit/CBit/TBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) 进行原子的单位更改。
- **电机使能/失能**——手动输出与 `MotorOn` 无关；无论伺服是否使能，该位都驱动引脚。
- **模式无关性**——与 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 无关。
- **功能更新后的读取**——读取 `DOutPort` 返回控制器**实际正在驱动**的位，其中包括功能输出；不要假设读取值就是你上次写入的值。
- **取反极性**——引脚电平为 `DOutPort XOR DOutLog`；读取 `DOutPort` 显示的是取反前的值。
- **双向引脚**——由 [BiDirConfig](../01-general-keywords/BiDirConfig.md) 路由为输出的引脚，当作为输入回读时会按照 [DInPort](../04-digital-inputs/DInPort-DInPortHigh.md) 中的方式反映该值。
- **保存**——不可保存至闪存；每次重启时复位为默认值。

## 参见

- [DOutPortSBit-DOutPortCBit-DOutPortTBit](DOutPortSBit-DOutPortCBit-DOutPortTBit.md) — 单个位的中断安全置位/清除/翻转
- [DOutLog](DOutLog.md) — 与 DOutPort 进行 XOR 的逐位极性
- [DOutType](DOutType.md) — 最终字的灌/拉电流路由
- [DOutSelect](DOutSelect.md) / [DOutMode](DOutMode.md) — 两者都必须为 0 才能手动写入 DOutPort
