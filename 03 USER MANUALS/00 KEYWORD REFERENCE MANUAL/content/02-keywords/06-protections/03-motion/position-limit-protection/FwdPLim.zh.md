---
keyword: FwdPLim
summary: 正向软件行程限位；参考位置在此处被钳位。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 83
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 2000000000
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
# FwdPLim

正向软件行程限位；参考位置在此处被钳位。

## 概述

`FwdPLim` 是正向（正方向）软件行程限位，以 counts 为单位。它是合法行程范围的上界；`RevPLim` 是下界。参考位置在正方向上绝不允许越过 `FwdPLim`，会使轴越过该限位的运动要么在 `Begin` 处被拒绝，要么减速并在限位处停止。

与 `LimitsStat` 报告的硬件限位开关（属于物理输入）不同，`FwdPLim`/`RevPLim` 是由固件计算、作用于位置参考的边界。该值保存在闪存中，且在轴运动期间不能更改。

## 工作原理

![速度-位置示意图：在合法行程区间内，规划速度 Vel 以指令值运行，随后预先制动的停止距离钳位将其曲线下降，恰好在 FwdPLim 处归零](soft-limit-decel.svg)

规划器以多个层次的方式强制执行正向限位：

**1. 预先制动（在限位处规划停止）。** 当点到点 / 点动曲线正在运行时，规划器通过停止距离的平方根公式，持续计算在当前减速度下仍能恰好停在 `FwdPLim` 处的最大速度：

```text
DecelerationSpeed = -Decel·T + sqrt(Decel²·T² + 2·Decel·(FwdPLim·2^k - PosRef)·T)
```

其中 `T` 是控制周期时间，`k` 是固件的采样频率二的幂常数（默认 16 kHz 版本为 14，快速采样 65 kHz 版本为 16）。如果规划速度超过 `DecelerationSpeed`，则将其钳位到该值，从而使轴减速并以零速度到达 `FwdPLim`，而不会过冲。

**2. 参考越过限位时的停止请求。** 如果整形/滤波后的参考在正向运动时确实越过了 `FwdPLim`，规划器会在 [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) 中发出停止请求，并记录 [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) = 7（运动在正向软件限位处结束）。当该原因生效时，停止使用紧急减速 `EmrgDec`，而非常规的 `Decel`。

**3. 参考的硬钳位。** 在多种规划器模式下，位置参考和绝对目标会被硬钳位，使其永远不能超过 `FwdPLim`。同样的硬钳位也应用于缓冲/流式（FIFO）运动路径。

**4. Begin 时刻的拒绝。** 在“处于限位之外、且指向更外侧”的情况下，运动无法启动：如果位置参考已经超出 `FwdPLim`/`RevPLim`，且运动模式不属于能驱动回到内侧的直接/点动模式之一，则 `Begin` 被拒绝（轴在位置限位之外时无法启动运动）。

**方向门控——远离限位的运动始终允许。** 正向检查（既包括软件限位，即将整形/滤波后的指令位置参考与 `FwdPLim` 比较，也包括硬件 FLS 测试）仅在规划速度为正时运行；反向检查（针对 `RevPLim`，以及硬件 RLS 测试）仅在其为负时运行。由于限位检查受速度符号门控，已经停在某一生效限位上的轴可以被驱动*远离*该限位——从 `FwdPLim` 反向移动，或从 `RevPLim` 正向移动——而不会重新发出停止请求或重新写入 [MotionReason](../../../10-motion/05-motion-status/MotionReason.md)。只有*朝向*其所在限位的运动才会被停止。

| MotionReason | 含义 |
|--------------|---------|
| 7 | 运动在正向软件限位处停止 |
| 6 | 运动在反向软件限位处停止 |

### 实时状态与停止原因

除了在停止事件时记录的一次性 [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) 6/7 之外，控制器还在 [StatReg](../../../07-status-and-faults/StatReg.md) 中报告一个连续可轮询的标志：每当整形/滤波后的位置参考超过 `FwdPLim` 时置位位 20，每当其低于 `RevPLim` 时置位位 19（否则均清零，每个控制周期重新评估）。这些仅为状态，不会引发 [ConFlt](../../../07-status-and-faults/ConFlt.md)。参见 [StatReg](../../../07-status-and-faults/StatReg.md) 位 19/20。

### 按版本的数据类型

在 central-i v5 上，限位以 64 位位置存储，将可用行程范围扩展到远超 standalone/v4 所用的 32 位范围（参见前置数据中的 `range` 覆盖）。除此之外，制动与钳位逻辑完全相同。

### 边界情况

- **电机失能：** 规划器未运行，因此不会发生预先制动。当稍后启动运动时，位置参考的硬钳位和 `Begin` 时刻的拒绝仍然生效。
- **模式相关性：** 预先制动和停止请求机制适用于间接/规划运动模式（Jog、PTP 等）。直接流式模式（例如脉冲方向直接）在规划器之外驱动参考——硬钳位仍会将其固定在 `FwdPLim`，但不会获得预先减速斜坡。
- **未到达限位但参考已越过：** 硬钳位在每个周期都生效，因此即使规划器配置错误，参考位置也不能超过 `FwdPLim`。
- **不引发故障：** 位置限位制动是一次受控减速；它**不会**引发 [ConFlt](../../../07-status-and-faults/ConFlt.md)，也不与 [ProtectMask](../../01-general-protection/ProtectMask.md) 交互。其原因仅出现在 [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) 中。
- **运动中无法更改：** `FwdPLim` 受 `ok_in_motion: false` 门控——运动期间写入会被拒绝。
- **范围溢出：** v4 关键字范围为 `−2147483648…2147483647`；v5 扩展到 ±2^51（参见前置数据 `central-i.v5` 覆盖）。

## 示例

```text
AFwdPLim[1]=1000000    ; forward soft limit (counts)
AFwdPLim[1]            ; read back the forward soft limit
```

### 操作演示：确认正向软件限位跳闸

要验证正向软件限位确实被强制执行，请点动越过它并检查停止原因：

```text
AFwdPLim[1]=100000    ; set the forward soft limit
AMotionMode=0         ; jog
ASpeed=50000          ; positive sign drives toward FwdPLim
ABegin                ; jog forward
```

规划器的预先制动会使轴减速，从而使参考以零速度到达 `100000`。停止后，检查：

```text
AMotionStat                   ; expect 0 (motion ended)
AMotionReason                 ; expect 7 (forward software limit)
ALimitsStat                   ; expect 0 (no hardware switch active)
APosRef                       ; clamped at FwdPLim (100000)
```

如果 `MotionReason` 报告的是 `5`（正向限位开关）而非 `7`，则外部 FLS 先行接合了——检查 [LimitsStat](LimitsStat.md) 位 1。无论哪种情况，停止都使用了 [EmrgDec](../../../10-motion/03-kinematics-configuration/EmrgDec.md)，而非常规的 `Decel`。

## 另请参阅

- [RevPLim](RevPLim.md) — 反向软件行程限位（同一范围的下界）
- [LimitsStat](LimitsStat.md) — 硬件限位开关状态（物理 RLS/FLS 输入）
- [MotionStat](../../../10-motion/05-motion-status/MotionStat.md) — 携带命中限位时置位的停止请求位
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — 运动在此结束时记录原因码 7
- [EmrgDec](../../../10-motion/03-kinematics-configuration/EmrgDec.md) — 此停止使用的紧急速率（而非常规的 `Decel`）
- [Decel](../../../10-motion/03-kinematics-configuration/Decel.md) — 到达限位前预先制动所使用的速率
