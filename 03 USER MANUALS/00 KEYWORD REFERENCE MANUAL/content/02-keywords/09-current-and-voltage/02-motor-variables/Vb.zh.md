---
keyword: Vb
summary: 只读 B 相电压参考，用于空间矢量调制（PWM 计数分数 ×1000）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 14
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.144
  implemented: final
overrides:
  central-i.v4:
    scaling: 1.526
  central-i.v5:
    data_type: float32
    range: null
    scaling: 1.526
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# Vb

只读 B 相电压参考，用于空间矢量调制（PWM 计数分数 ×1000）。

## 概述

`Vb` 是用于空间矢量调制 (SVM) 的 B 相电压参考，表示为满 PWM 计数的分数乘以系数 1000（±1000 = 最大 PWM 幅值的 ±100 %）。B 相在硬件参考指南中定义。它与 [Va](Va.md) 和 [Vc](Vc.md) 一起，构成发送至调制器并最终形成 PWM 占空比的三相电压指令。

每 1000 的 PWM 计数等于所报告的缩放系数 × 1000：在 central-i 系统上，`Vb` = 1000 指令满半周期计数 1526 个 PWM 时钟（缩放 1.526），而在 standalone 控制器上，它指令该构建的满计数——根据 PWM/采样率构建为 1144 或 4577 个 PWM 时钟（缩放 1.144 或 4.577，本页缩放中所示的值）。内部 PWM 比较值为 `Vb` × 缩放，且 `Vb` = ±1000 即为 PWM 半周期的 ±100 %（应用 [MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md) 之前的满调制深度）。

## 工作原理

`Vb` 的产生方式与 [Va](Va.md) 相同，移相至 B 相：

| 情况 | Vb 的来源 |
|----|----|
| 无刷，矢量 (dq0) 控制（[MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 或 4，[ControlMode](ControlMode.md) 位 1 = 0，位 2 = 0） | dq0 电压输出的逆变换：$\text{Vb}\ = \ \text{Vq} \cdot \sin(\theta - 120^\circ) + \text{Vd} \cdot \cos(\theta - 120^\circ)$，其中 [Vd](Vd.md)/[Vq](Vq.md) 来自 dq 电流环。 |
| 无刷，abc（相）控制（[MotorType](../../02-motor-and-amplifier/MotorType.md) = 3 或 4，[ControlMode](ControlMode.md) 位 1 = 1，位 2 = 0） | 基于 [IbErr](IbErr.md) 的 B 相电流 PI 调节器的输出（[CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 积分项 + 比例项，按 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 缩放）。[Vq](Vq.md) 和 [Vd](Vd.md) 强制为 0。 |
| 步进电机（[MotorType](../../02-motor-and-amplifier/MotorType.md) = 6 或 7） | 基于 [IbErr](IbErr.md) 的 B 相电流 PI 调节器的输出，其中 [IbRef](IbRef.md) 生成为 $\text{CurrRef} \cdot \cos(\text{stepper electrical angle})$。步进路径始终为逐相（abc 域）并忽略 [ControlMode](ControlMode.md) 位 1 和位 2。 |
| 有刷 / 音圈电机（[MotorType](../../02-motor-and-amplifier/MotorType.md) = 1 或 2，[ControlMode](ControlMode.md) 位 2 = 0） | $\text{Vb}\ = \ -\text{Va}$（有刷路径驱动跨越 A 相和 B 相的单个 H 桥）。 |
| 无刷电流环旁路（[ControlMode](ControlMode.md) 位 2 = 1） | $\text{Vb}\ = \ \text{IbRef}$。（此情况下有刷将 [IbRef](IbRef.md) 设为 0；步进电机忽略此位。） |

随后应用与 [Va](Va.md) 相同的后处理：无刷 $\text{Vc} = -(\text{Va} + \text{Vb})$，有刷/步进 $\text{Vc} = 0$，增强速度范围中点减法（[ControlMode](ControlMode.md) 位 0，仅无刷和步进），以及饱和到最大 PWM 幅值（[MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md)），后者会置位电压饱和位（[StatReg](../../07-status-and-faults/StatReg.md) 位 22）。`MaxPWM` 以与 `Vb` 相同的每 1000 单位表示，默认为满计数的 90 %（900 个关键字单位），并且永远无法达到 ±1000，因为半周期中有一部分被预留给 PWM 死区。在正常的无刷矢量控制中，[Vq](Vq.md)/[Vd](Vd.md) 矢量在逆变换之前被限幅，从而保持正弦关系；到 ±`MaxPWM` 的直接逐相钳位仅在旁路模式下应用（参见 [Va](Va.md)）。

Vb 在电角度上滞后 Va 120°，而 Vc 又进一步滞后 Vb 120°：

![Three balanced phase voltages 120 degrees apart across one electrical cycle](three-phase-waveforms.svg)

### 边界情况

- **电机失能。** 当 [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) 为 0 时，电流环复位，`Vb` 强制为 0。
- **力 / 位置 / 电流运行模式。** 电流环在所有模式下运行方式相同；仅 [CurrRef](CurrRef.md) 的来源不同。
- **开环电压模式。** 当开环电压指令激活时（[OpenLoopVolt](../../08-axis-operation/01-general-keywords/OpenLoopVolt.md) / [OpenLoopCurr](../../08-axis-operation/01-general-keywords/OpenLoopCurr.md)），`Vb` 反映该指令路径而非闭环。
- **仿真。** 在仿真中，`Vb` 遵循相同的公式。
- **外部电流指令驱动器（[AmpType](../../02-motor-and-amplifier/AmpType.md) = 电流指令）。** 电流环在驱动器中运行，而非控制器中。

## 示例

```text
AVb                 ; read phase B SVM voltage reference
```

## 另请参阅

- [Va](Va.md)、[Vc](Vc.md) — A 相和 C 相电压参考
- [Vd](Vd.md)、[Vq](Vq.md) — 形成 Va/Vb/Vc 的 dq0 电压输出
- [IbRef](IbRef.md)、[IbErr](IbErr.md) — 馈入 Vb 的 B 相电流参考与误差
- [ControlMode](ControlMode.md) — 控制域和环路旁路选项
- [StatReg](../../07-status-and-faults/StatReg.md) — Vb 被钳位时置位的电压饱和状态
