---
keyword: Vc
summary: 只读的 C 相电压参考，用于空间矢量调制（PWM 计数分数 ×1000）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 15
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# Vc

只读的 C 相电压参考，用于空间矢量调制（PWM 计数分数 ×1000）。

## 概述

`Vc` 是用于空间矢量调制（SVM）的 C 相电压参考，以完整 PWM 计数的分数乘以系数 1000 表示（±1000 = 最大 PWM 幅值的 ±100 %）。C 相在硬件参考指南中定义。它与 [Va](Va.md) 和 [Vb](Vb.md) 一起构成发送给调制器并最终决定 PWM 占空比的三相电压指令。

每 1000 的 PWM 计数等于所报告的缩放系数 × 1000：在 central-i 系统上 `Vc` = 1000 指令对应完整半周期计数 1526 个 PWM 时钟（缩放 1.526），而在独立控制器上则指令对应该构建版本的完整计数——根据 PWM/采样率构建版本不同，为 1144 或 4577 个 PWM 时钟（缩放 1.144 或 4.577，即本页缩放栏中显示的值）。内部 PWM 比较值为 `Vc` × scaling，`Vc` = ±1000 即 PWM 半周期的 ±100 %（应用 [MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md) 之前的满调制深度）。

## 工作原理

与 [Va](Va.md) 和 [Vb](Vb.md) 不同，C 相并非由其自身的电流环产生——它是为补全相组而导出的：

| 电机类型组 | Vc 来源 |
|----|----|
| 三相无刷电机 | $\text{Vc}\ = \ -(\text{Va} + \text{Vb})$，使三相电压之和为零（平衡星形）。 |
| 有刷（单相）电机 | $\text{Vc}\ = \ 0$（仅驱动 A、B 两相，且 $\text{Vb} = -\text{Va}$）。 |
| 两相步进电机 | 在增强速度范围步骤之前 $\text{Vc}\ = \ 0$（电机回线连接到驱动器的 C 桥臂）。 |

形成之后，`Vc` 与其他相经历相同的后处理：增强速度范围中点减法（ControlMode 第 0 位，可使步进电机的 `Vc` 变为非零），以及饱和到最大 PWM 幅值（[MaxPWM](../../06-protections/02-current-and-voltage/MaxPWM.md)），后者会置位电压饱和位（[StatReg](../../07-status-and-faults/StatReg.md) 第 22 位）。`MaxPWM` 与 `Vc` 采用相同的每 1000 单位，默认为完整计数的 90 %（900 个关键字单位；central-i v5 上为 89 %，即 890 单位），并且永远无法达到 ±1000，因为半周期的一部分被预留给 PWM 死区。

对于三相电机，`Vc` 是补全平衡相组的第三个相隔 120° 的相位（$\text{Va} + \text{Vb} + \text{Vc} = 0$）：

![Three balanced phase voltages 120 degrees apart across one electrical cycle](three-phase-waveforms.svg)

### 边界情况

- **电机失能。** 当 [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) 为 0 时，电流环被复位，`Vc` 被强制为 0。
- **有刷电机。** 无论 [ControlMode](ControlMode.md) 如何，`Vc` 始终保持为 0（有刷电机不运行增强速度范围中点步骤）。
- **步进电机。** `Vc` 从 0 开始，当 [ControlMode](ControlMode.md) 第 0 位置位时再由负相位中点进行偏移。对于两相步进电机，该中点为 $\tfrac{1}{2}(\text{Va} + \text{Vb})$（起始时 `Vc` = 0），因此减法之后 $\text{Vc} = -\tfrac{1}{2}(\text{Va} + \text{Vb})$——这与无刷情形不同，后者的中点为 $\tfrac{1}{2}\big(\max(\text{Va},\text{Vb},\text{Vc}) + \min(\text{Va},\text{Vb},\text{Vc})\big)$。在饱和时，`Vc` 与 `Va`、`Vb` 一起缩放以保持其关系。
- **无刷电流环旁路（[ControlMode](ControlMode.md) 第 2 位 = 1）。** `Vc` 仍以旁路模式的 `Va`、`Vb` 值补全为 $-(\text{Va} + \text{Vb})$。
- **仿真。** 与硬件上的公式相同。

## 示例

```text
AVc                 ; read phase C SVM voltage reference
```

## 另请参阅

- [Va](Va.md), [Vb](Vb.md) — Vc 所补全的 A 相和 B 相电压参考
- [Vd](Vd.md), [Vq](Vq.md) — 构成 Va/Vb/Vc 的 dq0 电压输出
- [ControlMode](ControlMode.md) — 控制域、环路旁路及增强速度范围选项
- [StatReg](../../07-status-and-faults/StatReg.md) — Vc 被钳位时置位的电压饱和状态
