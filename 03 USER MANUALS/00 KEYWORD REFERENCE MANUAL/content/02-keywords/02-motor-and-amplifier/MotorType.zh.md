---
keyword: MotorType
summary: 定义连接到轴的电机类型，决定电流和电压如何计算与保护。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 50
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
  - 0
  - 7
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MotorType

定义连接到轴的电机类型，决定电流和电压如何计算与保护。

## 概述

`MotorType` 定义连接到内置或外部驱动器的电机类型。它决定电流和电压如何计算并施加到电机，以及如何保护电机免受过流。

> [!warning]
> 选择错误的 `MotorType` 可能导致严重损坏。在使能电机之前请正确设置。

`MotorType` 与若干其他配置关键字相互作用。对于无刷电机，它与 [PolePrs](PolePrs.md) 和 [EncRes](../03-encoder/01-general-settings/EncRes.md)（换相与反馈）协同工作；对于步进电机，它与 [StepBits](StepBits.md)、[StepInMotCurr](StepInMotCurr.md) 和 [StepInPosCurr](StepInPosCurr.md) 协同工作。由于它是轴相关且保存至闪存，因此无法在电机使能或运动中更改。各电机类型应使用哪些端子，请参见产品手册。

> [!note]
> 前置数据范围为 0–7。值 8（闭环步进、无刷）保留供内部使用（固件将其标记为"not supported yet"），此处记录仅为完整性考虑。

## 工作原理

在内部，`MotorType` 归并为实时控制环每个周期都会测试的三个**电机类别标志**之一（因此无需重新检查具体类型）：*brush*（涵盖直流有刷、音圈和仿真）、*brushless*（直线、旋转和保留的无刷步进）以及 *stepper*（开环和闭环）。类别标志选择控制环中运行哪条电流/电压生成路径，并设置换相要求：无刷类型被标记为"需要换相"（[StatReg](../07-status-and-faults/StatReg.md) 换相位在自动定相完成前被清除），而有刷和步进类型则立即被标记为"换相完成/不需要换相"。

当 `MotorType` 为无刷类型时更改它会重新置位换相——换相位被清除，轴在使能前必须重新定相。（更改 [EncRes](../03-encoder/01-general-settings/EncRes.md)、[PolePrs](PolePrs.md)、[AmpType](AmpType.md) 或编码器/电流方向也会如此。）

| MotorType | 类别 | 描述 |
|---|---|---|
| 0 Unknown | — | 新控制器的默认值。不施加任何电压输出。 |
| 1 DC brush | brush | 仅需两个电机输出端子，且不需要换相（物理换相）。 |
| 2 Voice coil | brush | 具有 1 个磁极对和 1 个执行线圈。仅需两个电机输出端子，且不需要换相。其运行与直流有刷电机相同。 |
| 3 Linear DC brushless | brushless | 3 相（3 组执行线圈，相隔 120 电角度），需要 3 个电机输出端子。换相通过 Park/逆 Park 变换决定电流/电压输出。该轴被视为直线电机；[EncRes](../03-encoder/01-general-settings/EncRes.md) 为每磁极对（磁周期）的编码器计数，且 [PolePrs](PolePrs.md) 必须为 1。 |
| 4 Rotary DC brushless | brushless | 3 相（3 组执行线圈，相隔 120 电角度），需要 3 个电机输出端子。换相通过逆 Park 变换决定电流/电压输出。该轴被视为旋转电机；[EncRes](../03-encoder/01-general-settings/EncRes.md) 为每转的编码器计数，且 [PolePrs](PolePrs.md) 定义每转的极对数。 |
| 5 Simulation | brush | 用于开发期间的仿真。在无物理电机的情况下生成仿真运动曲线、输入和输出；换相/电流环被绕过，反馈被强制跟随参考。 |
| 6 Stepper in open loop | stepper | 参见下文"开环步进"。 |
| 7 Stepper in closed loop | stepper | 参见下文"闭环步进"。 |
| 8 Stepper in closed loop (brushless) | brushless | 保留选项，供内部使用（不支持）。 |

> [!note]
> 当 [AmpType](AmpType.md) 选择闭合其自身电流环的**外部驱动器**时（在 v4 上，除内置 PWM 驱动器或线性适配器之外的任何模式；在 v5 上数字 SPI 模式也保留内部环），控制器将电机标记为"外部驱动"，并无论 `MotorType` 如何都跳过其内部电流环——此时控制器仅输出指令（模拟电流、模拟速度或脉冲方向），并让外部驱动器处理换相和电流控制。

### 换相（无刷类型 3、4）

对于无刷电机，电角度由反馈导出。控制器预先计算一个电气周期为

$$Counts\ per\ electrical\ cycle = \frac{\text{EncRes}}{\text{PolePrs}}$$

并通过将反馈位置的周期内位置乘以 $2\pi / (\text{EncRes}/\text{PolePrs})$ 将其转换为电气弧度。随后，三个相电压（$\text{Va}$、$\text{Vb}$、$\text{Vc}$）通过逆 Park 变换使用此角度从 q/d 电流参考产生。因此错误的 [PolePrs](PolePrs.md) 或 [EncRes](../03-encoder/01-general-settings/EncRes.md) 会错误缩放电角度，换相将无法工作。

### 开环步进（MotorType = 6）

2 相步进电机，需要 3 个引脚（A 相、B 相以及合并的 A/B 相回线）。一个电气周期（一个完整步励磁序列）包含 4 个整步。制造商通常将分辨率指定为每整步的物理角度。在 Agito 控制器上，每个电气周期的步数由 [StepBits](StepBits.md) 定义（最小为 2，即 4 个整步）。

每个电气周期的位置计数数（用于 [PosRef](../10-motion/01-kinematics-status/PosRef.md)、[AbsTrgt](../10-motion/13-motion-mode-ptp/AbsTrgt.md) 等）为 $2^{\text{StepBits}}$。

物理分辨率为

$$Resolution\ \left\lbrack \frac{physical\ deg}{count} \right\rbrack = \ \frac{4 \cdot Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{count} \right\rbrack}{2^{\text{StepBits}}}$$

每转的计数数为

$$Counts\ per\ revolution = \ \ \frac{360\lbrack physical\ deg\rbrack \cdot 2^{\text{StepBits}}}{4 \cdot Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{count} \right\rbrack}$$

在开环步进控制中，不使用位置反馈（[Pos](../10-motion/01-kinematics-status/Pos.md) = 0 且 [PosErr](../10-motion/01-kinematics-status/PosErr.md) = 0）。用户通过更改位置参考（[PosRef](../10-motion/01-kinematics-status/PosRef.md)）来指令运动，该参考用于确定 A 相和 B 相的步进电流并跟踪步进位置。

步进电流在每个控制周期根据电气周期内位置生成。固件将 `PosRef` 掩码到该周期（`PosRef & (2^StepBits − 1)`），将其转换为电角度 $\theta = \text{position} \cdot 2\pi/2^{\text{StepBits}}$，并从正弦/余弦查找表（由当前步进电流 [StepInMotCurr](StepInMotCurr.md) / [StepInPosCurr](StepInPosCurr.md) 缩放，保存在电流参考中）设置两个相电流参考：

$$\text{IaRef} = I \cdot \sin\theta \qquad \text{IbRef} = I \cdot \cos\theta$$

随后 2 相电流环对 $\text{Ia}$ 和 $\text{Ib}$ 闭环，产生相电压 $\text{Va}$ 和 $\text{Vb}$，且 **$\text{Vc} = 0$**（A/B 相回线连接到驱动器的 C 相）。q/d（Park）分量对步进电机不使用，并报告为零。

### 闭环步进（MotorType = 7）

与上文相同的 2 相步进硬件（3 个引脚；每个电气周期 4 个整步；每个电气周期的步数由 [StepBits](StepBits.md) 定义，最小为 2）。

每个电气周期的步数为 $2^{\text{StepBits}}$ [step count]。

物理分辨率为

$$Resolution\ \left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack = \ \frac{4 \cdot Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}{2^{\text{StepBits}}}$$

每转的步数为

$$Steps\ per\ revolution = \ \ \frac{360\lbrack physical\ deg\rbrack \cdot 2^{\text{StepBits}}}{4 \cdot Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}$$

在闭环步进控制中，使用编码器反馈，位置以编码器计数（而非步进计数）定义。必须同时提供每转的极对数（[PolePrs](PolePrs.md)）和每转的编码器计数（[EncRes](../03-encoder/01-general-settings/EncRes.md)）。仅使用位置闭环：[VelRef](../10-motion/01-kinematics-status/VelRef.md) 为位置环输出与位置微分之和。

控制器预先计算一个 *steps-per-count* 系数

$$Steps\ per\ count = \frac{\text{PolePrs} \cdot 2^{\text{StepBits}}}{\text{EncRes}}$$

并在每个周期将 `VelRef`（单位 count/s）转换为每个采样的步进计数增量，将其累加到步进电气周期位置中（在一个电气周期内环绕），然后运行与开环步进**相同**的相电流生成（掩码到 `2^StepBits − 1`，由步进电流缩放的正弦/余弦查找，然后是 Vc = 0 的 Ia/Ib 电流环）。允许每个控制周期行进超过一个电气周期的 `MaxVel` 会被掩码屏蔽，因此请合理设置 [MaxVel](../06-protections/03-motion/general-maximum-limits/MaxVel.md)。

## 示例

```text
AMotorType=4         ; rotary DC brushless motor
AMotorType=6         ; open-loop stepper motor
AMotorType          ; query the configured motor type
```

## 另请参阅

- [PolePrs](PolePrs.md) — 极对数，无刷（3、4）和闭环步进（7）电机所需
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — 编码器分辨率，按电机类型解释
- [StepBits](StepBits.md) — 步进电机（6、7）每个电气周期的步数
- [StepInMotCurr](StepInMotCurr.md) / [StepInPosCurr](StepInPosCurr.md) — 运动中/静止时的步进相电流
- [AmpType](AmpType.md) — 驱动电机的驱动器模式
