---
keyword: AccelFact
summary: 应用于 Accel 的缩放因子，用于在不改变 Accel 的情况下调整有效加速度。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 168
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
  - 1
  - 40
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AccelFact

应用于 `Accel` 的缩放因子，用于在不改变 `Accel` 的情况下调整有效加速度。

## 概述

`AccelFact` 是一个整数乘数（范围 1–40，默认值 1），同时作用于 [Accel](Accel.md) 和 [Decel](Decel.md)，因此规划器实际使用的加速度和减速度分别为 `Accel × AccelFact` 和 `Decel × AccelFact`。它允许以整数倍比例放大或缩小已存储的斜坡曲线，而无需修改 `Accel`/`Decel` 本身——当同一基础配方需要以更快或更慢的速度运行时非常便捷。该参数为读写型、轴作用域，并保存至闪存，可在任意时刻更改，包括运动过程中。

## 工作原理

每个控制周期，规划器在使用加速度和减速度之前，会先将两者均乘以 `AccelFact`：

$$
\text{Accel}_{\text{eff}} = \text{Accel} \cdot \text{AccelFact} ,\qquad
\text{Decel}_{\text{eff}} = \text{Decel} \cdot \text{AccelFact}
$$

关键行为说明：

- **同样作用于紧急减速率。** 当 [EmrgDec](EmrgDec.md) 在限位开关、软件限位或受控停止输入触发的停止时取代 `Decel`，该值同样会乘以 `AccelFact`，因此紧急停止也随该因子缩放。[Abort](../04-motion-command/Abort.md) 不进行斜坡减速，因此不受 `AccelFact` 影响。
- **仅限整数。** `AccelFact` 为 1–40 之间的整数，不支持小数缩放——如需更精细的控制，请直接调整 `Accel`/`Decel`。
- **实时生效。** 由于乘法在每个周期执行，在运动过程中更改 `AccelFact` 将在下一个周期即时重新缩放斜坡斜率。
- **适用于两种规划器阶次。** 缩放后的 `Accel_eff`/`Decel_eff` 直接用于二阶斜坡，并作为峰值加速度/峰值减速度约束传递给三阶急动度规划器。

该参数无量纲（无用户单位缩放），**不**对 [Speed](Speed.md) 或急动度设置进行缩放，仅缩放加速度/减速度。

### 边界情况

- **电机关闭：** 参数值保持不变；规划器不运行。
- **超范围写入：** 参数系统将写入值钳位至 `1`–`40`；超出范围的值将被拒绝。
- **仿真模式（`MotorType` = 5）：** 行为不变。
- **ModRev 环绕：** 与此参数无关。
- **激活故障：** 轴被禁用；下一次 `Begin` 将重新读取 `AccelFact`。
- **其他运动模式：** 适用于所有规划器驱动模式（点动/PTP/PD 间接/电子齿轮间接/摇杆间接），并作用于正常 `Decel` 和 `EmrgDec`。直接模式不使用 `Accel`/`Decel`，因此忽略 `AccelFact`。
- **`AccelFact = 1`：** 默认值；速率按配置值使用。

## 示例

```text
AAccelFact=2         ; double the effective acceleration and deceleration
AAccelFact=1         ; restore base rates (default)
AAccelFact           ; read current factor
```

## 另请参阅

- [Accel](Accel.md) — 本因子所乘的基础加速度
- [Decel](Decel.md) — 本因子所乘的基础减速度
- [EmrgDec](EmrgDec.md) — 紧急减速率，同样受本因子缩放
- [Speed](Speed.md) — 巡航速度（不受 `AccelFact` 影响）
