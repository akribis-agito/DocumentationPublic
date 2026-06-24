---
keyword: VelFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 108
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000000
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VelFFW

速度前馈增益，作用于位置参考的一阶导数。

## 概述

`VelFFW` 是速度前馈增益。它与速度参考 [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md)（位置参考经滤波后的一阶时间导数）相乘，并在反馈动作之前将结果叠加至驱动电流环的电流参考。通过作用于参考速度，它补偿了速度比例（阻尼/摩擦）项，从而使控制器无需等待跟随误差积累即可输出维持速度所需的力。

`VelFFW` 与加速度前馈 [AccFFW](AccFFW.md) 一同叠加至**电流参考**。它与通过 [VelTrackFact](../04-velocity-control/VelTrackFact.md) 缩放后叠加至速度环参考 [VelRef](../../../02-keywords/10-motion/01-kinematics-status/VelRef.md) 的速度前馈是不同的机制。

速度前馈仅在位置运行模式（[OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 3）下生效，在速度、力或电流运行模式下无效。

`VelFFW` 是用于增益调度的数组。不使用增益调度时，第一个元素 `VelFFW[1]` 为有效值。各调度方法下所选用的数组元素请参阅 [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md)。

## 工作原理

每个控制周期，速度前馈项为参考速度 [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) 乘以 `VelFFW` 再乘以固定增益缩放 1/2¹⁶（= 1.52587890625 × 10⁻⁵）：

$$
\text{VelTerm} = \frac{\text{dPosRef} \cdot \text{VelFFW}}{2^{16}}
$$

源量 [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) 是参考的平滑一阶差分：它携带由 [dPosRefFilt](../04-velocity-control/dPosRefFilt.md) 设定的参考微分低通滤波，因此速度前馈项在其源头即已固有地平滑。这与加速度前馈项（参见 [AccFFW](AccFFW.md)）不同，后者的源量是参考的原始二阶差分，本身不含平滑处理。

速度项与加速度前馈项求和，形成合并前馈输出，再叠加至速度环输出，构成电流参考 [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)：

$$
\text{CurrRefCtrl} = (\text{velocity-loop output}) + (\text{feedforward output})
$$

在 central-i v5 中，当前馈滤波器使能时（[FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md)），合并前馈输出首先经过该滤波器。v4 没有前馈滤波器：速度和加速度项直接以各自固定的 2 次幂增益缩放求和后加入电流参考。

在每次协调运动或矢量运动段切换时，控制器将对恰好两个控制周期抑制前馈，因为跨段边界计算的参考加速度精度有限，否则会产生电流尖峰。在 central-i v5 中，这两个周期内合并前馈输出（加速度项与速度项之和）被整体保持为零。然而在 v4 中，仅加速度前馈项在此两周期窗口内被抑制——速度前馈项**不**被抑制，在切换过程中持续生效。

### 缩放、范围与默认值

| | v4（standalone & central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位整数 | 32 位浮点数 |
| 范围 | 0 to 50000 | 0 to 1000000000 |
| 默认值 | 0 | 0 |
| 增益缩放 | 1/2¹⁶ (1.52587890625 × 10⁻⁵) | 1/2¹⁶ (1.52587890625 × 10⁻⁵) |

默认值 `0` 时，速度前馈关闭。

## 示例

```text
AVelFFW[1]=32768     ; set velocity feedforward gain (first array element)
AVelFFW[1]           ; read back the gain
```

### 应用示例：匀速运动中的贡献量

以 `VelFFW = 65536`（经内部 1/2^16 缩放后等效增益为 1；在 v5 中有效，因范围远超 65536）和参考速度 `dPosRef = 50000`（用户速度单位）为例，贡献至电流参考的速度前馈项为：

`VelTerm = 50000 x 65536 x (1 / 65536) = 50000`（电流单位）

无论位置环是否存在误差，同样的 `VelTerm` 均被叠加，因此维持匀速所需的稳态电流由前馈提供，速度环仅作用于残差。

## 另请参阅

- [AccFFW](AccFFW.md) — 加速度前馈增益（与速度项求和）
- [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) — 该增益所乘的速度参考
- [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) — 应用于合并前馈输出的前馈滤波器
- [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — 前馈叠加至的电流参考
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — 叠加至速度环参考的速度前馈（不同路径）
- [VelGain](../04-velocity-control/VelGain.md) — 此前馈所减少的速度环跟踪误差所在的速度环
- [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) — 增益调度对数组元素的选取
