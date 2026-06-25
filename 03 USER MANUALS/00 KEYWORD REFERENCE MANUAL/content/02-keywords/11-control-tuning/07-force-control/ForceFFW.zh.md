---
keyword: ForceFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 589
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
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 电流维度力前馈增益。
---
# ForceFFW

电流维度力前馈增益。

## 概述

`ForceFFW` 是电流维度力前馈增益。它与经滤波的力参考值 [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) 相乘，并联力 PID 输出直接叠加至电流参考值：

$$
\text{ForceFFW term} = \text{ForceRef} \cdot \text{ForceFFW} \cdot 0.001
$$

内部缩放系数为 1E-3。值范围为 `0` 至 `1000000`，默认值为 `0`。该关键字保存至闪存，可在电机使能及运动中修改。

`ForceFFW` 在 [ForcePIVOn](ForcePIVOn.md) 选择的两种力控制结构中均有效：

- **标准力控制**（`ForcePIVOn = 0`）：前馈项在经过力输出滤波器之前加至 PID 输出，共同形成电流参考值。
- **Force-over-PIV 控制**（`ForcePIVOn = 1`）：前馈项与速度补偿项（[ForceVelFFW](ForceVelFFW.md)）一同加至速度环输出，形成电流参考值。

## 工作原理

由于该项与（经滤波的）指令力成比例，而非与误差成比例，因此它提供一个跟踪力指令的电流贡献，无需等待环路积累误差，使 PID 仅需作用于残余误差。

## 示例

```text
AForceFFW[1]=1000       ; set the current-wise force feedforward gain
AForceFFW[1]            ; read the current-wise force feedforward gain
```

### 计算示例：稳态力指令下的贡献

当 `ForceFFW = 1000`，（经滤波的）力参考值 `ForceRef = 50`（力单位）时，该前馈路径的电流贡献为：

`ForceFFW term = 50 x 1000 x 0.001 = 50`（电流单位）

PID 随后仅需作用于实际力与指令之间的残余误差，稳态分量由前馈承担。

## 另请参阅

- [ForceFFWP](ForceFFWP.md) — 位置维度力前馈（仅 force-over-PIV）
- [ForceVelFFW](ForceVelFFW.md) — 电流参考处的速度反馈补偿
- [ForceRef](../../08-axis-operation/04-force-operation-mode/ForceRef.md) — 乘以本增益的经滤波参考值
- [Force control](00-overview.md) — 力环结构概述
