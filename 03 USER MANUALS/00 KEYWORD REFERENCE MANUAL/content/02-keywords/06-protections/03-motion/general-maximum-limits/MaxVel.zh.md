---
keyword: MaxVel
summary: 最大闭环速度；超过该值（含 +25% 缓冲）将禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 80
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
    default: 1000000
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MaxVel

最大闭环速度；超过该值（含 +25% 缓冲）将禁用轴。

## 概述

`MaxVel` 是所允许的最大速度，单位为用户单位/s。它在三个不同的环节起作用：对内部生成的速度参考进行饱和限幅；当测量反馈失控时触发超速故障；并作为一个验证关卡，拒绝其规划速度会超过该值的运动指令。

## 工作原理

**1. 速度参考饱和限幅（每个控制周期）。** 在速度环中，生成的速度参考被钳位至 ±`MaxVel`。发生钳位时，[StatReg](../../../07-status-and-faults/StatReg.md) 的速度饱和位（bit 23，`0x00800000`）被置位，以标记速度参考已饱和。

**2. 超速故障跳闸（每个控制周期）。** 测量得到的反馈速度会与 `MaxVel` 加上 25% 裕量进行比较：

```text
if |Vel| > MaxVel × 1.25
    turn the axis off and log the fault
```

一旦超过，轴会立即关闭，并由 [ConFlt](../../../07-status-and-faults/ConFlt.md) 记录故障码 1019（速度过高）。

**3. 指令时验证。** 在间接/带轨迹规划的模式（Jog、PTP、PD/Gear/eCam 间接模式、位置 joystick 间接模式）下，如果指令的 `Speed` 超过 `MaxVel`，则运动无法*启动*——`Begin` 会被拒绝（错误 271）。同样，在已经运动时，将 `Speed` 设置为大于 `MaxVel` 会被拒绝（错误 269），将 `MaxVel` 设置为低于当前 `Speed` 也会被拒绝（错误 270）；这两项运动中检查仅在轴处于运动状态时适用。直接模式（例如脉冲方向直接模式）不受此关卡限制，因为用户直接驱动参考；对于这些模式，机制 1 和 2 仍然适用。

### 边界情况

- **电机失能：** 超速跳闸和饱和限幅均被跳过（速度环不运行）。`Begin` 处的验证关卡是独立的，仍然适用。
- **模式依赖：** 只要电机使能，超速跳闸即生效；它不依赖于运行模式。速度环中的饱和限幅仅在速度环运行时适用。
- **所用反馈：** 超速跳闸使用瞬时反馈 `Vel[1]`（而非堵转检测所使用的深度滤波 `Vel[3]`）。
- **25% 裕量：** 跳闸阈值为 `MaxVel × 10/8 = MaxVel × 1.25`（固件使用 `(MaxVel >> 3) * 10` 以避免在高 MaxVel 值时溢出）。
- **范围溢出：** 超出有效范围（v4 上为 `0…1300000000`）的写入将以越界错误被拒绝，存储值保持不变；在 v5 上 `MaxVel` 为 `int64`，范围更宽且下界非零。
- **清除故障：** ConFlt 故障码 1019 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍然保留。
- **HWProtectBits / ProtectMask：** 超速跳闸无法通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅涵盖硬件保护位）。

## 示例

```text
AMaxVel[1]=500000     ; maximum velocity (user units/s)
AMaxVel[1]            ; read back the limit
```

## 另请参阅

- [Speed](../../../10-motion/03-kinematics-configuration/Speed.md) — 指令巡航速度；在间接模式下 `Begin` 会拒绝 `Speed > MaxVel`
- [MaxVelErr](MaxVelErr.md) — 速度跟随误差跳闸（一种不同的故障）
- [MaxAcc](MaxAcc.md) — 加速度限值
- [VelRef](../../../10-motion/01-kinematics-status/VelRef.md) — 被针对 `MaxVel` 进行饱和限幅的信号
- [StatReg](../../../07-status-and-faults/StatReg.md) — 速度饱和位（bit 23），在速度参考被钳位至 `MaxVel` 时置位
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 在超速跳闸时记录故障码 1019（速度过高）
