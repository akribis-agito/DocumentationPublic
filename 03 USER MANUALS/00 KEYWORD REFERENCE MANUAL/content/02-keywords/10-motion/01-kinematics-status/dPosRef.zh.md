---
keyword: dPosRef
summary: 速度参考，即位置参考 PosRef 的滤波微分。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 155
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
# dPosRef

速度参考，即位置参考 PosRef 的滤波微分。

## 概述

`dPosRef` 是速度参考，计算为位置参考 [PosRef](PosRef.md) 的滤波微分。该滤波器是由 [dPosRefFilt](../../11-control-tuning/04-velocity-control/dPosRefFilt.md) 定义的一阶低通滤波器。它是馈入速度环参考的速度前馈。

`dPosRef` 是*速度参考*，不可与 [VelRef](VelRef.md)（*速度环参考/输入*）混淆。`VelRef` 是位置控制器输出与缩放后的速度参考之和，而 `dPosRef` 纯粹是 `PosRef` 的（滤波）微分。

## 工作原理

每个控制周期，在电机使能时，控制器取经完整后处理的参考（经整形+滤波的位置参考，即位置环所用的同一信号）的逐周期变化，并可选地对其进行低通滤波：

$$
\Delta = (\text{shaped/filtered reference}) - (\text{previous shaped/filtered reference})
$$

- **无滤波**（[dPosRefFilt](../../11-control-tuning/04-velocity-control/dPosRefFilt.md) 系数 = 1.0）：`dPosRef = Δ` 直接采用。
- **带滤波：** 应用一阶低通。为在宽动态范围内保持精度，滤波器在内部上缩放的值上运行（缩放 ×16），使分数步进不丢失，然后再向下移位还原。一个 1 计数的残差修正在稳态时将输出对齐到 `Δ`，从而精确跟踪斜坡指令。

电机失能时，`dPosRef`（及其缩放后的滤波器状态）被复位为 `0`，使滤波器在下次使能时从干净状态开始。作为特例，对于 CNCA/B 或矢量运动的成员轴，若其主轴指示其跳过该计算，则 `dPosRef` 保持不变，以避免在以零速结束的段末出现尖峰。

`dPosRef` 随后成为 [VelRef](VelRef.md) 中的速度前馈：$\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}$，其中 [VelTrackFact](../../11-control-tuning/04-velocity-control/VelTrackFact.md) 缩放前馈的施加量。

### 边界情况

- **电机失能：** `dPosRef` 及其内部缩放 ×16 的滤波器状态均复位为 `0`；下次电机使能时滤波器从干净状态开始。
- **仿真模式（`MotorType` = 5）：** 计算照常运行（固件中的注释明确指出，它必须在仿真中运行，以使合成环路跟踪斜坡）。
- **CNC / 矢量成员轴：** 若 CNC 或矢量主轴要求成员轴跳过 `dPosRef` 计算，则该周期 `dPosRef` 保持不变，以避免在零结束速度的段末出现尖峰。
- **ModRev 回绕：** 回绕在同一周期内以相同量移动当前经整形+滤波的参考及其上一周期值，因此逐周期增量——从而 `dPosRef`——在回绕过程中得以保留。
- **超出范围写入：** `dPosRef` 为只读。
- **活动故障：** 轴被禁用——`dPosRef` 保持为 `0`（与电机失能路径相同）。
- **龙门：** `dPosRef` 由各轴的参考按轴计算；它不进行龙门共模/相位拆分。

## 示例

```text
AdPosRef            ; read the current velocity reference
```

## 版本间变更

在 **v5（central-i）** 中，微分基于 64 位参考计算，其值为 64 位；逐周期差值计算、`dPosRefFilt` 低通和电机失能复位均相同，且它仍用作 `VelRef` 中的速度前馈。**v5 仅限 central-i。**

## 另请参阅

- [PosRef](PosRef.md) — 位置参考，本微分的来源
- [dPosRefFilt](../../11-control-tuning/04-velocity-control/dPosRefFilt.md) — 施加于微分的低通滤波器
- [VelTrackFact](../../11-control-tuning/04-velocity-control/VelTrackFact.md) — `VelRef` 中施加于 `dPosRef` 的前馈增益
- [VelRef](VelRef.md) — 速度环参考/输入（不同信号）
