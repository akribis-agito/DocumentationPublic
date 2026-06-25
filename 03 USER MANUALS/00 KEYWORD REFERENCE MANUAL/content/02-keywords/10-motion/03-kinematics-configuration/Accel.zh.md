---
keyword: Accel
summary: 点到点运动的加速度，单位为用户单位每二次方秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 136
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 100.0
    - 686700000000.0
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Accel

点到点运动的加速度，单位为用户单位每二次方秒。

## 概述

`Accel` 是轨迹规划器在将轴向指令 [Speed](Speed.md) 加速时所保持不超过的加速度限值。它是运动规划器据以塑形运动的四个核心运动学限值之一——`Speed`、`Accel`、[Decel](Decel.md) 以及加加速度设置。减速侧由 `Decel` 单独设置；数值由 [AccelFact](AccelFact.md) 缩放；斜坡起止的陡缓程度则由 [Jerk](Jerk.md)（二阶）或 [JerkInAcc](JerkInAcc.md)/[JerkInDec](JerkInDec.md)（三阶）控制，并由 [JerkMode](../02-motion-configuration/JerkMode.md) 选择。

`Accel` 为读/写、轴范围且保存至闪存。它可在任意时刻更改，包括在运动过程中——运动规划器每个控制周期都会重新读取它，因此新值在下一个周期生效。

## 工作原理

### 每个周期的有效加速度

运动规划器每个控制周期运行一次（标准伺服速率为 16,384 Hz，采样时间约 61 µs）。每个周期它将 `Accel` 与整数缩放因子 [AccelFact](AccelFact.md) 的乘积作为**有效加速度**：

$$
\text{Accel}_{\text{eff}} = \text{Accel} \cdot \text{AccelFact}
$$

在正常加速阶段，运动规划器的速度随后每个周期增加 `Accel_eff × T_s`（控制周期采样时间），直到达到 `Speed`：

$$
v_{k} = v_{k-1} + \text{Accel}_{\text{eff}} \cdot T_s ,\qquad v_k \le \text{Speed}
$$

由于 `Accel` 和 `AccelFact` 每个周期都会重新读取，在运动中途更改任一者都会立即改变速度斜坡的斜率。

### 减速距离限制（梯形）

运动规划器不会盲目加速到 `Speed`。每个周期它根据到 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) 的剩余距离，计算出仍能使用 `Decel` 及时停车的速度：

$$
v_{\text{dec}} = -\text{Decel}_{\text{eff}}\,T_s + \sqrt{\text{Decel}_{\text{eff}}^{2}\,T_s^{2} + 2\,\text{Decel}_{\text{eff}}\,(\text{target} - \text{PosRef})\,T_s}
$$

`Accel` 将速度提升至 `Speed`；该 `v_dec` 钳位则在目标临近时将其降低。两者共同产生经典的梯形（或在短距离运动时为三角形）速度曲线。因此 `Accel` 设定梯形的**前缘斜率**；`Decel` 设定后缘斜率。

### 点动与操纵杆运动

同样的 `Accel_eff = Accel × AccelFact` 构造也用于点动模式和操纵杆间接速度模式。操纵杆**直接**速度模式通过将内部加/减速度强制设为一个很大的值来绕过斜坡，因此除停车期间外，那里不使用 `Accel`。

### 何时不使用 Accel

- 在限位开关、软件位置限位或受控停止输入上的受控停止会以 [EmrgDec](EmrgDec.md) 替代减速度；`Accel` 仍然控制任何再加速。
- 在三阶模式（[JerkMode](../02-motion-configuration/JerkMode.md) = 1）下，`Accel` 是传递给结构化加加速度规划器的**峰值加速度**约束，规划器以 `JerkInAcc` 设定的速率将加速度斜升至该值，而非瞬间跳变至该值。

### 加速度整形

如果启用了加速度整形（[AccShapeOn](AccShapeOn.md) ≠ 0），有效加速度还会额外乘以一个由 [AccShapeDist](AccShapeDist.md)/[AccShapeFact](AccShapeFact.md) 表插值得到的、与位置相关的因子，因此 `Accel` 成为整形所缩放的基准值。

### 边界情况

- **电机失能：** 数值保持不变；不运行运动规划器计算。
- **越界写入：** 参数系统将写入钳位到 `100`–`2,000,000,000` 用户单位/s²；超出范围的值被拒绝。
- **仿真模式（`MotorType` = 5）：** 行为不变；运动规划器在仿真中运行。
- **ModRev 环绕：** 无关——`Accel` 是运动学速率，而非位置。
- **存在活动故障：** 轴被禁用且运动规划器停止；下一次 `Begin` 会重新读取 `Accel`。
- **其他运动模式：** `Accel` 被点动、PTP、重复 PTP、PD 间接、齿轮间接和操纵杆间接模式所使用。直接模式（PD、齿轮、ECAM、FIFO、CNC、矢量、操纵杆位置直接/速度直接、从轴、样条）忽略 `Accel`，因为用户直接提供位置指令；例外是这些模式中的受控停止，它使用 [EmrgDec](EmrgDec.md) 而非 `Accel`。
- **操纵杆速度直接（`MotionMode = 14`）：** 内部将 `Accel` 设得很高，因此响应基本上是一个阶跃；用户的 `Accel` 仅在停车斜坡期间使用。
- **不能为零：** 最小值为 `100` 用户单位/s²，以保持运动规划器算术为有限值。

## 示例

```text
AAccel=200000        ; set acceleration to 200000 user units/s^2
AAccel               ; read current acceleration
```

## 版本间的变更

在 **v4** 中，`Accel` 是 32 位整数（counts/s²）。在 **v5（central-i）** 中，它是单精度浮点数；运动规划器的 `Accel × AccelFact` 构造、梯形限制和加加速度交互在其他方面保持不变。**v5 仅限 central-i**——在 standalone 上 `Accel` 仍为 v4 的 32 位值。

## 另请参阅

- [Decel](Decel.md) — 减速度（梯形的后缘斜率）
- [Speed](Speed.md) — 斜坡加速所趋向的巡航速度
- [AccelFact](AccelFact.md) — 每个周期施加于 `Accel` 的整数乘数
- [Jerk](Jerk.md) — 斜坡的二阶 S 曲线平滑
- [JerkInAcc](JerkInAcc.md) — 三阶模式下加速阶段的加加速度
- [JerkMode](../02-motion-configuration/JerkMode.md) — 选择二阶还是三阶规划
- [EmrgDec](EmrgDec.md) — 在受控/限位停止时替代 `Decel`
- [AccShapeOn](AccShapeOn.md) — 与位置相关的加速度整形
