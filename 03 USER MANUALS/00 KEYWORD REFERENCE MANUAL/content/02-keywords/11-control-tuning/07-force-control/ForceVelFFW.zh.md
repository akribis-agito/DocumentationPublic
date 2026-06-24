---
keyword: ForceVelFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 580
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 力环中的速度反馈补偿增益。
---
# ForceVelFFW

力环中的速度反馈补偿增益。

## 概述

`ForceVelFFW` 是在力控制运行模式下施加于电流参考的速度反馈补偿增益。它将速度反馈乘以该增益，并从电流参考中**减去**：

$$
\text{ForceVelFFW term} = -\,\text{Vel} \cdot \text{ForceVelFFW} \cdot 0.00000001
$$

其中 `Vel` 为速度反馈（即 [Vel](../../10-motion/01-kinematics-status/Vel.md) 索引 1 所报告的值）。内部缩放系数为 1E-8。

值域为 `-2147483648` 至 `2147483647`，默认值为 `0`。该关键字保存至闪存，可在电机使能及运动中修改。

`ForceVelFFW` 在 [ForcePIVOn](ForcePIVOn.md) 所选的两种力控制结构中均有效：

- **标准力控制**（`ForcePIVOn = 0`）：该项与 PID 输出及电流前馈（[ForceFFW](ForceFFW.md)）合并，在力输出滤波器之前形成电流参考。
- **Force-over-PIV 控制**（`ForcePIVOn = 1`）：该项与速度环输出及电流前馈合并，形成电流参考。

## 工作原理

由于该项与速度反馈方向相反，它在电流参考处相当于一个与速度成比例的项。在两种控制结构中，它均与电流前馈 [ForceFFW](ForceFFW.md) 在同一求和点处叠加。

## 示例

```text
AForceVelFFW[1]=100     ; set the velocity feedback compensation gain
AForceVelFFW[1]         ; read the velocity feedback compensation gain
```

### 计算示例：贡献量的符号与大小

当 `ForceVelFFW = 100`、速度反馈 `Vel[1] = 5000`（用户速度单位）时，在电流参考求和点处叠加的项为：

`-Vel x ForceVelFFW x 1E-8 = -5000 x 100 x 1E-8 = -0.005`（电流单位）

若轴沿反方向运动（`Vel[1] = -5000`），则该项变为 `+0.005`。由于该项被减去，它始终与运动方向相反，在电流指令中起到额外粘性阻尼的作用，并提供克服速度比例负载所需的稳态电流。

## 参见

- [ForceFFW](ForceFFW.md) — 电流前馈（在同一求和点处叠加）
- [ForceFFWP](ForceFFWP.md) — 位置前馈（仅限 Force-over-PIV）
- [ForcePIVOn](ForcePIVOn.md) — 选择力控制结构
- [Force control](00-overview.md) — 力环结构概述
