---
keyword: AOutGain
summary: 应用于模拟量输出上被监视参数的浮点缩放系数（v5）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 221
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AOutGain

应用于模拟量输出上被监视参数的浮点缩放系数（v5）。

## 概述

`AOutGain` 通过浮点系数对被监视参数（见 [AOutMode](AOutMode.md)）进行缩放，使其适配输出的动态范围。数组索引即模拟量输出编号（从 1 开始：`AOutGain[1]` 应用于模拟量输出 1）。这是[模拟量输出信号路径](00-overview.md)的缩放阶段，**仅在监视模式下**适用——在直接指令模式下，输出跟随 [AOutPort](AOutPort.md)，不使用 `AOutGain`。

`AOutGain` 是 v4 的 2 的幂缩放器 [AOutShifts](AOutShifts.md) 在 **v5（Central-i）** 上的替代项：v5 不再将缩放限制为 2 的幂，而是允许任意实数乘子。默认值为 `1`（单位增益）。

## 工作原理

对于处于监视模式的输出，每个控制周期内，被监视参数乘以 `AOutGain`，然后加上偏置，结果再转换为 DAC 码：

$$
\text{DAC code} = \big(\text{parameter} \cdot \text{AOutGain} + \text{AOutOffset}\big) \cdot \text{(mV-to-DAC factor)}
$$

由于被仿真参数被视为毫伏，应选择 `AOutGain`，使参数的工作范围有效地映射到 ±11905 mV 的输出范围。负增益会反相输出。

## 版本间差异

`AOutGain` 仅存在于 **Central-i v5**。在 v4（standalone 与 Central-i）上，等效缩放为 2 的幂缩放器 [AOutShifts](AOutShifts.md)；v5 以此浮点增益取代该整数移位。

## 示例

```text
AAOutGain[1]=4       ; scale the monitored value by 4
AAOutGain[1]=0.5     ; scale the monitored value by one half
AAOutGain[1]          ; read back the gain
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AOutGain[1]`–`AOutGain[4]`。`AOutGain[0]` 不存在。
- **模式错误**（[AOutMode](AOutMode.md) = 0，直接指令）— **不使用** `AOutGain`；DAC 直接跟随 [AOutPort](AOutPort.md)。在此模式下设置 `AOutGain` 将静默无效，直到 `AOutMode` 被更改。
- **零增益** — `AOutGain = 0` 会在加上偏置之前将被监视参数压缩为 `0` mV；只有 [AOutOffset](AOutOffset.md) 到达 DAC。
- **负增益** — 反相被监视值。
- **饱和** — 所得的 DAC 码在 DAC 阶段被钳位到 ±11905 mV 的输出范围；超出范围的值不会环绕，而是限幅至边界。
- **电机使能/失能** — 无论 `MotorOn` 状态如何，每个周期均运行。
- **保存** — 可保存至闪存；启动时重新加载。
- **平台** — 仅 central-i v5。在 v4（standalone 或 central-i）上，使用 [AOutShifts](AOutShifts.md) 实现等效的 2 的幂缩放。

## 另请参阅

- [AOutMode](AOutMode.md) — 选择被监视参数（增益仅在监视模式下适用）
- [AOutShifts](AOutShifts.md) — v5 中取代的 v4 2 的幂缩放
- [AOutOffset](AOutOffset.md) — 输出偏置（在此缩放之后、DAC 转换之前加上）
- [AOutPort](AOutPort.md) — 直接模式值（不受此增益影响）
- [analog-output overview](00-overview.md) — 完整信号路径
