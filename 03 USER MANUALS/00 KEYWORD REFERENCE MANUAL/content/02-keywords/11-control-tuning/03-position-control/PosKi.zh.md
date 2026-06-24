---
keyword: PosKi
availability:
  standalone: []
  central-i:
  - v5
can_code: 714
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 位置环积分增益（central-i v5）——对经缩放的位置控制器输出进行累积，以在速度指令中加入积分项。
---
# PosKi

位置环积分增益（central-i v5）——对经缩放的位置控制器输出进行累积，以在速度指令中加入积分项。

## 概述

`PosKi` 是外环（位置环）的积分增益。它将位置控制器转变为 PI 控制器：[PosGain](PosGain.md) 单独提供比例指令，而 `PosKi` 随时间累积该比例输出，并将累积值加入速度环参考值 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)。这使位置环能够将稳态位置误差驱动至零。

`PosKi` 仅在 **central-i v5** 上可用。它是一个数组，因此可以参与增益调度；未使用调度时，使用第一个元素 `PosKi[1]`。请参阅 [ScheduleMode](../01-general-keywords/ScheduleMode.md)。

## 工作原理

每个控制周期，（经滤波的）位置误差被 [PosGain](PosGain.md) 乘以形成比例项。`PosKi` 随后将该比例项相乘，结果加入运行中的位置积分器。比例项加上位置积分，以及速度前馈，共同构成速度环参考值：

$$
\text{VelRef} = \left( \text{PosErr} \cdot \text{PosGain} \right) + \int \left( \text{PosErr} \cdot \text{PosGain} \cdot \text{PosKi} \right) \, dt + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

- **乘以对象：** 位置控制器比例输出。（可选经滤波，参见 [PosFiltOn](PosFiltOn.md) 索引 2）位置误差被 [PosGain](PosGain.md) 乘以形成比例项，`PosKi` 随后对该项进行积分——即 `PosKi` 在乘积（`PosErr_filt × PosGain`）进入积分累加器之前将其相乘。
- **相加位置：** 累积的积分与比例项和速度前馈相加，构建 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)。
- **抗积分饱和：** 积分饱和值由内部控制。位置积分增量受三个级联抗积分饱和条件约束。若速度参考在位置误差持续推入钳位方向时被钳位至 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)（[StatReg](../../07-status-and-faults/StatReg.md) 位 23），则积分器在该周期内保持不变；若下游任一环路饱和——速度环达到电流限制（位 21）或电流环达到电压限制（位 22）——积分器同样冻结。以上任一条件均会冻结位置积分器，防止其在下游饱和阶段后方产生积分饱和。
- **默认值：** `0`（位置积分禁用，位置环为纯比例）。

## 示例

```text
APosKi[1]=2.5       ; 启用位置环积分项（第一个调度元素）
APosKi[1]           ; 读取位置环积分增益
```

### 演练：添加位置积分并观察稳态效果

该场景在已整定好的比例位置环基础上添加 v5 位置积分，并使用速度饱和状态位确认环路未触及 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)。

1. **确认比例位置环已就位**：

   ```text
   APosGain[1]                  ; 应为非零值
   ```

2. **添加积分项**（调度关闭时保存在组 1 中）：

   ```text
   APosKi[1]=2.5
   ```

3. **指令稳态保持**（轴静止于目标位置）。仅使用 `PosGain` 时，任何恒定残余力（重力、摩擦偏置）都会留下小的 `PosErr`；当 `PosKi > 0` 时，累加器持续累积，直至 `PosGain*PosErr + 积分` 之和足以平衡该力，将稳态误差驱动至零。

4. **在积分器上升期间检查 [StatReg](../../07-status-and-faults/StatReg.md) 位 23**：

   ```text
   (AStatReg & 0x800000) >> 23   ; 速度饱和
   ```

   若位 23 读取为 `1`，则位置环 PI 输出请求超过 `MaxVel`，速度参考被钳位，该周期积分器抗饱和已激活。若保持 `0`，则积分器正在自由累积。

> **注意。** [ClearIntegral](../01-general-keywords/ClearIntegral.md) 仅清除*速度*环积分器；位置环积分器不受该指令影响。若需干净地重置位置积分，请禁用电机后重新使能，或临时将 `PosKi` 设置为 `0`。

## 另请参阅

- [PosGain](PosGain.md) — `PosKi` 对其输出进行积分的比例增益
- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — 位置环输入处的位置误差
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — 由位置 PI 输出形成的速度环参考值
- [VelKi](../04-velocity-control/VelKi.md) — 内环（速度环）的积分增益
- [ClearIntegral](../01-general-keywords/ClearIntegral.md) — 清除速度环积分器（**不**影响位置积分器）
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 23（速度饱和），显示 PI 输出被钳位的时机
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — 选择哪个数组元素处于激活状态
