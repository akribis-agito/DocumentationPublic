---
keyword: LmFFWLevel
summary: 应用于感性（L di/dt）电压前馈贡献量的百分比级别。
availability:
  standalone: []
  central-i:
  - v5
can_code: 846
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 200.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# LmFFWLevel

应用于感性（L di/dt）电压前馈贡献量的百分比级别。

> 从 central-i v5 起可用。

## 概述

`LmFFWLevel` 对电压前馈中的感性项进行缩放。要改变绕组中的电流，控制器必须施加一个与电感和电流变化率成比例的电压（即 L·di/dt 项）。控制器根据测量得到的电机电感 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) 和指令电流变化量计算该电压；`LmFFWLevel` 是一个百分比，设定该计算电压中实际施加的比例。该项在快速电流瞬变（例如运动开始时）时预先提供所需电压，使电流环在跟踪上升和下降的电流参考时滞后更小。

`LmFFWLevel` 仅缩放该 L·di/dt 感性贡献量，该贡献量存在于交轴和直轴前馈输出 [VqFFW](VqFFW.md) 和 [VdFFW](VdFFW.md) 中。这两个输出还包含与速度相关的 d-q 交叉耦合项，但该项不由 `LmFFWLevel` 设置（见[工作原理](#工作原理)）。感性项仅在 [VoltageFFWOn](VoltageFFWOn.md) 启用电压前馈时才生效。

## 工作原理

`LmFFWLevel` 的单位为百分比（%）。感性前馈电压为建模 L·di/dt 电压（由 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) 和每控制周期参考电流变化量计算）乘以 `LmFFWLevel`/100：

- `0` — 无感性前馈（默认）；
- `100` — 施加全部建模感性电压；
- 最大值以内的其他值允许对建模项进行过补偿或欠补偿。

对于三相电机，控制器使用每相电感：若存储的 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) 为线间值，则在计算前内部将其折半得到每相值。同样出现在 [VqFFW](VqFFW.md) 和 [VdFFW](VdFFW.md) 中的与速度相关的 d-q 交叉耦合项，由电机电感 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md)、母线电压、电气周期及电机速度共同决定，**不**受 `LmFFWLevel` 缩放。只要电压前馈使能且电机运动，该交叉耦合项即存在，与 `LmFFWLevel` 的设置无关。

有效范围为 0 至 200（%），默认值为 0。`LmFFWLevel` 为闪存存储参数，可在电机使能或运动中设置；更改在下一个控制周期生效。`LmFFWLevel` 为 0 时，感性项为零。[Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) 不能低于其最小值 1（单位 µH），因此应通过将 `LmFFWLevel` 设为 0 来禁用感性项，而非降低 [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md)。

## 示例

```text
ALmFFWLevel=100      ; 施加全部建模感性电压
ALmFFWLevel          ; 读取已配置的级别
ALmFFWLevel=0        ; 禁用感性前馈项
```

## 另请参阅

- [Lm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Lm.md) — 该级别所缩放的测量电机电感
- [RmFFWLevel](RmFFWLevel.md) — 阻性（R·i）前馈项的级别
- [BEMFFFWLevel](BEMFFFWLevel.md) — 反电动势前馈项的级别
- [VqFFW](VqFFW.md) / [VdFFW](VdFFW.md) — 承载感性项的前馈输出
- [VoltageFFWOn](VoltageFFWOn.md) — 电压前馈的主使能开关
