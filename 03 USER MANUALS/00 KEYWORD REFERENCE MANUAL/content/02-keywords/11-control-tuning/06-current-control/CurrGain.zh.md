---
keyword: CurrGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 104
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
  - 200000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrGain

电流环比例增益。

## 概述

`CurrGain` 是电流环（控制级联最内层环路）的比例增益。它将电流误差与电流误差积分之和相乘，生成指令电压。`CurrGain` 与积分增益 [CurrKi](CurrKi.md) 共同构成电流环 PI 控制器。

同一个 `CurrGain` 适用于电机类型所需的每一路电流通道：

| 电机类型 | 受 `CurrGain` 控制的通道 |
|---|---|
| 音圈 / 有刷（单相） | A 相 |
| 步进（两相） | A 相和 B 相 |
| 三相，dq0 域（矢量）控制 | 交轴（q 轴）和直轴（d 轴） |
| 三相，abc 域控制 | A 相和 B 相 |

## 工作原理

对于每路受控通道，电流误差积分累加（以 [CurrKi](CurrKi.md) 缩放），将电流误差加至积分后，`CurrGain` 与该和相乘，形成通道电压指令。以三相电机的交轴为例（电流误差为 [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md)，输出电压为 [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)）：

$$
\begin{aligned}
\text{Integral} &\mathrel{+}= \text{IqErr} \cdot \text{CurrKi} \cdot 0.001 \cdot \text{noClamp} \\
\text{Vq} &= (\text{Integral} + \text{IqErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

其中 `0.001` 是同时应用于 `CurrGain` 和 `CurrKi` 的固定增益缩放，`noClamp` 为抗积分饱和因子（详见 [CurrKi](CurrKi.md)）。其他电流通道采用完全相同的结构，各自使用对应的误差和电压项。

### 缩放、范围与默认值

| | v4（standalone & central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位整数 | 32 位浮点数 |
| 范围 | 0 to 200000 | 0 to 200000 |
| 默认值 | 0 | 0 |
| 增益缩放 | 0.001 | 0.001 |

## 示例

```text
ACurrGain=15000      ; set current-loop proportional gain
ACurrGain            ; read back the gain
```

### 应用示例：由电流误差计算 q 轴电压

以 `CurrGain = 15000`、`CurrKi = 0`、瞬时 q 轴误差 `IqErr = 200`（电流单位，无积分累计）为例，电流 PI 产生的 q 轴电压指令为：

`Vq = (0 + 200) x 15000 x 0.001 = 3000`（电压单位）

若积分项已累积至 `Integral = 500`，则电压变为 `(500 + 200) x 15000 x 0.001 = 10500`。若 `CurrGain = 0`，任意误差均产生零电压，环路变为开环。

## 另请参阅

- [CurrKi](CurrKi.md) — 电流环积分增益（与 `CurrGain` 共同构成 PI 控制器）
- [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md) — 该增益作用的交轴电流误差
- [IaErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IaErr.md) / [IbErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IbErr.md) — 该增益作用的相域误差
- [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) — PI 产生的交轴电压
- [ControlMode](../../../02-keywords/09-current-and-voltage/02-motor-variables/ControlMode.md) — 选择 dq0 域或 abc 域电流控制
- [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) — 位 22（电压饱和）指示 PI 输出被 [MaxPWM](../../../02-keywords/06-protections/02-current-and-voltage/MaxPWM.md) 限幅时的状态
- [VelGain](../04-velocity-control/VelGain.md) — 向本电流环输入信号的外层速度环比例增益
