---
keyword: VEncOn
summary: 使能或禁用该轴的软件生成虚拟编码器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 613
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
# VEncOn

使能或禁用该轴的软件生成虚拟编码器。

## 概述

`VEncOn` 使能或禁用该轴的虚拟编码器。虚拟编码器是一个**编码器信号生成器**：使能时，控制器会在该轴的硬件编码器仿真输出上发出真实的正交或脉冲/方向信号，并实时**跟踪一个内部源变量**。源由 [VEncSrc](VEncSrc.md) 选择，输出信号格式由 [VEncType](VEncType.md) 选择，源到输出的缩放由 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 设置，脉冲/方向建立延时由 [VEncDelay](VEncDelay.md) 设置。它是一个保存至闪存的轴相关参数，可在电机使能或运动中更改。

这与固定的编码器仿真输出（[EmulRat](../05-encoder-emulation/EmulRat.md)）不同，后者始终镜像该轴自身的反馈：虚拟编码器可以跟踪*任意*可选的源变量。

> **注意：** 虚拟编码器产生的是镜像某个变量的*输出*信号；它**不会**替代该轴自身的位置反馈（[Pos](../../10-motion/01-kinematics-status/Pos.md)）。生成的计数以只读方式通过 `VEncValue` 公开。

## 工作原理

| VEncOn | 状态 |
|---|---|
| 0 | 虚拟编码器禁用；仿真输出寄存器被清除。 |
| 1 | 虚拟编码器使能；每个控制周期，控制器读取源、对其进行缩放，并驱动编码器仿真硬件发出相应数量的边沿。 |

每个控制周期，控制器：

1. 读取由 [VEncSrc](VEncSrc.md) 选择的源变量，并处理源的任何 [ModRev](../04-modulo-mode/ModRev.md) 翻转。在 v4 固件中，源以 32 位整数读取；v5 Central-i 固件按其原生数据类型读取，然后转换为 32 位整数以用于跟踪。
2. 将其乘以 [VEncFact](VEncFact.md) 以进入输出平面。
3. 运行一个 PI 跟踪控制器加前馈，使发出的计数（按 `VEncFactDen` 缩放）以最小滞后跟随缩放后的源，并计算本周期要发出的边沿数量。
4. 将脉冲计数、50% 占空比周期以及"至首个脉冲的时钟数"（来自 [VEncDelay](VEncDelay.md)）写入硬件。

为某个周期计算出的边沿在该单个控制周期内均匀展开，并在每个周期重新置位，因此输出每个周期都被重新计时，而不是自由运行。控制周期以约 16.4 kHz 运行（每周期约 61 微秒），因此有效输出速率为在一个周期内发出的边沿数量在该固定的约 61 微秒窗口上的取值：在一个周期内发出 *N* 个边沿对应于每秒 *N* x 16,384 个边沿。

如果在电机使能时一个周期内所需的脉冲数量超过硬件限值，则该轴发生故障：[ConFlt](../../07-status-and-faults/ConFlt.md) 报告虚拟编码器最大脉冲数超出故障。每周期限值约为几千个边沿（确切数值取决于产品的内部时钟），因为每个边沿在周期内都需要一个导通半周期和一个关断半周期；因此该限值约为一个控制周期内可用时钟计数的一半。

### 硬件行为

虚拟编码器和固定的编码器仿真输出（[EmulRat](../05-encoder-emulation/EmulRat.md)）驱动**相同的物理 A/B 输出引脚**。当 `VEncOn` = 1 时，虚拟编码器接管这些 A/B 引脚；当 `VEncOn` = 0 时，A/B 引脚恢复为固定的仿真路径。索引（Z）线不由 `VEncOn` 切换——无论虚拟编码器状态如何，它都继续来自编码器仿真路径。

> **可用性：** 在当前固件中，完整的生成路径已为**独立控制器**实现；Central-i 远程输出路径取决于具体产品。

## 示例

```text
AVEncOn=1            ; enable the virtual encoder
AVEncOn=0            ; disable the virtual encoder
```

## 另请参阅

- [VEncSrc](VEncSrc.md) — 输出所跟踪的源变量
- [VEncType](VEncType.md) — 输出信号格式（脉冲/方向或 A-quad-B）
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — 源到输出缩放比例的分子 / 分母
- [VEncDelay](VEncDelay.md) — 脉冲/方向建立延时
- [EmulRat](../05-encoder-emulation/EmulRat.md) — 镜像该轴自身反馈的固定编码器仿真
