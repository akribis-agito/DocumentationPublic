---
keyword: MotorCurr
summary: 只读电机总反馈电流矢量幅值，单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 8
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MotorCurr

只读电机总反馈电流矢量幅值，单位为毫安。

## 概述

`MotorCurr` 是电机的总反馈电流矢量幅值，单位为毫安。它将测得的相电流合成为单一幅值，其计算公式取决于由 [MotorType](../../02-motor-and-amplifier/MotorType.md) 选定的电机组，随后采用下文所述的符号约定。它为监测电机所汲取的总电流提供单一数值。

该值在每个控制环采样周期内由测得的相电流 [Ia](Ia.md)、[Ib](Ib.md)（以及三相电机推导出的 C 相电流 `Ic = -(Ia + Ib)`）计算得出。所报告的值是经 [CurrDir](CurrDir.md) 反转之后的值。

## 工作原理

幅值根据电机组由测得的相电流构建，随后附加符号：

| 电机组（MotorType） | 幅值公式 | 符号 |
|----|----|----|
| 单相 / 有刷电机（MotorType = 1 有刷，2 音圈） | $\left\| \text{MotorCurr} \right\|\ \lbrack mA\rbrack\ = \ \left\| \text{Ia} \right\|\ \lbrack mA\rbrack$ | [Ia](Ia.md) 的符号（值直接为 `Ia`）。 |
| 三相无刷电机（MotorType = 3 直线，4 旋转） | $\left\| \text{MotorCurr} \right\|\ \lbrack mA\rbrack\ = \ \sqrt{\frac{2}{3}\left(\text{Ia}^{2} + \text{Ib}^{2} + \text{Ic}^{2}\right)}\ \lbrack mA\rbrack$ | [Iq](Iq.md) 的符号：$\text{Iq} \geq 0$ 时为正，否则为负。 |
| 两相步进电机（MotorType = 6 开环，7 闭环） | $\left\| \text{MotorCurr} \right\|\ \lbrack mA\rbrack\ = \ \sqrt{\text{Ia}^{2} + \text{Ib}^{2}}\ \lbrack mA\rbrack$ | 始终为正（步进电机没有电流符号；方向由换相角承载）。 |

三相幅值 $\sqrt{\frac{2}{3}(\text{Ia}^{2}+\text{Ib}^{2}+\text{Ic}^{2})}$ 假设为正弦换相；对于平衡的三相组，它等于由 [Iq](Iq.md)/[Id](Id.md) 形成的 dq 帧幅值 $\sqrt{\text{Iq}^{2}+\text{Id}^{2}}$。

**CurrDir 反转。** 在幅值与符号形成后，当 [CurrDir](CurrDir.md) = 1（翻转激励方向）时所报告的值取负，当 CurrDir = 0 时则原样传递。

无符号幅值及其平方在内部被复用于电机 I²T 功率保护以及堵转电机和动态制动逻辑；`MotorCurr` 暴露的是带符号的结果。

## 示例

```text
AMotorCurr          ; read total feedback current amplitude (mA)
```

## 另请参阅

- [Ia](Ia.md)、[Ib](Ib.md) — 用于构建幅值的测得相电流
- [Iq](Iq.md)、[Id](Id.md) — 测得的 dq 轴电流；Iq 为三相电机提供符号
- [CurrDir](CurrDir.md) — 使所报告值取负的激励方向标志
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 决定公式的电机类型
- [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) — 基于相同测得电流的逐相过流保护
