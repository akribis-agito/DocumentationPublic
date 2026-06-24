---
summary: 动态制动——通过短接电机相快速使电机停止（DynBrakeOn、DynBrkRef）。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Dynamic brake

动态制动通过短接电机相（经由低边 MOSFET）并耗散由反电动势产生的电流，从而快速使电机减速。当电机突然被禁用时，这是一种安全的停机方式。本页介绍 `DynBrakeOn` 和 `DynBrkRef`。

## 工作原理

### 接入条件

每个控制周期，驱动器仅在**同时**满足以下两个条件时才接入动态制动：

1. `DynBrakeOn ≠ 0`（功能已使能）；以及
2. 电机**失能**（`MotorOn = 0`）。

第三个条件——即没有任何禁止动态制动的活动 [ConFlt](../../07-status-and-faults/ConFlt.md)（依据逐故障许可表）——**仅**适用于 PWM 驱动器的次级轴（B 轴，以及 3 轴产品上的 C 轴）。在 PWM 驱动器的主轴（A）以及中央控制器产品的**所有**轴上，该逐故障检查被绕过，因此只要 `MotorOn = 0` 且 `DynBrakeOn ≠ 0`，无论是否存在活动的 `ConFlt`，制动都会接入。

接入时，驱动器激活动态制动并设置 [StatReg](../../07-status-and-faults/StatReg.md) **bit 28**（动态制动激活）；高边 MOSFET 被强制关断，仅低边器件由 PWM 驱动。如果任一条件不满足，制动被释放且状态位被清除。在 PWM 驱动器上，动态制动在 A 轴和 B 轴（以及 3 轴产品上的 C 轴）受支持。

### 制动占空比与电流限制

接入期间，短接占空比每个周期根据电流限制下方剩余的余量计算：

$$
\text{DynBrk} = \frac{\text{PeakCL}_{limited} - |\text{MotorCurr}|}{\text{PeakCL}_{limited}} \times \text{DynBrkRef} \times scaler
$$

- 结果被钳位至 `[0, DynBrkRef]`，因此当制动电流向 [PeakCL](../02-current-and-voltage/PeakCL.md)/[ContCL](../02-current-and-voltage/ContCL.md) 限制上升时，占空比会自动回退——驱动器内部减小占空比，以将电流保持在限制范围内。
- `scaler` 是一个软启动斜坡，从 **0.1** 开始，每周期递增 **0.3**，直至 1.0，因此制动是逐渐接入而非阶跃式接入的。
- **母线电压保护：** 如果母线电压达到 [MaxVBus](../02-current-and-voltage/MaxVBus.md)（持续超过 [MaxVBusTime](../02-current-and-voltage/MaxVBusTime.md)）或 [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md)，占空比将被强制为 0，以避免将能量泵回已经偏高的母线。

## DynBrakeOn

使能或禁用动态制动。默认 0（禁用）。

| 取值 | 说明 |
|-------|-------------|
| 0 | 禁用 |
| 1 | 使能 |

## DynBrkRef

设置用于动态制动的最大短接占空比——即上述余量公式向下缩放的起点，亦即最强制动的上限。越大 = 制动越强。其范围/默认值覆盖整个 PWM 范围。如果制动电流将超过 [ContCL](../02-current-and-voltage/ContCL.md)/[PeakCL](../02-current-and-voltage/PeakCL.md)，控制器会在内部减小所施加的占空比，以将电流保持在限制范围内。

> **未找到 `DynBrakeSpeed`：** 早期草稿曾列出 `DynBrakeSpeed` 关键字。在 v4（LTS）固件中并不存在此类关键字；接入的软启动“速度”由上述斜坡（0.1 → 1.0，步长 0.3）固定，不可由用户配置。

### 边界情况

- **电机使能：** 动态制动**仅**在电机失能时接入——它无法对抗活动的电流环输出。
- **模式依赖性：** 接入与 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 无关；它取决于 `MotorOn`、`DynBrakeOn`，以及——仅在 PWM 驱动器的次级轴（B 轴，以及 3 轴产品上的 C 轴）上——逐故障许可表。
- **某些故障禁止：** 在 PWM 驱动器的次级轴（B 轴，以及 3 轴产品上的 C 轴）上，特定的 [ConFlt](../../07-status-and-faults/ConFlt.md) 故障码通过逐故障许可表禁止动态制动（例如接地短路、IPM 故障）——在这些情况下，即使 `DynBrakeOn ≠ 0`，制动也保持释放。该逐故障门控在 PWM 驱动器的主轴（A）以及中央控制器产品上被绕过，此时即使存在活动的 `ConFlt`，制动仍会接入。
- **母线过压：** 如果母线电压达到 [MaxVBus](../02-current-and-voltage/MaxVBus.md)（持续超过 [MaxVBusTime](../02-current-and-voltage/MaxVBusTime.md)）或 [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md)，占空比将被强制为 `0`，以避免将更多再生能量泵入已经偏高的母线。
- **`DynBrakeOn = 0`：** 制动从不接入，且 [StatReg](../../07-status-and-faults/StatReg.md) bit 28 从不置位。
- **范围溢出 / 静默饱和：** 计算出的占空比每个周期被钳位至 `[0, DynBrkRef]`；对 `DynBrkRef` 写入超出关键字 `range` 的值会被钳位。

## 参见

- [Static brake](Staticbrake.md) — 抱闸（静态制动器）控制
- [ContCL](../02-current-and-voltage/ContCL.md) / [PeakCL](../02-current-and-voltage/PeakCL.md) — 限制制动的电流限值
- [MaxVBus](../02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../02-current-and-voltage/MaxVBusAbs.md) — 强制占空比为 0 的母线电压上限
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 28 报告动态制动激活
