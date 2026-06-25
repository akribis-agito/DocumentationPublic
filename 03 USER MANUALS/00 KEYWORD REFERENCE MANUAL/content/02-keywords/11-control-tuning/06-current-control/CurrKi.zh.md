---
keyword: CurrKi
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 105
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
summary: 电流环积分增益，含抗积分饱和功能。
---
# CurrKi

电流环积分增益，含抗积分饱和功能。

## 概述

`CurrKi` 是电流环的积分增益。它在将电流误差累积进电流误差积分项之前，先对电流误差进行缩放。与比例增益 [CurrGain](CurrGain.md) 共同构成电流环 PI 调节器——控制级联中的最内环。积分项将稳态电流误差驱动至零。

与 `CurrGain` 相同，同一个 `CurrKi` 应用于电机类型所需的所有电流通道（有刷电机为 A 相；步进电机和 abc 域三相控制为 A 相和 B 相；dq0 域矢量控制为 q 轴和 d 轴）。

## 工作原理

每个控制周期，电流误差乘以 `CurrKi` 后加入运行积分项；比例路径将原始误差加上后再乘以 [CurrGain](CurrGain.md) 以形成通道电压。以三相电机的交轴为例（误差 [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md)，输出 [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)）：

$$
\begin{aligned}
\text{Integral} &\mathrel{+}= \text{IqErr} \cdot \text{CurrKi} \cdot 0.001 \cdot \text{noClamp} \\
\text{Vq} &= (\text{Integral} + \text{IqErr}) \cdot \text{CurrGain} \cdot 0.001
\end{aligned}
$$

`0.001` 是对 `CurrKi` 和 `CurrGain` 均适用的固定增益缩放系数。

### 抗积分饱和

`noClamp` 是对积分增量进行缩放的抗积分饱和因子：

- `noClamp = 1` — 正常运行，积分项正常累积。
- `noClamp = 0` — 积分项冻结（该周期的积分增量被置零）。

当输出处于电压饱和状态，且继续积分会将输出进一步推入饱和（输出与电流误差同号）时，积分项被冻结。电压饱和检测作用于合成输出幅值——对于 dq0 域控制，检测 [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)/[Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) 矢量与最大 PWM 幅值的关系——并通过 [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) 中的电压饱和状态位上报。当饱和解除时，积分恢复正常。

### 缩放、范围与默认值

| | v4（standalone 及 central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位整数 | 32 位浮点 |
| 范围 | 0 to 200000 | 0 to 200000 |
| 默认值 | 0 | 0 |
| 增益缩放 | 0.001 | 0.001 |

## 示例

```text
ACurrKi=8000         ; set current-loop integral gain
ACurrKi              ; read back the gain
```

### 操作示例：配置电流 PI 并验证电压饱和

电流环是最内环，其饱和受限于可用母线电压而非电流上限。[StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) 中的电压饱和位指示 PI 输出何时达到调制器限值。

1. **先设置比例增益**，使环路具有可供积分的响应（参见 [CurrGain](CurrGain.md)）：

   ```text
   ACurrGain=15000
   ```

2. **添加积分项**：

   ```text
   ACurrKi=8000
   ```

3. **施加电流阶跃**（在电流运行模式下，或在位置模式下指令快速运动）。观察电压饱和位：

   ```text
   (AStatReg & 0x400000) >> 22   ; bit 22 - voltage saturation
   ```

   当位 22 读为 `1` 时，合成 [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)/[Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) 矢量已被 [MaxPWM](../../../02-keywords/06-protections/02-current-and-voltage/MaxPWM.md) 限幅。抗积分饱和门控将这些周期内的积分器增量强制置零，从而防止积分饱和。

4. **确认积分项未发生饱和**：在饱和解除后立即检查 [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md)，其值应随误差平滑回落，而非超调——超调将表明抗积分饱和未正常介入。

## 另请参阅

- [CurrGain](CurrGain.md) — 电流环比例增益（与本参数共同构成 PI 调节器）
- [IqErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IqErr.md) — 增益所积分的交轴电流误差
- [IaErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IaErr.md) / [IbErr](../../../02-keywords/09-current-and-voltage/02-motor-variables/IbErr.md) — 同一增益所积分的相域误差
- [Vq](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vq.md) / [Vd](../../../02-keywords/09-current-and-voltage/02-motor-variables/Vd.md) — PI 调节器产生的电压
- [MaxPWM](../../../02-keywords/06-protections/02-current-and-voltage/MaxPWM.md) — 触发电压饱和的调制器上限
- [StatReg](../../../02-keywords/07-status-and-faults/StatReg.md) — 位 22 上报电压饱和（抗积分饱和已介入）
