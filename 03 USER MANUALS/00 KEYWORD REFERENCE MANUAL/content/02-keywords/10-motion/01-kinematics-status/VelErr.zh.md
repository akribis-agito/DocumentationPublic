---
keyword: VelErr
summary: 速度误差（参考值减去反馈值），用于控制和保护。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 19
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VelErr

速度误差（参考值减去反馈值），用于控制和保护。

## 概述

`VelErr` 报告速度参考值与速度反馈值之间的误差，单位为主用户单位每秒。它是位置误差 [PosErr](PosErr.md) 的速度环对应量，也是速度 PI 控制器（及其高速度误差保护）所作用的信号。

`VelErr` 仅在轴使能且处于位置或速度运行模式（或力矩覆盖 PIV 模式）且非开环时报告；否则强制为 `0`。

### 符号约定

`VelErr` 遵循与 [PosErr](PosErr.md) 相同的参考值减反馈值符号规则：正值表示指令速度高于测量速度（负载滞后——环路加速），负值表示负载速度高于指令速度（环路制动）。`VelErr` 的符号即速度环将施加的修正力矩/电流的符号。

例如，当 `VelRef = 50000` 用户单位/s 且 `Vel[1] = 49500` 时，`VelErr = +500`；当 `Vel[1] = 50200` 时，`VelErr = -200`。

## 工作原理

`VelErr` 在每个控制周期计算为（饱和后的）速度参考值减去速度环反馈 `Vel[1]`：

$$
\text{VelErr} = \text{VelRef} - \text{Vel}[1]
$$

由于被减数为 [Vel](Vel.md)`[1]`，`VelErr` 实际测量的对象随环路配置而变化：`Vel[1]` 通常为主编码器导数，在双环模式下为（缩放后的）[AuxVel](AuxVel.md)，在模拟测速机双环模式下为模拟测速机，在龙门模式下（A/B 轴）为 [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md)。误差公式本身不因配置而分支——配置在上游改变 `Vel[1]`。

### 强制为零的条件

对于步进开环电机（`MotorType` = 6），以及当 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) 既非位置控制也非速度控制且力矩覆盖 PIV 关闭时，`VelErr` 设为 `0`。因此在电流控制或力控制模式下，`VelErr` 报告为 `0`，除非力矩覆盖 PIV 使能——此时保留实时误差并馈入速度 PI 积分项，以防切换回位置/速度控制时电流指令发生跳变。

### 高速度误差保护

计算 `VelErr` 后，控制器在位置/速度/力矩 PIV 模式下将其幅值与 [MaxVelErr](../../06-protections/03-motion/general-maximum-limits/MaxVelErr.md) 比较；超限时禁用轴，[ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1021（速度误差超过限值）。当相关 `MaxErrStat` 位指示开环时，改用 [MaxVelErrOL](../../06-protections/03-motion/general-maximum-limits/MaxVelErrOL.md) 作为阈值，报告故障码 1056（开环状态下速度误差超过限值）。此检查对模拟速度指令驱动器跳过。否则 `VelErr` 驱动速度 PI（增益 × 误差，累积进速度积分项）。

### 边界情况

- **电机失能 / 换相未完成：** 速度环不运行；积分项保持；`VelErr` 因上述条件强制为 `0`。
- **仿真模式（`MotorType` = 5）：** 速度环被旁路，因此 `VelErr` 不重新计算，保持上次值（来自最近一次电机失能时的 `0`）。
- **电流 / 力控制运行模式：** `VelErr` 强制为 `0`，除非力矩覆盖 PIV 使能。力矩覆盖 PIV 使能时，保留实时误差并馈入速度 PI 积分项，防止轴返回位置或速度模式时电流指令发生跳变。当模式既非位置、速度也非力矩覆盖 PIV 时，跳过高误差跳闸检查。
- **ModRev 环绕：** 由于 `Vel[1]` 是在环绕修正后从 `ΔPos` 构建的（参见 [Vel](Vel.md)），环绕不会出现在 `Vel[1]` 中，因此不会在 `VelErr` 中产生尖峰。
- **超出范围写入：** `VelErr` 为只读——写入被拒绝。
- **活动故障：** 轴被禁用——`VelErr` 强制为 `0`；[ConFlt](../../07-status-and-faults/ConFlt.md) 快照字段记录跳闸时刻的值。
- **龙门：** 龙门使能时，`Vel[1] = GantryVel`（龙门共模/相速度），因此 `VelErr` 自动成为龙门速度误差。

## 示例

```text
AVelErr             ; read the current velocity error
```

## 版本变更

在 **v5（central-i）** 中，`VelErr` 为 64 位值（`VelErr = VelRef − Vel[1]`），范围如前置数据所示，并与缩放后的 64 位 `MaxVelErr` 比较；置零条件和 PI 使用方式保持不变。**v5 仅适用于 central-i。**

## 另请参阅

- [VelRef](VelRef.md) — 速度环参考值（被减数）
- [Vel](Vel.md) — 反馈速度数组（非龙门模式下 `Vel[1]` 为减数）
- [GantryVel](../../12-gantry-control/03-gantry-tuning/GantryVel.md) — 龙门模式下使用的反馈值
- [MaxVelErr](../../06-protections/03-motion/general-maximum-limits/MaxVelErr.md) — 禁用轴的闭环误差阈值
- [MaxVelErrOL](../../06-protections/03-motion/general-maximum-limits/MaxVelErrOL.md) — 开环等效阈值
- [PosErr](PosErr.md) — 位置误差对应量
