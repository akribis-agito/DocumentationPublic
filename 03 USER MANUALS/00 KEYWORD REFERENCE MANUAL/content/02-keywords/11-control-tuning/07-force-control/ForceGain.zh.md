---
keyword: ForceGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 577
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
summary: 力环 PID 控制器的比例增益。
---
# ForceGain

力环 PID 控制器的比例增益。

## 概述

`ForceGain` 是力控制环中标准形式 PID 控制器的比例（P）项。每个控制周期，它将力误差 [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md)（滤波后的参考值 [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) 减去 [Force](../../08-axis-operation/04-force-operation-mode/Force.md) 反馈）乘以一个内部缩放因子，该因子取决于 [ForcePIVOn](ForcePIVOn.md) 所选的力控制结构：

| ForcePIVOn | 力控制结构         | 内部缩放 |
|------------|--------------------|----------|
| 0          | 标准力控制         | 1E-6     |
| 1          | 力叠加 PIV 控制    | 1E-3     |

缩放后的乘积即为增益误差：

$$
\text{gained error} = \text{ForceErr} \cdot \text{ForceGain} \cdot \text{scaling}
$$

此增益误差是 PID 输出的 P 分量，同时也是积分项（[ForceKi](ForceKi.md)）和微分项（[ForceKd](ForceKd.md)）的作用信号。

取值范围为 `0` 至 `2147483647`，默认值为 `0`。该关键字保存至闪存，可在电机使能且运动中时修改。

## 工作原理

在**标准力控制**（`ForcePIVOn = 0`）下，PID 输出（P + I + D）加上前馈项，经过力输出滤波器后形成电流参考。此时 `ForceGain` 的缩放系数为 1E-6。

在**力叠加 PIV 控制**（`ForcePIVOn = 1`）下，PID 输出加上位置式前馈（[ForceFFWP](ForceFFWP.md)），乘以控制器采样时间后叠加到进入位置，形成送入内部位置/速度级联的位置参考。此时 `ForceGain` 的缩放系数为 1E-3。

## 示例

```text
AForceGain[1]=120       ; set the force-loop proportional gain
AForceGain[1]           ; read the force-loop proportional gain
```

### 演练：配置力叠加 PIV 的 PID

力叠加 PIV 控制（`ForcePIVOn = 1`）将力 PID 包裹在现有的位置+速度级联外部。三个力环增益共用同一增益误差信号，须同时设置。以下示例假设 PIV 级联已整定完毕，在此基础上添加力环。

1. **选择力叠加 PIV 结构**（电机关闭，轴静止）：

   ```text
   AForcePIVOn[1]=1
   ```

2. **设置外部力环的三个 PID 项**：

   ```text
   AForceGain[1]=120        ; P term (scaled by 1e-3 in force-over-PIV)
   AForceKi[1]=50           ; I term (scaled by 1e-3)
   AForceKd[1]=200          ; D term (scaled by 1e-3)
   ```

3. **添加位置式前馈**，使力环无需追踪负载的稳态重力：

   ```text
   AForceFFWP[1]=...
   ```

4. **进入力运行模式**并指令力设定值。力 PID 输出加上前馈形成位置参考，乘以控制器采样时间后叠加到进入位置，再由内部位置/速度环驱动。积分器抗饱和的钳位反馈来自内环限制（参见 [ForceKi](ForceKi.md)）。

> **关于缩放的说明。** 在 [ForcePIVOn](ForcePIVOn.md) 的 0 和 1 之间切换会改变 `ForceGain` 的内部缩放（1E-6 对比 1E-3），因此相同的数值会产生相差 1000 倍的有效增益——切换结构后需重新整定。

## 另请参阅

- [ForceKi](ForceKi.md) — 力环积分增益（使用相同的增益误差）
- [ForceKd](ForceKd.md) — 力环微分增益（使用相同的增益误差）
- [ForcePIVOn](ForcePIVOn.md) — 选择力控制结构（设置 ForceGain 的缩放系数）
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — 被 ForceGain 相乘的误差信号
- [ForceFFW](ForceFFW.md) / [ForceFFWP](ForceFFWP.md) / [ForceVelFFW](ForceVelFFW.md) — 在环输出端叠加的前馈项
- [Force control](00-overview.md) — 力环结构概述
