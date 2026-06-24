---
keyword: MaxMotorCurr
summary: 电机电流的硬限制；超过该值将禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 99
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
  - 76000
  default: 76000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MaxMotorCurr

电机电流的硬限制；超过该值将禁用轴。

## 概述

`MaxMotorCurr` 是允许的最大电机电流（`MotorCurr`），单位 mA。与 I²t 方案（用于*限制*持续电流）不同，本项是快速过流**跳闸**：一旦超过，轴将被禁用并触发故障。

> **注意：** 对于三相电机，`MotorCurr` 是电机电流相量的幅值。

## 工作原理

驱动器在每个控制周期将 `|MotorCurr|` 与 `MaxMotorCurr` 进行比较，并运行一个消抖计数器：

- 若 `|MotorCurr| > MaxMotorCurr`，过流计数器递增；否则复位为 0。
- 当计数器达到 **4 个连续采样（≈ 0.25 ms）** 时，轴将被禁用，[ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1016（电机电流过高），并附带快照及一条 [ErrLog](../../07-status-and-faults/ErrLog.md) 记录。

![Sample-by-sample over-current debounce: the counter increments on each consecutive over-limit sample and resets to 0 on any below-limit sample; only 4 unbroken over-limit samples cause a trip](overcurrent-debounce.svg)

较短的 4 采样窗口可剔除单周期测量尖峰，同时在真正发生过流时仍能快速跳闸。由于它监测的是总电机电流，请同时使用 [MaxPhaseCurr](MaxPhaseCurr.md) 以捕获总电流看似正常时的单相故障（例如堵转）。

### 边界情形

- **电机失能/非电流模式：** 过流检查仅在电机使能、电机类型不是仿真类型（见 [MotorType](../../02-motor-and-amplifier/MotorType.md)）且驱动器类型不是位置检测器（PD）类型（见 [AmpType](../../02-motor-and-amplifier/AmpType.md)，此类型下电流环被旁路）时运行。每当检查被跳过（电机失能、仿真或 PD）时，固件会复位过流计数器，因此下次恢复检查时将从干净状态开始。
- **模式依赖性：** 该跳闸不论运行模式如何均会运行（它是硬件安全检查，而非闭环状态检查）。
- **与 `PeakCL`/I²t 的独立性：** 这是瞬时过流跳闸，而非电流限制——它独立于 [PeakCL](PeakCL.md)/[ContCL](ContCL.md) 的 I²t 方案。被 `PeakCL` *限制*的电流通常不会达到 `MaxMotorCurr`；应将 `MaxMotorCurr` 设置在 `PeakCL` 之上，使跳闸仅捕获真正的故障。
- **范围溢出：** 写入超出 `0…76000`（v4）范围的值会被拒绝并返回越界错误，存储值保持不变。
- **清除故障：** ConFlt 故障码 1016 在重新使能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../07-status-and-faults/ErrLog.md) 记录则保留。
- **HWProtectBits / ProtectMask：** 电机过流跳闸无法通过 [ProtectMask](../01-general-protection/ProtectMask.md) 屏蔽。[HWProtectBits](../01-general-protection/HWProtectBits.md) 中独立的硅片级过流位（触发 ConFlt 故障码 1025 / 1036 / 1059）同样不可屏蔽——它们无论 [ProtectMask](../01-general-protection/ProtectMask.md) 如何均被强制开启；只有主编码器（第 2 位）和辅助编码器（第 3 位）保护可屏蔽。

## 版本间变更

在 **v4** 中 `MaxMotorCurr` 为 32 位整数；在 **v5**（仅 central-i）中为 32 位浮点数（`float32`）。过流跳闸机制保持不变。

## 示例

```text
AMaxMotorCurr=50000  ; trip if motor current exceeds 50 A (mA units)
```

## 参见

- [MaxPhaseCurr](MaxPhaseCurr.md) — 单相过流跳闸
- [PeakCL](PeakCL.md) / [ContCL](ContCL.md) — 电流限制（区别于跳闸）
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 跳闸时触发故障 1016
