---
keyword: ForceKd
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 588
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
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 力环 PID 控制器的微分增益。
---
# ForceKd

力环 PID 控制器的微分增益。

## 概述

`ForceKd` 是力控制环中标准形式 PID 控制器的微分（D）项——力环在力运行模式下为完整的 PID（P + I + D）。它适用于两种力控制结构（标准模式和由 [ForcePIVOn](ForcePIVOn.md) 选择的力叠加 PIV 模式），内部缩放系数固定为 1E-3。

每个控制周期，微分项作用于本周期与上一周期增益力误差的变化量：

$$
D = \text{ForceKd} \cdot (\text{gained error} - \text{gained error}_{\text{prev}}) \cdot 0.001
$$

其中，*gained error* 为经过 [ForceGain](ForceGain.md) 阶段后的力误差，下标 *prev* 表示上一周期的值。这是 PID 输出的 D 分量。

取值范围为 `0` 至 `2000000000`，默认值为 `0`。该关键字保存至闪存，可在电机使能且运动中时修改。

## 示例

```text
AForceKd[1]=200         ; set the force-loop derivative gain
AForceKd[1]             ; read the force-loop derivative gain
```

## 另请参阅

- [ForceGain](ForceGain.md) — 力环比例增益（提供此处求差分的增益误差）
- [ForceKi](ForceKi.md) — 力环积分增益
- [ForcePIVOn](ForcePIVOn.md) — 选择力控制结构
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — 环路驱动趋零的误差
- [ForceRefFilt](ForceRefFilt.md) — 参考值的一阶低通滤波器（影响 D 项所见信号）
- [Force control](00-overview.md) — 力环结构概述
