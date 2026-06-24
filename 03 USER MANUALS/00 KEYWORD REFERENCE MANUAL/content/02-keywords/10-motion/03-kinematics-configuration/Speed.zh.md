---
keyword: Speed
summary: 点到点和点动运动的目标（最大）速度，单位为每秒用户单位。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 138
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# Speed

点到点和点动运动的目标（最大）速度，单位为每秒用户单位。

## 概述

`Speed` 是轨迹规划器将轴加速逼近的巡航（目标）速度，单位为每秒用户单位。轴按 [Accel](Accel.md) 设定的速率加速至 `Speed`，并按 [Decel](Decel.md) 设定的速率减速至停止，从而产生梯形（或在短行程时为三角形）速度曲线。它为读/写、轴范围、保存至闪存，并可在任意时刻更改，包括运动期间。

![速度曲线：梯形与 S 曲线对比](velocity-profile.svg)

## 工作原理

### 点到点：幅值即巡航上限

在点到点运动中，规划器取 `Speed` 的**幅值**作为巡航上限；运动方向由 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) 与当前参考之间的关系决定，而不由 `Speed` 的符号决定。每个周期，规划器将其速度增加 `Accel × AccelFact × Ts`，直至达到巡航上限，然后保持该速度，直到减速距离前瞻（使用 `Decel`）强制进入制动阶段：

$$
v_k \le |\text{Speed}| ,\qquad
v_k = v_{k-1} + \text{Accel}_{\text{eff}} \cdot T_s \ \ \text{(accel phase)}
$$

如果行程太短而无法达到 `Speed`，则曲线变为三角形，且 `Speed` 永远不会被达到。

### 点动：符号设定方向

在点动（以及操纵杆间接速度）模式中，**带符号的** `Speed` 被直接用作目标速度，因此负的 `Speed` 会朝负方向点动。轴使用 `Accel` 斜坡逼近此带符号目标，并在接近软件限位或收到停止请求时使用 `Decel` 减速。

### 与 MaxVel 的关系

`Speed` 是规划器的*指令*巡航速度。它不同于速度环的硬钳位 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)，后者无论曲线如何生成，都会在下游限制速度**参考**（[VelRef](../01-kinematics-status/VelRef.md)）。frontmatter 中的范围（±1.3 × 10⁹）为允许的最大速度。在间接模式中，控制器会主动对照 `MaxVel` 防护 `Speed`：若 `|Speed| > MaxVel`，`Begin` 会被拒绝（错误 271），而运动期间发出的 `|Speed| > MaxVel` 写入会被拒绝（错误 269），因此对于这些模式，`Speed` 通常不能超过 `MaxVel`。当参考确实达到 `MaxVel` 钳位时，[StatReg](../../07-status-and-faults/StatReg.md) 的速度饱和位（位 23）会被置位，因此你可以检测到该状态。

### 实时更改

规划器每个周期都会读取 `Speed`，因此在运动途中提高或降低它，会使轴在下一个周期朝新的巡航值加速或减速。（关于运动期间由位置触发的速度更改，参见 [SpeedChgNew](SpeedChgNew.md)/[SpeedChgOn](SpeedChgOn.md)/[SpeedChgPos](SpeedChgPos.md)。）

### 边界情况

- **电机失能：** 数值被保持；不运行任何规划器计算。
- **超范围写入：** 超出 ±1.3 × 10⁹ 的写入会被拒绝（不会被钳位）；存储值保持不变。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 无关——`Speed` 是速率，而非位置。
- **存在故障：** 轴被禁用；下一次 `Begin` 会重新读取 `Speed` 并重新对照 `MaxVel` 检查。
- **`Speed = 0`：** 对于点动，轴只会减速/保持静止；对于 PTP，`Begin` 被接受且运动进入运动中状态，但由于巡航速度为零，轴不会前进——它将保持停滞，直到 `Speed` 被提高。
- **`Begin` 时 `|Speed| > MaxVel`：** 对于间接模式（点动、PTP、重复 PTP、PD 间接、齿轮间接、ecam 间接、操纵杆位置间接）会以指令错误 271（指令 `Speed` 超出 `MaxVel` 限值）被拒绝；用户必须降低 `Speed` 或提高 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)。直接模式接受任意 `Speed`，因为用户直接提供位置指令。
- **运动期间实时提高至高于 `MaxVel`：** 被拒绝。轴运动期间发出的 `|Speed| > MaxVel` 写入会以指令错误 269（`Speed` 不能被设置为高于 `MaxVel`）被拒绝；保留先前的 `Speed`。该检查仅在轴处于运动中时适用——当轴未运动时写入被接受，并改由下一次 `Begin` 对照 `MaxVel` 进行校验（错误 271）。（运动期间将 `MaxVel` 写入为低于当前 `Speed` 是对称情形，以错误 270 被拒绝。）
- **运动途中点动 `Speed = 0`：** 轴按 `Decel` 减速至停止。

## 示例

```text
ASpeed=500000        ; cruise velocity 500000 user units/s
ASpeed=-500000       ; jog in the negative direction
ASpeed               ; read current value
```

### 实例演算

在 `Speed = 500000`、`Accel = 1000000` 和 `Decel = 1000000`（均为用户单位）的情况下，一段长 PTP 运动会花费 `500000 / 1000000 = 0.5 s` 加速，然后以 500000 巡航，直到减速距离前瞻在另一段 0.5 s 内将其降下。加速斜坡期间的行程为 `½ × 500000 × 0.5 = 125000` 用户单位；减速侧相同。如果请求的行程小于 `2 × 125000 = 250000` 单位，则运动永远不会达到 `Speed`，转而呈三角形。

## 版本间的变更

在 **v4** 中，`Speed` 是 32 位整数。在 **v5（central-i）** 中，它是 64 位整数，与 64 位位置流水线匹配。规划器对 `Speed` 的使用（PTP 中取幅值、点动中带符号）保持不变。**v5 仅适用于 central-i**——在 standalone 上，`Speed` 仍为 v4 的 32 位值。

## 另请参阅

- [Accel](Accel.md) — 朝此速度的加速速率
- [Decel](Decel.md) — 从此速度的减速速率
- [AccelFact](AccelFact.md) — 缩放加/减速斜坡（不缩放 `Speed`）
- [Jerk](Jerk.md) — 斜坡的 S 曲线平滑
- [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) — 速度环硬钳位（区别于 `Speed`）；在间接模式中 `Begin` 会拒绝 `Speed > MaxVel`
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 23 报告对照 `MaxVel` 的速度饱和
- [SpeedChgNew](SpeedChgNew.md) — 运动期间由位置触发的速度更改
- [Begin](../04-motion-command/Begin.md) — 读取 `Speed` 并准备运动
