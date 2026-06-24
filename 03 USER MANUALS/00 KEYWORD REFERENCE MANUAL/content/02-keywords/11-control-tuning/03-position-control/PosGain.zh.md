---
keyword: PosGain
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 100
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 0
    - 1000000
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 位置环比例增益——将位置误差乘以该系数以产生速度指令。
---
# PosGain

位置环比例增益——将位置误差乘以该系数以产生速度指令。

## 概述

`PosGain` 是 PIV 级联中外环（位置环）的比例增益。每个控制周期，它将位置误差相乘，产生位置控制器输出，该输出是速度环参考值 [VelRef](../../10-motion/01-kinematics-status/VelRef.md) 的主要贡献。它是将位置误差（以主用户单位为单位）转换为指令速度（以主用户单位/秒为单位）的单一比例系数。

`PosGain` 是一个数组，因此可以参与增益调度。未使用增益调度时，使用第一个元素 `PosGain[1]` 进行控制。有关每种调度方法下使用哪个数组元素，请参阅 [ScheduleMode](../01-general-keywords/ScheduleMode.md)。

在龙门模式下，对于龙门化的轴，使用龙门专用位置增益代替 `PosGain`。

## 工作原理

位置控制器作用于 [PosErr](../../10-motion/01-kinematics-status/PosErr.md)（位置参考减去位置反馈）。比例输出随后与速度前馈（经缩放的参考速度 [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md)）相加，形成速度环参考值：

$$
\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

该乘积以扩展精度计算，然后钳位至可存储范围后成为 `VelRef`。`VelRef` 随后被硬限幅至 ±[MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)。

- **乘以对象：** 位置误差 [PosErr](../../10-motion/01-kinematics-status/PosErr.md)（经可选位置误差滤波器后；参见 [PosFiltOn](PosFiltOn.md)）。
- **相加位置：** 其输出与经 [VelTrackFact](../04-velocity-control/VelTrackFact.md) 缩放的速度前馈相加，构建 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)，即速度环的输入。
- **缩放/单位：** 作为直接乘数使用（比例系数 1.0）。值为 `0` 时，位置环不产生比例指令，仅保留速度前馈。

### 范围与默认值

| | v4（独立版和 central-i） | v5（central-i） |
|---|---|---|
| 数据类型 | 32 位整数 | 32 位浮点 |
| 范围 | 0 到 20000 | 0 到 1000000 |
| 默认值 | 0 | 0 |

## 示例

```text
APosGain[1]=350     ; 设置位置环比例增益（第一个调度元素）
APosGain[1]         ; 读取位置环比例增益
```

### 示例演练：读取稳态跟随误差

以 `PosGain = 350`、`VelTrackFact = 1024`（单位前馈）、轴以恒定速度参考 `dPosRef = 20000` 用户单位/秒跟踪为例，如果在稳态下速度环完全跟随 `VelRef`，则可推导出位置环平衡残余贡献所需的位置误差：

`VelRef = PosErr x PosGain + dPosRef x VelTrackFact / 1024`

在恒速跟踪的稳态下，`VelRef ≈ dPosRef`，比例项 `PosErr x PosGain` 只需补偿微小差值。在零速度前馈（`VelTrackFact = 0`）时，位置环必须单独提供全部 `VelRef`，因此 `PosErr = VelRef / PosGain = 20000 / 350 ≈ 57.1` 用户单位。同一轴使用单位前馈时，通常误差为上述值的一小部分。

## 版本差异

在 **v4** 中，位置环为纯比例：其输出为 `PosErr × PosGain`。在 **v5（central-i）** 中，`PosGain` 为浮点值，范围更宽（`0` 到 `1000000`），位置误差可先通过二阶位置误差滤波器，并在 `PosGain` 输出形成 `VelRef` 之前加入可选的位置积分项（[PosKi](PosKi.md)）。**v5 为 central-i 专属。**

## 另请参阅

- [PosErr](../../10-motion/01-kinematics-status/PosErr.md) — `PosGain` 所乘的位置误差
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — 由 `PosGain` 输出产生的速度环参考值
- [PosKi](PosKi.md) — 对 `PosGain` 输出进行积分的位置积分增益（v5）
- [PosFiltOn](PosFiltOn.md) / [PosFiltDef](PosFiltDef.md) — 可选的位置环滤波器
- [VelTrackFact](../04-velocity-control/VelTrackFact.md) — 对与 `PosGain` 输出相加的速度前馈进行缩放
- [AccFFW](../05-feedforwards/AccFFW.md) / [VelFFW](../05-feedforwards/VelFFW.md) — 在位置环下游添加的配套前馈
- [VelGain](../04-velocity-control/VelGain.md) — 内环（速度环）的比例增益
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 23（速度饱和），当位置环输出超过 MaxVel 时置位
- [ScheduleMode](../01-general-keywords/ScheduleMode.md) — 选择哪个数组元素处于激活状态
