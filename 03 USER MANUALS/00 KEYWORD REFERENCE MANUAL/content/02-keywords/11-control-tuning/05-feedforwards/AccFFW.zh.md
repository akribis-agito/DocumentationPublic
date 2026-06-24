---
keyword: AccFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 101
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 加速度前馈增益，作用于位置参考的二阶微分。
---
# AccFFW

加速度前馈增益，作用于位置参考的二阶微分。

## 概述

`AccFFW` 是加速度前馈增益。它乘以后处理位置参考的加速度（整形/滤波后参考的二阶时间微分），并将结果提前于反馈作用叠加到驱动电流环的电流参考中。通过作用于参考加速度，它补偿了负载的惯性（质量）项，使控制器无需等待跟随误差累积就能指令所需的加速力。

加速度前馈仅在位置运行模式（[OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 3）下有效，在速度、力或电流运行模式下无效。

`AccFFW` 是用于增益调度的数组。未启用增益调度时，第一个元素 `AccFFW[1]` 为激活值。各调度方法下选取的数组元素参见 [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md)。

## 工作原理

每个控制周期，参考加速度由后处理（整形和滤波后）位置参考的二阶差分形成——与位置环使用的参考信号相同：

$$
a_{\text{ref}} = \text{ref}_{k} - 2 \cdot \text{ref}_{k-1} + \text{ref}_{k-2}
$$

加速度前馈项为参考加速度乘以 `AccFFW` 并经固定增益缩放 $1/2^{8}$（= 3.90625 × 10⁻³）：

$$
\text{AccTerm} = \frac{a_{\text{ref}} \cdot \text{AccFFW}}{2^{8}}
$$

此处使用的参考加速度是参考的*原始*二阶差分：与速度前馈不同——其来源 [dPosRef](../../../02-keywords/10-motion/01-kinematics-status/dPosRef.md) 是参考微分平滑后的一阶差分（参见 [VelFFW](VelFFW.md)）——加速度项直接取自参考，不经任何额外平滑。

加速度项与速度前馈项（参见 [VelFFW](VelFFW.md)）求和，构成合并前馈输出，然后叠加到速度环输出上，构成电流参考 [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)：

$$
\text{CurrRefCtrl} = (\text{velocity-loop output}) + (\text{feedforward output})
$$

在 central-i v5 中，当前馈滤波器启用时，合并前馈输出首先通过前馈滤波器（[FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md)）；该滤波器是唯一应用于加速度前馈项的平滑处理。在 v4 中没有前馈滤波器：加速度项和速度项直接求和进入电流参考，仅有各自固定的二的幂次增益缩放。

在每个协调运动或矢量运动分段过渡时，控制器抑制前馈恰好两个控制周期，因为跨分段边界计算的参考加速度精度有限，否则会产生电流尖峰。在 central-i v5 中，整个合并前馈输出（加速度项加速度项）在这两个周期内保持为零。在 v4 中，仅加速度前馈项在此窗口内被抑制；速度前馈项继续作用。

### 缩放、范围与默认值

| | v4（standalone 及 central-i）| v5（central-i）|
|---|---|---|
| 数据类型 | 32 位整数 | 32 位浮点 |
| 范围 | 0 到 50000 | 0 到 1000000000 |
| 默认值 | 0 | 0 |
| 增益缩放 | 1/2⁸（3.90625 × 10⁻³）| 1/2⁸（3.90625 × 10⁻³）|

默认值 `0` 时，加速度前馈关闭。

## 示例

```text
AAccFFW[1]=2560      ; set acceleration feedforward gain (first array element)
AAccFFW[1]           ; read back the gain
```

### 计算示例：峰值参考加速度时的贡献

当 `AccFFW = 2560`（v4 整数）、参考加速度 `a_ref = 1000`（用户单位/s²/周期，即参考的二阶差分）时，加速度前馈项对电流参考的贡献为：

`AccTerm = 1000 x 2560 x (1 / 256) = 10000`（电流单位）

前馈将此电流提前注入到环路中，速度环无需建立跟随误差来产生加速电流。

### 操作步骤：配合加速度前馈和速度前馈

`AccFFW` 与 [VelFFW](VelFFW.md) 在环路中的同一点求和（合并前馈输出叠加到速度环输出上构成电流参考），通常需要一起配置。

1. **在第 1 组上启用两个前馈**（不启用调度）。从两者均为零开始，然后写入计算或测量所得的值：

   ```text
   AAccFFW[1]=2560
   AVelFFW[1]=65536
   ```

2. **可选：应用前馈滤波器**，对合并前馈输出进行平滑（当参考存在量化或噪声时有用）：

   ```text
   AFFFiltDef[1]=1; AFFFiltDef[2]=100000   ; first-order low-pass at 1 kHz
   AFFFiltOn[1]=1
   ACalcFilters
   ```

3. **运行一次规划运动**，读取环路侧电流参考 [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md)（v5），观察叠加在速度 PI 输出上的前馈贡献。在匀加速阶段 `AccFFW` 项占主导；在匀速阶段 `VelFFW` 项占主导。

4. **观察 [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) 位 21**（电流饱和）。尺寸正确的前馈组合可减少位置/速度环需要建立的跟随误差，从而降低加速阶段电流指令饱和的可能性。

## 另请参见

- [VelFFW](VelFFW.md) — 速度前馈增益（与加速度项求和）
- [FFFiltOn](FFFiltOn.md) / [FFFiltDef](FFFiltDef.md) — 应用于合并前馈输出的前馈滤波器
- [CurrRefCtrl](../../../02-keywords/09-current-and-voltage/02-motor-variables/CurrRefCtrl.md) — 前馈叠加到其上的电流参考
- [PosGain](../03-position-control/PosGain.md) — 该前馈有助于抑制误差的位置环增益
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — 进入速度环参考的速度前馈（并行路径）
- [ScheduleMode](../../../02-keywords/11-control-tuning/01-general-keywords/ScheduleMode.md) — 增益调度的数组元素选择
