---
keyword: Vel
summary: 反馈速度数组；每个元素对应一种不同的速度估算方法。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 5
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Vel

反馈速度数组；每个元素对应一种不同的速度估算方法。

## 概述

`Vel` 是一个数组，用于报告反馈速度，每个元素采用不同的速度计算或近似方法（简单导数、移动平均以及 1/T 方法——在可测量时间内的固定位置变化量）。

`Vel[1]` 是非龙门模式下速度环的反馈值，因此其含义随龙门模式和双环条件的变化而改变。`Vel[4]` 是 1/T 测量值，由 [OneOverTOn](OneOverTOn.md)、[OneOverTFreq](OneOverTFreq.md) 和 [OneOverTGap](OneOverTGap.md) 控制；当 1/T 测量禁用时报告 `0`。速度误差 [VelErr](VelErr.md) 由 `Vel[1]` 推导得出。

## 工作原理

### 数组元素

所有元素的单位均为主用户单位每秒。基本估算值为每个控制周期的位置变化量乘以采样频率，即 `ΔPos × 每秒采样数`。由于采样率是 2 的幂，该缩放通过左移实现（在独立模式采样率下移位 14 位，在快速采样率下移位 16 位），而非乘法运算。

| 索引 | 方法 |
|-------|--------|
| `Vel[1]` | **速度环反馈** — 实际用于闭合速度环的值。根据环路配置选取（见下文）。 |
| `Vel[2]` | 主编码器的简单后向导数（`ΔPos × 每秒采样数`）。 |
| `Vel[3]` | `Vel[2]` 的 32 次采样移动平均。 |
| `Vel[4]` | **1/T 测量** — 在精确计时区间内测量的位置变化量；参见 [OneOverTOn](OneOverTOn.md)。 |

`Vel[0]` 不由控制周期产生。该关键字以轴前缀语法 `AVel[n]` 读取。

`Vel[3]` 是 `Vel[2]` 的精确 32 次采样滑动窗口平均，而非指数滤波器：每个控制周期将存储的 32 个样本中最旧的替换为最新的，并将累积和除以 32。在独立模式采样率下，32 次采样窗口约跨 2 ms；在快速采样率下约跨 0.5 ms。窗口历史记录和累积和仅在控制器启动时清除一次——不会在电机失能或故障时复位，因此 `Vel[3]` 在这些切换期间保留上次的样本，直到窗口重新填满。

### Vel[1] 的选择方式

`Vel[1]` 是速度环使用的速度值，其含义随双环/龙门配置变化。双环优先；若双环关闭，龙门模式在 A/B 轴上覆盖；否则 `Vel[1]` 跟随主编码器导数。

| 优先级 | 配置 | `Vel[1]` 来源 |
|---|---------------|-----------------|
| 1 | 双环（[DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1） | [AuxVel](AuxVel.md) $\times \frac{\text{DualLoopFact}}{65536}$，当 [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) $\ge 1$ 时（`Vel[1]` 以主编码器单位表示）。当 `DualLoopFact` $< 1$ 时反馈增益为 1.0，因此 `Vel[1]` 保持辅助编码器单位，速度环*指令*（[VelRef](VelRef.md)）改为按 $\frac{1}{\text{DualLoopFact}/65536}$ 缩放。 |
| 2 | 模拟测速机双环（`DualLoopOn` = 2） | 经滤波的模拟测速机输入 |
| 3 | 龙门使能（A/B 轴，无双环） | 龙门速度（[GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md)） |
| 4 | 正常（无双环，无龙门） | `Vel[2]` — 主编码器导数 |

`Vel[1]` 直接从所选反馈赋值（它是原始选定速度，未单独滤波）。类型转换是唯一的后处理步骤；所有速度滤波在速度控制器的下游完成。

`Vel[1]`（及速度参考）以主编码器还是辅助编码器单位表示，取决于 [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md)：当 `DualLoopFact` ≥ 1 时反馈缩放至主编码器单位；当 `DualLoopFact` < 1 时反馈保留辅助编码器单位，指令改为缩放。两端始终保持相同单位。

![Vel[1] 反馈选择](vel-feedback-selection.svg)

### 1/T 测量（Vel[4]）

`Vel[1]`、`Vel[2]` 和 `Vel[3]` 在控制采样的前半段计算，*早于*位置、速度、加速度和电流控制滤波器运行，因为它们为控制环提供输入。`Vel[4]` 在采样的后半段计算，*晚于*控制滤波器，因为其 1/T 计算涉及一次相对较慢的除法运算，且结果仅用于显示和记录，从不用于控制。[OneOverTOn](OneOverTOn.md) 仅控制每个控制周期是否执行该除法（以节省处理时间）：当 1/T 测量关闭时跳过除法，`Vel[4]` 报告 `0`。

> **注意：**
>
> 1. 竖线表示控制器采样时刻。
> 2. 间隔为 1（`OneOverTGap = 0`），轮询频率为 300 MHz（`OneOverTFreq = 0`）。
> 3. 在第零个控制周期/中断时 `Vel[4] = 0`。
> 4. 在第零次和第一次控制中断之间，硬件记录 12000 个轮询周期内位置变化 1 计数，并保存该值。在第一次控制中断时，控制器从硬件读取该值并计算 `Vel[4]`。
> 5. 在第二次和第三次控制中断之间，硬件更新两次，因为位置变化 1 计数发生了两次。第一次更新值为 7200 个轮询计数；第二次更新值为 4800 个轮询计数。

有关双环控制类型的更多信息，请参阅 [控制整定 – 双环控制](../../11-control-tuning/02-dual-loop-control/00-overview.md)。

### 边界情况

- **电机失能：** `Vel[2]` 和 `Vel[3]` 继续从编码器更新（因此在禁用状态下反向驱动负载会产生非零读数）。`Vel[1]` 跟随与使能时相同的来源。`Vel[4]` 无论电机状态如何均跟随 [OneOverTOn](OneOverTOn.md)。
- **仿真模式（`MotorType` = 5）：** [Pos](Pos.md) 跟踪 [PosRef](PosRef.md)，因此 `Vel[2]/[3]` 反映*参考*速度。`Vel[4]` 为 `0`，因为没有硬件来计时编码器跳变。
- **ModRev 环绕：** 控制器在环绕时同时从 `Pos` 和 `PosPrev` 中加减 [ModRev](../../03-encoder/04-modulo-mode/ModRev.md)，因此 `ΔPos` 不会感知到环绕跳变，`Vel[2]/[3]` 在环绕处保持连续。
- **超出范围：** `Vel` 为只读；无需写入。在内部，若 `|Vel[1]|` 超过 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) 约 25% 以上，控制器会触发"速度过高"故障（`ConFlt` 1019）并禁用轴；它不会在该阈值处钳位 `Vel[1]` 或清除缓冲区。
- **活动故障：** 所有四个数组元素继续更新——它们来源于编码器而非控制环，因此在故障后仍可作为有效诊断信息。
- **龙门：** 如上所述，龙门使能时 `Vel[1]` 变为 [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md)（A 轴为线性模式速度，B 轴为相速度）；`Vel[2]/[3]/[4]` 仍为各轴独立值。

## 示例

```text
AVel[1]             ; read the velocity-loop feedback
AVel[4]             ; read the 1/T velocity measurement
```

## 版本变更

在 **v5（central-i）** 中，速度数组为 64 位，`Vel[1]` 的选择方式相同（主编码器 / 双环辅助编码器 / 模拟测速机 / 龙门）。数据类型和范围差异见前置数据。**v5 仅适用于 central-i**，因此在独立模式下 `Vel` 仍为 v4 的 32 位数组。

## 另请参阅

- [VelErr](VelErr.md) — 速度误差（`VelRef − Vel[1]`）
- [VelRef](VelRef.md) — 速度环参考值/输入
- [OneOverTOn](OneOverTOn.md) / [OneOverTFreq](OneOverTFreq.md) / [OneOverTGap](OneOverTGap.md) — 配置 `Vel[4]` 的 1/T 方法
- [DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) / [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — 更改 `Vel[1]` 的测量对象
- [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md) — 龙门模式下 `Vel[1]` 的来源
- [AuxVel](AuxVel.md) — 辅助速度（缩放前的双环反馈）
