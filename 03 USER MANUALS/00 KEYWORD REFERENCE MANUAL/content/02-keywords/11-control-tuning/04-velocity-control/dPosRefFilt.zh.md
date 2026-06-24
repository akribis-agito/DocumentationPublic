---
keyword: dPosRefFilt
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 106
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
  - 20000
  - 1000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 应用于参考速度（位置参考微分）的一阶低通滤波器截止频率。
---
# dPosRefFilt

应用于参考速度（位置参考微分）的一阶低通滤波器截止频率。

## 概述

`dPosRefFilt` 设置一阶低通滤波器的截止频率，该滤波器对参考速度 [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md)（位置参考的微分）进行平滑，然后用作速度前馈。滤波后的参考速度随后由 [VelTrackFact](VelTrackFact.md) 缩放，并叠加到位置控制器输出上，构成速度环参考 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)。

单位为 Hz/100。例如，截止频率 4500 Hz 输入为 `dPosRefFilt = 450000`。

## 工作原理

位置参考逐周期差分以获得原始参考速度；该信号通过截止频率为 `dPosRefFilt` 的单极低通滤波器。滤波系数由截止频率和控制采样时间导出，因此较低的 `dPosRefFilt` 对前馈平滑更多（但会增加滞后），较高的值则更紧密地跟踪原始参考速度。滤波后的结果即为 [VelTrackFact](VelTrackFact.md) 所缩放的 [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md)：

$$
\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

- **范围/默认值：** `20000` 到 `1000000`（即 200 Hz 到 10000 Hz），默认 `1000000`。
- **单位：** Hz/100。

**注意：** 当截止频率超过 8192 Hz 时，低通滤波器被旁路（不进行滤波）；在默认值 `1000000` 下，参考速度直接通过，不经滤波。

## 示例

```text
AdPosRefFilt=450000 ; low-pass the reference velocity at 4500 Hz
AdPosRefFilt        ; read the reference-velocity filter cutoff
```

### 计算示例：选择截止频率

假设运动曲线产生的参考速度阶跃包含数 kHz 以内的显著频率成分，且位置环带宽约为 200 Hz。截止频率 `dPosRefFilt = 100000`（1000 Hz）可使速度前馈跟随位置环能响应的全部曲线内容，同时滤除 1 kHz 以上的量化抖动。将截止频率提高至旁路阈值以上（`dPosRefFilt > 819200`，即 8192 Hz）——例如默认值 `1000000`——则参考速度不经滤波直接通过。

## 另请参见

- [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) — 该滤波器所平滑的参考速度
- [VelTrackFact](VelTrackFact.md) — 将滤波后参考速度缩放为前馈
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — 前馈加入的速度环参考
- [PosGain](../03-position-control/PosGain.md) — 前馈叠加到其输出上的位置增益
